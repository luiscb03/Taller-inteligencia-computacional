def tercerPunto():
    sueldoBase = int(input("Ingrese el sueldo base"))
    comision = sueldoBase * 0.15
    total = sueldoBase + comision
    print(f"El vendedor recibira: \nSueldo base -------- {sueldoBase} \nComision ---------- {comision} \nTotal ----------- {total}")


tercerPunto()