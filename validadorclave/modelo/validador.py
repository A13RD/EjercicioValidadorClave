# TODO: Implementa el código del ejercicio aquí

from abc import abstractmethod, ABC
from validadorclave.modelo.errores import *


class ReglaValidacion(ABC):

    def __init__(self, longitud_esperada: int):
        self._longitud_esperada: int = longitud_esperada

    def _validar_longitud(self, clave: str) -> bool:
        if len(clave) > self._longitud_esperada:
            return True
        else:
            return False

    @staticmethod
    def _contiene_mayuscula(self, clave: str) -> bool:
        for caracter in clave:
            if caracter.isupper():
                return True
        return False

    @staticmethod
    def _contiene_minuscula(self, clave: str) -> bool:
        for caracter in clave:
            if caracter.islower():
                return True
        return False

    @staticmethod
    def _contiene_numero(self, clave: str) -> bool:
        for caracter in clave:
            if caracter.isdigit():
                return True
        return False

    @abstractmethod
    def es_valida(self, clave: str) -> bool:
        pass


class ReglaValidacionCalisto(ReglaValidacion):

    def __init__(self):
        super().__init__(6)

    @staticmethod
    def contiene_calisto(clave: str) -> bool:
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

    def __init__(self):
        super().__init__(8)

    @staticmethod
    def contiene_caracter_especial(self, clave: str) -> bool:
        for caracter in clave:
            if caracter in ["@", "_", "#", "$", "%"]:
                return True
            else:
                pass
        return False

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

    def __init__(self, regla: ReglaValidacion):
        self.regla = regla

    def es_valida(self, clave: str) -> bool:
        if self.regla.es_valida(clave):
            return True
        else:
            return False
