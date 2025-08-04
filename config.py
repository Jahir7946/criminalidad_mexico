import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

class Config:
    """Configuración base de la aplicación"""
    
    # MongoDB Configuration
    MONGODB_URI = os.getenv('MONGODB_URI')
    DATABASE_NAME = os.getenv('DATABASE_NAME', 'criminalidad_mexico')
    COLLECTION_NAME = os.getenv('COLLECTION_NAME', 'crime_data')
    
    # Flask Configuration
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')
    DEBUG = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'
    
    # API Configuration
    API_VERSION = os.getenv('API_VERSION', 'v1')
    CORS_ORIGINS = os.getenv('CORS_ORIGINS', '*')
    
    # Data Configuration
    DATA_SOURCE = os.getenv('DATA_SOURCE', 'incidencias.xlsx')
    LAST_UPDATE = os.getenv('LAST_UPDATE', '2024-01-01')
    
    # Logging Configuration
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    
    @staticmethod
    def validate_config():
        """Valida que las configuraciones críticas estén presentes"""
        required_vars = ['MONGODB_URI', 'DATABASE_NAME']
        missing_vars = []
        
        for var in required_vars:
            if not getattr(Config, var):
                missing_vars.append(var)
        
        if missing_vars:
            raise ValueError(f"Variables de configuración faltantes: {', '.join(missing_vars)}")
        
        return True

class DevelopmentConfig(Config):
    """Configuración para desarrollo"""
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    """Configuración para producción"""
    DEBUG = False
    TESTING = False

class TestingConfig(Config):
    """Configuración para testing"""
    DEBUG = True
    TESTING = True
    DATABASE_NAME = 'test_criminalidad_mexico'

# Configuración por defecto
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
