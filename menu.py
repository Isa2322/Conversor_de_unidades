import os
import conversiones
from conversiones import conversion_temperatura, conversiones_longitud, conversiones_masa, conversiones_velocidad, conversiones_volumen
import submenu
from submenu import submenu

opcion = 1

while opcion != 0:
    
    os.system("cls")
    
    print("Seleccione que desea convertir:")
    print("1) Longitud")
    print("2) Masa")
    print("3) Volumen")
    print("4) Velocidad")
    print("5) Temperatura")
    print("0) Salir")

    while True:
        try:
            opcion = int(input("Seleccione que desea convertir: "))
            if 0 <= opcion <= 5:
                break
            else:
                print(f"Error: La opción debe estar entre 0 y 5.")
        except ValueError:
            print("Error: Debes ingresar un número entero válido.")
    
    sist = {}
    
    match opcion:
        case 1:
            sist = conversiones_longitud.conversiones
        case 2: 
            sist = conversiones_masa.conversiones
        case 3:
            sist = conversiones_volumen.conversiones
        case 4:
            sist = conversiones_velocidad.conversiones
        case 5:
            sist = conversion_temperatura.conversion_a
    
    if opcion != 0:  
        submenu(sist)
