#Siendo X e Y las dimensiones del techo y A y B las dimensiones de los paneles solares
def max_solar_panels(x, y, a, b):
    if x < a or y < b:
        return "Error: Las dimensiones del techo son menores que las dimensiones de los paneles solares"
    # Calculamos paneles en orientación original (a,b)
    horizontal_panels = x // a
    vertical_panels = y // b
    total_panels = horizontal_panels * vertical_panels
    
    # Calculamos el espacio restante usando el módulo (%)
    remaining_y = y % b
    remaining_x = x % a
    
    # Si hay espacio suficiente en la parte restante eje y, intentamos colocar paneles rotados
    if remaining_y >= a:
        # En el espacio restante, los paneles estarán rotados (b,a)
        rotated_horizontal_panels = x // b
        rotated_vertical_panels = remaining_y // a
        additional_panels = rotated_horizontal_panels * rotated_vertical_panels
        total_panels += additional_panels


    # Si hay espacio suficiente en la parte restante eje x, intentamos colocar paneles rotados
    if remaining_x >= b:
        # En el espacio restante, los paneles estarán rotados (b,a)
        rotated_horizontal_panels = y // b
        rotated_vertical_panels = remaining_x // a
        additional_panels = rotated_horizontal_panels * rotated_vertical_panels
        total_panels += additional_panels
    
    return total_panels

# Caso 1: Paneles 1x2 y techo 2x4
print("Caso 1: Paneles 1x2 y techo 2x4")
print("Resultado:", max_solar_panels(2, 4, 1, 2), "paneles")
print()

# Caso 2: Paneles 1x2 y techo 3x5
print("Caso 2: Paneles 1x2 y techo 3x5")
print("Resultado:", max_solar_panels(3, 5, 1, 2), "paneles")
print()

# Caso 3: Paneles 2x2 y techo 1x10
print("Caso 3: Paneles 2x2 y techo 1x10")
print("Resultado:", max_solar_panels(1, 10, 2, 2), "paneles")
print()


