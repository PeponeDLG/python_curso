# Informe técnico: Videoclub con Flask

## 1. Herencia de plantillas (Jinja2)

### Explicación

La herencia de plantillas en Jinja2 permite definir una estructura base común (HTML, CSS, scripts) en un único archivo y que el resto de páginas del sitio extiendan de él. Esto evita repetir código, facilita el mantenimiento y garantiza una apariencia uniforme en toda la aplicación. Si se quiere cambiar el encabezado o el pie de página, solo hay que modificar la plantilla base.

### Fragmento de `base.html`

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Videoclub{% endblock %}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/estilo.css') }}">
</head>
<body>
    <header>
        <h1><a href="{{ url_for('index') }}">🎬 Videoclub</a></h1>
    </header>
    <main>
        {% block content %}{% endblock %}
    </main>
</body>
</html>
```

Se definen dos bloques:
- **`title`**: permite que cada página personalice el título de la pestaña del navegador.
- **`content`**: es el lugar donde cada página hija inserta su contenido principal.

### Fragmento de `index.html` que hereda de `base.html`

```html
{% extends "base.html" %}
{% import "macros.html" as macros %}

{% block title %}Videoclub - Listado{% endblock %}

{% block content %}
<h2>Películas disponibles</h2>
<a href="{{ url_for('nueva') }}" class="btn">➕ Añadir película</a>
<div class="lista-peliculas">
    {% if peliculas %}
        {% for pelicula in peliculas %}
            {{ macros.tarjeta_pelicula(pelicula) }}
        {% endfor %}
    {% else %}
        <p>No hay películas registradas.</p>
    {% endif %}
</div>
{% endblock %}
```

Con `{% extends "base.html" %}` se indica que esta plantilla hereda de la base. Solo es necesario redefinir los bloques `title` y `content`; el resto de la estructura (DOCTYPE, `<head>`, `<header>`, estilos) lo proporciona `base.html` automáticamente.

---

## 2. Macros en Jinja2

### Justificación

Los macros en Jinja2 son el equivalente a las funciones en Python: encapsulan fragmentos de HTML que se repiten en varias partes de la aplicación. En este proyecto, la tarjeta de una película (con su título, director, año y precio) se muestra tanto en el listado principal como potencialmente en otras vistas. Usar un macro aporta:

- **Reutilización**: se escribe una vez y se usa donde sea necesario.
- **Mantenimiento**: si cambia el diseño de la tarjeta, solo hay que modificar el macro.
- **DRY (Don't Repeat Yourself)**: se evita duplicar el mismo HTML en múltiples plantillas.

### Fragmento de `macros.html`

```html
{% macro tarjeta_pelicula(pelicula) %}
<div class="tarjeta">
    <h3><a href="{{ url_for('detalle', id=pelicula.id) }}">{{ pelicula.titulo }}</a></h3>
    <p><strong>Director:</strong> {{ pelicula.director }}</p>
    <p><strong>Año:</strong> {{ pelicula.año }}</p>
    <p><strong>Precio alquiler:</strong> {{ "%.2f"|format(pelicula.precio_alquiler) }} €</p>
</div>
{% endmacro %}
```

El macro `tarjeta_pelicula` recibe un objeto `pelicula` y renderiza una tarjeta HTML con sus datos. El título es un enlace a la página de detalle de esa película.

### Fragmento de `index.html` usando el macro

```html
{% import "macros.html" as macros %}
...
{% for pelicula in peliculas %}
    {{ macros.tarjeta_pelicula(pelicula) }}
{% endfor %}
```

Se importa el archivo de macros con `{% import "macros.html" as macros %}` y se invoca el macro dentro del bucle como si fuera una función, pasándole cada película.

---

## 3. SQLAlchemy y SQLite

### Ventajas del ORM frente a SQL directo

SQLAlchemy es un **ORM (Object-Relational Mapper)** que permite trabajar con la base de datos usando objetos y métodos de Python en lugar de escribir sentencias SQL directamente. Las principales ventajas son:

| Aspecto | SQL directo | ORM (SQLAlchemy) |
|---|---|---|
| **Abstracción** | Hay que conocer la sintaxis SQL de cada gestor | El mismo código funciona con SQLite, PostgreSQL, MySQL, etc. |
| **Seguridad** | Propenso a inyección SQL si no se sanitizan las consultas | Las consultas parametrizadas son automáticas |
| **Productividad** | Hay que escribir mucho SQL repetitivo (INSERT, SELECT, etc.) | Operaciones CRUD con métodos de Python (`db.session.add()`, `query.all()`, etc.) |
| **Mantenimiento** | Los cambios de esquema requieren revisar todo el SQL | Los cambios en el modelo de Python se reflejan con migraciones |

### Fragmento del modelo `Pelicula` extraído de `app.py`

```python
class Pelicula(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    director = db.Column(db.String(100), nullable=False)
    año = db.Column(db.Integer, nullable=False)
    precio_alquiler = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Pelicula {self.titulo}>'
```

Cada clase que hereda de `db.Model` se corresponde con una tabla de la base de datos. Cada atributo de tipo `db.Column` es una columna. El tipo de dato (Integer, String, Float) y las restricciones (primary_key, nullable) se definen de forma declarativa.

### Fragmento de una inserción (ruta `/nueva`)

```python
@app.route('/nueva', methods=['GET', 'POST'])
def nueva():
    if request.method == 'POST':
        titulo = request.form['titulo']
        director = request.form['director']
        año = int(request.form['año'])
        precio_alquiler = float(request.form['precio_alquiler'])

        pelicula = Pelicula(
            titulo=titulo,
            director=director,
            año=año,
            precio_alquiler=precio_alquiler
        )
        db.session.add(pelicula)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('nueva.html')
```

En lugar de escribir `INSERT INTO pelicula (titulo, director, ...) VALUES (?, ?, ...)`, se crea una instancia del modelo `Pelicula`, se añade a la sesión con `db.session.add()` y se confirma con `db.session.commit()`. El ORM se encarga de generar y ejecutar el SQL internamente.

---

## Conclusión

Este proyecto demuestra cómo Flask, Jinja2 y SQLAlchemy se integran para crear una aplicación web funcional con poco código y buenas prácticas:

- **Jinja2** proporciona un sistema de plantillas potente con herencia y macros que mantienen el HTML organizado y reutilizable.
- **SQLAlchemy** como ORM simplifica el acceso a la base de datos, haciendo el código más seguro, portable y fácil de mantener que usando SQL directo.
- La combinación de estas herramientas permite desarrollar aplicaciones web rápidamente, con una separación clara entre la lógica de negocio (Python), la presentación (plantillas) y los datos (modelos).
