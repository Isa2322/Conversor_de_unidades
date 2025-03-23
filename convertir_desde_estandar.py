def convertir_desde_estandar(cantidad, sistema, unidad, conversiones):
    factor = conversiones[sistema][unidad]
    return cantidad / factor