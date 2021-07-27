class Jugadores:

    def __init__(self,nombre,edad,nacionalidad,posicion,altura,peso):
        self._nombre = nombre
        self._edad = edad
        self._nacionalidad = nacionalidad
        self._posicion = posicion
        self._altura = altura
        self._peso = peso

    def __str__(self):
        return f'Nombre y apellido: {self._nombre}' \
               f'Edad: {self._edad}' \
               f'Nacionalidad: {self._nacionalidad}' \
               f'Puesto: {self._posicion}' \
               f'Altura: {self._altura}' \
               f'Peso: {self._peso}'

    @property
    def nombre(self):
        return self._nombre

    @property
    def edad(self):
        return self._edad

    @property
    def nacionalidad(self):
        return self._nacionalidad

    @property
    def posicion(self):
        return self._posicion

    @property
    def altura(self):
        return self._altura

    @property
    def peso(self):
        return self._peso

    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    @nacionalidad.setter
    def nacionalidad(self,nacionalidad):
        self._nacionalidad = nacionalidad

    @posicion.setter
    def posicion(self, posicion):
        self._posicion= posicion

    @altura.setter
    def altura(self,altura):
        self._altura = altura

    @peso.setter
    def peso(self,peso):
        self._peso = peso