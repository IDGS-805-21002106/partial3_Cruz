from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, RadioField
from wtforms import validators

class UserForm(FlaskForm):
    nombre = StringField('Nombre', [
        validators.DataRequired(message='El campo es requerido'),
        validators.Length(min=4, max=100, message='Ingresa un nombre válido')
    ])
    username = StringField('Username', [
        validators.DataRequired(message='El campo es requerido'),
        validators.Length(min=4, max=50, message='Ingresa un username válido')
    ])
    contrasenia = PasswordField('Contraseña', [
        validators.DataRequired(message='El campo es requerido'),
        validators.Length(min=4, max=255, message='Ingresa una contraseña válida')
    ])
    rol = RadioField('Rol', choices=[('admin', 'Administrador'), ('user', 'Usuario')], default='user', validators=[validators.DataRequired()])


class LoginForm(FlaskForm):
    username = StringField('Usuario', [
        validators.DataRequired(message='El campo es requerido'),
        validators.Length(min=4, max=50, message='Ingresa un username válido')
    ])
    password = PasswordField('Contraseña', [
        validators.DataRequired(message='El campo es requerido'),
        validators.Length(min=4, max=255, message='Ingresa una contraseña válida')
    ])