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
        
auto_pepito = Auto("Toyota", "Corolla", 2020)
auto_pepito.mostrar_informacion()
auto_pepito.actualizar_kilometraje(15000)
print(auto_pepito.kilometraje)
auto_pepito.realizar_viaje(15000)
print(auto_pepito.estado_auto())
