# PROYECTO FINAL

Plataforma: CODERHOUSE

Curso: PYTHON

Comision: 78315

Profesor: Miguel Rodenas

Tutora= Camila Belen Arena

Alumno: Daniel Furche

Link a mi video: https://www.loom.com/share/2f5e7fc0c8e046ca9adddb1f5e18d156?sid=99ddc256-65aa-4e3c-92dd-b59ad10ee2ed

# Proyecto Django - Repuestos, Accesorios e Indumentaria para Motos
-  La idea del proyecto fue crear una plataforma donde se puedan ver artículos de distintos rubros "Accesorios, Repuestos e Indumentaria" de motos. En un próximo paso se estarán cargando fotos, con el fin de convertirlo en catalogo. 


# ¿Qué se puede hacer?
- Crear, listar, editar y eliminar:
- Repuestos
- Accesorios
- Indumentaria
- Registrar y administrar usuarios
- Acceso autenticado a funcionalidades de carga y edición
- Búsqueda por número de parte
- Página de inicio y página "Acerca de mí"

# Tecnologia usadas
- asgiref==3.8.1
- Django==5.2.3
- sqlparse==0.5.3
- tzdata==2025.2
- Python 5.2.4
- Entorno virtual (venv)

# Cómo ejecutar el proyecto
1) Clonar el repositorio
Abrí una terminal y ejecutá:
git clone https://github.com/danifurche/TP3_django.git
cd TP3_django

2) Crear y activar el entorno virtual
python -m venv .venv

3) Luego activalo:
.venv\Scripts\activate

4) Instalar las dependencias
pip install -r requirements.txt

5) Aplicar migraciones a la base de datos
python manage.py makemigrations
python manage.py migrate

6) Ejecutar el servidor de desarrollo
python manage.py runserver

7) Abrir en el navegador
Ingresar a: http://127.0.0.1:8000

# Usuario de prueba
- usuario: admin
- clave: 1234

- usuario: fede
- clave: Federico1

# Estructura del Proyecto
TP3_DJANGO/
│
├── .venv/                         # Entorno virtual (no se sube al repo)
├── avatars/                       # Carpeta adicional (puede estar vacía o para imágenes)
├── ejemplo_django/               # Configuración principal del proyecto
│   ├── __pycache__/              # Archivos compilados por Python
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py               # Configuración del proyecto Django
│   ├── urls.py                   # Enrutamiento general del proyecto
│   └── wsgi.py
│
├── mi_primer_app/                # Aplicación principal
│   ├── __init__.py
│   ├── urls.py                   # URLs específicas de la app
│   ├── views.py                  # Vistas de la app
│   ├── models.py                 # Modelos de la app (no visible en la imagen, pero se asume)
│   ├── forms.py                  # Formularios personalizados
│   └── templates/                # Plantillas HTML de la app
│       └── mi_primer_app/
│           ├── inicio.html
│           ├── about.html
│           ├── crear_repuesto.html
│           ├── eliminar_repuesto.html
│           └── ...
│
├── static/                       # Archivos estáticos (CSS, JS, imágenes, etc.)
├── templates/                    # Plantillas generales (como padre.html)
│   └── padre.html
│
├── usuarios/                     # App para autenticación de usuarios (login, register, etc.)
│   └── (archivos propios no visibles en imagen)
│
├── db.sqlite3                    # Base de datos SQLite generada por Django
├── manage.py                     # Comando para interactuar con Django
├── README.md                     # Documentación del proyecto
├── requirements.txt             # Lista de dependencias del entorno
├── .gitignore                    # Archivos/Carpetas excluidas del control de versiones
└── consigna.md                   # Archivo con la consigna del trabajo
