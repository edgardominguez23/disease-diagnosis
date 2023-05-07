from django_unicorn.components import UnicornView
from user.models import HistorialConsultas

class HistorialListView(UnicornView):
    paciente = None
    historial = HistorialConsultas.objects.none()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.paciente = None if kwargs.get("paciente") == 'paciente' else kwargs.get("paciente")

    def mount(self):
        self.load_table()

    def load_table(self):
        self.historial = HistorialConsultas.objects.filter(paciente_id=self.paciente.id)
