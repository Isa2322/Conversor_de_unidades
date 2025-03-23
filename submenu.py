import os
import mostrar_sistemas
import mostrar_unidades
import convertir_a_estandar
from mostrar_sistemas import mostrar_sistemas
from mostrar_unidades import mostrar_unidades
from convertir_a_estandar import convertir_a_estandar


def submenu(conversiones):
    os.system("cls")

    print("Sistema de origen")
    print("-----------------")

    sistema_origen = mostrar_sistemas(conversiones)

    if sistema_origen == None:
        return

    os.system("cls")

    print("Unidades de origen")
    print("-----------------")

    unidades_origen = mostrar_unidades(sistema_origen, conversiones)

    while True:
            try:
                cantidad_inicial = float(input("Ingresa la cantidad a convertir: "))
                if cantidad_inicial > 0:
                    break
                else:
                    print("Error: La cantidad debe ser mayor que cero.")
            except ValueError:
                print("Error: Debes ingresar un número válido.")

    os.system("cls")

    print("Sistema de destino")
    print("-----------------")

    sistema_destino = mostrar_sistemas(conversiones)
    
    if sistema_destino == None:
        return

    os.system("cls")

    print("Unidades de destino")
    print("-----------------")

    unidades_destino = mostrar_unidades(sistema_destino, conversiones)

    os.system("cls")
    
    
    if "Escalas Históricas y Especiales de temperatura" in conversiones:
        import conversiones.conversion_temperatura as convertir
        cantidad_estandar = convertir.conversion_a[sistema_origen][unidades_origen](cantidad_inicial)
        cantidad_destino = convertir.conversion_b[sistema_destino][unidades_destino](cantidad_estandar)
    else:
        cantidad_estandar = convertir_a_estandar(cantidad_inicial, sistema_origen, unidades_origen, conversiones, True)
        cantidad_destino = convertir_a_estandar(cantidad_estandar, sistema_destino, unidades_destino, conversiones, False)
    

    print(f"{cantidad_inicial} {unidades_origen} ({sistema_origen}) son {cantidad_destino} {unidades_destino} ({sistema_destino})")

    input("\nPresione una tecla para continuar...")