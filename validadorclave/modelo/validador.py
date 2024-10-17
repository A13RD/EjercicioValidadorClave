# TODO: Implementa el código del ejercicio aquí

from abc import abstractmethod, ABC
from validadorclave.modelo.errores import *


class ReglaValidacion(ABC):

    def __init__(self, _longitud_esperada: int):
        self._longitud_esperada = _longitud_esperada

    def _validar_longitud(self, clave: str) -> bool:
        return len(clave) > self._longitud_esperada

    @staticmethod
    def _contiene_mayuscula(self, clave: str) -> bool:
        return any(letra.isupper() for letra in clave)

    @staticmethod
    def _contiene_minuscula(self, clave: str) -> bool:
        return any(letra.islower() for letra in clave)

    @staticmethod
    def _contiene_numero(self, clave: str) -> bool:
        return any(letra.isdigit() for letra in clave)

    @abstractmethod
    def es_valida(self, clave: str) -> bool:
        pass


class ReglaValidacionCalisto(ReglaValidacion):

    def contiene_calisto(self):
        pass

    def es_valida(self, clave: str) -> bool:
        if not self._validar_longitud(clave):
            raise NoCumpleLongitudMinimaError
        if not self._contiene_numero(clave):
            raise NoTieneNumeroError
        if not self.contiene_calisto(clave):
            raise NoTienePalabraSecretaError
        return True


class ReglaValidacionGanimedes(ReglaValidacion):

    def contiene_caracter_especial(self, clave: str) -> bool:
        caracter_especial = "@_#$%"
        return any(letra in caracter_especial for letra in clave)

    def es_valida(self, clave: str) -> bool:
        if not self._validar_longitud(clave):
            raise NoCumpleLongitudMinimaError

        if not self._contiene_mayuscula(clave):
            raise NoTieneLetraMayusculaError

        if not self._contiene_minuscula(clave):
            raise NoTieneLetraMinusculaError

        if not self._contiene_numero(clave):
            raise NoTieneNumeroError

        if not self.contiene_caracter_especial(clave):
            raise NoTieneCaracterEspecialError

        return True


class Validador:

    def es_valida(self, clave: str) -> bool:
        pass