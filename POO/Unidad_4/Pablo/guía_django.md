# Pasos para crear un proyecto de Django:

1. Crear el directorio

2. En el directorio, ejecutar
    `python3 -m venv venv_django`

3. Activar el entorno:
    `source venv_django/bin/activate`

4. Instalar Django:
    `pip install django==6.0.1`

5. Crear el archivo de instalación para que otro pueda instalar el mismo entorno
    `pip freeze > requirements.txt`

Para volver a instalar el entorno:
    `pip install -r requirements.txt`

Para ver la versión de Django
    `django-admin --version`

6. Crear proyecto:
    `django-admin startproject test_django_orm`
    `cd test_django_orm`

7. Levantar el servidor:
    `python3 manage.py runserver`


## Crear la aplicación:

1. Dentro del directorio del proyecto (test_django_orm) ejecutar:
    `python3 manage.py startapp persona`

2. En el archivo settings.py, en la lista INSTALLED_APPS incluir 'persona.apps.PersonaConfig' (que es la aplicación). Quedaría así:
    ```py
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'persona.apps.PersonaConfig',
    ]
    ```

3. Crear modelo:
En models.py añadir la clase correspondiente al modelo quedando así:
    ```py
    from django.db import models

    # Create your models here.
    class Persona(models.Model):
        nombre = models.CharField(max_length=100, null=True)
        telefono = models.CharField(max_length=15, null=True)
        correo = models.EmailField(null=True)

        def __str__(self):
            return f"{self.nombre} - {self.telefono} - {self.correo}"
    ```

4. En settings.py especificar la base de datos en el diccionario DATABASES quedando así:
    ```py
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'personas.db',
        }
    }
    ```

5. Migrar ejecutando:
    `python manage.py makemigrations`
    `python manage.py migrate`

makemigration genera el código python. Migrate lo ejecuta.


## Ejemplo de inserción de personas en la base de datos:

1. en el directorio raíz (donde está la base de datos) crear el archivo ej1_insertar_personas.py

2. En dicho archivo meter:
    ```py
    import os
    import django

    # Configuración del entorno Django (ajusta con tu proyecto)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_django_orm.settings')
    django.setup()

    from persona.models import Persona

    class Main:
        @staticmethod
        def main():
            # Lista de personas a insertar
            personas = [
                Persona(nombre='Juan', telefono='123456789', correo='juan@gmail.com'),
                Persona(nombre='Ana', telefono='987654321', correo='ana@gmail.com'),
                Persona(nombre='Pedro', telefono='456789123', correo='peter@pan.es'),
                Persona(nombre='María', telefono='654987321', correo='maria@cuetara.es'),
                Persona(nombre='Luis', telefono='789123456', correo='luis@ito.es'),
            ]

            # Guardar en la base de datos
            for persona in personas:
                persona.save()
                print(f"Persona {persona.nombre} guardada en la base de datos")

    if __name__ == "__main__":
        Main.main()
    ```
    
Nota: Si al ejecutar pone que no encuentra el módulo, cerrar Codium y volver a abrir. Al ejecutar debe mostrarse en terminal que está ejecutando dentro del entorno y ya tira.

3. Ejecutar el archivo y se insertarán los datos.

Ver resto de ejemplos en el proyecto de ejemplo



# Tipos de campos

Algunos de los tipos de campos que podemos utilizar en los modelos son:

## Campos de texto

- CharField
Texto corto con longitud máxima obligatoria.
`nombre = models.CharField(max_length=100)`
   - Requiere max_length
   - Ideal para nombres, títulos, códigos
   
- TextField
Texto largo sin límite práctico.
`descripcion = models.TextField()`
   - No requiere max_length
   - Para descripciones, comentarios, contenido
   
- SlugField
Texto optimizado para URLs.
`slug = models.SlugField(unique=True)`
   - Solo letras, números, guiones y guiones bajos
   - Muy usado en URLs amigables
   
- EmailField
`email = models.EmailField()`
   - Valida URLs
   
   
## Campos numéricos

- IntegerField
`edad = models.IntegerField()`

- BigIntegerField
`poblacion = models.BigIntegerField()`
   - Para enteros muy grandes
   
- SmallIntegerField
`nivel = models.SmallIntegerField()`

- PositiveIntegerField
`stock = models.PositiveIntegerField()`

- FloatField
`peso = models.FloatField()`
   - Números decimales en coma flotante
   - Puede tener errores de precisión
   
- DecimalField (recomendado para dinero)
`precio = models.DecimalField(max_digits=8, decimal_places=2)`
   
   
## Campos de fecha y hora

- DateField
`fecha = models.DateField()`
Opciones útiles:
`fecha = models.DateField(auto_now_add=True)  # al crear`
`fecha = models.DateField(auto_now=True)      # al actualizar`
   
- DateTimeField
`creado = models.DateTimeField(auto_now_add=True)`
   
- TimeField
`hora = models.TimeField()`


## Booleanos
   
- BooleanField
`activo = models.BooleanField(default=True)`
`campo = models.BooleanField(null=True)`


## Archivos e imágenes

- FileField
`archivo = models.FileField(upload_to="docs/")`

- ImageField
`imagen = models.ImageField(upload_to="imagenes/")`
   - Requiere Pillow
   
- Campos especiales
`datos = models.JSONField()`
   - Guarda JSON directamente
   - Muy útil para estructuras flexibles
   
- UUIDField
```py
import uuid

id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
```
   - Identificadores únicos universales
   

# Opciones de campo importantes en Django

- Ejemplo base
```py
nombre = models.CharField(
    max_length=100,
    null=False,
    blank=False,
    default="",
    unique=False,
    db_index=False,
    help_text="Introduce el nombre completo",
    verbose_name="Nombre"
)
```

- max_length (OBLIGATORIO en CharField)
`titulo = models.CharField(max_length=200)`
   - Define longitud máxima
   - Crea restricción en BD
   - Se usa en validación de formularios

- null
`edad = models.IntegerField(null=True)`
   - Permite guardar NULL en la base de datos
   - Afecta solo a la BD

- blank
`nombre = models.CharField(max_length=100, blank=True)`
Permite campo vacío en:
   - formularios
   - admin
   - validación Django

- default
```py
activo = models.BooleanField(default=True)
fecha = models.DateField(default=date.today)
stock = models.IntegerField(default=0)
```
   - Valor automático si no se especifica

- unique
`email = models.EmailField(unique=True)`
   - No permite valores repetidos
   - Crea índice único en BD

- primary_key
`id = models.UUIDField(primary_key=True)`
   - Define clave primaria

- db_index
`nombre = models.CharField(max_length=100, db_index=True)`
   - Crea índice en BD

- choices
```py
ESTADOS = [
    ("P", "Pendiente"),
    ("E", "Enviado"),
    ("R", "Recibido"),
]

estado = models.CharField(max_length=1, choices=ESTADOS)
```
   - Restringe valores posibles
   - Crea selector en admin
   - Evita datos inválidos

- help_text
```py
precio = models.DecimalField(
    max_digits=6,
    decimal_places=2,
    help_text="Precio en euros con 2 decimales"
)
```
   - Texto de ayuda en formularios y admin

- verbose_name
```py
nombre = models.CharField(
    max_length=100,
    verbose_name="Nombre completo"
)
```
   - Nombre legible del campo en admin

- validators
```py
from django.core.validators import MinValueValidator

edad = models.IntegerField(
    validators=[MinValueValidator(18)]
)
```
   - Reglas de validación personalizadas

- editable
```py
creado = models.DateTimeField(
    auto_now_add=True,
    editable=False
)
```
   - No aparece en formularios/admin

- auto_now y auto_now_add
```py
creado = models.DateTimeField(auto_now_add=True)
modificado = models.DateTimeField(auto_now=True)
```
   - auto_now_add:  solo al crear
   - auto_now:  cada guardado

- Ejemplo completo
```py
class Cliente(models.Model):
    email = models.EmailField(unique=True, db_index=True)
    nombre = models.CharField(max_length=120)
    edad = models.IntegerField(null=True, blank=True)
    activo = models.BooleanField(default=True)
    tipo = models.CharField(
        max_length=1,
        choices=[("P","Premium"), ("N","Normal")],
        default="N"
    )
    creado = models.DateTimeField(auto_now_add=True)
```


# Pasos para usar MySQL con Django

1. Crear la base de datos en tu servidor MySQL.

2. Crear un usuario con permisos para esa base de datos.

3. Modificar en el archivo settings.py del proyecto la configuración referente a las bases de datos, adaptándola a MySQL.

Nota: Usar 127.0.0.1 en lugar de localhost obliga a Django a usar la red local en lugar del archivo de socket /run/mysqld/mysqld.sock solucionando el típico problema de conexión al migrar.

```py
DATABASES = {
    'sqlite': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.test_django_orm',
    },
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test_django_orm',
        'USER': 'root',
        'PASSWORD': 'Trassierra2026$',
        'HOST': '127.0.0.1',    # Importante: 'localhost' puede dar problemas. sustituir por '127.0.0.1'
        'PORT': 3309,
    }
}
```

4. Instalar en el sistema (fuera del entorno virtual) estas librerías necesarias para poder desempaquetar el mysqlclient y así poder instalarlo en el venv:
`sudo apt update`
`sudo apt install build-essential pkg-config python3-dev libmariadb-dev`

5. Instalar el cliente de MySQL:
`pip install mysqlclient`

6. Levantar el servicio MySQL dockerizado. Es necesario tener el docker-compose.yml preparado para el proyecto y ejecutar en ese directorio:
`docker compose up -d`

7. Conectar con la base de datos en el DBeaver

8. Migrar

