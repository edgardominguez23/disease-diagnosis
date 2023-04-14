from django_unicorn.components import UnicornView
from main.models import Sintoma
from main.forms import SintomaForm

class SintomasListView(UnicornView):
    sintomas = Sintoma.objects.none()
    sintoma = None
    isOpenModal = "hidden"

    form_class = SintomaForm
    nombre = ""

    def mount(self):
        self.load_table()

    def hydrate(self):
        self.load_table()

    def load_table(self):
        self.sintomas = Sintoma.objects.all()

    def open_modal(self, id=None):
        self.form_class = SintomaForm
        self.isOpenModal = ""

        if id:
            self.sintoma = Sintoma.objects.get(id=id)
            self.nombre = self.sintoma.nombre

    def close_modal(self):
        self.restablecer_valores()

    def save_sintoma(self):
        if self.is_valid() and self.validar_nombre_unico():
            if self.sintoma:
                self.sintoma.nombre = self.nombre
                self.sintoma.save()
                self.call("alerta_actualizacion_satisfactoria")
            else:
                sintoma = Sintoma(nombre=self.nombre)
                sintoma.save()
                self.call("alerta_creacion_satisfactoria")

            self.restablecer_valores()

    def delete_sintoma(self, id):
        sintoma = Sintoma.objects.get(id=id)
        sintoma.delete()
        self.call("alerta_eliminacion_satisfactoria")

    def restablecer_valores(self):
        self.nombre = ""
        self.sintoma = None
        self.isOpenModal = "hidden"

    def validar_nombre_unico(self):
        if self.sintoma:
            if not self.sintoma.nombre == self.nombre:
                if Sintoma.objects.filter(nombre=self.nombre).exists():
                    self.call("alerta_nombre_existente")
                    return False
        else:
            if Sintoma.objects.filter(nombre=self.nombre).exists():
                    self.call("alerta_nombre_existente")
                    return False
        
        return True
