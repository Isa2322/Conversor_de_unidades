conversion_a = {
    "Sistema Internacional (SI)": {
        "Kelvin (K)": lambda k: k,  # Kelvin a Kelvin
        "Celsius (°C)": lambda c: c + 273.15
    },
    
    "Sistema Imperial y Estadounidense": {
        "Fahrenheit (°F)": lambda f: (f + 459.67) * 5 / 9,
        "Rankine (°R o °Ra)": lambda r: r * 5 / 9
    },
    
    "Escalas Históricas y Especiales de temperatura": {
        "Réaumur (°Re)": lambda re: (re * 5 / 4) + 273.15,
        "Rømer (°Rø)": lambda ro: ((ro - 7.5) * 40 / 21) + 273.15,
        "Delisle (°De)": lambda de: 373.15 - (de * 2 / 3),
        "Newton (°N)": lambda n: (n * 100 / 33) + 273.15
    }
}

conversion_b = {
    "Sistema Internacional (SI)": {
        "Kelvin (K)": lambda k: k,  # Kelvin a Kelvin
        "Celsius (°C)": lambda k: k - 273.15
    },
    
    "Sistema Imperial y Estadounidense": {
        "Fahrenheit (°F)": lambda k: (k * 9 / 5) - 459.67,
        "Rankine (°R o °Ra)": lambda k: k * 9 / 5
    },
    
    "Escalas Históricas y Especiales": {
        "Réaumur (°Re)": lambda k: (k - 273.15) * 4 / 5,
        "Rømer (°Rø)": lambda k: ((k - 273.15) * 21 / 40) + 7.5,
        "Delisle (°De)": lambda k: (373.15 - k) * 3 / 2,
        "Newton (°N)": lambda k: (k - 273.15) * 33 / 100
    }
}
