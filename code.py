vehiculos = []

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

    try:
        hora = int(input("Hora de entrada (0 a 23): "))
        permanencia = float(input("Horas de permanencia: "))
    except ValueError:
        print("Dato inválido. Se rechaza el registro.")
        continue

    if hora < 0 or hora > 23:
        print("Hora fuera de los límites. Vehículo no contado.")
        continue

    if permanencia < 0:
        print("Las horas de permanencia no pueden ser negativas.")
        continue

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

    if hora > 19 or hora < 6:
        tarifa *= 0.90

    tarifa = round(tarifa, 2)
    vehiculos.append({
        "placa": placa,
        "tipo": tipo,
        "hora": hora,
        "permanencia": permanencia
    })
    recaudo += tarifa
    horas_totales += permanencia
    contador += 1

    print("Vehículo registrado correctamente.")
    print("Tarifa:", tarifa, "COP")

    if contador == cupos:
        print("\nPARQUEADERO LLENO")