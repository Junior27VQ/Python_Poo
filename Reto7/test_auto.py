from auto import Auto

auto1 = Auto("Honda", "Civic", 2018, 25000)
auto2 = Auto("Ford", "Focus", 2019, 15000)

#auto_pepito = Auto("Toyota", "Corolla", 2020)
# auto_pepito.mostrar_informacion()
# auto_pepito.actualizar_kilometraje(15000)
# print(auto_pepito.kilometraje)
# auto_pepito.realizar_viaje(15000)
# print(auto_pepito.estado_auto())
    
print(Auto.comparar_kilometraje(auto1, auto2))
print(Auto.comparar_año(auto1, auto2))

for kilometraje in range(0, 100000, 20000):
    auto_nuevo = Auto.auto_nuevo(kilometraje)
    print(auto_nuevo.__dict__)
for marca in ["Mazda", "Nissan", "Chevrolet"]:
    auto_usado = Auto.auto_usado(marca)
    print(auto_usado.__dict__)

    