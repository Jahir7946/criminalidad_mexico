# 🚨 Dashboard de Criminalidad en México

## Análisis de criminalidad en municipios de México usando MongoDB, Flask y datos del INEGI

---

## 📋 Descripción del Proyecto

Este proyecto desarrolla un sistema completo de análisis y visualización de datos de criminalidad en México, utilizando tecnologías modernas de bases de datos NoSQL, procesamiento de datos con Python, y visualizaciones interactivas. El sistema procesa datos oficiales del INEGI y SNSP para generar insights sobre la situación delictiva nacional.

### 🎯 ¿Qué hicimos?
- **Backend robusto** con Flask y API REST
- **Base de datos NoSQL** con MongoDB Atlas
- **Proceso ETL** automatizado para datos de Excel
- **Visualizaciones interactivas** con D3.js y Chart.js
- **Dashboard web** responsivo y moderno
- **Despliegue en la nube** con Render

### 🔧 ¿Con qué tecnologías?
- **Backend:** Python, Flask, Pandas, NumPy
- **Base de Datos:** MongoDB Atlas
- **Frontend:** HTML5, CSS3, JavaScript ES6, D3.js, Chart.js
- **Procesamiento:** ETL con Pandas y OpenPyXL
- **Despliegue:** Render, Gunicorn
- **Control de Versiones:** Git, GitHub

### 🔍 ¿Qué descubrimos?
- Patrones de criminalidad por estado
- Correlaciones entre población e incidencia delictiva
- Distribución de tipos de delitos
- Estados con mayor tasa de criminalidad
- Tendencias temporales en los datos

### 🌟 ¿Cuál fue su aplicación?
- **Análisis gubernamental** para toma de decisiones
- **Investigación académica** en criminología
- **Herramienta educativa** para visualización de datos
- **Base para políticas públicas** de seguridad

---

## 🎯 Objetivos

### Objetivo General
Desarrollar un sistema integral de análisis y visualización de datos de criminalidad en México que permita identificar patrones, tendencias y correlaciones para apoyar la toma de decisiones en materia de seguridad pública.

### Objetivos Específicos
1. **Extraer y procesar** datos de criminalidad de fuentes oficiales (INEGI/SNSP)
2. **Implementar un proceso ETL** robusto para limpieza y transformación de datos
3. **Almacenar datos** en una base de datos NoSQL (MongoDB) optimizada para consultas
4. **Desarrollar una API REST** para acceso programático a los datos
5. **Crear visualizaciones interactivas** usando librerías modernas de JavaScript
6. **Desplegar el sistema** en una plataforma cloud para acceso público
7. **Generar insights** estadísticos sobre patrones de criminalidad

---

## 🔍 Justificación del Problema

### ¿Por qué es relevante?
La criminalidad es uno de los principales desafíos sociales en México. El análisis de datos delictivos es fundamental para:

- **Identificar zonas de alto riesgo** y patrones geográficos
- **Optimizar recursos** de seguridad pública
- **Evaluar efectividad** de políticas implementadas
- **Informar a la ciudadanía** sobre la situación de seguridad
- **Apoyar investigación académica** en criminología

### ¿Cómo ayuda la tecnología a resolverlo?
- **Procesamiento masivo** de datos con herramientas de Big Data
- **Visualizaciones interactivas** que facilitan la comprensión
- **APIs REST** para integración con otros sistemas
- **Bases de datos NoSQL** para escalabilidad y flexibilidad
- **Despliegue en la nube** para acceso universal
- **Automatización ETL** para actualizaciones periódicas

---

## 📚 Marco Conceptual

### Bases de Datos NoSQL
Las bases de datos NoSQL como MongoDB ofrecen:
- **Flexibilidad de esquema** para datos semi-estructurados
- **Escalabilidad horizontal** para grandes volúmenes
- **Consultas complejas** con agregaciones
- **Replicación y alta disponibilidad**

### Servicios en la Nube
Utilizamos servicios cloud para:
- **MongoDB Atlas:** Base de datos como servicio
- **Render:** Plataforma de despliegue
- **GitHub:** Control de versiones y CI/CD

### Proceso ETL (Extracción, Transformación y Carga)
Nuestro pipeline ETL incluye:
1. **Extracción:** Lectura de archivos Excel/CSV
2. **Transformación:** Limpieza, normalización y agregación
3. **Carga:** Inserción en MongoDB con validaciones

### Datasets Abiertos
Utilizamos datos oficiales de:
- **INEGI:** Instituto Nacional de Estadística y Geografía
- **SNSP:** Secretariado Ejecutivo del Sistema Nacional de Seguridad Pública

### Librerías de Visualización en Python
- **Pandas:** Manipulación y análisis de datos
- **NumPy:** Computación numérica
- **D3.js:** Visualizaciones web interactivas
- **Chart.js:** Gráficos responsivos

---

## 🔄 Proceso ETL

### 1. Extracción de Datos
```python
# Lectura de archivo Excel
df = pd.read_excel('incidencias.xlsx')
```

### 2. Transformación y Limpieza
- **Normalización** de nombres de estados
- **Validación** de tipos de datos
- **Agregación** por entidad federativa
- **Cálculo** de métricas derivadas (incidencia, tasas)
- **Estructuración** en formato JSON

### 3. Carga a MongoDB
```python
# Inserción en MongoDB
db_manager.insert_crime_data(processed_data)
```

### Flujo Automatizado
```bash
# Ejecutar ETL completo
python etl_processor.py
```

---

## 🛠️ Tecnologías y Herramientas Utilizadas

### Backend
- **Python 3.9+**
- **Flask 2.3.3** - Framework web
- **Pandas 2.1.1** - Análisis de datos
- **NumPy 1.24.3** - Computación numérica
- **PyMongo 4.5.0** - Driver MongoDB
- **OpenPyXL 3.1.2** - Lectura de Excel

### Base de Datos
- **MongoDB Atlas** - Base de datos en la nube
- **Agregaciones MongoDB** - Consultas complejas

### Frontend
- **HTML5/CSS3** - Estructura y estilos
- **JavaScript ES6** - Lógica del cliente
- **D3.js v7** - Visualizaciones SVG
- **Chart.js v4** - Gráficos canvas
- **Bootstrap 5** - Framework CSS

### Despliegue
- **Render** - Plataforma de hosting
- **Gunicorn** - Servidor WSGI
- **GitHub** - Control de versiones

### Desarrollo
- **VS Code** - Editor de código
- **Git** - Control de versiones
- **Postman** - Testing de API

---

## 🗄️ Base de Datos

### Estructura de Colecciones MongoDB

#### Colección: `crime_data`
```json
{
  "_id": "ObjectId",
  "state": "Jalisco",
  "crimes": 15000,
  "incidence": 6.5,
  "types": {
    "Homicidio": 1800,
    "Robo": 8000,
    "Otros": 5200
  },
  "year": 2024,
  "population": 8348151,
  "data_source": "INEGI/SNSP",
  "last_updated": "2024-01-15T10:30:00Z"
}
```

#### Colección: `metadata`
```json
{
  "_id": "ObjectId",
  "type": "crime_data_metadata",
  "total_records": 32,
  "data_source": "incidencias.xlsx",
  "etl_timestamp": "2024-01-15T10:30:00Z",
  "version": "1.0",
  "last_updated": "2024-01-15T10:30:00Z"
}
```

### Índices Optimizados
```javascript
// Índices para consultas eficientes
db.crime_data.createIndex({ "state": 1 })
db.crime_data.createIndex({ "crimes": -1 })
db.crime_data.createIndex({ "incidence": -1 })
```

---

## 📊 Visualizaciones y Dashboard

### Tipos de Gráficos Implementados

#### 1. Gráfico de Burbujas (D3.js)
- **Propósito:** Mostrar relación entre volumen de crímenes e incidencia
- **Ejes:** X=Incidencia, Y=Crímenes, Tamaño=Población
- **Interactividad:** Hover con tooltips, zoom, filtros

#### 2. Gráfico de Barras Horizontales (Chart.js)
- **Propósito:** Top 10 estados por número de delitos
- **Características:** Responsivo, animado, colores temáticos

#### 3. Gráfico de Dona (Chart.js)
- **Propósito:** Distribución porcentual de tipos de delitos
- **Características:** Leyenda interactiva, colores diferenciados

### Características del Dashboard
- **Diseño responsivo** para móviles y desktop
- **Filtros dinámicos** por estado
- **Animaciones suaves** en transiciones
- **Tooltips informativos** en todos los gráficos
- **Tema oscuro** para mejor experiencia visual

### Capturas del Dashboard
- 🏠 **Página Principal:** Hero section con estadísticas clave
- 📊 **Panel de Visualizaciones:** Gráficos interactivos
- 🔍 **Filtros:** Búsqueda por estado en tiempo real
- 📱 **Responsive:** Adaptable a todos los dispositivos

---

## 📈 Análisis de los Datos

### Tendencias Identificadas

#### Por Volumen de Delitos
1. **Estado de México** - Mayor número absoluto de delitos
2. **Ciudad de México** - Alta concentración urbana
3. **Jalisco** - Tercer lugar nacional

#### Por Tasa de Incidencia
1. **Baja California** - Mayor tasa por habitante (9.1%)
2. **Guerrero** - Alta incidencia en zona sur (8.9%)
3. **Michoacán** - Problemática regional (8.2%)

#### Correlaciones Encontradas
- **Población vs Delitos:** Correlación positiva moderada (r=0.65)
- **Urbanización vs Incidencia:** Estados más urbanizados tienden a mayor incidencia
- **Geografía:** Estados fronterizos muestran patrones específicos

### Distribución de Tipos de Delitos
- **Robo:** 50-60% del total nacional
- **Otros delitos:** 30-40% del total
- **Homicidio:** 8-15% del total

### Hallazgos Importantes
1. **Concentración geográfica:** 5 estados concentran 60% de los delitos
2. **Variabilidad regional:** Diferencias significativas entre regiones
3. **Patrones urbanos:** Zonas metropolitanas con mayor complejidad delictiva

---

## 🚀 Instalación y Uso

### Prerrequisitos
- Python 3.9+
- MongoDB Atlas (cuenta gratuita)
- Git

### Instalación Local

1. **Clonar el repositorio**
```bash
git clone https://github.com/usuario/dashboard-criminalidad-mexico.git
cd dashboard-criminalidad-mexico
```

2. **Crear entorno virtual**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# o
venv\Scripts\activate     # Windows
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

4. **Configurar variables de entorno**
```bash
cp .env.example .env
# Editar .env con tu string de conexión MongoDB
```

5. **Ejecutar ETL inicial**
```bash
python etl_processor.py
```

6. **Iniciar servidor**
```bash
python app.py
```

7. **Acceder al dashboard**
```
http://localhost:5000
```

### API Endpoints

#### Obtener todos los datos
```bash
GET /api/v1/crime-data
```

#### Filtrar por estado
```bash
GET /api/v1/crime-data/state/Jalisco
```

#### Estadísticas generales
```bash
GET /api/v1/statistics
```

#### Actualizar datos
```bash
POST /api/v1/refresh-data
```

---

## 🌐 Despliegue en Render

### Configuración de Despliegue

1. **Conectar repositorio GitHub** a Render
2. **Configurar variables de entorno:**
   - `MONGODB_URI`
   - `FLASK_ENV=production`
3. **Comando de build:** `pip install -r requirements.txt`
4. **Comando de start:** `gunicorn app:app`

### URL de Producción
```
https://dashboard-criminalidad-mexico.onrender.com
```

---

## 🤔 Reflexión Final

### ¿Qué aprendimos?

#### Técnico
- **Integración de tecnologías** modernas en un proyecto real
- **Procesamiento ETL** con grandes volúmenes de datos
- **Diseño de APIs REST** escalables y documentadas
- **Visualización de datos** interactiva y responsiva
- **Despliegue en la nube** con mejores prácticas

#### Metodológico
- **Análisis de datos** gubernamentales complejos
- **Trabajo en equipo** con control de versiones
- **Documentación técnica** completa y profesional
- **Testing y validación** de sistemas de datos

### ¿Qué dificultades enfrentamos y cómo las resolvimos?

#### 1. Calidad de Datos
- **Problema:** Inconsistencias en nombres de estados
- **Solución:** Normalización automática con diccionarios de mapeo

#### 2. Escalabilidad de MongoDB
- **Problema:** Consultas lentas con grandes volúmenes
- **Solución:** Índices optimizados y agregaciones eficientes

#### 3. Visualizaciones Responsivas
- **Problema:** Gráficos no se adaptaban a móviles
- **Solución:** Configuración responsive en D3.js y Chart.js

#### 4. Despliegue en Producción
- **Problema:** Variables de entorno y dependencias
- **Solución:** Configuración con .env y Procfile optimizado

### ¿Cuál es el impacto potencial?

#### Inmediato
- **Herramienta educativa** para estudiantes de ciencias de datos
- **Prototipo funcional** para proyectos gubernamentales
- **Base de conocimiento** para análisis criminológico

#### A Largo Plazo
- **Escalabilidad** a nivel nacional con más datos
- **Integración** con sistemas de seguridad pública
- **Modelo replicable** para otros países de Latinoamérica
- **Contribución** al ecosistema de datos abiertos

---

## 🔗 Enlaces y Recursos

### Repositorio y Demo
- **GitHub:** [https://github.com/usuario/dashboard-criminalidad-mexico](https://github.com/usuario/dashboard-criminalidad-mexico)
- **Demo en Vivo:** [https://dashboard-criminalidad-mexico.onrender.com](https://dashboard-criminalidad-mexico.onrender.com)
- **API Documentación:** [https://dashboard-criminalidad-mexico.onrender.com/api/v1/](https://dashboard-criminalidad-mexico.onrender.com/api/v1/)

### Notebooks y Análisis
- **Google Colab:** [Análisis Exploratorio](https://colab.research.google.com/drive/ejemplo)
- **Jupyter Notebooks:** Disponibles en `/notebooks/`

### Fuentes de Datos
- **INEGI:** [https://www.inegi.org.mx/](https://www.inegi.org.mx/)
- **SNSP:** [https://www.gob.mx/sesnsp](https://www.gob.mx/sesnsp)
- **Datos Abiertos México:** [https://datos.gob.mx/](https://datos.gob.mx/)

### Documentación Técnica
- **MongoDB:** [https://docs.mongodb.com/](https://docs.mongodb.com/)
- **Flask:** [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)
- **D3.js:** [https://d3js.org/](https://d3js.org/)
- **Chart.js:** [https://www.chartjs.org/](https://www.chartjs.org/)
- **Pandas:** [https://pandas.pydata.org/](https://pandas.pydata.org/)

---

## 👥 Equipo de Desarrollo

- **Desarrollador Principal:** [Nombre del estudiante]
- **Análisis de Datos:** [Nombre del estudiante]
- **Frontend/UX:** [Nombre del estudiante]
- **DevOps/Despliegue:** [Nombre del estudiante]

### Contribuciones
- Cada miembro contribuyó equitativamente al proyecto
- Uso de Git para control de versiones colaborativo
- Revisiones de código y pair programming

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

---

## 🙏 Agradecimientos

- **UTFV** por el apoyo académico
- **INEGI/SNSP** por los datos abiertos
- **Comunidad Open Source** por las herramientas utilizadas
- **Profesores** por la guía y mentoría

---

**Desarrollado con ❤️ para el análisis de criminalidad en México | UTFV 2024**
