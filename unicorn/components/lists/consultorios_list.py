from django_unicorn.components import UnicornView
from user.models import Consultorio

class ConsultoriosListView(UnicornView):
    consultorios = Consultorio.objects.none()

    def mount(self):
        self.load_table()

    def hydrate(self):
        self.load_table()

    def load_table(self):
        self.consultorios = Consultorio.objects.all()

    def delete_consultorio(self, id):
        consultorio = Consultorio.objects.get(id=id)
        consultorio.delete()
        self.call("alerta_eliminacion_satisfactoria")