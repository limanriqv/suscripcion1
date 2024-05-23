from django import forms

class RegistroForm(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True)
    apellido = forms.CharField(label="Apellido", required=True)
    dni = forms.DecimalField(label="DNI", required=True)
    email = forms.EmailField(label="Email", required=True)
    contraseña = forms.CharField(widget=forms.PasswordInput(),label="Contraseña", required=True)