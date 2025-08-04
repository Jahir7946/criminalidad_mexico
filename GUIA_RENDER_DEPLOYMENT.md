# 🚀 Guía Completa para Desplegar en Render

## ✅ Problema Identificado y Solucionado

**Problema:** La aplicación se ejecutaba pero Render no detectaba el puerto correctamente porque estaba configurada para desarrollo local.

**Solución:** Se actualizó `run_server.py` para detectar automáticamente el entorno de producción y usar el puerto correcto.

## 📋 Configuración Correcta para Render

### Paso 1: Configuración en Render Dashboard

1. **Ir a Render.com** y conectar tu cuenta de GitHub
2. **Crear nuevo Web Service:**
   - Repository: `Jahir7946/criminalidad_mexico`
   - Branch: `blackboxai/dashboard-criminalidad-mexico`
   - Name: `dashboard-criminalidad-mexico`
   - Region: `Oregon (US West)`
   - Runtime: `Python 3`

### Paso 2: Configuración de Build y Deploy

**IMPORTANTE:** Usa estas configuraciones exactas:

```
Build Command: pip install -r requirements.txt
Start Command: gunicorn app:app --bind 0.0.0.0:$PORT --workers 2 --timeout 120
```

**NO uses:** `python run_server.py` como Start Command (esto causaba el problema)

### Paso 3: Variables de Entorno

Configura estas variables en Render:

```
FLASK_ENV=production
MONGODB_URI=tu_string_de_conexion_mongodb_atlas
PORT=10000
```

### Paso 4: Configurar MongoDB Atlas

1. **Crear cluster gratuito** en [MongoDB Atlas](https://cloud.mongodb.com)
2. **Database Access:** Crear usuario con permisos de lectura/escritura
3. **Network Access:** Agregar `0.0.0.0/0` para permitir conexiones desde Render
4. **Obtener Connection String:**
   ```
   mongodb+srv://usuario:password@cluster.mongodb.net/criminalidad_mexico?retryWrites=true&w=majority
   ```

## 🔧 Archivos de Configuración

### Procfile (Ya configurado correctamente)
```
web: gunicorn app:app --bind 0.0.0.0:$PORT --workers 2 --timeout 120
```

### run_server.py (Actualizado para producción)
- ✅ Detecta automáticamente entorno de producción
- ✅ Usa puerto dinámico de Render ($PORT)
- ✅ Desactiva debug mode en producción

### requirements.txt (Incluye todas las dependencias)
- ✅ gunicorn>=21.0.0 (servidor WSGI para producción)
- ✅ Todas las dependencias necesarias

## 🚀 Proceso de Despliegue

### Opción 1: Usar Procfile (RECOMENDADO)
```
Start Command: (dejar vacío, usará Procfile automáticamente)
```

### Opción 2: Comando directo
```
Start Command: gunicorn app:app --bind 0.0.0.0:$PORT --workers 2 --timeout 120
```

## 📊 Verificación del Despliegue

Una vez desplegado, tu aplicación estará disponible en:
```
https://dashboard-criminalidad-mexico.onrender.com
```

### Endpoints para verificar:
- **Dashboard:** `https://tu-app.onrender.com/`
- **API Health:** `https://tu-app.onrender.com/api/v1/health`
- **API Datos:** `https://tu-app.onrender.com/api/v1/criminalidad`

## 🔍 Solución de Problemas

### Si el build falla:
1. Verificar que `requirements.txt` esté completo
2. Revisar logs de build en Render dashboard

### Si no detecta puerto:
1. ✅ **SOLUCIONADO:** Usar `gunicorn` en lugar de `python run_server.py`
2. Verificar que `FLASK_ENV=production` esté configurado

### Si falla conexión MongoDB:
1. Verificar `MONGODB_URI` en variables de entorno
2. Confirmar que `0.0.0.0/0` esté en Network Access de MongoDB Atlas
3. Verificar usuario y contraseña en connection string

### Si la aplicación no responde:
1. Revisar logs en tiempo real en Render
2. Verificar que todas las variables de entorno estén configuradas
3. Confirmar que el puerto se está bindeando correctamente

## 📝 Logs Esperados (Exitosos)

```
==> Build successful 🎉
==> Deploying...
==> Running 'gunicorn app:app --bind 0.0.0.0:$PORT --workers 2 --timeout 120'
INFO:database:✅ Conexión exitosa a MongoDB: criminalidad_mexico
INFO:app:✅ Configuración validada correctamente
INFO:app:✅ Conexión a MongoDB establecida
[INFO] Starting gunicorn 21.2.0
[INFO] Listening at: http://0.0.0.0:10000
[INFO] Using worker: sync
[INFO] Booting worker with pid: [PID]
```

## 🔄 Actualizaciones Futuras

Para actualizar la aplicación:
1. Hacer cambios en el código local
2. Commit y push a GitHub:
   ```bash
   git add .
   git commit -m "Descripción del cambio"
   git push origin blackboxai/dashboard-criminalidad-mexico
   ```
3. Render detectará automáticamente los cambios y redesplegará

## 📞 Soporte Adicional

Si persisten los problemas:
1. Revisar logs detallados en Render dashboard
2. Verificar configuración de MongoDB Atlas
3. Confirmar que todas las variables de entorno estén correctas

---

**¡Tu aplicación está lista para producción! 🎉**

**URL del repositorio:** https://github.com/Jahir7946/criminalidad_mexico
**Branch de despliegue:** `blackboxai/dashboard-criminalidad-mexico`
