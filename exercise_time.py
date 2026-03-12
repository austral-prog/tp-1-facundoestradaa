def time():
    """
    Ejercicio 4 - Calculadora de Tiempo

    Dado un total de segundos, calcular e imprimir:
    1. Horas completas
    2. Minutos completos restantes
    3. Segundos restantes
    """
    total_segundos = 3665
    horas = total_segundos//3600
    segundos = total_segundos%3600
    minutos = segundos//60
    segundos_finales = segundos%60

    print(horas)
    print(minutos)
    print(segundos_finales)

