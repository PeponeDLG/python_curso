from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    param = "Ana"
    lista = ["Ana", "Luis", "Marta"]
    return render_template("index.html",nombre=param,edad=21,alumnos=lista)

if __name__ == "__main__":
    app.run(debug=True)

