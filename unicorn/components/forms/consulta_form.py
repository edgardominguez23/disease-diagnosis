from django_unicorn.components import UnicornView
from ai.inferenceEngine.learning import show_symptoms, show_signs
from ai.inferenceEngine.engine import diagnose
from multiprocessing import Process, Queue
from queue import Empty

class ConsultaFormView(UnicornView):
    cita = None
    symptoms = show_symptoms()
    signs = show_signs()

    diagnistico = ""
    tratamiento = ""

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.cita = None if kwargs.get("cita") == 'cita' else kwargs.get("cita")

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
