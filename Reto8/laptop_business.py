from laptop import Laptop
import random

class Laptop_Business(Laptop):
    def __init__(self, marca, procesador, ram, almacenamiento,espacio_disco, duracion_bateria, costo=1200, impuesto=0.18):
        super().__init__(marca, procesador, ram, almacenamiento, costo, impuesto)
        self.espacio_disco = espacio_disco
        self.duracion_bateria = duracion_bateria
    
    def realizar_diagnostico_sistema(self):
        resultado = super().realizar_diagnostico_sistema()
        resultado["ESPACIO DISCO"] = "OK " if self.espacio_disco >= 256 else "Aumentar espacio de disco"
        resultado["DURACION BATERIA"] = "OK " if self.duracion_bateria >= 8 else "Revisar duración de batería"
        return resultado
    
    def verificar_conectividad_red(self):
        diagnostico_red = {
            "WIFI": random.choice([True, False]),
            "ACCESO_SERVIDORES": random.choice([True, False]),
            "LATENCIA_RED": random.choice([True, False])
        }
        return diagnostico_red