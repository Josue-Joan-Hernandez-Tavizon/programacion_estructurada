"""lista=[
        ["Ruben", 10.0,8.9,9.2],
        ["Andres", 10.0,10.0,10.0],
        ["Maria", 10.0,10.0,10.0]
      ]"""

def borrarPantalla():
    import os
    os.system("cls")
    
def esperarTecla():
    input("Oprima cualquier tecla para continuar")

def menu_principal():
        print("Sistema de Gestión de Calificaciones " \
        "\n1.- Agregar " \
        "\n2.- Mostrar " \
        "\n3.- Cálcular Promedios " \
        "\n4.- SALIR")
        opcion=input("Elige una opción (1-4): ")
        return opcion
    
def agregar_calificaciones(lista):
    borrarPantalla()
    print("Agregar Calificaciones")
    nombre = input("Nombre del alumno: ").strip().upper()
    calificaciones = []
    for i in range(1,4):
        bandera = True
        while bandera:
            try:
                cal = float(input(f"Calificación {i}: "))
                if cal >= 0 and cal <= 10:
                    calificaciones.append(cal)
                    bandera=False
                else:
                    print("Ingrese un valor comprendido entre 0 y 10")
            except ValueError:
                print("Ingrese un valor numerico")
    lista.append([nombre]+calificaciones)
    print("Accion realizada con exito")

"""def mostrar_calificaciones(lista):
    borrarPantalla()
    print("Mostrar calificaciones")
    if len(lista)>0:
        print(f"{"nombre"}:<15{"Calif 1"}<10{"Calif 2"}<10{"Calif 2"}")
        print("-"+50)
        for fila in lista:
            print(f"{"fila[0]"}:<15{"fila[1]"}<10{"fila[2]"}<10{"fila[3]"}")
        print("-"+50)
    else:
        print("No hay calificaciones registradas")"""
        
def mostrar_calificaciones(lista):
    borrarPantalla()
    print(".::Mostrar Calificaciones::.")
    if len(lista) > 0:
        print(f"{"Nombre":<15} {"Cali.1":<10} {"Cali.2":<10} {"Cali.3":<10}")
        print("=" * 60)
        for fila in lista:
            print(f"{fila[0]:<15} {fila[1]:<10} {fila[2]:<10} {fila[3]:<10}")
        print("=" * 60)
        print(f"Son {len(lista)} alumnos")
    else:
        print("No hay calificaciones en el sistema")
        
def calcular_promedios(lista):
    borrarPantalla()
    print(".::Promedios::.")
    promf=0
    if len(lista) > 0:
        print(f'{'Nombre':<15} {'Promedio':<10}')
        print("=" * 30)
        for fila in lista:
            promedio=(fila[1]+fila[2]+fila[3])/3
            alumnos=len(lista)
            promf+=promedio/alumnos
            print(f"{fila[0]:<15}Su promedio es:",promedio)
        print("=" * 30)
        print(f"Son {len(lista)} alumnos")
        print("El promedio final es",promf)
    else:
        print("No hay calificaciones en el sistema")