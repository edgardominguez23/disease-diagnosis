from django_unicorn.components import UnicornView
from user.models import Consultorio

class ConsultoriosListView(UnicornView):
    consultorios = Consultorio.objects.none()

    def mount(self):
        self.load_table()

    def load_table(self):
        self.consultorios = Consultorio.objects.all()