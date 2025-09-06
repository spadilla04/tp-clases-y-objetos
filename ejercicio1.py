# Este archivo corresponde al Ejercicio 1 de la guía práctica sobre Clases.
# Aquí deberás implementar la clase Camion y resolver los puntos a, b, c, d y f según las consignas

#A) Me diria que le estoy dando 5 argumentos pero solo recibe 3

#B)
# def __eq__(self, other):
#         try:
#             return (self.patente == other.patente and
#                     self.marca == other.marca and
#                     self.carga == other.carga and
#                     self.anio == other.anio)
#         except Exception:
#             return False


#C) El atributo que hace unico a un camion , es su patente.Codigo modificado:

# class Camion:
#     def __init__(self, patente:str, marca:str,carga,anio):
#         self.patente = patente
#         self.marca = marca
#         self.carga = carga
#         self.anio = anio

#     def __str__(self):
#         return f"Camión: #{self.patente} \nCarga: {self.carga} \nMarca: {self.marca} \nAño: {self.anio}"
#     def __eq__(self, otro):
#         if not isinstance(otro,Camion):
#             raise TypeError("tiene que ser un objeto clase camion")
#         elif self.patente == otro.patente:    
#             return True
#         else:
#             return False
    

                    
#D)
class Camion:
    patentes_registradas = []
    
    def __init__(self, patente:str, marca:str,carga,anio):
        if not isinstance(patente, str) or marca.strip() == "":
            raise ValueError("La patente debe ser un string no vacio.")
        if not isinstance(marca, str) or marca.strip() == "":
            raise ValueError("La marca debe ser un string no vacio.")
        if not isinstance(carga, int):
            raise ValueError("La carga debe ser un número entero.")
        if not isinstance(anio, int):
            raise ValueError("El año debe ser un número entero.")
        if patente in Camion.patentes_registradas:
            raise ValueError(f"La patente {patente} ya está registrada.")
        
        self.patente = patente
        self.marca = marca
        self.carga = carga
        self.anio = anio
        Camion.patentes_registradas.append(patente)

    def __str__(self):
        return f"Camión: #{self.patente} \nCarga: {self.carga} \nMarca: {self.marca} \nAño: {self.anio}"
    def mostrar(self):
        return  f"Camión: #{self.patente} \nCarga: {self.carga} \nMarca: {self.marca} \nAño: {self.anio}"

    def __eq__(self, otro):
        if not isinstance(otro,Camion):
            raise TypeError("tiene que ser un objeto clase camion")
        elif self.patente == otro.patente:    
            return True
        else:
            return False
class SistemaCamiones:
    def __init__(self):
        self.flota = []  # lista de camiones registrados

    def menu(self):
        continuar = True
        while continuar:
            print("\n--- MENÚ ---")
            print("1. Registrar camión")
            print("2. Modificar carga")
            print("3. Mostrar todos")
            print("4. Marca más registrada")
            print("0. Salir")

            opcion = self.pedir_entero("Elige una opción: ")

            if opcion == 1:
                print("Elegiste la opción 1")
                self.registrar_camion()
            elif opcion == 2:
                print("Elegiste la opción 2")
                self.cambio_carga()
            elif opcion == 3:
                print("Elegiste la opción 3")
                self.mostrar_todos()
            elif opcion == 4:
                print("Elegiste la opción 4")
                self.marca_mas_registrada()
            elif opcion == 0:
                print("Saliendo...")
                continuar = False
            else:
                print("Opción inválida")

    def registrar_camion(self):
        patente = input("Ingrese patente: ")
        marca = input("Ingrese marca: ")
        carga = self.pedir_entero("Ingrese carga máxima (número entero): ")
        anio = self.pedir_entero("Ingrese año (número entero): ")

        try:
            camion = Camion(patente, marca, carga, anio)
            self.flota.append(camion)
            print("Camión registrado con éxito:")
            print(camion.mostrar())
        except ValueError as e:
            print(f"Error: {e}")

    def cambio_carga(self):
        patente = input("Ingrese patente: ")
        for c in self.flota:
            if c.patente == patente:
                nueva_carga = self.pedir_entero("Ingrese nueva carga: ")
                c.carga = nueva_carga
                print("Carga cambiada con éxito")
                print(c.mostrar())
                return
        print("No se encontró la patente")

    def mostrar_todos(self):
        if not self.flota:
            print("No hay camiones registrados")
            return
        for c in sorted(self.flota, key=lambda x: x.anio):
            print(c.mostrar())

    def marca_mas_registrada(self):
        if not self.flota:
            print("No hay camiones registrados")
            return
        marcas = [c.marca for c in self.flota]
        print("Marca más registrada:", max(marcas, key=marcas.count))

    def pedir_entero(self, mensaje):
        """Método auxiliar para pedir enteros y validar entrada."""
        while True:
            try:
                return int(input(mensaje))
            except ValueError:
                print("Error: Debes ingresar un número entero.")


if __name__ == "__main__":
    sistema = SistemaCamiones()
    sistema.menu()        

#///////////////

#     def registrar_camion(cls,lista):
#         patente = input("Ingrese patente: ")
#         marca = input("Ingrese marca: ")
#         carga = input("Ingrese carga máxima: ")
#         anio = input("Ingrese año: ")

#         try:
#             camion = cls(patente, marca, carga, anio)
#             lista.append(camion)
#             print("Camión registrado con éxito:")
#             print(camion.mostrar())
#         except ValueError as e:
#             print(f"Error: {e}")
#     # def modificar_carga(self):

#     #     for camion in flota:
#     #         if self.getter_patente()==
#     #         print(Camion.mostrar(camion))
#     #     return
# def cambio_carga(lista):
#     patente=input("ingrese patente")
#     try:
#         for c in lista:
#             if c.patente==patente:
#                 nueva_carga=input("ingrese que carga quiere")
#                 c.carga=nueva_carga
#                 print(c.mostrar())
#                 return ("carga cambiada")
#     except ValueError:
#         return ("algo fallo")
#     return "no se encontro la patente"
# def mostrar_todos(lista):
#     try:
#         for c in sorted(lista,key=lambda x: x.anio):
#             print(c.mostrar())
#     except ValueError:
#         return ("algo fallo")
# def marca_mas_registrada(lista: list):
#     marcas = []
#     for c in lista:
#         marcas.append(c.marca)
#     print( max(marcas, key=marcas.count))
    


# flota = []

# # furgon1 = Camion("ABC123", "Mercedes", 1000, 2020)
# # furgon2 = furgon1
# # furgon3 = Camion("DEF456", "Volvo", 2000, 2021)
# # furgon4 = Camion("ABC123", "Mercedes", 1000, 2020)

# # print(furgon1 == furgon2)
# # print(furgon1 is furgon2)
# # print(furgon3 == furgon4)
# # print(furgon3 is furgon4)
# # print(furgon1 == furgon4)


# def main():

#     # Implementar lógica de menú

#     print("\n--- MENÚ ---")
#     print("1. registrar camion")
#     print("2. modificar carga")
#     print("3. mostrar todos")
#     print("4. marca mas registrada")
#     print("0. Salir")

#     opcion = int(input("Elige una opción: "))
#     if opcion == 1:
#         print("Elegiste la opción 1")
#         Camion.registrar_camion(flota)
#         main()  # vuelve a mostrar el menú
#     elif opcion == 2:
#         print("Elegiste la opción 2")
#         cambio_carga(flota)
#         main()
#     elif opcion == 3:
#         print("Elegiste la opción 3")
#         mostrar_todos(flota)
#         main()
#     elif opcion == 4:
#         print("Elegiste la opción 4")
#         marca_mas_registrada(flota)
#         main()
#     elif opcion == 0:
#         print("Saliendo...")
#     else:
#         print("Opción inválida")
#         main()
#     return
# main()
