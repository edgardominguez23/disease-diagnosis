from django_unicorn.components import UnicornView
from user.models import Cita

class CitasListView(UnicornView):
    citas = Cita.objects.none()

    def mount(self):
        self.load_table()

    def hydrate(self):
        self.load_table()

    def load_table(self):
        self.citas = Cita.objects.all()

    def delete_cita(self, id):
        cita = Cita.objects.get(id=id)
        cita.delete()
        self.call("alerta_eliminacion_satisfactoria")
