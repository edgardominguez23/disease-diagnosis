from django_unicorn.components import UnicornView
from django.contrib.auth.models import Group
from user.forms import GroupForm

class RolesListView(UnicornView):
    roles = Group.objects.none()
    rol = None
    isOpenModal = "hidden"

    form_class = GroupForm
    name = ""

    def mount(self):
        self.load_table()

    def hydrate(self):
        self.load_table()

    def load_table(self):
        self.roles = Group.objects.all()

    def open_modal(self, id=None):
        self.form_class = GroupForm
        self.isOpenModal = ""

        if id:
            self.rol = Group.objects.get(id=id)
            self.name = self.rol.name

    def close_modal(self):
        self.restablecer_valores()

    def save_rol(self):
        if self.is_valid() and self.validar_nombre_unico():
            if self.rol:
                self.rol.name = self.name
                self.rol.save()
                self.call("alerta_actualizacion_satisfactoria")
            else:
                print("Guardar")
                rol = Group(name=self.name)
                rol.save()
                self.call("alerta_creacion_satisfactoria")

            self.restablecer_valores()

    def delete_rol(self, id):
        rol = Group.objects.get(id=id)
        rol.delete()
        self.call("alerta_eliminacion_satisfactoria")

    def restablecer_valores(self):
        self.name = ""
        self.rol = None
        self.isOpenModal = "hidden"

    def validar_nombre_unico(self):
        if self.rol:
            if not self.rol.name == self.name:
                if Group.objects.filter(name=self.name).exists():
                    self.call("alerta_nombre_existente")
                    return False
        else:
            if Group.objects.filter(name=self.name).exists():
                    self.call("alerta_nombre_existente")
                    return False
        
        return True