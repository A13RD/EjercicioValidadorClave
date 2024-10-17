# TODO: Implementa el código del ejercicio aquí

from abc import abstractmethod, ABC


class Validador:
    def __init__(self):
        pass

    def es_valida(self, clave: str) -> bool:
        pass


class ReglaValidacion(ABC):

    def __init__(self, _longitud_esperada):
        self._longitud_esperada: int = _longitud_esperada

    def _validar_longitud(self, clave: str) -> bool:
        return len(clave) > self._longitud_esperada

    def _contiene_mayuscula(self, clave: str) -> bool:
        return any(caracter.isupper() for caracter in clave)

    def _contiene_minuscula(self, clave: str) -> bool:
        return any(caracter.islower() for caracter in clave)

    def _contiene_numero(self, clave: str) -> bool:
        return any(caracter.isdigit() for caracter in clave)

    @abstractmethod
    def es_valida(self, clave: str) -> bool:
        pass
