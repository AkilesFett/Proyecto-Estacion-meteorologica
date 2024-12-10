import math

def calcular_altura(presion_hpa, temperatura_c, p0=1013.25):
    """Calcula la altura en metros basada en la presión y la temperatura."""
    R = 8.31432  # Constante de gases
    M = 0.0289644  # Masa molar promedio del aire
    g = 9.80665  # Gravedad (m/s²)
    T = temperatura_c + 273.15  # Convertimos a Kelvin
    altura = (R * T) / (M * g) * math.log(p0 / presion_hpa)
    return altura

def calcular_probabilidad_lluvia(humedad, presion, temperatura, presion_base=775):
    """
    Calcula una probabilidad básica de lluvia usando humedad, presión y temperatura.
    Args:
        humedad (float): Humedad relativa en %.
        presion (float): Presión atmosférica en hPa.
        temperatura (float): Temperatura en grados Celsius.
        presion_base (float): Presión atmosférica típica en hPa de la región.
    Returns:
        float: Probabilidad estimada de lluvia en %.
    """
    # Base por humedad
    prob_lluvia = max(0, min(100, (humedad - 50) * 1.5 - temperatura * 0.5))
    
    # Ajuste dinámico por presión baja
    if presion < presion_base:
        prob_lluvia += (presion_base - presion) / 10  # Ajuste proporcional
    
    # Limitar entre 0% y 100%
    return min(100, prob_lluvia)

