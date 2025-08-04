import logging
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError
from config import Config
from datetime import datetime
import json

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DatabaseManager:
    """Gestor de conexiones y operaciones con MongoDB"""
    
    def __init__(self):
        self.client = None
        self.db = None
        self.collection = None
        self._connect()
    
    def _connect(self):
        """Establece conexión con MongoDB"""
        try:
            # Validar configuración
            Config.validate_config()
            
            # Crear cliente MongoDB
            self.client = MongoClient(
                Config.MONGODB_URI,
                serverSelectionTimeoutMS=5000,  # 5 segundos timeout
                connectTimeoutMS=10000,         # 10 segundos timeout
                socketTimeoutMS=20000           # 20 segundos timeout
            )
            
            # Probar conexión
            self.client.admin.command('ping')
            
            # Seleccionar base de datos y colección
            self.db = self.client[Config.DATABASE_NAME]
            self.collection = self.db[Config.COLLECTION_NAME]
            
            logger.info(f"✅ Conexión exitosa a MongoDB: {Config.DATABASE_NAME}")
            
        except (ConnectionFailure, ServerSelectionTimeoutError) as e:
            logger.error(f"❌ Error de conexión a MongoDB: {e}")
            raise
        except Exception as e:
            logger.error(f"❌ Error inesperado al conectar a MongoDB: {e}")
            raise
    
    def test_connection(self):
        """Prueba la conexión a la base de datos"""
        try:
            self.client.admin.command('ping')
            return {"status": "success", "message": "Conexión exitosa"}
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    def insert_crime_data(self, data):
        """Inserta datos de criminalidad en la base de datos"""
        try:
            if isinstance(data, list):
                # Insertar múltiples documentos
                result = self.collection.insert_many(data)
                logger.info(f"✅ Insertados {len(result.inserted_ids)} documentos")
                return {
                    "status": "success",
                    "inserted_count": len(result.inserted_ids),
                    "inserted_ids": [str(id) for id in result.inserted_ids]
                }
            else:
                # Insertar un solo documento
                result = self.collection.insert_one(data)
                logger.info(f"✅ Insertado documento con ID: {result.inserted_id}")
                return {
                    "status": "success",
                    "inserted_count": 1,
                    "inserted_id": str(result.inserted_id)
                }
        except Exception as e:
            logger.error(f"❌ Error al insertar datos: {e}")
            return {"status": "error", "message": str(e)}
    
    def get_all_crime_data(self, limit=None):
        """Obtiene todos los datos de criminalidad"""
        try:
            cursor = self.collection.find({})
            if limit:
                cursor = cursor.limit(limit)
            
            data = list(cursor)
            
            # Convertir ObjectId a string para JSON serialization
            for item in data:
                if '_id' in item:
                    item['_id'] = str(item['_id'])
            
            logger.info(f"✅ Obtenidos {len(data)} documentos")
            return {
                "status": "success",
                "count": len(data),
                "data": data
            }
        except Exception as e:
            logger.error(f"❌ Error al obtener datos: {e}")
            return {"status": "error", "message": str(e)}
    
    def get_crime_data_by_state(self, state_name):
        """Obtiene datos de criminalidad filtrados por estado"""
        try:
            # Búsqueda case-insensitive
            query = {"state": {"$regex": state_name, "$options": "i"}}
            data = list(self.collection.find(query))
            
            # Convertir ObjectId a string
            for item in data:
                if '_id' in item:
                    item['_id'] = str(item['_id'])
            
            logger.info(f"✅ Obtenidos {len(data)} documentos para el estado: {state_name}")
            return {
                "status": "success",
                "count": len(data),
                "state": state_name,
                "data": data
            }
        except Exception as e:
            logger.error(f"❌ Error al obtener datos por estado: {e}")
            return {"status": "error", "message": str(e)}
    
    def get_crime_statistics(self):
        """Obtiene estadísticas generales de criminalidad"""
        try:
            pipeline = [
                {
                    "$group": {
                        "_id": None,
                        "total_crimes": {"$sum": "$crimes"},
                        "avg_incidence": {"$avg": "$incidence"},
                        "total_states": {"$addToSet": "$state"},
                        "max_crimes": {"$max": "$crimes"},
                        "min_crimes": {"$min": "$crimes"}
                    }
                },
                {
                    "$project": {
                        "_id": 0,
                        "total_crimes": 1,
                        "avg_incidence": {"$round": ["$avg_incidence", 2]},
                        "total_states": {"$size": "$total_states"},
                        "max_crimes": 1,
                        "min_crimes": 1
                    }
                }
            ]
            
            result = list(self.collection.aggregate(pipeline))
            
            if result:
                stats = result[0]
                
                # Obtener estado con más crímenes
                top_state = self.collection.find_one(
                    {"crimes": stats["max_crimes"]},
                    {"state": 1, "crimes": 1, "_id": 0}
                )
                
                if top_state:
                    stats["top_crime_state"] = top_state
                
                logger.info("✅ Estadísticas generales obtenidas")
                return {
                    "status": "success",
                    "statistics": stats,
                    "last_updated": datetime.now().isoformat()
                }
            else:
                return {
                    "status": "success",
                    "statistics": {},
                    "message": "No hay datos disponibles"
                }
                
        except Exception as e:
            logger.error(f"❌ Error al obtener estadísticas: {e}")
            return {"status": "error", "message": str(e)}
    
    def clear_collection(self):
        """Limpia todos los datos de la colección"""
        try:
            result = self.collection.delete_many({})
            logger.info(f"✅ Eliminados {result.deleted_count} documentos")
            return {
                "status": "success",
                "deleted_count": result.deleted_count
            }
        except Exception as e:
            logger.error(f"❌ Error al limpiar colección: {e}")
            return {"status": "error", "message": str(e)}
    
    def update_metadata(self, metadata):
        """Actualiza metadatos de la base de datos"""
        try:
            metadata_collection = self.db['metadata']
            metadata['last_updated'] = datetime.now().isoformat()
            
            result = metadata_collection.replace_one(
                {"type": "crime_data_metadata"},
                {**metadata, "type": "crime_data_metadata"},
                upsert=True
            )
            
            logger.info("✅ Metadatos actualizados")
            return {"status": "success", "metadata": metadata}
        except Exception as e:
            logger.error(f"❌ Error al actualizar metadatos: {e}")
            return {"status": "error", "message": str(e)}
    
    def get_metadata(self):
        """Obtiene metadatos de la base de datos"""
        try:
            metadata_collection = self.db['metadata']
            metadata = metadata_collection.find_one({"type": "crime_data_metadata"})
            
            if metadata:
                metadata['_id'] = str(metadata['_id'])
                return {"status": "success", "metadata": metadata}
            else:
                return {"status": "success", "metadata": None}
        except Exception as e:
            logger.error(f"❌ Error al obtener metadatos: {e}")
            return {"status": "error", "message": str(e)}
    
    def close_connection(self):
        """Cierra la conexión a MongoDB"""
        if self.client:
            self.client.close()
            logger.info("🔒 Conexión a MongoDB cerrada")

# Instancia global del gestor de base de datos
db_manager = DatabaseManager()
