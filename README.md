# 📦 Proyecto Django – Sistema de Inventario

[![Deploy](https://img.shields.io/badge/deploy-render-green)](https://proyecto-django-jxkv.onrender.com)
![Django](https://img.shields.io/badge/Django-6.x-darkgreen)
![Python](https://img.shields.io/badge/Python-3.14-blue)
![Version](https://img.shields.io/badge/version-1.0-orange)
![License](https://img.shields.io/badge/license-MIT-purple)

Aplicación web desarrollada con **Django** para la gestión de inventario.  
El sistema permite administrar registros, visualizar información y operar mediante una interfaz web desplegada en la nube.

## 🚀 Demo en producción

👉 https://proyecto-django-jxkv.onrender.com 

👉 Credenciales default: User: Admin / Password: 1234

---

## 🧰 Tecnologías usadas

- Python 3
- Django
- Gunicorn
- Render (deploy)
- SQLite / PostgreSQL (según configuración)
- HTML / CSS / Bootstrap

---

## ⚙️ Instalación local

Sigue estos pasos para correr el proyecto en tu máquina:

```bash
# Clonar repositorio
git clone TU_URL_DEL_REPO
cd TU_REPO

# Crear entorno virtual
python -m venv venv

# Activar entorno
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Ejecutar servidor
python manage.py runserver
```

Luego abre en el navegador:

```
http://127.0.0.1:8000
```

---

## 🗂️ Estructura básica

```
inventario/
 ├── inventario/
 │   ├── settings.py
 │   ├── urls.py
 │   └── wsgi.py
 ├── app/
 ├── manage.py
 ├── requirements.txt
 └── Procfile
```

---

## 🧪 Variables importantes para producción

En `settings.py`:

```python
DEBUG = False
ALLOWED_HOSTS = ["proyecto-django-jxkv.onrender.com"]
```

---

## 🧨 Procfile usado

```
web: gunicorn inventario.wsgi
```

Ese comando levanta el servidor Gunicorn apuntando al módulo WSGI del proyecto.

---

## 📦 requirements.txt típico

```
Django
gunicorn
whitenoise
psycopg2-binary
```

---

## 🌐 Deploy en Render

Pasos resumidos:

1. Subir proyecto a GitHub
2. Crear Web Service en Render
3. Conectar repositorio
4. Build command:

```
pip install -r requirements.txt
```

5. Start command:

```
gunicorn inventario.wsgi
```

6. Configurar variables de entorno si aplica
7. Deploy automático

---

## 🛠️ Funcionalidades esperadas

- Gestión de inventario
- Panel administrativo
- CRUD de registros
- Acceso web remoto
- Escalable para nuevas funciones

---

## 🧠 Notas finales

Si algo truena en producción:

- Revisa `ALLOWED_HOSTS`
- Verifica Procfile
- Confirma que `requirements.txt` esté completo
- Ejecuta migraciones en el deploy

---

Hecho para correr ligero, firme y sin dramas.
