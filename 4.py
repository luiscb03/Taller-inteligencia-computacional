from tokenize import Double


def cuartoPunto():
    taller1 = int(input("Ingrese la nota del primer taller"))
    taller2 = int(input("Ingrese la nota del segundo taller"))
    taller3 = int(input("Ingrese la nota del tercer taller"))
    Examen = int(input("Ingrese la notal del examen"))
    proyecto = int(input("Ingrese la nota del proyecto"))

    notaTalleres = ((taller1+taller2+taller3)/3) * 0.5
    notaExamen = Examen * 0.3
    notaProyecto = proyecto * 0.2

    notaFinal = notaTalleres + notaExamen + notaProyecto
    print(f"Su nota final es: {notaFinal}")


cuartoPunto()
