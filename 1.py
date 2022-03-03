def primerPunto():
    monto = int(input("Ingrese donacion"))
    telecomunicacione = monto * 0.1
    sistemas = monto * 0.25
    administracion = monto * 0.35
    contabilidad = monto * 0.30
    print(f"La donacion fue de: {monto}  y se repartiran de la siguiente forma: \nTelecomunicaciones = {telecomunicacione} \nSistemas = {sistemas} \nAdministracion = {administracion} \nContabilidad = {contabilidad}")

primerPunto()
