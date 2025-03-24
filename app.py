from flask import Flask, render_template, redirect, url_for, request, flash 
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import forms
from models import db, Usuarios
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.secret_key = "esta es mi clave secreta"
csrf = CSRFProtect(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin):
    def __init__(self, id, username, role):
        self.id = id
        self.username = username
        self.role = role



@login_manager.user_loader
def load_user(user_id):
    user = Usuarios.query.get(int(user_id))
    if user:
        return User(user.id, user.username, user.rol)
    return None

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route("/registro", methods=['GET', 'POST'])
def Registro():
    create_form = forms.UserForm(request.form)

    if request.method == 'POST' and create_form.validate():
        user = Usuarios(
            nombre=create_form.nombre.data,
            username=create_form.username.data,
            contrasenia=create_form.contrasenia.data,
            rol=create_form.rol.data
        )
        db.session.add(user)
        db.session.commit()
        flash('Usuario registrado exitosamente', 'success')
        return redirect(url_for('Registro'))

    return render_template('registro.html', form=create_form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = Usuarios.query.filter_by(username=username, contrasenia=password).first()
        if user:
            login_user(User(user.id, user.username, user.rol))
            if user.rol == 'admin':
                return redirect(url_for('administrador'))
            else:
                return redirect(url_for('usuario'))
        flash('Usuario o contraseña incorrectos', 'error')
    return render_template('login.html', form=form)

@app.route('/administrador')
@login_required
def administrador():
    if current_user.role != 'admin':
        flash('No tienes permiso para acceder a esta pagina :/ ', 'error')
        return redirect(url_for('usuario'))
    return render_template('administrador.html')

@app.route('/usuario')
@login_required
def usuario():
    return render_template('usuario.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Se cerro la sesion', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(debug=True)
