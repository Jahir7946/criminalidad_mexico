#!/usr/bin/env python3
"""
Script para ejecutar el servidor Flask
Detecta automáticamente si está en producción o desarrollo
"""

import sys
import os
from datetime import datetime

def check_dependencies():
    """Verifica que las dependencias estén instaladas"""
    required_modules = [
        ('flask', 'flask'),
        ('flask_cors', 'flask_cors'), 
        ('pymongo', 'pymongo'),
        ('pandas', 'pandas'),
        ('openpyxl', 'openpyxl'),
        ('dotenv', 'python-dotenv')
    ]
    
    missing = []
    for import_name, package_name in required_modules:
        try:
            __import__(import_name)
        except ImportError:
            missing.append(package_name)
    
    if missing:
        print(f"❌ Módulos faltantes: {', '.join(missing)}")
        print("Ejecuta: pip install -r requirements.txt")
        return False
    
    print("✅ Todas las dependencias están instaladas")
    return True

def main():
    print("🚀 Iniciando Dashboard de Criminalidad en México")
    print(f"🕐 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Verificar dependencias
    if not check_dependencies():
        sys.exit(1)
    
    # Importar y ejecutar la aplicación
    try:
        from app import app
        print("✅ Aplicación Flask cargada correctamente")
        
        # Detectar entorno
        port = int(os.environ.get('PORT', 5000))
        is_production = os.environ.get('FLASK_ENV') == 'production'
        
        if is_production:
            print(f"🌐 Servidor de producción en puerto: {port}")
            print("📊 API disponible en: /api/v1/")
            print("🔍 Health check: /api/v1/health")
            # En producción, usar configuración optimizada
            app.run(host='0.0.0.0', port=port, debug=False)
        else:
            print("🌐 Servidor disponible en: http://localhost:5000")
            print("📊 API disponible en: http://localhost:5000/api/v1/")
            print("🔍 Health check: http://localhost:5000/api/v1/health")
            print("\n" + "="*50)
            print("Presiona Ctrl+C para detener el servidor")
            print("="*50)
            # En desarrollo, usar debug mode
            app.run(host='0.0.0.0', port=port, debug=True)
        
    except ImportError as e:
        print(f"❌ Error al importar la aplicación: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error al iniciar el servidor: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
