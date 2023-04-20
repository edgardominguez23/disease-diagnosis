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

    def save_consultorio(self):
        if self.is_valid():
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

