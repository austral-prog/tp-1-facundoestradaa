def price():
    """
    Ejercicio 8 - Cálculo de Precio Final

    Dado un precio base, calcular e imprimir:
    1. El monto del impuesto (21%)
    2. El subtotal (precio base + impuesto)
    3. El monto de la propina (10% del subtotal)
    4. El precio final (subtotal + propina)
    """
    precio_base=input(100)
    impuesto =float((100*21)/100)
    subtotal =float((precio_base + impuesto))
    propina = float((0.1*100))
    final = float((subtotal+propina))

    print(impuesto)
    print(subtotal)
    print(propina)
    print(final)

price()
