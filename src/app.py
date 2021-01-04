#python3
# pip install mysqlclient
# pip install Flask
# pip install Flask-SQLAlchemy
# pip install virtualenv
# virtualenv venv

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from config import Developementconfig, Config


app = Flask(__name__)
app.secret_key = "Secret Key"

#SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1/crudflask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Datos(db.Model):
    Id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100))
    email = db.Column(db.String(100))
    telefono = db.Column(db.String(100))


    def __init__ (self, nombre, email, telefono):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono


@app.route('/')
def Index():
    all_data = Datos.query.all()
    return render_template("index.html", empleados = all_data)

@app.route('/insertar', methods = ['POST'])
def insertar():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        telefono = request.form['telefono']

        my_data = Datos(nombre, email, telefono)
        db.session.add(my_data)
        db.session.commit()
        flash("Empleado " + nombre + " insertado correctamente")

        return redirect(url_for('Index'))

@app.route('/actualizar', methods = ['GET','POST'])
def actualizar():
    if request.method == 'POST':
        my_data = Datos.query.get(request.form.get('id'))
        my_data.nombre = request.form['nombre']
        my_data.email = request.form['email']
        my_data.telefono = request.form['telefono']

        db.session.commit()
        flash("Empleado " + my_data.nombre + " actualizado correctamente")
        return redirect(url_for('Index'))

@app.route('/eliminar/<id>', methods = ['GET', 'POST'])
def eliminar(id):
    my_data = Datos.query.get(id)

    db.session.delete(my_data)
    db.session.commit()
    flash("Empleado " + my_data.nombre + " eliminado correctamente")
    return redirect(url_for('Index'))

if __name__ == "__main__":
    
    app.run(debug = True)