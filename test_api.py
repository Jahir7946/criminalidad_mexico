#!/usr/bin/env python3
"""
Script de pruebas para la API del Dashboard de Criminalidad en México
Ejecuta pruebas básicas de todos los endpoints
"""

import requests
import json
import sys
import time
from datetime import datetime

# Configuración de la API
API_BASE_URL = "http://localhost:5000/api/v1"
TIMEOUT = 10

def print_banner():
    """Imprime banner de pruebas"""
    banner = """
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║        🧪 PRUEBAS DE API - CRIMINALIDAD MÉXICO 🧪           ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
    """
    print(banner)

def test_endpoint(method, endpoint, description, expected_status=200, data=None):
    """
    Prueba un endpoint específico
    
    Args:
        method (str): Método HTTP (GET, POST, etc.)
        endpoint (str): Endpoint a probar
        description (str): Descripción de la prueba
        expected_status (int): Código de estado esperado
        data (dict): Datos para enviar (en caso de POST)
    
    Returns:
        tuple: (success, response_data, response_time)
    """
    url = f"{API_BASE_URL}{endpoint}"
    
    print(f"\n🔍 Probando: {description}")
    print(f"   📍 {method} {url}")
    
    try:
        start_time = time.time()
        
        if method.upper() == 'GET':
            response = requests.get(url, timeout=TIMEOUT)
        elif method.upper() == 'POST':
            response = requests.post(url, json=data, timeout=TIMEOUT)
        else:
            print(f"   ❌ Método HTTP no soportado: {method}")
            return False, None, 0
        
        response_time = time.time() - start_time
        
        # Verificar código de estado
        if response.status_code == expected_status:
            print(f"   ✅ Status: {response.status_code} (esperado: {expected_status})")
        else:
            print(f"   ❌ Status: {response.status_code} (esperado: {expected_status})")
            return False, None, response_time
        
        # Intentar parsear JSON
        try:
            response_data = response.json()
            print(f"   📊 Respuesta JSON válida")
            
            # Verificar estructura básica de respuesta
            if 'status' in response_data:
                print(f"   📋 Status de respuesta: {response_data['status']}")
            
            if 'data' in response_data and response_data['data']:
                if isinstance(response_data['data'], list):
                    print(f"   📦 Datos: {len(response_data['data'])} elementos")
                elif isinstance(response_data['data'], dict):
                    print(f"   📦 Datos: objeto con {len(response_data['data'])} campos")
                else:
                    print(f"   📦 Datos: {type(response_data['data']).__name__}")
            
        except json.JSONDecodeError:
            print(f"   ⚠️ Respuesta no es JSON válido")
            response_data = response.text
        
        print(f"   ⏱️ Tiempo de respuesta: {response_time:.3f}s")
        
        return True, response_data, response_time
        
    except requests.exceptions.Timeout:
        print(f"   ❌ Timeout después de {TIMEOUT}s")
        return False, None, 0
    except requests.exceptions.ConnectionError:
        print(f"   ❌ Error de conexión - ¿Está el servidor ejecutándose?")
        return False, None, 0
    except Exception as e:
        print(f"   ❌ Error inesperado: {e}")
        return False, None, 0

def run_all_tests():
    """Ejecuta todas las pruebas de la API"""
    print(f"🕐 Iniciando pruebas en: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    tests = [
        # Pruebas básicas
        ("GET", "/health", "Health Check - Verificar estado de la API"),
        
        # Pruebas de datos
        ("GET", "/crime-data", "Obtener todos los datos de criminalidad"),
        ("GET", "/crime-data?limit=5", "Obtener datos con límite"),
        ("GET", "/statistics", "Obtener estadísticas generales"),
        ("GET", "/metadata", "Obtener metadatos de la base de datos"),
        
        # Pruebas de filtros
        ("GET", "/crime-data/state/Jalisco", "Filtrar por estado - Jalisco"),
        ("GET", "/crime-data/state/Ciudad de México", "Filtrar por estado - Ciudad de México"),
        ("GET", "/crime-data/state/EstadoInexistente", "Filtrar por estado inexistente"),
        
        # Pruebas de errores
        ("GET", "/endpoint-inexistente", "Endpoint inexistente", 404),
        ("POST", "/crime-data", "Método no permitido en crime-data", 405),
    ]
    
    results = {
        'total': len(tests),
        'passed': 0,
        'failed': 0,
        'total_time': 0,
        'details': []
    }
    
    for method, endpoint, description, *args in tests:
        expected_status = args[0] if args else 200
        
        success, response_data, response_time = test_endpoint(
            method, endpoint, description, expected_status
        )
        
        results['total_time'] += response_time
        
        if success:
            results['passed'] += 1
            status = "✅ PASS"
        else:
            results['failed'] += 1
            status = "❌ FAIL"
        
        results['details'].append({
            'endpoint': endpoint,
            'description': description,
            'status': status,
            'response_time': response_time
        })
    
    return results

def test_data_integrity():
    """Prueba la integridad de los datos"""
    print(f"\n🔍 Probando integridad de datos...")
    
    try:
        # Obtener datos
        response = requests.get(f"{API_BASE_URL}/crime-data", timeout=TIMEOUT)
        
        if response.status_code != 200:
            print(f"   ❌ No se pudieron obtener datos: {response.status_code}")
            return False
        
        data = response.json()
        
        if data['status'] != 'success':
            print(f"   ❌ Respuesta de API no exitosa: {data.get('message', 'Sin mensaje')}")
            return False
        
        crime_data = data.get('data', [])
        
        if not crime_data:
            print(f"   ❌ No hay datos de criminalidad")
            return False
        
        print(f"   📊 Total de registros: {len(crime_data)}")
        
        # Verificar estructura de datos
        required_fields = ['state', 'crimes', 'incidence', 'types']
        valid_records = 0
        
        for record in crime_data:
            if all(field in record for field in required_fields):
                valid_records += 1
            else:
                missing = [field for field in required_fields if field not in record]
                print(f"   ⚠️ Registro incompleto - Faltan: {missing}")
        
        print(f"   ✅ Registros válidos: {valid_records}/{len(crime_data)}")
        
        # Verificar tipos de datos
        numeric_errors = 0
        for record in crime_data:
            if not isinstance(record.get('crimes'), (int, float)):
                numeric_errors += 1
            if not isinstance(record.get('incidence'), (int, float)):
                numeric_errors += 1
        
        if numeric_errors == 0:
            print(f"   ✅ Todos los campos numéricos son válidos")
        else:
            print(f"   ⚠️ {numeric_errors} errores en campos numéricos")
        
        # Verificar estados únicos
        states = [record.get('state') for record in crime_data if record.get('state')]
        unique_states = set(states)
        
        print(f"   📍 Estados únicos: {len(unique_states)}")
        
        if len(unique_states) >= 10:  # Esperamos al menos 10 estados
            print(f"   ✅ Cantidad de estados parece correcta")
        else:
            print(f"   ⚠️ Pocos estados encontrados, revisar datos")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Error durante prueba de integridad: {e}")
        return False

def print_results(results):
    """Imprime resumen de resultados"""
    print("\n" + "="*60)
    print("📊 RESUMEN DE PRUEBAS")
    print("="*60)
    
    print(f"Total de pruebas: {results['total']}")
    print(f"✅ Exitosas: {results['passed']}")
    print(f"❌ Fallidas: {results['failed']}")
    print(f"⏱️ Tiempo total: {results['total_time']:.3f}s")
    print(f"📈 Tasa de éxito: {(results['passed']/results['total']*100):.1f}%")
    
    if results['failed'] > 0:
        print(f"\n❌ PRUEBAS FALLIDAS:")
        for detail in results['details']:
            if "FAIL" in detail['status']:
                print(f"   • {detail['endpoint']}: {detail['description']}")
    
    print("="*60)

def main():
    """Función principal"""
    print_banner()
    
    # Verificar que el servidor esté ejecutándose
    print("🔍 Verificando conexión al servidor...")
    try:
        response = requests.get(f"{API_BASE_URL}/health", timeout=5)
        print("✅ Servidor accesible")
    except:
        print("❌ No se puede conectar al servidor")
        print("   Asegúrate de que el servidor Flask esté ejecutándose:")
        print("   python app.py")
        sys.exit(1)
    
    # Ejecutar pruebas
    results = run_all_tests()
    
    # Probar integridad de datos
    data_integrity_ok = test_data_integrity()
    
    # Mostrar resultados
    print_results(results)
    
    if data_integrity_ok:
        print("✅ Integridad de datos: OK")
    else:
        print("❌ Integridad de datos: PROBLEMAS DETECTADOS")
    
    # Código de salida
    if results['failed'] == 0 and data_integrity_ok:
        print("\n🎉 Todas las pruebas pasaron exitosamente")
        sys.exit(0)
    else:
        print("\n⚠️ Algunas pruebas fallaron")
        sys.exit(1)

if __name__ == "__main__":
    main()
