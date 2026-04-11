from laptop import Laptop

class LaptopGaming(Laptop):
    def __init__(self, marca, procesador, ram, almacenamiento,tarjeta_grafica, costo=1500, impuesto=0.20):
        super().__init__(marca, procesador, ram, almacenamiento, costo, impuesto)
        self.tarjeta_grafica = tarjeta_grafica

    def realizar_diagnostico_juegos(self):
        juegos = ["Cyberpunk 2077", "Red Dead Redemption 2", "Assassin's Creed Valhalla", "Call of Duty: Warzone"]
        resultados = {}
        for juego in juegos:
            fps_base = 30
            if "RTX" in self.tarjeta_grafica:
                fps = fps_base * 3
            elif "GTX" in self.tarjeta_grafica:
                fps_base * 2
            else:
                fps = fps_base
            resultados[juego] = f"{fps} FPS"
        return resultados
    

    def realizar_diagnostico_sistema(self):
        resultados_diagnostico = super().realizar_diagnostico_sistema()
        resultado_juegos = self.realizar_diagnostico_juegos()
        resultados_diagnostico["Resultado juegos"] = resultado_juegos 
        return resultados_diagnostico

    pass