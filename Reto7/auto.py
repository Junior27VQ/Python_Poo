class Auto:
    def __init__(self, marca, modelo, año, kilometraje=0):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = kilometraje

    def mostrar_informacion(self):
        print(f"{self.marca} {self.modelo} ({self.año}) ")

    def actualizar_kilometraje(self, nuevo_kilometraje):
        if nuevo_kilometraje >= self.kilometraje:
            self.kilometraje = nuevo_kilometraje
        else:
            print("No se puede reducir el kilometraje.")

    def realizar_viaje(self, kilometros):
        if kilometros > 0:
            self.kilometraje += kilometros
        else:
            print("Los kilometros del viaje debe ser positivo.")

    def estado_auto(self):
        if self.kilometraje < 20000:
            return "Estoy como nuevo"
        elif self.kilometraje > 20000 and self.kilometraje < 100000:
            return "Ya estoy usando"
        elif self.kilometraje > 100000:
            return "Ya dejame descansar por favor!"
        else:
            return "Viejo"
        
    @staticmethod
    def comparar_kilometraje(auto1, auto2):
        if auto1.kilometraje < auto2.kilometraje:
            return f"{auto1.marca} {auto1.modelo} tiene menos kilometraje que {auto2.marca} {auto2.modelo}"
        elif auto1.kilometraje > auto2.kilometraje:
            return f"{auto2.marca} {auto2.modelo} tiene menos kilometraje que {auto1.marca} {auto1.modelo}"
        else:
            return "Ambos autos tienen el mismo kilometraje"
    @classmethod
    def auto_nuevo(cls, kilometraje):
        marca = "Tollota"
        modelo = "Corolla"
        año = 2026
        return cls(marca, modelo, año, kilometraje)
    @staticmethod
    def comparar_año(auto1, auto2):
        if auto1.año < auto2.año:
            return f"{auto1.marca} {auto1.modelo} es más antiguo que {auto2.marca} {auto2.modelo}"
        elif auto1.año > auto2.año:
            return f"{auto2.marca} {auto2.modelo} es más antiguo que {auto1.marca} {auto1.modelo}"
        else:
            return "Ambos autos tienen el mismo año"
    @classmethod
    def auto_usado(cls, marca):
        modelo = "Corolla"
        año = 2020
        kilometraje = 50000
        return cls(marca, modelo, año, kilometraje)