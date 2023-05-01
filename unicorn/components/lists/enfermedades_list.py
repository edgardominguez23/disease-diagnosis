from django_unicorn.components import UnicornView
from user.models import Enfermedad

class EnfermedadesListView(UnicornView):
    enfermedades = Enfermedad.objects.none()

    def mount(self):
        self.load_table()

    def hydrate(self):
        self.load_table()

    def load_table(self):
        self.enfermedades = Enfermedad.objects.all()

    def delete_enfermedad(self, id):
        enfermedad = Enfermedad.objects.get(id=id)
        enfermedad.delete()
        self.call("alerta_eliminacion_satisfactoria")
