def segundoPunto():
    primeraInversiona = int(input("Ingrese monto de la primera persona"))
    segundaInversiona = int(input("Ingrese monto de la segunda persona"))
    terceraInversiona = int(input("Ingrese monto de la tercera persona"))

    total = primeraInversiona+segundaInversiona+terceraInversiona
    primerPorcentaje = round((primeraInversiona * 100)/total)
    segundoPorcentaje = round((segundaInversiona * 100)/total)
    tercerPorcentaje = round((terceraInversiona * 100)/total)

    print(f"El total de inversion fue = {total} \nPrimera persona invirtio = {primerPorcentaje}% \nSegunda persona invirtio = {segundoPorcentaje}% \nTercera persona invirtio = {tercerPorcentaje}% \n")


segundoPunto()