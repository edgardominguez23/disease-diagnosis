from django_unicorn.components import UnicornView
from django.contrib.auth.models import Permission

class PermisosListView(UnicornView):
    permisos = Permission.objects.none()

    def mount(self):
        self.load_table()

    def hydrate(self):
        self.load_table()

    def load_table(self):
        self.permisos = Permission.objects.all()
