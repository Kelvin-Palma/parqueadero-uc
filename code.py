cupos = 30
contador = 0
recaudo = 0
horas_totales = 0
estudiantes = 0
docentes = 0
visitantes = 0

while contador < cupos:
    print("\nVehículo", contador + 1)
    print("Ingrese los datos del vehículo:")
    print("Si no hay más vehículos, ingrese la palabra 'Salir'.")

    placa = input("Placa: ").strip().upper()
    if placa == "SALIR":
        break

    tipo = input("Tipo de usuario (E=Estudiante, D=Docente, V=Visitante): ").strip().upper()

    entrada_hora = input("Hora de entrada (0 a 23): ")

    if not entrada_hora.isdigit():
        print("Dato inválido. Se rechaza el registro.")
        continue

    hora = int(entrada_hora)

    entrada_permanencia = input("Horas de permanencia: ")

    if not entrada_permanencia.replace(".", "", 1).isdigit():
        print("Dato inválido. Se rechaza el registro.")
        continue

    permanencia = float(entrada_permanencia)

    if hora < 0 or hora > 23:
        print("Hora fuera de los límites. Vehículo no contado.")
        continue

    if permanencia < 0:
        print("Las horas de permanencia no pueden ser negativas.")
        continue

    if tipo == "V":
        dia = input("Día de la semana: ").strip().upper()
    else:
        dia = ""

    if tipo == "E":
        estudiantes += 1
        tarifa = 0 if permanencia <= 2 else (permanencia - 2) * 800

    elif tipo == "D":
        docentes += 1
        tarifa = permanencia * 500

    else:
        if tipo != "V":
            print("Tipo inválido. Se toma como visitante.")

        tipo = "V"
        visitantes += 1

        tarifa = 1500 if permanencia <= 1 else 1500 + (permanencia - 1) * 1200

        if dia == "SABADO":
            tarifa *= 0.80
            print("Se aplicó el descuento especial del sábado: 20%.")

    # No se aplica descuento si es sábado
    if hora > 19 or hora < 6:
        if not (tipo == "V" and dia == "SABADO"):
            tarifa *= 0.90
            print("Se aplicó el descuento nocturno del 10%.")

    recaudo += tarifa
    horas_totales += permanencia
    contador += 1

    print("Vehículo registrado correctamente.")
    print("\nTarifa:", round(tarifa, 2), "COP")

    if contador == cupos:
        print("\nPARQUEADERO LLENO")

print("\n== RESUMEN DEL DIA ==")

print("Vehículos registrados:", contador)
print("Ocupación:", round((contador / 30) * 100, 2), "%")
print("Recaudo total:", round(recaudo, 2), "COP")

print("Estudiantes:", estudiantes)
print("Docentes:", docentes)
print("Visitantes:", visitantes)

if contador > 0:
    promedio = horas_totales / contador
else:
    promedio = 0

print("Promedio de permanencia:", round(promedio, 2), "horas")