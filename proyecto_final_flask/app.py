from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///videoclub.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Pelicula(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    director = db.Column(db.String(100), nullable=False)
    año = db.Column(db.Integer, nullable=False)
    precio_alquiler = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Pelicula {self.titulo}>'


with app.app_context():
    db.create_all()


@app.route('/')
def index():
    peliculas = Pelicula.query.all()
    return render_template('index.html', peliculas=peliculas)


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


@app.route('/pelicula/<int:id>')
def detalle(id):
    pelicula = Pelicula.query.get_or_404(id)
    return render_template('detalle.html', pelicula=pelicula)


@app.route('/pelicula/<int:id>/eliminar', methods=['POST'])
def eliminar(id):
    pelicula = Pelicula.query.get_or_404(id)
    db.session.delete(pelicula)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
