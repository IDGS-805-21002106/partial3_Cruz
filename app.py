from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.secret_key = 'mi clave secretoa'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

users = {
    'admin': {'password': 'admin123', 'role': 'admin'},
    'user1': {'password': 'user1123', 'role': 'user'},
    'user2': {'password': 'user2123', 'role': 'user'}
}

class User(UserMixin):
    def __init__(self, username):
        self.id = username
        self.role = users[username]['role']

    @staticmethod
    def get(username):
        if username in users:
            return User(username)
        return None

@login_manager.user_loader
def load_user(username):
    return User.get(username)


@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            user = User.get(username)
            login_user(user)
            if user.role == 'admin':
                return redirect(url_for('administrador'))
            else:
                return redirect(url_for('usuario'))
        flash('Usuario o contraseña incorrectos', 'error')
    return render_template('login.html')

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
    app.run(debug=True)