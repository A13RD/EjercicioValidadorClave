# TODO: Implementa el código del ejercicio aquí

from abc import abstractmethod, abstractclassmethod
class Validador:
    def __init__(self):
        pass

    def es_valida(self, clave: str) -> bool:
        pass

@abstractclassmethod
class ReglaValidacion:

