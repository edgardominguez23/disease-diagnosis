from django_unicorn.components import UnicornView
from user.models import Cita, Consulta, Paciente
from django.contrib.auth.models import User
from django.shortcuts import redirect

class CitasListView(UnicornView):
    medico = None
    citas = Cita.objects.none()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.medico = None if kwargs.get("medico") == 'medico' else kwargs.get("medico")

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

    def generar_consulta(self, id):
        cita = Cita.objects.get(id=id)
        if not hasattr(cita, 'consulta'):
            consulta = Consulta( 
                cita = cita,
                medico = User.objects.get(id=self.medico.id),
                paciente = Paciente.objects.get(id=cita.paciente.id)
            )
            consulta.save()

        return redirect(f"/admin/citas/{cita.id}/consulta")

