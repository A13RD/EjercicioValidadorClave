from validadorclave.modelo.validador import Validador, ReglaValidacionGanimedes, ReglaValidacionCalisto


def validar_clave(clave: str, reglas: list):
    for regla in reglas:
        validador = Validador(regla)
        try:
            if validador.es_valida(clave):
                print(f"La clave es válida para la validación {regla.__class__.__name__}")
        except Exception as e:
            print(f"Error: {regla.__class__.__name__}: {str(e)}")