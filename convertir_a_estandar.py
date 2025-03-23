def convertir_a_estandar(cantidad, sistema, unidad, conversiones ,sentido):
    factor = conversiones[sistema][unidad]
    if sentido:
        return cantidad * factor
    else:
        return cantidad / factor