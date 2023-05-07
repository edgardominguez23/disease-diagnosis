from django_unicorn.components import UnicornView
from user.models import Consulta

class ConsultasListView(UnicornView):
    consultas = Consulta.objects.none()

    def mount(self):
        self.load_table()

    def load_table(self):
        self.consultas = Consulta.objects.all()
