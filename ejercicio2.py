# Ejercicio 2: Modelar una computadora
# 
# En este archivo debés crear la clase Computadora siguiendo las consignas del README.
# Recordá:
# - Definir atributos relevantes en el constructor (__init__), con valores por defecto.
# - Implementar el método __str__ para mostrar la información esencial.
# - Instanciar al menos 3 computadoras con distintos valores.
# - Llevar la cuenta de computadoras creadas (usar variable de clase).
# - Implementar al menos 2 métodos de los sugeridos (updateOS, PM, addRAM, getCapacity).
# - Crear otra clase para un componente (ej: Disco, RAM, etc.) con su propio __init__, __str__ y al menos un método.
# 
# ¡No olvides probar todos los métodos y comentar tu criterio para los valores

class Computadora:
    contador=0
    lista_computadoras=[]
    def __init__(self, nro_serie, marca="Genérica", procesador="Intel i3", ram=8, almacenamiento=256, gpu="Integrada", sistema_operativo="Linux"):
        if not isinstance(nro_serie, str) or nro_serie.strip() == "":
            raise ValueError("La patente debe ser un string no vacio.")
        if not isinstance(marca, str) or marca.strip() == "":
            raise ValueError("La marca debe ser un string no vacio.")
        if not isinstance(procesador, str) or procesador.strip() == "":
            raise ValueError("El procesador debe ser un string no vacio.")
        if not isinstance(ram, int):
            raise ValueError("la ram debe ser un número entero.")
        if not isinstance(almacenamiento, int):
            raise ValueError("El almacenamiento debe ser un número entero.")
        if not isinstance(gpu, str) or gpu.strip() == "":
            raise ValueError("El gpu debe ser un string no vacio.")
        if not isinstance(sistema_operativo, str) or sistema_operativo.strip() == "":
            raise ValueError("El sistema operativo debe ser un string no vacio.")
        
        self.nro_serie = nro_serie
        self.marca = marca
        self.procesador = procesador
        self.ram = ram  # en GB
        self.almacenamiento = almacenamiento  # en GB
        self.gpu = gpu
        self.sistema_operativo = sistema_operativo
        Computadora.lista_computadoras.append(self)
        Computadora.contador+=1
    def __str__(self):
        return (f"Computadora #{self.nro_serie} ({self.marca}) \n"
                f"Procesador: {self.procesador} \n"
                f"RAM: {self.ram} GB \n"
                f"Almacenamiento: {self.almacenamiento} GB \n"
                f"GPU: {self.gpu} \n"
                f"Sistema operativo: {self.sistema_operativo}")
    def mostrar(self):
        return (f"Computadora #{self.nro_serie} ({self.marca}) \n"
                f"Procesador: {self.procesador} \n"
                f"RAM: {self.ram} GB \n"
                f"Almacenamiento: {self.almacenamiento} GB \n"
                f"GPU: {self.gpu} \n"
                f"Sistema operativo: {self.sistema_operativo}")
    @classmethod
    def addRAM(cls):
        numero_serie = input("Ingrese nro de serie: ")
        for c in cls.lista_computadoras:   
            if numero_serie == c.nro_serie:
                try:
                    ram_agregada = int(input("Ingrese nueva RAM a agregar: "))
                except ValueError:
                    print("Error: Debes ingresar un número entero.")
                    return
                c.ram += ram_agregada
                print(c.mostrar())
                return
        print("No se encontró una computadora con ese número de serie.")
    @classmethod
    def getCapacity(cls):
        numero_serie = input("Ingrese nro de serie: ")
        for c in cls.lista_computadoras:   
            if numero_serie == c.nro_serie: 
                componente = str(input("Ingrese componente (ram o almacenamiento): ").strip().lower())
                if componente == "ram":
                    print(f"RAM actual: {c.ram} GB")
                    return c.ram
                elif componente == "almacenamiento":
                    print(f"Almacenamiento actual: {c.almacenamiento} GB")
                    return c.almacenamiento
                else:
                    print("Componente inválido, intente de nuevo.")                                          
        print("No se encontró una computadora con ese número de serie.")
        return
class Monitor:
    def __init__(self,pantalla:str,pulgadas:int,marca:str):
        if not isinstance(pantalla, str) or pantalla.strip() == "":
            raise ValueError("La patente debe ser un string no vacio.")
        if not isinstance(marca, str) or marca.strip() == "":
            raise ValueError("La marca debe ser un string no vacio.")
        if not isinstance(pulgadas, int):
            raise ValueError("la ram debe ser un número entero.")
        self.pantalla=pantalla
        self.pulgadas=pulgadas
        self.marca=marca
    def __str__(self):
        return (f"Pantalla #{self.pantalla} \n"
                f"Tiene: {self.pulgadas} pulgadas \n"
                f"y es marca: {self.marca}  \n")
    def mostrar(self):
        return (f"Este monitor tiene pantalla {self.pantalla}, "
                f"{self.pulgadas}\" y es marca {self.marca}.")
        
    
# computadora1=Computadora("AAA111","APPLE","M1",16,1000,"Integrada","MacOs")
# computadora2=Computadora("AAA112","SAMSUNG","Intel i7",16,1000,"Integrada","Windows")
# computadora3=Computadora("AAA113","TOSHIBA","Intel i5",16,500,"Integrada","Linux")
# Computadora.addRAM()
# Computadora.getCapacity()
monitor1=Monitor("OLED",24,"SAMSUNG")
print(monitor1.mostrar())