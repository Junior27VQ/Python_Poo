from laptop import Laptop
from laptop_gaiming import LaptopGaming
from laptop_business import Laptop_Business

laptop_maria = Laptop("Dell", "XPS 13", "Intel Core i7", 16, 512)
laptop_pepito = Laptop("HP", "Spectre x360", "Intel Core i5", 8, 256)

# print(laptop_maria.calcular_precio_final())  # Precio final de la laptop de María
# print(laptop_pepito.calcular_precio_final())  # Precio final de la laptop de Pepito
# print(Laptop.comparar_costos(laptop_maria, laptop_pepito))  # Comparación de costos entre las dos laptops

# for numero in range(1, 1000):
#     laptop_asus = Laptop.asus_laptop(numero)  # Creación de una laptop Asus utilizando el método de clase
#     print(laptop_asus.__dict__)  # Imprime los atributos de la laptop Asus creada con el costo actual del bucle

# laptop_juanito = LaptopGaming("Alienware", "Intel Core i9", 32, 1024, "NVIDIA RTX 3080")
# print(laptop_juanito.realizar_diagnostico_sistema())  # Resultado del diagnóstico del sistema de la laptop gaming

laptop_julisa = Laptop_Business("Dell", "Intel Core i7", 16, 512, 10, 8)
print(laptop_julisa.realizar_diagnostico_sistema())  # Resultado del diagnóstico del sistema de la laptop business
print(laptop_julisa.verificar_conectividad_red())  # Resultado de la verificación de conectividad de red de la laptop business