import random

class Laptop:
    def __init__(self, marca, procesador, ram, almacenamiento, costo=1000, impuesto=0.15):
        self.marca = marca
        self.procesador = procesador
        self.ram = ram
        self.almacenamiento = almacenamiento
        self.costo = costo
        self.impuesto = impuesto

    def calcular_precio_final(self):
        return self.costo * (1 + self.impuesto)
    
    def descuento(self, porcentaje):
        descuento_amount = self.costo * (porcentaje / 100)
        return self.costo - descuento_amount
    def realizar_diagnostico_sistema(self):
        resultado = {
            "MARCA": f"{self.marca}",
            "PROCESADOR": f"{self.procesador}",
            "RAM": "OK " if self.ram >= 8 else "Aumentar memoria ram",
            "BATERIA": "OK " if random.choice([True, False]) else "Revisar batería",
        }
        return resultado

    #metodos estaticos
    @staticmethod
    def comparar_costos(laptop1, laptop2):
        if laptop1.costo < laptop2.costo:
            return f"{laptop1.marca} es más barata que {laptop2.marca}"
        elif laptop1.costo > laptop2.costo:
            return f"{laptop2.marca} es más barata que {laptop1.marca}"
        else:
            return "Ambas laptops tienen el mismo costo"
    @classmethod
    def asus_laptop (cls, costo):
        marca = "Lenovo"
        procesador = "AMD Ryzen 5"
        memoria = 16
        almacenamiento = 512
        return cls(marca, procesador, memoria, almacenamiento, costo)