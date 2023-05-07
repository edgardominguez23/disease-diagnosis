from django_unicorn.components import UnicornView
from ai.inferenceEngine.learning import show_symptoms, show_signs, show_lab_tests, show_postmortem_tests
from ai.inferenceEngine.engine import diagnose
from multiprocessing import Process, Queue
from queue import Empty
from django.shortcuts import redirect
from user.models import HistorialConsultas

class ConsultaFormView(UnicornView):
    cita = None
    symptoms = show_symptoms()
    signs = show_signs()
    lab_tests = show_lab_tests()
    postmortem_tests = show_postmortem_tests()

    diagnistico = ""
    tratamiento = ""
    estaVivo = True
    motivo = ""

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.cita = None if kwargs.get("cita") == 'cita' else kwargs.get("cita")
        self.estaVivo = self.cita.paciente.estaVivo

    def get_consulta(self, padecimientos):
        queue = Queue()
        p = Process(target=diagnose, args=(padecimientos.split(","), queue))
        p.start()

        # Esperar a que se completen los resultados
        p.join()

        try:
            lista = queue.get(timeout=10)
            self.diagnistico = lista[0]
            self.tratamiento = ', '.join(lista[1])
            print(self.diagnistico)
        except Empty:
            self.diagnistico = "No se encontraron resultados en el tiempo especificado."
    
    def guardar_consulta(self):
        if self.tratamiento and self.diagnistico:
            consulta = self.cita.consulta

            consulta.motivo = self.motivo
            consulta.diagnostico = self.diagnistico
            consulta.tratamiento = self.tratamiento
            consulta.save()

            self.cita.estado = "Completada"
            self.cita.save()

            historial = HistorialConsultas(
                paciente = consulta.paciente,
                consulta = consulta
            )
            historial.save()

            return redirect(f"/admin/citas")
