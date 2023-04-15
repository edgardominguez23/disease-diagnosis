from django_unicorn.components import UnicornView
from main.models import PruebaPostmorten
from main.forms import PruebaPostmortenForm

class PruebasPostmortenListView(UnicornView):
    pruebas = PruebaPostmorten.objects.none()
    prueba = None
    isOpenModal = "hidden"

    form_class = PruebaPostmortenForm
    nombre = ""

    def mount(self):
        self.load_table()

    def hydrate(self):
        self.load_table()

    def load_table(self):
        self.pruebas = PruebaPostmorten.objects.all()

    def open_modal(self, id=None):
        self.form_class = PruebaPostmortenForm
        self.isOpenModal = ""

        if id:
            self.prueba = PruebaPostmorten.objects.get(id=id)
            self.nombre = self.prueba.nombre

    def close_modal(self):
        self.restablecer_valores()

    def save_prueba(self):
        if self.is_valid() and self.validar_nombre_unico():
            if self.prueba:
                self.prueba.nombre = self.nombre
                self.prueba.save()
                self.call("alerta_actualizacion_satisfactoria")
            else:
                prueba = PruebaPostmorten(nombre=self.nombre)
                prueba.save()
                self.call("alerta_creacion_satisfactoria")

            self.restablecer_valores()

    def delete_prueba(self, id):
        prueba = PruebaPostmorten.objects.get(id=id)
        prueba.delete()
        self.call("alerta_eliminacion_satisfactoria")

    def restablecer_valores(self):
        self.nombre = ""
        self.prueba = None
        self.isOpenModal = "hidden"

    def validar_nombre_unico(self):
        if self.prueba:
            if not self.prueba.nombre == self.nombre:
                if PruebaPostmorten.objects.filter(nombre=self.nombre).exists():
                    self.call("alerta_nombre_existente")
                    return False
        else:
            if PruebaPostmorten.objects.filter(nombre=self.nombre).exists():
                    self.call("alerta_nombre_existente")
                    return False
        
        return True
