enfermeria=["Rocha", "Batres", "Cupillar"]
goles={}
while True:
    print("---------------------------")
    print("1.- Anotar goles")
    print("2.- Consultar jugador")
    print("3.- Informe del equipo")
    print("4.- Salir")
    print("---------------------------")
    opcion=int(input("Qué opcion desea elegir?(1-4): "))
    if opcion == 1:
        anotarnombre=input("Cuál es el nombre del jugador?: ")
        if anotarnombre in enfermeria:
            print("Ese jugador está lesionado!")
            continue
        while True:
            try:
                anotargoles=int(input("Cuántos goles deseas agregar?: "))
                break;
            except ValueError:
                print("Debes de introducir un número!")
        goles[anotarnombre] = anotargoles
        print("Se ha agregado el jugador y sus goles!")
    if opcion == 2:
        consultarjugador=input("Qué jugador desea consultar?: ")
        if consultarjugador not in goles:
            print("Ese jugador no existe!")
        else:
            jugadorconsultar= goles.get(consultarjugador)
            print(f"Los goles de {consultarjugador} son {jugadorconsultar}")
    if opcion == 3:
        print (goles)
        total = 0
        for consultarjugador in goles:
            total = total + goles[consultarjugador]
            print(f"Los goles totales son {total}")
    if opcion == 4:
        print ("Saliendo del programa")
        break;
