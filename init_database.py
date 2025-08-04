#!/usr/bin/env python3
"""
Script de inicialización para el Dashboard de Criminalidad en México
Ejecuta el proceso ETL y prepara la base de datos con datos iniciales
"""

import sys
import os
import logging
from datetime import datetime

# Agregar el directorio actual al path para importar módulos locales
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from etl_processor import CrimeDataETL
from database import db_manager
from config import Config

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('init_database.log')
    ]
)
logger = logging.getLogger(__name__)

def print_banner():
    """Imprime banner de inicio"""
    banner = """
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║        🚨 DASHBOARD DE CRIMINALIDAD EN MÉXICO 🚨             ║
    ║                                                              ║
    ║              Inicialización de Base de Datos                ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
    """
    print(banner)

def check_prerequisites():
    """Verifica que todos los prerequisitos estén disponibles"""
    logger.info("🔍 Verificando prerequisitos...")
    
    errors = []
    
    # Verificar archivo de datos
    if not os.path.exists(Config.DATA_SOURCE):
        errors.append(f"❌ Archivo de datos no encontrado: {Config.DATA_SOURCE}")
    else:
        logger.info(f"✅ Archivo de datos encontrado: {Config.DATA_SOURCE}")
    
    # Verificar configuración
    try:
        Config.validate_config()
        logger.info("✅ Configuración validada")
    except ValueError as e:
        errors.append(f"❌ Error de configuración: {e}")
    
    # Verificar conexión a MongoDB
    try:
        connection_test = db_manager.test_connection()
        if connection_test['status'] == 'success':
            logger.info("✅ Conexión a MongoDB establecida")
        else:
            errors.append(f"❌ Error de conexión a MongoDB: {connection_test['message']}")
    except Exception as e:
        errors.append(f"❌ Error al conectar con MongoDB: {e}")
    
    if errors:
        logger.error("❌ Errores encontrados durante la verificación:")
        for error in errors:
            logger.error(f"   {error}")
        return False
    
    logger.info("✅ Todos los prerequisitos verificados correctamente")
    return True

def initialize_database():
    """Inicializa la base de datos con datos de criminalidad"""
    logger.info("🚀 Iniciando inicialización de base de datos...")
    
    try:
        # Crear instancia del procesador ETL
        etl = CrimeDataETL()
        
        # Ejecutar proceso ETL completo
        logger.info("📊 Ejecutando proceso ETL...")
        results = etl.run_full_etl()
        
        if results['overall_status'] == 'success':
            logger.info("🎉 Base de datos inicializada exitosamente")
            
            # Mostrar resumen de resultados
            print("\n" + "="*60)
            print("📊 RESUMEN DE INICIALIZACIÓN")
            print("="*60)
            
            if results.get('extract'):
                extract = results['extract']
                print(f"📥 EXTRACCIÓN:")
                print(f"   • Filas procesadas: {extract.get('rows', 'N/A')}")
                print(f"   • Columnas: {extract.get('columns', 'N/A')}")
            
            if results.get('transform'):
                transform = results['transform']
                print(f"🔄 TRANSFORMACIÓN:")
                print(f"   • Registros procesados: {transform.get('processed_records', 'N/A')}")
            
            if results.get('load'):
                load = results['load']
                print(f"💾 CARGA:")
                print(f"   • Registros insertados: {load.get('loaded_records', 'N/A')}")
            
            print("="*60)
            
            # Verificar datos cargados
            verify_data()
            
            return True
            
        else:
            logger.error("❌ Error en el proceso ETL")
            print("\n❌ ERRORES ENCONTRADOS:")
            for phase, result in results.items():
                if phase != "overall_status" and result and result.get('status') == 'error':
                    print(f"   • {phase.upper()}: {result.get('message', 'Error desconocido')}")
            return False
            
    except Exception as e:
        logger.error(f"❌ Error durante la inicialización: {e}")
        return False

def verify_data():
    """Verifica que los datos se hayan cargado correctamente"""
    logger.info("🔍 Verificando datos cargados...")
    
    try:
        # Obtener estadísticas generales
        stats_result = db_manager.get_crime_statistics()
        
        if stats_result['status'] == 'success':
            stats = stats_result['statistics']
            
            print(f"\n📈 ESTADÍSTICAS DE DATOS CARGADOS:")
            print(f"   • Total de delitos: {stats.get('total_crimes', 0):,}")
            print(f"   • Incidencia promedio: {stats.get('avg_incidence', 0):.2f}%")
            print(f"   • Estados procesados: {stats.get('total_states', 0)}")
            print(f"   • Delitos máximos: {stats.get('max_crimes', 0):,}")
            print(f"   • Delitos mínimos: {stats.get('min_crimes', 0):,}")
            
            if stats.get('top_crime_state'):
                top_state = stats['top_crime_state']
                print(f"   • Estado con más delitos: {top_state.get('state', 'N/A')} ({top_state.get('crimes', 0):,})")
        
        # Obtener muestra de datos
        sample_result = db_manager.get_all_crime_data(limit=3)
        
        if sample_result['status'] == 'success' and sample_result['data']:
            print(f"\n📋 MUESTRA DE DATOS (primeros 3 registros):")
            for i, record in enumerate(sample_result['data'][:3], 1):
                print(f"   {i}. {record.get('state', 'N/A')}: {record.get('crimes', 0):,} delitos")
        
        logger.info("✅ Verificación de datos completada")
        
    except Exception as e:
        logger.error(f"❌ Error durante la verificación: {e}")

def show_next_steps():
    """Muestra los siguientes pasos para el usuario"""
    print("\n" + "="*60)
    print("🚀 PRÓXIMOS PASOS")
    print("="*60)
    print("1. Iniciar el servidor Flask:")
    print("   python app.py")
    print()
    print("2. Acceder al dashboard:")
    print("   http://localhost:5000")
    print()
    print("3. Probar la API:")
    print("   http://localhost:5000/api/v1/health")
    print("   http://localhost:5000/api/v1/crime-data")
    print()
    print("4. Para desplegar en Render:")
    print("   - Subir código a GitHub")
    print("   - Conectar repositorio en Render")
    print("   - Configurar variables de entorno")
    print("="*60)

def main():
    """Función principal"""
    print_banner()
    
    logger.info(f"🕐 Iniciado en: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Verificar prerequisitos
    if not check_prerequisites():
        logger.error("❌ No se pueden cumplir los prerequisitos. Abortando.")
        sys.exit(1)
    
    # Inicializar base de datos
    if initialize_database():
        logger.info("🎉 Inicialización completada exitosamente")
        show_next_steps()
        sys.exit(0)
    else:
        logger.error("❌ Error durante la inicialización")
        sys.exit(1)

if __name__ == "__main__":
    main()
