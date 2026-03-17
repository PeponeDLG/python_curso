from flask import Flask, render_template,render_template,render_template_string

app = Flask(__name__)

@app.route("/")
def inicio():
    alumnos = [
        {"nombre": "Ana", "nota": 8},
        {"nombre": "Luis", "nota": 4}]
    return render_template("index.html",alumnos=alumnos)


@app.route("/hola")
def hola():
    return render_template_string("<h1>Hola {{ nombre }}</h1>", nombre="Rey")


if __name__ == "__main__":
    app.run(debug=True)