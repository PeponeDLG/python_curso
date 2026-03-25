from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "123456_secret_key"

# 🟢 Variables globales para las actividades
usuarios = ["ana", "pedro", "luis"]
numeros = [4, 7, 10, 3]
ciudades = ["Córdoba", "Sevilla", "Granada"]
productos_stock = [
    {"nombre": "ratón", "stock": 3},
    {"nombre": "teclado", "stock": 0},
    {"nombre": "monitor", "stock": 5}
]
precios = [10, 50, 120]

# 🔹 Filtros personalizados
@app.template_filter()
def precio_euro(valor):
    return f"{valor:,.2f} €".replace(",", "X").replace(".", ",").replace("X", ".")

@app.template_filter()
def color_precio(valor):
    if valor < 20:
        return "barato"
    elif 20 <= valor <= 100:
        return "medio"
    else:
        return "caro"

@app.template_filter()
def estado_stock(stock):
    if stock == 0:
        return "Sin stock"
    elif 1 <= stock <= 3:
        return "Pocas unidades"
    else:
        return "Disponible"

# 🟢 Actividad 1-3: Variables y renderizado
@app.route("/")
def index():
    nombre = "Ana"
    edad = 22
    from datetime import datetime
    fecha = datetime.now().strftime("%d/%m/%Y")
    return render_template("index.html", nombre=nombre, edad=edad, fecha=fecha)

# 🔁 Actividades 4-6: Bucles
@app.route("/bucles")
def bucles():
    return render_template("bucles.html", ciudades=ciudades, numeros=numeros)

# ⚖️ Actividades 7-8: Condicionales
@app.route("/condicionales")
def condicionales():
    return render_template("condicionales.html", numeros=numeros, productos=productos_stock)

# 🎨 Actividades 13-18: Filtros
@app.route("/filtros")
def filtros():
    return render_template("filtros.html", usuarios=usuarios, precios=precios, productos=productos_stock)

# 🧰 Actividades 19-22: Macros incluidas en filtros.html y macros.html
# No se requiere ruta extra; se usan en las plantillas

# 💬 Actividades 23-24: Flash messages
@app.route("/flash", methods=["GET", "POST"])
def flash_form():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        if nombre:
            usuarios.append(nombre)
            flash(f"Usuario {nombre} añadido correctamente", "success")
        else:
            flash("Debes introducir un nombre", "error")
        return redirect(url_for("flash_form"))
    return render_template("flash_form.html", usuarios=usuarios)

if __name__ == "__main__":
    app.run(debug=True)