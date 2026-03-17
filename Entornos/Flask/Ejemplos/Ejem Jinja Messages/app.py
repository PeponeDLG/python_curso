from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'secret_flash_example'

usuarios = []

@app.route('/', methods=['GET', 'POST'])
def flash_form():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        if nombre:
            usuarios.append(nombre)
            flash(f'Usuario {nombre} añadido correctamente', 'success')
        else:
            flash('Debes introducir un nombre', 'error')
        return redirect(url_for('flash_form'))
    return render_template('flash_form.html', usuarios=usuarios)

if __name__ == '__main__':
    app.run(debug=True)
