from flask import Flask, request

app = Flask(__name__)

@app.route("/") # http://127.0.0.1:5000
def inicio():
    return "<h1>Hola mundo</h1>"

@app.route("/saluda/<nombre>") # http://127.0.0.1:5000/saluda/pepe
def saludo(nombre):
    return f"Hola {nombre}"

@app.route("/suma",methods = ["GET","POST"])
@app.route("/suma",methods = ["GET","POST"])
def suma():
    htmlCode = ""

    if request.method == "POST":
        p


if __name__=="__main__":
    app.run(debug=True)