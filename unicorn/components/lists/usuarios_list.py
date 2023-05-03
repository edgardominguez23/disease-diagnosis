from django_unicorn.components import UnicornView
from django.contrib.auth.models import User

class UsuariosListView(UnicornView):
    usuarios = User.objects.none()

    def mount(self):
        self.load_table()

    def hydrate(self):
        self.load_table()

    def load_table(self):
        self.usuarios = User.objects.all()

    def delete_usuario(self, id):
        usuario = User.objects.get(id=id)
        usuario.delete()
        self.call("alerta_eliminacion_satisfactoria")
