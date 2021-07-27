from Dominio.Jugadores import Jugadores
from Servicio.Plantel import Plantel
opcion = None
while opcion != 4:
    try:
        print('Opciones: ')
        print('1. Agregar Jugador ')
        print('2. Lista de Jugadores')
        print('3. Eliminar Jugador')
        print('4. Salir')
        opcion = int(input('Ingrese una opcion: '))
        if opcion == 1:
            nombre = input('Ingrese el nombre y apellido del jugador: ')
            edad = int(input('Ingrese edad del jugador: '))
            nacionalidad = input('Ingrese nacionalidad del jugador: ')
            posicion = input('Ingrese el puesto del jugador: ')
            altura = float(input('Ingrese la altura del jugador: '))
            peso = int(input('Ingrese el peso del jugador: '))

            newplayer = Jugadores(nombre, edad, nacionalidad, posicion, altura, peso)

            Plantel.agregarJugador(newplayer)
        elif opcion == 2:
            Plantel.ListarJugadores()

        elif opcion == 3:
            Plantel.eliminar_jugador()


    except Exception as e:
        print(f'Error: {e}')
        opcion= None
else:
    print('Finalizo el programa')