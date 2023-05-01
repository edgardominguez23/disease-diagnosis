from django_unicorn.components import UnicornView
from user.models import Enfermedad
from main.forms import EnfermedadForm

class EnfermedadFormView(UnicornView):
    enfermedad = None

    form_class = EnfermedadForm
    nombre = ""

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.enfermedad = None if kwargs.get("enfermedad") == 'enfermedad' else kwargs.get("enfermedad")

    def mount(self):
        if self.enfermedad:
            self.nombre = self.enfermedad.nombre

    def save_paciente(self):
        if self.is_valid() and self.validar_nombre_unico():
            if self.enfermedad:
                self.enfermedad.nombre = self.nombre
                self.enfermedad.save()

                self.call("alerta_actualizacion_satisfactoria")
            else:
                enfermedad = Enfermedad(
                                nombre=self.nombre,
                            )
                enfermedad.save()

                self.call("alerta_creacion_satisfactoria")

    def validar_nombre_unico(self):
        if self.enfermedad:
            if not self.enfermedad.nombre == self.nombre:
                if Enfermedad.objects.filter(nombre=self.nombre).exists():
                    self.call("alerta_nombre_existente")
                    return False
        else:
            if Enfermedad.objects.filter(nombre=self.nombre).exists():
                    self.call("alerta_nombre_existente")
                    return False
        
        return True

