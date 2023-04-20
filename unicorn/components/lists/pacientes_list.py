from django_unicorn.components import UnicornView
from user.models import Paciente

class PacientesListView(UnicornView):
    pacientes = Paciente.objects.none()

    def mount(self):
        self.load_table()

    def hydrate(self):
        self.load_table()

    def load_table(self):
        self.pacientes = Paciente.objects.all()

    def delete_consultorio(self, id):
        paciente = Paciente.objects.get(id=id)
        paciente.delete()
        self.call("alerta_eliminacion_satisfactoria")
