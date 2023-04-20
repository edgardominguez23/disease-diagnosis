from django_unicorn.components import UnicornView
from user.models import Paciente, Direccion
from main.forms import PacienteForm

class PacienteFormView(UnicornView):
    paciente = None

    form_class = PacienteForm
    nombre = ""
    apellidos = ""
    telefono = None
    municipio = ""
    colonia = ""
    codigoPostal = None
    calle = ""
    numero = None

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.paciente = None if kwargs.get("paciente") == 'paciente' else kwargs.get("paciente")

    def mount(self):
        if self.paciente:
            self.nombre = self.paciente.nombre
            self.apellidos = self.paciente.apellidos
            self.telefono = self.paciente.telefono
            self.municipio = self.paciente.direccion.all()[0].municipio
            self.colonia = self.paciente.direccion.all()[0].colonia
            self.codigoPostal = self.paciente.direccion.all()[0].codigoPostal
            self.calle = self.paciente.direccion.all()[0].calle
            self.numero = self.paciente.direccion.all()[0].numero

    def save_paciente(self):
        if self.is_valid() and self.validar_nombre_unico():
            if self.paciente:
                self.paciente.nombre = self.nombre
                self.paciente.apellidos = self.apellidos
                self.paciente.telefono = self.telefono
                self.paciente.save()

                direccion = self.paciente.direccion.all()[0]
                direccion.municipio = self.municipio
                direccion.colonia = self.colonia
                direccion.codigoPostal = self.codigoPostal
                direccion.calle = self.calle
                direccion.numero = self.numero
                direccion.save()

                self.call("alerta_actualizacion_satisfactoria")
            else:
                paciente = Paciente(
                                nombre=self.nombre,
                                apellidos = self.apellidos,
                                telefono = self.telefono,
                            )
                paciente.save()

                direccion = Direccion(
                                municipio = self.municipio,
                                colonia = self.colonia,
                                codigoPostal = self.codigoPostal,
                                calle = self.calle,
                                numero = self.numero,
                                content_object = paciente,
                            )
                direccion.save()

                self.call("alerta_creacion_satisfactoria")

    def validar_nombre_unico(self):
        if self.paciente:
            if not self.paciente.nombre == self.nombre:
                if Paciente.objects.filter(nombre=self.nombre).exists():
                    self.call("alerta_nombre_existente")
                    return False
        else:
            if Paciente.objects.filter(nombre=self.nombre).exists():
                    self.call("alerta_nombre_existente")
                    return False
        
        return True

