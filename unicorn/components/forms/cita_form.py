from django_unicorn.components import UnicornView
from user.models import Cita, Paciente, Consultorio
from django.contrib.auth.models import User
from main.forms import CitaForm
from datetime import datetime

class CitaFormView(UnicornView):
    cita = None
    secretario = None

    estados = None
    pacientes = None
    consultorios = None
    medicos = None

    form_class = CitaForm
    consultorio = None
    paciente = None
    medico = None
    fecha = None
    hora = None
    estado = ""


    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.cita = None if kwargs.get("cita") == 'cita' else kwargs.get("cita")
        self.secretario = None if kwargs.get("secretario") == 'secretario' else kwargs.get("secretario")

    def mount(self):
        self.load_data()

        if self.cita:
            self.consultorio = self.cita.consultorio.id
            self.paciente = self.cita.paciente.id
            self.medico = self.cita.medico.id
            self.fecha = self.cita.fecha
            self.hora = self.cita.hora
            self.estado = self.cita.estado

    def load_data(self):
        self.estados = [member.value for name, member in Cita.EstadoCita.__members__.items()]
        self.pacientes = Paciente.objects.all()
        self.consultorios = Consultorio.objects.all()
        self.medicos = User.objects.all()

    def save_cita(self):
        if self.is_valid():
            if self.cita:
                self.cita.fecha = self.fecha
                self.cita.hora = self.hora
                self.cita.paciente = Paciente.objects.get(id=self.paciente)
                self.cita.medico = User.objects.get(id=self.medico)
                self.cita.secretaria = User.objects.get(id=self.secretario.id)
                self.cita.consultorio = Consultorio.objects.get(id=self.consultorio)
                self.cita.estado = self.estado
                self.cita.save()

                self.call("alerta_actualizacion_satisfactoria")
            else:
                cita = Cita(
                    fecha = self.fecha,
                    hora = self.hora,
                    paciente = Paciente.objects.get(id=self.paciente),
                    medico = User.objects.get(id=self.medico),
                    secretaria = User.objects.get(id=self.secretario.id),
                    consultorio = Consultorio.objects.get(id=self.consultorio),
                    estado = self.estado
                )
                cita.save()

                self.call("alerta_creacion_satisfactoria")
