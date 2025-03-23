def mostrar_unidades(sistema, conversiones):
    print(f"Seleccione la unidad de {sistema}")
    unidades = conversiones[sistema]
    
    i = 0
    
    for i, unidade in enumerate(unidades.keys(), 1):
        print(f"{i}) {unidade}")
    
    while True:
        try:
            opcion = int(input("Selecciona la unidad: "))
            if 1 <= opcion <= i:
                break
            else:
                print(f"Error: La opción debe estar entre 1 y {i}.")
        except ValueError:
            print("Error: Debes ingresar un número entero válido.")
            
    
    return list(unidades.keys())[opcion-1]