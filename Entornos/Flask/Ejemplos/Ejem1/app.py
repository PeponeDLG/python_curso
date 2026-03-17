from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Hola mundo II"


@app.route("/saludo/<nombre>")
def saludo(nombre):
    return f"Hola {nombre}"


@app.route('/suma',methods = ["GET", "POST"])
@app.route('/suma/',methods = ["GET", "POST"])
def suma():
    htmlCode = ""
    if request.method == "POST":
        print("POST") # Obtenemos datos y calcula
        sumando1 = int(request.form.get("Sumando1"))
        sumando2 = int(request.form.get("Sumando2"))
        htmlCode = "Resultado: " +  str(sumando1 +sumando2)
    else:
        print("GET") # Mostramos HTML
        htmlCode = '''<form action="/suma" method="POST">
                <label>Sumando 1:</label>
                <input type="text" name="Sumando1"/>
                <label>Sumando 2:</label>
                <input type="text" name="Sumando2"/><br/><br/>
                <input type="submit"/>
                </form>'''
    return htmlCode



if __name__ == "__main__":
    app.run(debug=True)