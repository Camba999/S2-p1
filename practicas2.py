for cat in range(3):
    cat = cat + 1
    ventasT = 0
    for prod in range(4):
        prod = prod + 1
        produ = float(input(f"Ingrese el precio del producto {prod} de la categoria {cat}:"))
        ventas = int(input(f"Ingrese la cantidad de ventas del producto {prod} de la categoria {prod}:"))
        total = produ * ventas
        print(f"Las ventas del producto {prod} de la categoria {cat} son en total: {total}")
        ventasT += total
    print(f"Las ventas totales de la categoria {cat} son: {ventasT}")
