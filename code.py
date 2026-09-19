vehiculos = []

cupos = 30


for i in range(cupos):
    print("\nVehículo", i + 1)
    print("Ingrese los datos del vehículo:")
    print("Si no hay mas vehiculos ingrese la palabra 'Salir'.")

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

    if tipo != "E" and tipo != "D" and tipo != "V":
        tipo = "V"

    # Guardar el vehículo
    vehiculo = {
        "placa": placa,
        "tipo": tipo,
        "hora": hora,
        "permanencia": permanencia
    }

    vehiculos.append(vehiculo)

    print("Vehículo registrado correctamente.")
