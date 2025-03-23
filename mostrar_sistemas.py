def mostrar_sistemas(conversiones):
    
    i = 0
    
    for i, sist in enumerate(conversiones.keys(), 1):
        print(f"{i}) {sist}")
        
    print("0) Salir")
    
    while True:
        try:
            opcion = int(input("Selecciona el sistema: "))
            if 0 <= opcion <= i:
                break
            else:
                print(f"Error: La opción debe estar entre 0 y {i}.")
        except ValueError:
            print("Error: Debes ingresar un número entero válido.")
    
    if(opcion == 0):
        return None
            
    return list(conversiones.keys())[opcion-1]