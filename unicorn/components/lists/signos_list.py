from django_unicorn.components import UnicornView
from main.models import Signo
from main.forms import SignoForm

class SignosListView(UnicornView):
    signos = Signo.objects.none()
    signo = None
    isOpenModal = "hidden"

    form_class = SignoForm
    nombre = ""

    def mount(self):
        self.load_table()

    def hydrate(self):
        self.load_table()

    def load_table(self):
        self.signos = Signo.objects.all()

    def open_modal(self, id=None):
        self.form_class = SignoForm
        self.isOpenModal = ""

        if id:
            self.signo = Signo.objects.get(id=id)
            self.nombre = self.signo.nombre

    def close_modal(self):
        self.restablecer_valores()

    def save_signo(self):
        if self.is_valid() and self.validar_nombre_unico():
            if self.signo:
                self.signo.nombre = self.nombre
                self.signo.save()
                self.call("alerta_actualizacion_satisfactoria")
            else:
                signo = Signo(nombre=self.nombre)
                signo.save()
                self.call("alerta_creacion_satisfactoria")

            self.restablecer_valores()

    def delete_signo(self, id):
        signo = Signo.objects.get(id=id)
        signo.delete()
        self.call("alerta_eliminacion_satisfactoria")

    def restablecer_valores(self):
        self.nombre = ""
        self.signo = None
        self.isOpenModal = "hidden"

    def validar_nombre_unico(self):
        if self.signo:
            if not self.signo.nombre == self.nombre:
                if Signo.objects.filter(nombre=self.nombre).exists():
                    self.call("alerta_nombre_existente")
                    return False
        else:
            if Signo.objects.filter(nombre=self.nombre).exists():
                    self.call("alerta_nombre_existente")
                    return False
        
        return True
