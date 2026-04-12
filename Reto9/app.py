from laptop_business import Laptop_Business
from laptop import Laptop
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

class app:
    def __init__(self, root):
        self.root = root
        self.laptop = []
        self.imagenes = ["C:\\PROGRAMACION.FAVQ\\MODULO5\\CONTENIDO\\Clae1\\img\\asus.png", 
                         "C:\\PROGRAMACION.FAVQ\\MODULO5\\CONTENIDO\\Clae1\\img\\game.png", 
                         "C:\\PROGRAMACION.FAVQ\\MODULO5\\CONTENIDO\\Clae1\\img\\hp.png", 
                         "C:\\PROGRAMACION.FAVQ\\MODULO5\\CONTENIDO\\Clae1\\img\\lenovo.png", 
                         "C:\\PROGRAMACION.FAVQ\\MODULO5\\CONTENIDO\\Clae1\\img\\neutro.png"
                         ]

        root.title("Ingresar Datos")

        self.setup_ui()
    def setup_ui(self):
        ttk.Label(self.root, text="Marca:").grid(row=0, column=0)
        self.marca = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.marca).grid(row=0, column=1)
        
        ttk.Label(self.root, text="Procesador:").grid(row=1, column=0)
        self.procesador = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.procesador).grid(row=1, column=1)
        
        ttk.Label(self.root, text="RAM:").grid(row=2, column=0)
        self.ram = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.ram).grid(row=2, column=1)
        
        ttk.Label(self.root, text="Almacenamiento:").grid(row=3, column=0)
        self.almacenamiento = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.almacenamiento).grid(row=3, column=1)
        
        ttk.Label(self.root, text="Espacio en Disco:").grid(row=4, column=0)
        self.espacio_disco = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.espacio_disco).grid(row=4, column=1)

        ttk.Label(self.root, text="Duración de la Batería:").grid(row=5, column=0)
        self.duracion_bateria = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.duracion_bateria).grid(row=5, column=1)

        ttk.Label(self.root, text="Costo:").grid(row=6, column=0)
        self.costo = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.costo).grid(row=6, column=1)

        ttk.Button(self.root, text="Agregar Laptop", command=self.agregar_laptop).grid(row=7, column=0, columnspan=2)
        self.mostrar_laptops = tk.Text(self.root, width=50, height=10)
        self.mostrar_laptops.grid(row=8, column=1, columnspan=2)

        self.canva = tk.Canvas(self.root, width=200, height=200)
        self.canva.grid(row=1, column=3, rowspan=6)
    
    def cargar_imagenes(self):
        imagen_path = random.choice(self.imagenes)
        imagen = Image.open(imagen_path)
        imagen = imagen.resize((200, 200), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(imagen)
        
        self.canva.create_image(0, 0, anchor=tk.NW, image=photo)
        self.canva.image = photo  # Mantener una referencia a la imagen para evitar que se elimine por el recolector de basura

    def agregar_laptop(self):
        nueva_laptop = Laptop_Business(
            self.marca.get(),
            self.procesador.get(),
            self.ram.get(),
            self.almacenamiento.get(),
            self.espacio_disco.get(),
            self.duracion_bateria.get(),
            self.costo.get()
        )
        self.laptop.append(nueva_laptop)
        messagebox.showinfo("Éxito", "Laptop agregada exitosamente")
        print(self.laptop[0])
        self.mostrar_laptops.insert(tk.END,f"{nueva_laptop}\n")
        self.cargar_imagenes()
        pass

root = tk.Tk()
app = app(root)
root.mainloop()