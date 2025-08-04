# 📚 Instrucciones para Subir el Proyecto a GitHub

## 🚀 Pasos para Crear el Repositorio en GitHub

### 1. Crear Repositorio en GitHub.com
1. Ve a [GitHub.com](https://github.com) e inicia sesión
2. Haz clic en el botón **"New"** o **"+"** → **"New repository"**
3. Configura el repositorio:
   - **Repository name:** `dashboard-criminalidad-mexico`
   - **Description:** `Dashboard interactivo de análisis de criminalidad en México usando MongoDB, Flask y visualizaciones D3.js/Chart.js`
   - **Visibility:** Public ✅
   - **NO marques** "Add a README file" (ya tenemos uno)
   - **NO marques** "Add .gitignore" (ya tenemos uno)
   - **NO marques** "Choose a license"
4. Haz clic en **"Create repository"**

### 2. Conectar el Repositorio Local con GitHub

Una vez creado el repositorio en GitHub, ejecuta estos comandos en la terminal:

```bash
# Agregar el repositorio remoto (reemplaza TU_USUARIO con tu nombre de usuario de GitHub)
git remote add origin https://github.com/TU_USUARIO/dashboard-criminalidad-mexico.git

# Verificar que se agregó correctamente
git remote -v

# Subir la rama principal
git push -u origin blackboxai/dashboard-criminalidad-mexico
```

### 3. Crear Pull Request (Opcional)
Si quieres crear un Pull Request desde la rama `blackboxai/dashboard-criminalidad-mexico` hacia `main`:

1. Ve a tu repositorio en GitHub
2. Verás un banner que dice "Compare & pull request"
3. Haz clic en él y completa la información del PR
4. Haz clic en "Create pull request"

## 📋 Estado Actual del Repositorio

✅ **Git inicializado** - Repositorio local creado  
✅ **Archivos agregados** - Todos los archivos del proyecto incluidos  
✅ **Commit inicial** - Commit con mensaje descriptivo realizado  
✅ **Rama creada** - `blackboxai/dashboard-criminalidad-mexico` activa  
✅ **.gitignore configurado** - Archivos sensibles excluidos  

## 📁 Archivos Incluidos en el Repositorio

### Backend Python
- `app.py` - Aplicación Flask principal
- `config.py` - Configuración de la aplicación
- `database.py` - Conexión y operaciones MongoDB
- `models.py` - Modelos de datos
- `etl_processor.py` - Proceso ETL automatizado
- `init_database.py` - Inicialización de base de datos
- `test_api.py` - Pruebas de API
- `run_server.py` - Script para ejecutar servidor

### Frontend
- `index.html` - Página principal del dashboard
- `main.js` - JavaScript con D3.js y Chart.js
- `style.css` - Estilos CSS responsivos
- `background.png` - Imagen de fondo
- `logo.png` - Logo del proyecto

### Configuración y Despliegue
- `requirements.txt` - Dependencias Python
- `Procfile` - Configuración para Render
- `.gitignore` - Archivos excluidos de Git

### Documentación
- `README.md` - Documentación técnica completa
- `DOCUMENTACION_PROYECTO.md` - Documentación académica
- `PRESENTACION_PROYECTO.md` - Guía de presentación
- `RESUMEN_EJECUTIVO.md` - Resumen ejecutivo
- `INSTRUCCIONES_GITHUB.md` - Este archivo

## 🔗 URLs del Proyecto

Una vez subido a GitHub, el repositorio estará disponible en:
```
https://github.com/TU_USUARIO/dashboard-criminalidad-mexico
```

## 🚀 Despliegue en Render

Después de subir a GitHub, puedes desplegar en Render:

1. Ve a [Render.com](https://render.com)
2. Conecta tu cuenta de GitHub
3. Selecciona el repositorio `dashboard-criminalidad-mexico`
4. Configura las variables de entorno:
   - `MONGODB_URI` - Tu string de conexión MongoDB Atlas
   - `FLASK_ENV` - `production`
5. Haz clic en "Deploy"

## 📞 Soporte

Si tienes problemas:
1. Verifica que Git esté instalado: `git --version`
2. Verifica tu configuración de Git:
   ```bash
   git config --global user.name "Tu Nombre"
   git config --global user.email "tu.email@ejemplo.com"
   ```
3. Si hay problemas de autenticación, considera usar un Personal Access Token

---

**¡Proyecto listo para compartir! 🎉**
