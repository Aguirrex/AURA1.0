# AURA2.0

Prototipo mejora aplicacion para reservar equipos utp

## Descripción

Este proyecto es una aplicación web desarrollada en Django que permite a los usuarios reservar equipos para ciertas horas. Proporciona una interfaz para administrar reservas, equipos y estudiantes.

## Requisitos

- Python 3.x
- Django 3.x
- asgiref==3.7.2
- DateTime==5.4
- pytz==2024.1
- sqlparse==0.4.4
- typing_extensions==4.9.0
- zope.interface==6.2

## Instalación

1. Clona el repositorio:

    ```bash
    git clone [https://github.com/Aguirrex/AURA1.0.git]
    ```

2. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

3. Configura la base de datos en `settings.py`:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
    ```

4. Aplica las migraciones:

    ```bash
    python manage.py migrate
    ```

## Uso

1. Inicia el servidor de desarrollo:

    ```bash
    python manage.py runserver
    ```

2. Accede a la aplicación en tu navegador web:

    ```
    http://localhost:8000/
    ``

## Licencia

Este proyecto está bajo ninguna licencia.
