import os


class Plantel:

    ruta_archivo = 'Jugadores1ra.txt'

    @classmethod
    def agregarJugador(cls,jugador):
        with open(cls.ruta_archivo,'a',encoding= 'utf8') as archivo:
            archivo.write(f'{jugador.nombre}\n')
            archivo.write(f'{jugador.edad}\n')
            archivo.write(f'{jugador.nacionalidad}\n')
            archivo.write(f'{jugador.posicion}\n')
            archivo.write(f'{jugador.altura}\n')
            archivo.write(f'{jugador.peso}\n')


    @classmethod
    def ListarJugadores(cls):
        with open(cls.ruta_archivo, 'r', encoding='utf8') as archivo:
            print(f'Jugadores Primera Division'.center(50,'-'))
            print(archivo.read())

    @classmethod
    def eliminar_jugador(cls):
        os.remove(cls.ruta_archivo)
        print(f'Archivo Eliminado: {cls.ruta_archivo}')