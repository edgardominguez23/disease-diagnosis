from django_unicorn.components import UnicornView
from django.contrib.auth.models import User, Group
from main.forms import UsuarioForm

class UsuarioFormView(UnicornView):
    usuario = None
    roles = ""

    form_class = UsuarioForm
    username = ""
    first_name = ""
    last_name = ""
    email = ""
    password = ""
    rol = ""

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        usuario = None if kwargs.get("usuario") == 'usuario' else kwargs.get("usuario")
        self.usuario =  None if usuario == None else User.objects.get(id=usuario.id)

    def mount(self):
        self.roles = Group.objects.all()

        if self.usuario:
            self.username = self.usuario.username
            self.first_name = self.usuario.first_name
            self.last_name = self.usuario.last_name
            self.email = self.usuario.email
            self.rol = self.usuario.groups.first().id

    def save_usuario(self):
        if self.is_valid() and self.validar_username_unico():
            if self.usuario:
                self.usuario.username = self.username
                self.usuario.first_name = self.first_name
                self.usuario.last_name = self.last_name
                self.usuario.email = self.email

                if self.password:
                    self.usuario.password = self.password

                self.usuario.save()

                grupo = Group.objects.get(id=self.rol)
                self.usuario.groups.add(grupo)

                self.call("alerta_actualizacion_satisfactoria")
            else:
                usuario = User.objects.create_user(
                                username = self.username,
                                first_name = self.first_name,
                                last_name = self.last_name,
                                email = self.email,
                                password = self.password if self.password else "1234567890"
                            )
                usuario.save()

                grupo = Group.objects.get(id=self.rol)
                usuario.groups.add(grupo)

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