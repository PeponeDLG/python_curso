from flask import Flask, render_template

app = Flask(__name__)



@app.template_filter()
def truncar(texto, longitud=20):
    if len(texto) > longitud:
        return texto[:longitud] + "..."
    return texto

@app.template_filter()
def euro(valor):
    return f"{valor:.2f} €"

@app.template_filter()
def color_precio(valor):
    if valor < 50:
        return "green"
    elif valor < 200:
        return "orange"
    else:
        return "red"

@app.template_filter()
def estado_stock(stock):
    if stock == 0:
        return "Sin stock"
    elif stock < 30:
        return "Pocas unidades"
    else:
        return "Disponible"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/filtro")
def filtro():
    descripcion = "Este es un texto muy largo que queremos acortar para que no rompa el diseño"
    return render_template("filtro_longitud.html", descripcion=descripcion)


@app.route("/ciudades")
def ciudades():
    ciudades = [
        {"nombre": "Burgos", "temp": -2},
        {"nombre": "Madrid", "temp": 20},
        {"nombre": "Córdoba", "temp": 40}
    ]
    return render_template("ciudades.html", ciudades=ciudades)

@app.route("/usuarios")
def usuarios():
    nombre = "Jacinto"
    usuarios = ["ana", "pedro", "luis"]
    return render_template("usuarios.html", usuarios=usuarios, nombre=nombre)

@app.route("/entradas")
def entradas():
    entradas = [
        {"artista": "Oasis", "precio": 200,"stock":12},
        {"artista": "Rosalía", "precio": 150,"stock":20},
        {"artista": "Medina Azahara", "precio": 40,"stock":0}
    ]
    return render_template("entradas.html", entradas=entradas)

if __name__ == "__main__":
    app.run(debug=True)