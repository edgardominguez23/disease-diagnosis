from django_unicorn.components import UnicornView
from ai.inferenceEngine.learning import show_symptoms, show_signs
from ai.inferenceEngine.engine import diagnose
from multiprocessing import Process, Queue
from queue import Empty

class ConsultaFormView(UnicornView):
    symptoms = show_symptoms()
    signs = show_signs()

    diagnistico = ""

    def get_consulta(self, padecimientos):
        #padecimientos = self.signos + self.sintomas
        queue = Queue()
        p = Process(target=diagnose, args=(padecimientos.split(","), queue))
        p.start()

        # Esperar a que se completen los resultados
        p.join()

        try:
            self.diagnistico = queue.get(timeout=10).title().replace("_", " ")
            print(self.diagnistico)
        except Empty:
            self.diagnistico = "No se encontraron resultados en el tiempo especificado."
