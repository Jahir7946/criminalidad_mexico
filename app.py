from flask import Flask, jsonify, request, render_template_string, send_from_directory, send_file
from flask_cors import CORS
import logging
from datetime import datetime
import os

# Importar módulos locales
from config import config, Config
from database import db_manager
from etl_processor import CrimeDataETL
from models import APIResponse, DataValidator, DataConverter

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def create_app(config_name='default'):
    """Factory function para crear la aplicación Flask"""
    
    app = Flask(__name__)
    
    # Configuración
    app.config.from_object(config[config_name])
    
    # CORS
    CORS(app, origins=app.config.get('CORS_ORIGINS', '*'))
    
    # Validar configuración al inicio
    try:
        Config.validate_config()
        logger.info("✅ Configuración validada correctamente")
    except ValueError as e:
        logger.error(f"❌ Error de configuración: {e}")
        raise
    
    # Probar conexión a base de datos
    try:
        connection_test = db_manager.test_connection()
        if connection_test['status'] == 'success':
            logger.info("✅ Conexión a MongoDB establecida")
        else:
            logger.warning(f"⚠️ Problema con MongoDB: {connection_test['message']}")
    except Exception as e:
        logger.error(f"❌ Error al conectar con MongoDB: {e}")
    
    # ==================== RUTAS DE LA API ====================
    
    @app.route('/dashboard')
    def dashboard():
        """Sirve el dashboard frontend"""
        try:
            return send_file('index.html')
        except Exception as e:
            logger.error(f"Error sirviendo dashboard: {e}")
            return jsonify({"error": "Dashboard no disponible"}), 500
    
    @app.route('/<path:filename>')
    def serve_static(filename):
        """Sirve archivos estáticos (CSS, JS, imágenes)"""
        try:
            # Lista de archivos permitidos
            allowed_files = ['main.js', 'style.css', 'background.png', 'logo.png']
            if filename in allowed_files:
                return send_from_directory('.', filename)
            else:
                return jsonify({"error": "Archivo no encontrado"}), 404
        except Exception as e:
            logger.error(f"Error sirviendo archivo estático {filename}: {e}")
            return jsonify({"error": "Archivo no encontrado"}), 404

    @app.route('/')
    def index():
        """Página principal - Dashboard interactivo"""
        try:
            return send_file('index.html')
        except Exception as e:
            logger.error(f"Error sirviendo dashboard principal: {e}")
            return jsonify({"error": "Dashboard no disponible"}), 500
    
    @app.route('/api-info')
    def api_info():
        """Página con información de la API"""
        html_template = """
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>API Dashboard Criminalidad México</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }
                .container { max-width: 800px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
                h1 { color: #2c3e50; border-bottom: 3px solid #3498db; padding-bottom: 10px; }
                h2 { color: #34495e; margin-top: 30px; }
                .endpoint { background: #ecf0f1; padding: 15px; margin: 10px 0; border-radius: 5px; border-left: 4px solid #3498db; }
                .method { font-weight: bold; color: #27ae60; }
                .url { font-family: monospace; background: #2c3e50; color: white; padding: 5px 10px; border-radius: 3px; }
                .status { padding: 10px; border-radius: 5px; margin: 20px 0; }
                .success { background: #d5f4e6; border: 1px solid #27ae60; color: #27ae60; }
                .info { background: #d6eaf8; border: 1px solid #3498db; color: #2980b9; }
                ul { line-height: 1.6; }
                .footer { margin-top: 40px; padding-top: 20px; border-top: 1px solid #bdc3c7; color: #7f8c8d; text-align: center; }
                .dashboard-link { background: #3498db; color: white; padding: 15px 30px; text-decoration: none; border-radius: 5px; display: inline-block; margin: 20px 0; font-weight: bold; }
                .dashboard-link:hover { background: #2980b9; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🚨 API Dashboard de Criminalidad en México</h1>
                
                <div class="status success">
                    <strong>✅ API Activa</strong> - Servidor funcionando correctamente
                </div>
                
                <div class="status info">
                    <strong>📊 Fuente de Datos:</strong> INEGI / SNSP (Secretariado Ejecutivo del Sistema Nacional de Seguridad Pública)
                </div>
                
                <a href="/" class="dashboard-link">🏠 Ir al Dashboard Principal</a>
                
                <h2>📋 Endpoints Disponibles</h2>
                
                <div class="endpoint">
                    <div class="method">GET</div>
                    <div class="url">/api/v1/health</div>
                    <p>Verifica el estado de la API y la conexión a la base de datos</p>
                </div>
                
                <div class="endpoint">
                    <div class="method">GET</div>
                    <div class="url">/api/v1/crime-data</div>
                    <p>Obtiene todos los datos de criminalidad</p>
                    <p><strong>Parámetros opcionales:</strong> ?limit=10</p>
                </div>
                
                <div class="endpoint">
                    <div class="method">GET</div>
                    <div class="url">/api/v1/crime-data/state/{nombre_estado}</div>
                    <p>Obtiene datos de criminalidad filtrados por estado</p>
                    <p><strong>Ejemplo:</strong> /api/v1/crime-data/state/Jalisco</p>
                </div>
                
                <div class="endpoint">
                    <div class="method">GET</div>
                    <div class="url">/api/v1/statistics</div>
                    <p>Obtiene estadísticas generales de criminalidad</p>
                </div>
                
                <div class="endpoint">
                    <div class="method">POST</div>
                    <div class="url">/api/v1/refresh-data</div>
                    <p>Ejecuta el proceso ETL para actualizar los datos desde el archivo Excel</p>
                </div>
                
                <div class="endpoint">
                    <div class="method">GET</div>
                    <div class="url">/api/v1/metadata</div>
                    <p>Obtiene metadatos sobre la base de datos y última actualización</p>
                </div>
                
                <h2>🛠️ Tecnologías Utilizadas</h2>
                <ul>
                    <li><strong>Backend:</strong> Flask (Python)</li>
                    <li><strong>Base de Datos:</strong> MongoDB Atlas</li>
                    <li><strong>Procesamiento:</strong> Pandas, NumPy</li>
                    <li><strong>Visualización:</strong> D3.js, Chart.js</li>
                    <li><strong>Despliegue:</strong> Render</li>
                </ul>
                
                <h2>📈 Estructura de Datos</h2>
                <p>Cada registro de criminalidad contiene:</p>
                <ul>
                    <li><strong>state:</strong> Nombre del estado</li>
                    <li><strong>crimes:</strong> Número total de delitos</li>
                    <li><strong>incidence:</strong> Tasa de incidencia por 100,000 habitantes</li>
                    <li><strong>types:</strong> Distribución por tipo de delito (Homicidio, Robo, Otros)</li>
                    <li><strong>year:</strong> Año de los datos</li>
                    <li><strong>data_source:</strong> Fuente de los datos</li>
                </ul>
                
                <div class="footer">
                    <p>Desarrollado para el análisis de criminalidad en México | UTFV 2024</p>
                    <p>Última actualización: {{ timestamp }}</p>
                </div>
            </div>
        </body>
        </html>
        """
        return render_template_string(html_template, timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    
    @app.route('/api/v1/health', methods=['GET'])
    def health_check():
        """Endpoint de verificación de salud"""
        try:
            # Probar conexión a base de datos
            db_status = db_manager.test_connection()
            
            health_data = {
                'api_status': 'healthy',
                'database_status': db_status['status'],
                'timestamp': datetime.now().isoformat(),
                'version': '1.0.0',
                'environment': os.getenv('FLASK_ENV', 'production')
            }
            
            if db_status['status'] != 'success':
                health_data['database_message'] = db_status['message']
            
            response = APIResponse.success(
                data=health_data,
                message="API funcionando correctamente"
            )
            
            return jsonify(response.to_dict()), 200
            
        except Exception as e:
            logger.error(f"Error en health check: {e}")
            response = APIResponse.error(
                message=f"Error en verificación de salud: {str(e)}"
            )
            return jsonify(response.to_dict()), 500
    
    @app.route('/api/v1/crime-data', methods=['GET'])
    def get_crime_data():
        """Obtiene todos los datos de criminalidad"""
        try:
            # Obtener parámetro de límite
            limit = request.args.get('limit', type=int)
            
            # Obtener datos de la base de datos
            result = db_manager.get_all_crime_data(limit=limit)
            
            if result['status'] == 'success':
                response = APIResponse.success(
                    data=result['data'],
                    count=result['count'],
                    message=f"Datos obtenidos exitosamente"
                )
                return jsonify(response.to_dict()), 200
            else:
                response = APIResponse.error(message=result['message'])
                return jsonify(response.to_dict()), 500
                
        except Exception as e:
            logger.error(f"Error al obtener datos de criminalidad: {e}")
            response = APIResponse.error(
                message=f"Error interno del servidor: {str(e)}"
            )
            return jsonify(response.to_dict()), 500
    
    @app.route('/api/v1/crime-data/state/<string:state_name>', methods=['GET'])
    def get_crime_data_by_state(state_name):
        """Obtiene datos de criminalidad por estado"""
        try:
            # Validar nombre del estado
            is_valid, error_message = DataValidator.validate_state_name(state_name)
            if not is_valid:
                response = APIResponse.error(message=error_message)
                return jsonify(response.to_dict()), 400
            
            # Obtener datos de la base de datos
            result = db_manager.get_crime_data_by_state(state_name)
            
            if result['status'] == 'success':
                response = APIResponse.success(
                    data=result['data'],
                    count=result['count'],
                    message=f"Datos obtenidos para {state_name}"
                )
                return jsonify(response.to_dict()), 200
            else:
                response = APIResponse.error(message=result['message'])
                return jsonify(response.to_dict()), 500
                
        except Exception as e:
            logger.error(f"Error al obtener datos por estado: {e}")
            response = APIResponse.error(
                message=f"Error interno del servidor: {str(e)}"
            )
            return jsonify(response.to_dict()), 500
    
    @app.route('/api/v1/statistics', methods=['GET'])
    def get_statistics():
        """Obtiene estadísticas generales"""
        try:
            result = db_manager.get_crime_statistics()
            
            if result['status'] == 'success':
                response = APIResponse.success(
                    data=result['statistics'],
                    message="Estadísticas obtenidas exitosamente"
                )
                return jsonify(response.to_dict()), 200
            else:
                response = APIResponse.error(message=result['message'])
                return jsonify(response.to_dict()), 500
                
        except Exception as e:
            logger.error(f"Error al obtener estadísticas: {e}")
            response = APIResponse.error(
                message=f"Error interno del servidor: {str(e)}"
            )
            return jsonify(response.to_dict()), 500
    
    @app.route('/api/v1/refresh-data', methods=['POST'])
    def refresh_data():
        """Ejecuta el proceso ETL para actualizar datos"""
        try:
            logger.info("🔄 Iniciando actualización de datos...")
            
            # Crear instancia del procesador ETL
            etl = CrimeDataETL()
            
            # Ejecutar proceso ETL completo
            results = etl.run_full_etl()
            
            if results['overall_status'] == 'success':
                response = APIResponse.success(
                    data={
                        'etl_results': results,
                        'updated_at': datetime.now().isoformat()
                    },
                    message="Datos actualizados exitosamente"
                )
                return jsonify(response.to_dict()), 200
            else:
                response = APIResponse.error(
                    message="Error en el proceso ETL",
                    data=results
                )
                return jsonify(response.to_dict()), 500
                
        except Exception as e:
            logger.error(f"Error en actualización de datos: {e}")
            response = APIResponse.error(
                message=f"Error interno del servidor: {str(e)}"
            )
            return jsonify(response.to_dict()), 500
    
    @app.route('/api/v1/metadata', methods=['GET'])
    def get_metadata():
        """Obtiene metadatos de la base de datos"""
        try:
            result = db_manager.get_metadata()
            
            if result['status'] == 'success':
                response = APIResponse.success(
                    data=result['metadata'],
                    message="Metadatos obtenidos exitosamente"
                )
                return jsonify(response.to_dict()), 200
            else:
                response = APIResponse.error(message=result['message'])
                return jsonify(response.to_dict()), 500
                
        except Exception as e:
            logger.error(f"Error al obtener metadatos: {e}")
            response = APIResponse.error(
                message=f"Error interno del servidor: {str(e)}"
            )
            return jsonify(response.to_dict()), 500
    
    # ==================== MANEJO DE ERRORES ====================
    
    @app.errorhandler(404)
    def not_found(error):
        response = APIResponse.error(
            message="Endpoint no encontrado"
        )
        return jsonify(response.to_dict()), 404
    
    @app.errorhandler(405)
    def method_not_allowed(error):
        response = APIResponse.error(
            message="Método HTTP no permitido"
        )
        return jsonify(response.to_dict()), 405
    
    @app.errorhandler(500)
    def internal_error(error):
        response = APIResponse.error(
            message="Error interno del servidor"
        )
        return jsonify(response.to_dict()), 500
    
    # ==================== MIDDLEWARE ====================
    
    @app.before_request
    def log_request_info():
        """Log información de cada request"""
        logger.info(f"📥 {request.method} {request.url} - IP: {request.remote_addr}")
    
    @app.after_request
    def log_response_info(response):
        """Log información de cada response"""
        logger.info(f"📤 {request.method} {request.url} - Status: {response.status_code}")
        return response
    
    return app

# Crear la aplicación
app = create_app(os.getenv('FLASK_ENV', 'default'))

if __name__ == '__main__':
    # Configuración para desarrollo
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'
    
    logger.info(f"🚀 Iniciando servidor Flask en puerto {port}")
    logger.info(f"🔧 Modo debug: {debug}")
    logger.info(f"🌐 Accede a: http://localhost:{port}")
    
    app.run(
        host='0.0.0.0',
        port=port,
        debug=debug
    )
