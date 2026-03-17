from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Datos de ejemplo
    usuarios = [
        {"nombre": "Ana", "edad": 22, "email": "ana@example.com"},
        {"nombre": "Pedro", "edad": 30, "email": "pedro@example.com"},
        {"nombre": "Luis", "edad": 27, "email": "luis@example.com"}
    ]
    columnas = ["nombre", "edad", "email"]
    return render_template("usuarios.html", usuarios=usuarios, columnas=columnas)

if __name__ == "__main__":
    app.run(debug=True)