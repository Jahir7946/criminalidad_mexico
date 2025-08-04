#!/usr/bin/env python3
"""
Script para ejecutar el servidor Flask
Optimizado para producción en Render
"""

import sys
import os
from datetime import datetime

def main():
    print("🚀 Iniciando Dashboard de Criminalidad en México")
    print(f"🕐 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Detectar entorno
    port = int(os.environ.get('PORT', 5000))
    is_production = os.environ.get('FLASK_ENV') == 'production'
    
    if is_production:
        print("🌐 Modo producción detectado - usando Gunicorn")
        print(f"📊 Puerto: {port}")
        
        # En producción, usar Gunicorn directamente
        import subprocess
        cmd = [
            'gunicorn', 
            'app:app',
            '--bind', f'0.0.0.0:{port}',
            '--workers', '2',
            '--timeout', '120',
            '--preload',
            '--max-requests', '1000',
            '--max-requests-jitter', '100'
        ]
        
        print(f"🚀 Ejecutando: {' '.join(cmd)}")
        subprocess.run(cmd)
        
    else:
        print("🌐 Modo desarrollo - usando Flask dev server")
        
        # Verificar dependencias solo en desarrollo
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
            sys.exit(1)
        
        print("✅ Todas las dependencias están instaladas")
        
        try:
            from app import app
            print("✅ Aplicación Flask cargada correctamente")
            print("🌐 Servidor disponible en: http://localhost:5000")
            print("📊 API disponible en: http://localhost:5000/api/v1/")
            print("🔍 Health check: http://localhost:5000/api/v1/health")
            print("\n" + "="*50)
            print("Presiona Ctrl+C para detener el servidor")
            print("="*50)
            
            app.run(host='0.0.0.0', port=port, debug=True)
            
        except ImportError as e:
            print(f"❌ Error al importar la aplicación: {e}")
            sys.exit(1)
        except Exception as e:
            print(f"❌ Error al iniciar el servidor: {e}")
            sys.exit(1)

if __name__ == "__main__":
    main()
