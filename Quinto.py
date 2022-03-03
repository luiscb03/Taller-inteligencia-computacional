def quintoPunto():
    nRedes = int(input("Ingrese la cantidad de alumnos de redes"))
    nContabilidad = int(input("Ingrese la cantidad de alumnos de Contabilidad"))
    nDiseño = int(input("Ingrese la cantidad de alumnos de Diseño"))
    totalAlumnos = nRedes + nContabilidad + nDiseño

    porcentajeRedes = round((nRedes * 100)/totalAlumnos)
    porcentajeContabilidad = round((nContabilidad * 100)/totalAlumnos)
    porcentajeDiseño = round((nDiseño * 100)/totalAlumnos)

    print(f"El total de alumnos fue = {totalAlumnos} \nPorcentaje alumnos en Redes = {porcentajeRedes}% \nPorcentaje alumnos en Contabilidad = {porcentajeContabilidad}% \nPorcentaje alumnos en Diseño = {porcentajeDiseño}% \n")


quintoPunto()