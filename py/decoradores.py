# decoradores.py

import time
import logging

def tiempo_de_ejecucion(func):
    """
    Decorador que registra el tiempo de ejecución de una función.
    """
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        logging.info(f"{func.__name__} tomó {fin - inicio} segundos en ejecutarse.")
        return resultado
    return wrapper
