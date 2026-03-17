from flask import Flask, render_template, request

app = Flask(__name__)
alumnos = [
        {"nombre": "Ana", "nota": 8},
        {"nombre": "Luis", "nota": 4}
    ]
@app.route("/")
def inicio():
    return render_template("formulario.html")

@app.route("/resultado", methods=["POST"])
def resultado():
    nombre = request.form["nombre"]
    edad = int(request.form["edad"])

    return render_template(
        "resultado.html",
        nombre=nombre,
        edad=edad
    )

@app.route("/clase")
def clase():
    
    return render_template(
        "clase.html",
        alumnos=alumnos
    )

@app.route("/detalle/<int:id>")
def detalle(id):
    alumno = alumnos[id]
    return render_template(
        "detalle.html",
        alumno=alumno
    )

if __name__ == "__main__":
    app.run(debug=True)