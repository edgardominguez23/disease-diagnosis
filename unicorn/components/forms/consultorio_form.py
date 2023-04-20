from django_unicorn.components import UnicornView
from user.models import Consultorio, Direccion
from main.forms import ConsultorioForm

class ConsultorioFormView(UnicornView):
    consultorio = None

    form_class = ConsultorioForm
    nombre = ""
    hora_abierto = None
    hora_cerrado = None
    municipio = ""
    colonia = ""
    codigoPostal = None
    calle = ""
    numero = None

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.consultorio = None if kwargs.get("consultorio") == 'consultorio' else kwargs.get("consultorio")

    def mount(self):
        if self.consultorio:
            self.nombre = self.consultorio.nombre
            self.hora_abierto = self.consultorio.hora_abierto
            self.hora_cerrado = self.consultorio.hora_cerrado
            self.municipio = self.consultorio.direccion.all()[0].municipio
            self.colonia = self.consultorio.direccion.all()[0].colonia
            self.codigoPostal = self.consultorio.direccion.all()[0].codigoPostal
            self.calle = self.consultorio.direccion.all()[0].calle
            self.numero = self.consultorio.direccion.all()[0].numero

    def save_consultorio(self):
        if self.is_valid() and self.validar_nombre_unico():
            if self.consultorio:
                self.consultorio.nombre = self.nombre
                self.consultorio.hora_abierto = self.hora_abierto
                self.consultorio.hora_cerrrado = self.hora_cerrado
                self.consultorio.save()

                direccion = self.consultorio.direccion.all()[0]
                direccion.municipio = self.municipio
                direccion.colonia = self.colonia
                direccion.codigoPostal = self.codigoPostal
                direccion.calle = self.calle
                direccion.numero = self.numero
                direccion.save()

                self.call("alerta_actualizacion_satisfactoria")
            else:
                consultorio = Consultorio(
                                nombre=self.nombre,
                                hora_abierto = self.hora_abierto,
                                hora_cerrado = self.hora_cerrado,
                            )
                consultorio.save()

                direccion = Direccion(
                                municipio = self.municipio,
                                colonia = self.colonia,
                                codigoPostal = self.codigoPostal,
                                calle = self.calle,
                                numero = self.numero,
                                content_object = consultorio,
                            )
                direccion.save()

                self.call("alerta_creacion_satisfactoria")
    
    def validar_nombre_unico(self):
        if self.consultorio:
            if not self.consultorio.nombre == self.nombre:
                if Consultorio.objects.filter(nombre=self.nombre).exists():
                    self.call("alerta_nombre_existente")
                    return False
        else:
            if Consultorio.objects.filter(nombre=self.nombre).exists():
                    self.call("alerta_nombre_existente")
                    return False
        
        return True

