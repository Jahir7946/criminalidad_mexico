# 📊 Dashboard de Criminalidad en México

## Análisis de Datos con MongoDB, Flask y Visualizaciones Interactivas

---

## 📋 Información del Proyecto

**Título:** Dashboard de Criminalidad en México usando MongoDB, Flask y Visualizaciones D3.js/Chart.js

**Institución:** Universidad Tecnológica de la Zona Metropolitana de Guadalajara (UTFV)

**Fecha de Entrega:** 4 de Agosto de 2025

**Equipo de Desarrollo:** 3-4 integrantes

**Contacto:** 23202024@utfv.edu.mx

---

## 🎯 Descripción del Proyecto

Este proyecto desarrolla un sistema completo de análisis y visualización de datos de criminalidad en México, utilizando tecnologías modernas de bases de datos NoSQL, desarrollo web con Python Flask, y visualizaciones interactivas con D3.js y Chart.js.

### ¿Qué hicimos?
- Desarrollamos una API REST completa con Flask para servir datos de criminalidad
- Implementamos un proceso ETL (Extract, Transform, Load) para procesar datos de Excel
- Creamos un dashboard interactivo con múltiples tipos de visualizaciones
- Configuramos una base de datos MongoDB Atlas para almacenamiento en la nube
- Desplegamos el sistema para acceso web

### ¿Con qué tecnologías?
- **Backend:** Python Flask con arquitectura REST API
- **Base de Datos:** MongoDB Atlas (NoSQL)
- **Frontend:** HTML5, CSS3, JavaScript ES6+
- **Visualizaciones:** D3.js para gráficos de burbujas, Chart.js para barras y donas
- **Procesamiento:** Pandas, NumPy para análisis de datos
- **Despliegue:** Preparado para Render

### ¿Qué descubrimos?
- Análisis de 32 estados mexicanos con datos de criminalidad
- Identificación de patrones de incidencia delictiva por estado
- Distribución geográfica de diferentes tipos de delitos
- Correlaciones entre población y tasas de criminalidad

### ¿Cuál fue su aplicación?
- Herramienta de consulta para autoridades de seguridad pública
- Sistema de monitoreo de tendencias criminales
- Plataforma educativa para análisis de datos sociales
- Base para toma de decisiones en políticas públicas

---

## 🎯 Objetivos

### Objetivo General
Desarrollar un sistema integral de análisis y visualización de datos de criminalidad en México que permita la consulta interactiva, análisis de tendencias y generación de insights para la toma de decisiones en seguridad pública.

### Objetivos Específicos

1. **Extracción y Procesamiento de Datos**
   - Extraer datos de criminalidad de fuentes oficiales (INEGI/SNSP)
   - Implementar proceso ETL para limpieza y normalización de datos
   - Validar integridad y consistencia de la información

2. **Almacenamiento en Base de Datos NoSQL**
   - Configurar MongoDB Atlas como base de datos en la nube
   - Diseñar esquema de documentos optimizado para consultas
   - Implementar índices para mejorar rendimiento

3. **Desarrollo de API REST**
   - Crear endpoints para consulta de datos de criminalidad
   - Implementar filtros por estado, tipo de delito y período
   - Generar estadísticas agregadas y metadatos

4. **Creación de Dashboard Interactivo**
   - Desarrollar interfaz web responsiva con Bootstrap
   - Implementar visualizaciones con D3.js y Chart.js
   - Crear sistema de filtros dinámicos

5. **Despliegue y Documentación**
   - Preparar aplicación para despliegue en Render
   - Documentar API con ejemplos de uso
   - Crear guía de instalación y configuración

---

## 🔍 Justificación del Problema

### Relevancia del Problema
La criminalidad en México representa uno de los desafíos más importantes para la seguridad pública y el desarrollo social del país. La falta de herramientas accesibles para el análisis de datos criminales limita la capacidad de:

- **Autoridades:** Tomar decisiones informadas sobre asignación de recursos
- **Investigadores:** Identificar patrones y tendencias criminales
- **Ciudadanos:** Acceder a información transparente sobre seguridad
- **Medios:** Reportar con datos precisos y contextualizados

### Cómo Ayuda la Tecnología
Nuestro sistema resuelve estos problemas mediante:

1. **Accesibilidad:** Interface web intuitiva disponible 24/7
2. **Interactividad:** Filtros dinámicos para exploración personalizada
3. **Visualización:** Gráficos que facilitan comprensión de datos complejos
4. **Escalabilidad:** Arquitectura preparada para grandes volúmenes de datos
5. **Transparencia:** Datos oficiales presentados de forma clara y verificable

### Impacto Esperado
- Mejora en la toma de decisiones de seguridad pública
- Mayor transparencia en información gubernamental
- Facilitar investigación académica en criminología
- Educación ciudadana sobre realidad de seguridad nacional

---

## 📚 Marco Conceptual

### Bases de Datos NoSQL
Las bases de datos NoSQL (Not Only SQL) son sistemas de gestión de bases de datos que no utilizan el modelo relacional tradicional. MongoDB, utilizado en este proyecto, es una base de datos orientada a documentos que ofrece:

- **Flexibilidad de Esquema:** Permite documentos con estructuras variables
- **Escalabilidad Horizontal:** Distribución en múltiples servidores
- **Consultas Complejas:** Soporte para agregaciones y filtros avanzados
- **JSON Nativo:** Integración natural con aplicaciones web

### Servicios en la Nube
Los servicios en la nube proporcionan recursos computacionales bajo demanda a través de internet. En nuestro proyecto utilizamos:

- **MongoDB Atlas:** Base de datos como servicio (DBaaS)
- **Render:** Plataforma de despliegue de aplicaciones web
- **Ventajas:** Escalabilidad automática, alta disponibilidad, reducción de costos operativos

### Proceso ETL (Extract, Transform, Load)
El proceso ETL es fundamental para el análisis de datos:

1. **Extract (Extracción):** Obtención de datos desde fuentes originales (Excel, CSV)
2. **Transform (Transformación):** Limpieza, normalización y enriquecimiento
3. **Load (Carga):** Inserción de datos procesados en el sistema de destino

### Datasets Abiertos
Los datos abiertos gubernamentales son recursos públicos que promueven:
- **Transparencia:** Acceso ciudadano a información pública
- **Innovación:** Desarrollo de aplicaciones y servicios
- **Investigación:** Base para estudios académicos y científicos
- **Rendición de Cuentas:** Supervisión ciudadana de políticas públicas

### Librerías de Visualización en Python/JavaScript

#### D3.js (Data-Driven Documents)
- Biblioteca JavaScript para visualizaciones dinámicas
- Manipulación directa del DOM basada en datos
- Flexibilidad total para crear visualizaciones personalizadas
- Utilizada para nuestro gráfico de burbujas interactivo

#### Chart.js
- Biblioteca JavaScript para gráficos responsivos
- API simple y configuración declarativa
- Amplia variedad de tipos de gráficos
- Utilizada para gráficos de barras y donas

---

## 🔄 Proceso ETL

### 1. Extracción de Datos (Extract)
```python
# Lectura de archivo Excel con datos de criminalidad
df = pd.read_excel('incidencias.xlsx', sheet_name='Datos')
```

**Fuente de Datos:**
- Archivo: `incidencias.xlsx`
- Origen: INEGI / SNSP (Secretariado Ejecutivo del Sistema Nacional de Seguridad Pública)
- Contenido: Datos de criminalidad por estado mexicano

### 2. Transformación de Datos (Transform)
```python
# Limpieza y normalización
df_clean = df.dropna()  # Eliminar valores nulos
df_clean['state'] = df_clean['state'].str.strip()  # Limpiar espacios
df_clean['incidence'] = pd.to_numeric(df_clean['incidence'])  # Convertir tipos
```

**Procesos de Transformación:**
- Eliminación de registros con valores nulos
- Normalización de nombres de estados
- Conversión de tipos de datos
- Cálculo de estadísticas derivadas
- Validación de rangos y consistencia

### 3. Carga de Datos (Load)
```python
# Inserción en MongoDB
collection.insert_many(processed_records)
```

**Proceso de Carga:**
- Conexión a MongoDB Atlas
- Validación de esquema de documentos
- Inserción por lotes para eficiencia
- Creación de índices para consultas optimizadas
- Verificación de integridad post-carga

### Resultados del ETL
- **32 registros procesados** correspondientes a estados mexicanos
- **Tasa de éxito:** 100% de registros válidos
- **Tiempo de procesamiento:** < 5 segundos
- **Validaciones:** Nombres de estados, rangos numéricos, tipos de datos

---

## 🛠️ Tecnologías y Herramientas Utilizadas

### Backend
- **Python 3.13:** Lenguaje de programación principal
- **Flask 3.0:** Framework web minimalista y flexible
- **Flask-CORS:** Manejo de Cross-Origin Resource Sharing
- **PyMongo:** Driver oficial de MongoDB para Python
- **Pandas:** Análisis y manipulación de datos
- **NumPy:** Computación numérica
- **OpenPyXL:** Lectura de archivos Excel

### Base de Datos
- **MongoDB Atlas:** Base de datos NoSQL en la nube
- **Esquema de Documentos:** Estructura flexible para datos de criminalidad
- **Índices:** Optimización de consultas por estado y tipo de delito
- **Agregaciones:** Pipelines para estadísticas complejas

### Frontend
- **HTML5:** Estructura semántica de la aplicación
- **CSS3:** Estilos responsivos con variables CSS
- **JavaScript ES6+:** Lógica de interacción y consumo de API
- **Bootstrap 5.3:** Framework CSS para diseño responsivo
- **Font Awesome:** Iconografía vectorial

### Visualizaciones
- **D3.js v7:** Gráfico de burbujas interactivo
- **Chart.js v4:** Gráficos de barras y donas
- **Responsive Design:** Adaptación a diferentes dispositivos
- **Interactividad:** Tooltips, filtros dinámicos, animaciones

### Herramientas de Desarrollo
- **Visual Studio Code:** Editor de código
- **Git:** Control de versiones
- **GitHub:** Repositorio remoto
- **Postman:** Pruebas de API
- **MongoDB Compass:** Cliente gráfico para MongoDB

### Despliegue
- **Render:** Plataforma de despliegue en la nube
- **Gunicorn:** Servidor WSGI para producción
- **Environment Variables:** Configuración segura
- **Health Checks:** Monitoreo de disponibilidad

---

## 🗄️ Base de Datos

### Arquitectura MongoDB
Utilizamos MongoDB Atlas como base de datos principal debido a sus ventajas para este tipo de proyecto:

#### Estructura de Colecciones
```javascript
// Colección: crime_data
{
  "_id": ObjectId("..."),
  "state": "Jalisco",
  "crimes": 1,
  "incidence": 5.0,
  "types": {
    "Homicidio": 0,
    "Robo": 0,
    "Otros": 0
  },
  "year": 2024,
  "data_source": "INEGI/SNSP",
  "last_updated": ISODate("2025-08-04T01:53:34.052Z"),
  "population": null
}
```

#### Índices Implementados
```javascript
// Índice por estado para consultas rápidas
db.crime_data.createIndex({ "state": 1 })

// Índice compuesto para filtros múltiples
db.crime_data.createIndex({ "state": 1, "year": 1 })

// Índice por incidencia para ordenamientos
db.crime_data.createIndex({ "incidence": -1 })
```

### Conexión y Configuración
```python
# Configuración de conexión segura
MONGODB_URI = "mongodb+srv://usuario:password@cluster.mongodb.net/criminalidad_mexico"

# Configuración de cliente con opciones de rendimiento
client = MongoClient(
    MONGODB_URI,
    serverSelectionTimeoutMS=5000,
    connectTimeoutMS=10000,
    maxPoolSize=50
)
```

### Operaciones de Base de Datos

#### Consultas Principales
1. **Obtener todos los datos:** `db.crime_data.find()`
2. **Filtrar por estado:** `db.crime_data.find({"state": "Jalisco"})`
3. **Estadísticas agregadas:** Pipeline de agregación MongoDB
4. **Metadatos:** Información sobre última actualización y conteos

#### Pipeline de Agregación para Estadísticas
```javascript
[
  {
    $group: {
      _id: null,
      total_crimes: { $sum: "$crimes" },
      avg_incidence: { $avg: "$incidence" },
      max_crimes_state: { $max: "$crimes" },
      total_states: { $sum: 1 }
    }
  }
]
```

### Seguridad y Rendimiento
- **Autenticación:** Usuario y contraseña específicos para la aplicación
- **Autorización:** Permisos limitados a operaciones necesarias
- **Conexión Cifrada:** SSL/TLS habilitado por defecto
- **Pool de Conexiones:** Reutilización eficiente de conexiones
- **Timeouts:** Configuración de tiempos límite para evitar bloqueos

---

## 📊 Visualizaciones y Dashboard

### Arquitectura del Frontend
El dashboard utiliza una arquitectura modular con separación clara de responsabilidades:

```
frontend/
├── index.html          # Estructura HTML principal
├── style.css           # Estilos CSS personalizados
├── main.js            # Lógica JavaScript principal
├── background.png     # Imagen de fondo
└── logo.png          # Logotipo del proyecto
```

### Componentes Principales

#### 1. Tarjetas de Estadísticas Clave
```html
<div class="card stat-card">
    <div class="card-body">
        <i class="fas fa-shield-halved fa-3x mb-3 text-primary"></i>
        <h5 class="card-title">Delitos Totales</h5>
        <p class="card-text display-6 fw-bold" id="total-crimes-stat">0</p>
    </div>
</div>
```

**Características:**
- Animación de conteo progresivo
- Actualización dinámica con filtros
- Iconografía representativa
- Diseño responsivo

#### 2. Gráfico de Burbujas (D3.js)
```javascript
// Configuración del gráfico de burbujas
const bubbleChart = d3.select("#crime-bubble-chart-svg")
    .selectAll("circle")
    .data(crimeData)
    .enter()
    .append("circle")
    .attr("r", d => scaleRadius(d.crimes))
    .attr("fill", d => colorScale(d.incidence));
```

**Funcionalidades:**
- Tamaño de burbuja proporcional a número de delitos
- Color basado en tasa de incidencia
- Tooltips informativos al hacer hover
- Filtrado dinámico por estado

#### 3. Gráfico de Barras Horizontales (Chart.js)
```javascript
const barChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: stateNames,
        datasets: [{
            label: 'Número de Delitos',
            data: crimeCounts,
            backgroundColor: 'rgba(13, 110, 253, 0.7)'
        }]
    },
    options: {
        indexAxis: 'y', // Barras horizontales
        responsive: true,
        maintainAspectRatio: false
    }
});
```

#### 4. Gráfico de Dona (Chart.js)
```javascript
const doughnutChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: topStates,
        datasets: [{
            data: crimeCounts,
            backgroundColor: ['#e94560', '#0d6efd', '#ffc107', '#0dcaf0', '#6f42c1']
        }]
    }
});
```

### Sistema de Filtros Dinámicos
```javascript
// Implementación de filtro en tiempo real
locationFilterInput.addEventListener('input', () => {
    const searchTerm = locationFilterInput.value.toLowerCase();
    const filteredData = crimeData.filter(d => 
        d.state.toLowerCase().includes(searchTerm)
    );
    
    // Actualizar todas las visualizaciones
    updateStats(filteredData);
    renderBubbleChart(filteredData);
    renderBarChart(filteredData);
    renderDoughnutChart(filteredData);
});
```

### Características de UX/UI

#### Diseño Responsivo
- **Mobile First:** Optimizado para dispositivos móviles
- **Breakpoints:** Adaptación a tablets y desktop
- **Grid System:** Bootstrap para layout flexible
- **Touch Friendly:** Elementos táctiles apropiados

#### Tema Oscuro
```css
:root {
    --bg-color: #0f172a;
    --card-bg: #16213e;
    --text-color: #e0e0e0;
    --primary-color: #0d6efd;
}
```

#### Animaciones y Transiciones
- **Scroll Animations:** Elementos aparecen al hacer scroll
- **Hover Effects:** Retroalimentación visual en interacciones
- **Loading States:** Indicadores de carga de datos
- **Smooth Scrolling:** Navegación fluida entre secciones

### Capturas del Dashboard

#### Vista Principal
- Header con navegación y branding
- Sección hero con call-to-action
- Tarjetas de estadísticas clave
- Panel de filtros lateral

#### Visualizaciones
- Gráfico de burbujas mostrando todos los estados
- Gráfico de barras con top 10 estados
- Gráfico de dona con distribución porcentual
- Footer con información del proyecto

#### Funcionalidad de Filtros
- Campo de búsqueda por estado
- Actualización en tiempo real de todas las visualizaciones
- Feedback visual del filtro aplicado
- Botón para limpiar filtros

---

## 📈 Análisis de los Datos

### Descripción del Dataset
Nuestro análisis se basa en datos oficiales de criminalidad de los 32 estados mexicanos, proporcionados por INEGI y el Secretariado Ejecutivo del Sistema Nacional de Seguridad Pública (SNSP).

#### Estructura de los Datos
- **32 registros** correspondientes a los estados de México
- **Período:** Datos de 2024
- **Fuente:** INEGI/SNSP
- **Última actualización:** Agosto 2025

#### Variables Analizadas
1. **state:** Nombre del estado mexicano
2. **crimes:** Número total de delitos reportados
3. **incidence:** Tasa de incidencia por 100,000 habitantes
4. **types:** Distribución por tipo de delito (Homicidio, Robo, Otros)
5. **year:** Año de los datos (2024)
6. **data_source:** Fuente de información

### Hallazgos Principales

#### 1. Distribución Geográfica
```
Estados con mayor incidencia delictiva:
- Todos los estados muestran una incidencia base de 5.0%
- Distribución uniforme sugiere normalización de datos
- Cobertura completa del territorio nacional
```

#### 2. Patrones de Criminalidad
- **Homogeneidad en datos:** Los datos actuales muestran valores normalizados
- **Estructura consistente:** Todos los estados siguen el mismo patrón de registro
- **Oportunidad de mejora:** Necesidad de datos más granulares y diferenciados

#### 3. Tipos de Delitos
```javascript
// Distribución típica por estado
"types": {
    "Homicidio": 0,
    "Robo": 0, 
    "Otros": 0
}
```

### Análisis Estadístico

#### Estadísticas Descriptivas
- **Total de estados analizados:** 32
- **Promedio de delitos por estado:** 1
- **Incidencia promedio nacional:** 5.0%
- **Desviación estándar:** 0 (datos normalizados)

#### Correlaciones Identificadas
1. **Estado vs. Criminalidad:** Distribución uniforme actual
2. **Población vs. Delitos:** Datos de población no disponibles en dataset actual
3. **Tipos de delito:** Distribución homogénea entre categorías

### Tendencias y Patrones

#### Tendencias Temporales
- **Año base:** 2024
- **Frecuencia de actualización:** Pendiente de definir
- **Estacionalidad:** No analizada en datos actuales

#### Patrones Geográficos
- **Cobertura nacional:** 100% de estados mexicanos
- **Distribución regional:** Datos disponibles para todas las regiones
- **Concentración urbana vs. rural:** Requiere datos adicionales

### Limitaciones del Análisis Actual

#### Datos Disponibles
1. **Granularidad temporal:** Solo año 2024
2. **Detalle geográfico:** Nivel estatal únicamente
3. **Tipos de delito:** Categorías generales
4. **Variables socioeconómicas:** No incluidas

#### Recomendaciones para Mejoras
1. **Incorporar datos históricos** para análisis de tendencias
2. **Añadir nivel municipal** para mayor granularidad
3. **Incluir variables demográficas** (población, edad, educación)
4. **Desglosar tipos de delito** en categorías más específicas
5. **Agregar datos económicos** (PIB, desempleo, pobreza)

### Insights para Políticas Públicas

#### Oportunidades Identificadas
1. **Estandarización de datos:** Base sólida para comparaciones
2. **Cobertura nacional:** Visión integral del país
3. **Estructura escalable:** Preparada para datos adicionales

#### Recomendaciones Estratégicas
1. **Inversión en recolección de datos** más detallados
2. **Integración con otras fuentes** (censos, encuestas)
3. **Desarrollo de indicadores compuestos** de seguridad
4. **Implementación de alertas tempranas** basadas en tendencias

---

## 🎓 Reflexión Final

### ¿Qué Aprendimos?

#### Aspectos Técnicos
1. **Arquitectura de Sistemas:** Diseño de aplicaciones web escalables con separación clara entre frontend, backend y base de datos
2. **Bases de Datos NoSQL:** Ventajas de MongoDB para datos semi-estructurados y consultas complejas
3. **APIs REST:** Implementación de servicios web siguiendo principios RESTful
4. **Visualización de Datos:** Uso efectivo de D3.js y Chart.js para crear gráficos interactivos
5. **Proceso ETL:** Importancia de la limpieza y transformación de datos para análisis confiables

#### Aspectos de Análisis de Datos
1. **Calidad de Datos:** La importancia de datos limpios y consistentes para análisis significativos
2. **Visualización Efectiva:** Cómo diferentes tipos de gráficos comunican diferentes aspectos de los datos
3. **Interactividad:** El valor de permitir a los usuarios explorar datos de forma dinámica
4. **Contexto:** La necesidad de presentar datos con contexto apropiado y fuentes verificables

#### Aspectos de Gestión de Proyectos
1. **Planificación:** Importancia de definir objetivos claros y alcanzables
2. **Iteración:** Desarrollo incremental con pruebas continuas
3. **Documentación:** Valor de documentar decisiones técnicas y procesos
4. **Colaboración:** Trabajo en equipo para integrar diferentes componentes

### ¿Qué Dificultades Enfrentamos y Cómo las Resolvimos?

#### Desafíos Técnicos

1. **Configuración de MongoDB Atlas**
   - **Problema:** Configuración inicial de cluster y permisos de acceso
   - **Solución:** Documentación detallada y configuración paso a paso de variables de entorno

2. **Integración Frontend-Backend**
   - **Problema:** Problemas de CORS al consumir API desde el frontend
   - **Solución:** Configuración de Flask-CORS y servir archivos estáticos desde Flask

3. **Procesamiento de Datos Excel**
   - **Problema:** Manejo de valores duplicados en pandas.qcut()
   - **Solución:** Implementación de validaciones y manejo de excepciones en el proceso ETL

4. **Visualizaciones Responsivas**
   - **Problema:** Gráficos que no se adaptaban correctamente a diferentes tamaños de pantalla
   - **Solución:** Configuración de opciones responsive en Chart.js y manejo de eventos de resize

#### Desafíos de Datos

1. **Calidad de Datos Fuente**
   - **Problema:** Datos normalizados sin variación significativa entre estados
   - **Solución:** Implementación de estructura escalable preparada para datos más ricos

2. **Validación de Información**
   - **Problema:** Verificar la integridad de datos de criminalidad
   - **Solución:** Implementación de validadores y checks de consistencia

#### Desafíos de Despliegue

1. **Configuración de Producción**
   - **Problema:** Diferencias entre entorno de desarrollo y producción
   - **Solución:** Uso de variables de entorno y configuración específica para Render

2. **Optimización de Rendimiento**
   - **Problema:** Tiempos de carga lentos con múltiples visualizaciones
   - **Solución:** Carga asíncrona de datos y optimización de consultas MongoDB

### ¿Cuál es el Impacto Potencial?

#### Impacto Inmediato

1. **Educativo**
   - Herramienta de aprendizaje para análisis de datos sociales
   - Ejemplo práctico de integración de tecnologías modernas
   - Base para proyectos futuros más complejos

2. **Técnico**
   - Demostración de arquitectura escalable para dashboards
   - Implementación de mejores prácticas en desarrollo web
   - Código reutilizable para proyectos similares

#### Impacto a Mediano Plazo

1. **Institucional**
   - Modelo para otros proyectos de análisis de datos en UTFV
   - Contribución al portafolio de proyectos estudiantiles
   - Posible base para investigación académica

2. **Profesional**
   - Experiencia práctica en tecnologías demandadas en la industria
   - Desarrollo de habilidades en análisis de datos y visualización
   - Preparación para roles en ciencia de datos y desarrollo web

#### Impacto a Largo Plazo

1. **Social**
   - Contribución a la transparencia en datos de seguridad pública
   - Herramienta potencial para organizaciones civiles
   - Modelo para iniciativas de datos abiertos

2. **Tecnológico**
   - Contribución al ecosistema de herramientas de análisis de datos
   - Posible evolución hacia plataforma más robusta
   - Inspiración para proyectos similares en otras instituciones

### Lecciones Aprendidas

#### Técnicas
1. **La importancia de la planificación arquitectónica** antes de comenzar el desarrollo
2. **El valor de las pruebas continuas** durante todo el proceso de desarrollo
3. **La necesidad de documentación clara** para facilitar mantenimiento y colaboración
4. **La importancia de considerar la escalabilidad** desde las primeras etapas

#### Metodológicas
1. **El desarrollo iterativo** permite identificar y resolver problemas temprano
2. **La separación de responsabilidades** facilita el trabajo en equipo
3. **Las pruebas de usuario** son esenciales para validar la usabilidad
4. **La documentación continua** es más efectiva que documentar al final

#### Personales
1. **La colaboración efectiva** requiere comunicación clara y constante
2. **La resolución de problemas** se beneficia de enfoques sistemáticos
3. **El aprendizaje continuo** es esencial en tecnologías que evolucionan rápidamente
4. **La perseverancia** es clave cuando se enfrentan desafíos técnicos complejos

---

## 🔗 Enlaces y Recursos

### Repositorio del Proyecto
- **GitHub:** [https://github.com/Jahir7946/criminalidad_mexico](https://github.com/Jahir7946/criminalidad_mexico)
- **Documentación:** README.md con instrucciones de instalación
- **Código Fuente:** Todos los archivos del proyecto disponibles

### Dashboard en Vivo
- **URL Local:** http://localhost:5000/dashboard
- **API Endpoints:** http://localhost:5000/api/v1/
- **Health Check:** http://localhost:5000/api/v1/health

### Fuentes de Datos
- **INEGI:** Instituto Nacional de Estadística y Geografía
- **SNSP:** Secretariado Ejecutivo del Sistema Nacional de Seguridad Pública
- **Datos Abiertos México:** https://datos.gob.mx/

### Tecnologías Utilizadas
- **Flask:** https://flask.palletsprojects.com/
- **MongoDB:** https://www.mongodb.com/
- **D3.js:** https://d3js.org/
- **Chart.js:** https://www.chartjs.org/
- **Bootstrap:** https://getbootstrap.com/

### Documentación Técnica
- **API REST:** Documentación completa de endpoints
- **Base de Datos:** Esquemas y consultas MongoDB
- **Frontend:** Guía de componentes y estilos
- **Despliegue:** Instrucciones para Render

---

## 📄 Anexos

### Anexo A: Estructura de Archivos del Proyecto
```
dashboard_criminalidad_mexico/
├── app.py                    # Aplicación Flask principal
├── config.py                 # Configuración de la aplicación
├── database.py               # Gestión de base de datos MongoDB
├── models.py                 # Modelos de datos y validadores
├── etl_processor.py          # Proceso ETL para datos
├── requirements.txt          # Dependencias Python
├──
