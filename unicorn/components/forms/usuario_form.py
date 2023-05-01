from django_unicorn.components import UnicornView
from django.contrib.auth.models import User
from main.forms import UsuarioForm

class UsuarioFormView(UnicornView):
    usuario = None

    form_class = UsuarioForm
    username = ""
    first_name = ""
    last_name = ""
    email = ""
    password1 = ""
    password2 = ""

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.usuario = None if kwargs.get("usuario") == 'usuario' else kwargs.get("usuario")

    def mount(self):
        if self.usuario:
            self.username = self.usuario.username
            self.first_name = self.usuario.first_name
            self.last_name = self.usuario.last_name
            self.email = self.usuario.email

    def save_usuario(self):
        if self.is_valid() and self.validar_username_unico():
            if self.usuario:
                self.usuario.username = self.username
                self.usuario.first_name = self.first_name
                self.usuario.last_name = self.last_name
                self.usuario.email = self.email
                self.usuario.save()

                self.call("alerta_actualizacion_satisfactoria")
            else:
                usuario = User(
                                username = self.username,
                                first_name=self.first_name,
                                last_name = self.last_name,
                                email = self.email,
                                password = self.password1,
                            )
                usuario.save()

                self.call("alerta_creacion_satisfactoria")

    def validar_username_unico(self):
        if self.usuario:
            if not self.usuario.username == self.username:
                if User.objects.filter(username=self.username).exists():
                    self.call("alerta_nombre_existente")
                    return False
        else:
            if User.objects.filter(username=self.username).exists():
                    self.call("alerta_nombre_existente")
                    return False
        
        return True