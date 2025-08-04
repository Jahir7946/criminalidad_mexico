from datetime import datetime
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict
import json

@dataclass
class CrimeTypes:
    """Modelo para tipos de delitos"""
    homicidio: int = 0
    robo: int = 0
    otros: int = 0
    
    def to_dict(self) -> Dict[str, int]:
        return {
            'Homicidio': self.homicidio,
            'Robo': self.robo,
            'Otros': self.otros
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, int]) -> 'CrimeTypes':
        return cls(
            homicidio=data.get('Homicidio', 0),
            robo=data.get('Robo', 0),
            otros=data.get('Otros', 0)
        )
    
    def total(self) -> int:
        return self.homicidio + self.robo + self.otros

@dataclass
class CrimeData:
    """Modelo principal para datos de criminalidad"""
    state: str
    crimes: int
    incidence: float
    types: CrimeTypes
    last_updated: str = None
    data_source: str = "INEGI/SNSP"
    year: int = 2024
    population: Optional[int] = None
    _id: Optional[str] = None
    
    def __post_init__(self):
        if self.last_updated is None:
            self.last_updated = datetime.now().isoformat()
        
        if isinstance(self.types, dict):
            self.types = CrimeTypes.from_dict(self.types)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convierte el modelo a diccionario para MongoDB"""
        data = {
            'state': self.state,
            'crimes': self.crimes,
            'incidence': round(self.incidence, 2),
            'types': self.types.to_dict() if isinstance(self.types, CrimeTypes) else self.types,
            'last_updated': self.last_updated,
            'data_source': self.data_source,
            'year': self.year
        }
        
        if self.population is not None:
            data['population'] = self.population
        
        if self._id is not None:
            data['_id'] = self._id
            
        return data
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'CrimeData':
        """Crea una instancia desde un diccionario"""
        return cls(
            state=data.get('state', ''),
            crimes=data.get('crimes', 0),
            incidence=data.get('incidence', 0.0),
            types=CrimeTypes.from_dict(data.get('types', {})),
            last_updated=data.get('last_updated'),
            data_source=data.get('data_source', 'INEGI/SNSP'),
            year=data.get('year', 2024),
            population=data.get('population'),
            _id=str(data.get('_id')) if data.get('_id') else None
        )
    
    def to_json(self) -> str:
        """Convierte el modelo a JSON"""
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=2)
    
    def calculate_homicide_rate(self) -> float:
        """Calcula la tasa de homicidios por cada 100,000 habitantes"""
        if self.population and self.population > 0:
            homicides = self.types.homicidio if isinstance(self.types, CrimeTypes) else self.types.get('Homicidio', 0)
            return round((homicides / self.population) * 100000, 2)
        return 0.0
    
    def get_crime_distribution(self) -> Dict[str, float]:
        """Obtiene la distribución porcentual de tipos de delitos"""
        if self.crimes == 0:
            return {'Homicidio': 0.0, 'Robo': 0.0, 'Otros': 0.0}
        
        types_dict = self.types.to_dict() if isinstance(self.types, CrimeTypes) else self.types
        
        return {
            crime_type: round((count / self.crimes) * 100, 2)
            for crime_type, count in types_dict.items()
        }

@dataclass
class CrimeStatistics:
    """Modelo para estadísticas generales"""
    total_crimes: int
    avg_incidence: float
    total_states: int
    max_crimes: int
    min_crimes: int
    top_crime_state: Optional[Dict[str, Any]] = None
    last_updated: str = None
    
    def __post_init__(self):
        if self.last_updated is None:
            self.last_updated = datetime.now().isoformat()
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            'total_crimes': self.total_crimes,
            'avg_incidence': round(self.avg_incidence, 2),
            'total_states': self.total_states,
            'max_crimes': self.max_crimes,
            'min_crimes': self.min_crimes,
            'top_crime_state': self.top_crime_state,
            'last_updated': self.last_updated
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'CrimeStatistics':
        return cls(
            total_crimes=data.get('total_crimes', 0),
            avg_incidence=data.get('avg_incidence', 0.0),
            total_states=data.get('total_states', 0),
            max_crimes=data.get('max_crimes', 0),
            min_crimes=data.get('min_crimes', 0),
            top_crime_state=data.get('top_crime_state'),
            last_updated=data.get('last_updated')
        )

@dataclass
class APIResponse:
    """Modelo estándar para respuestas de la API"""
    status: str
    message: str = ""
    data: Optional[Any] = None
    count: Optional[int] = None
    timestamp: str = None
    
    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now().isoformat()
    
    def to_dict(self) -> Dict[str, Any]:
        response = {
            'status': self.status,
            'timestamp': self.timestamp
        }
        
        if self.message:
            response['message'] = self.message
        
        if self.data is not None:
            response['data'] = self.data
        
        if self.count is not None:
            response['count'] = self.count
            
        return response
    
    @classmethod
    def success(cls, data: Any = None, message: str = "Operación exitosa", count: int = None) -> 'APIResponse':
        return cls(
            status="success",
            message=message,
            data=data,
            count=count
        )
    
    @classmethod
    def error(cls, message: str = "Error en la operación", data: Any = None) -> 'APIResponse':
        return cls(
            status="error",
            message=message,
            data=data
        )

@dataclass
class DatabaseMetadata:
    """Modelo para metadatos de la base de datos"""
    total_records: int
    data_source: str
    etl_timestamp: str
    version: str
    last_updated: str = None
    type: str = "crime_data_metadata"
    
    def __post_init__(self):
        if self.last_updated is None:
            self.last_updated = datetime.now().isoformat()
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            'total_records': self.total_records,
            'data_source': self.data_source,
            'etl_timestamp': self.etl_timestamp,
            'version': self.version,
            'last_updated': self.last_updated,
            'type': self.type
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'DatabaseMetadata':
        return cls(
            total_records=data.get('total_records', 0),
            data_source=data.get('data_source', ''),
            etl_timestamp=data.get('etl_timestamp', ''),
            version=data.get('version', '1.0'),
            last_updated=data.get('last_updated'),
            type=data.get('type', 'crime_data_metadata')
        )

class DataValidator:
    """Validador de datos"""
    
    @staticmethod
    def validate_crime_data(data: Dict[str, Any]) -> tuple[bool, List[str]]:
        """Valida datos de criminalidad"""
        errors = []
        
        # Campos requeridos
        required_fields = ['state', 'crimes', 'incidence']
        for field in required_fields:
            if field not in data or data[field] is None:
                errors.append(f"Campo requerido faltante: {field}")
        
        # Validaciones de tipo y rango
        if 'crimes' in data:
            if not isinstance(data['crimes'], (int, float)) or data['crimes'] < 0:
                errors.append("El campo 'crimes' debe ser un número no negativo")
        
        if 'incidence' in data:
            if not isinstance(data['incidence'], (int, float)) or data['incidence'] < 0:
                errors.append("El campo 'incidence' debe ser un número no negativo")
        
        if 'state' in data:
            if not isinstance(data['state'], str) or len(data['state'].strip()) == 0:
                errors.append("El campo 'state' debe ser una cadena no vacía")
        
        if 'year' in data:
            current_year = datetime.now().year
            if not isinstance(data['year'], int) or data['year'] < 2000 or data['year'] > current_year + 1:
                errors.append(f"El campo 'year' debe ser un año válido entre 2000 y {current_year + 1}")
        
        return len(errors) == 0, errors
    
    @staticmethod
    def validate_state_name(state_name: str) -> tuple[bool, str]:
        """Valida nombre de estado"""
        if not isinstance(state_name, str):
            return False, "El nombre del estado debe ser una cadena"
        
        if len(state_name.strip()) == 0:
            return False, "El nombre del estado no puede estar vacío"
        
        if len(state_name) > 100:
            return False, "El nombre del estado es demasiado largo"
        
        return True, ""

# Utilidades para conversión de datos
class DataConverter:
    """Convertidor de datos entre diferentes formatos"""
    
    @staticmethod
    def dict_list_to_crime_data_list(data_list: List[Dict[str, Any]]) -> List[CrimeData]:
        """Convierte lista de diccionarios a lista de CrimeData"""
        return [CrimeData.from_dict(item) for item in data_list]
    
    @staticmethod
    def crime_data_list_to_dict_list(crime_data_list: List[CrimeData]) -> List[Dict[str, Any]]:
        """Convierte lista de CrimeData a lista de diccionarios"""
        return [item.to_dict() for item in crime_data_list]
    
    @staticmethod
    def prepare_for_json_response(data: Any) -> Any:
        """Prepara datos para respuesta JSON"""
        if isinstance(data, list):
            return [item.to_dict() if hasattr(item, 'to_dict') else item for item in data]
        elif hasattr(data, 'to_dict'):
            return data.to_dict()
        else:
            return data

# Estados válidos de México para validación
VALID_MEXICAN_STATES = {
    'Aguascalientes', 'Baja California', 'Baja California Sur', 'Campeche',
    'Chiapas', 'Chihuahua', 'Ciudad de México', 'Coahuila', 'Colima',
    'Durango', 'Estado de México', 'Guanajuato', 'Guerrero', 'Hidalgo',
    'Jalisco', 'Michoacán', 'Morelos', 'Nayarit', 'Nuevo León', 'Oaxaca',
    'Puebla', 'Querétaro', 'Quintana Roo', 'San Luis Potosí', 'Sinaloa',
    'Sonora', 'Tabasco', 'Tamaulipas', 'Tlaxcala', 'Veracruz', 'Yucatán',
    'Zacatecas'
}

def is_valid_mexican_state(state_name: str) -> bool:
    """Verifica si un nombre de estado es válido en México"""
    return state_name.strip().title() in VALID_MEXICAN_STATES
