import random

class Diccionario:
    """
    Maneja la carga y selección de palabras para el juego del ahorcado.

    Atributos:
        palabras (list[str]): Lista de palabras cargadas desde un archivo.
    """

    def __init__(self):
        """
        Inicializa la instancia de Diccionario y carga las palabras desde el archivo.
        """
        self.palabras: list[str] = self.__cargar_palabras()

    def __cargar_palabras(self) -> list[str]:
        """
        Carga las palabras desde el archivo 'assets/palabras.txt'.

        Returns:
            list[str]: Lista de palabras.
        """
        palabras = []
        with open("assets/palabras.txt", "r", encoding="utf8") as archivo:
            for line in archivo:
                palabras.append(line.strip())
        return palabras

    def obtener_palabra(self) -> str:
        """
        Selecciona y retorna una palabra aleatoria de la lista.

        Returns:
            str: Una palabra seleccionada al azar.
        """
        indice_aleatorio = random.randint(0, len(self.palabras) - 1)
        return self.palabras[indice_aleatorio]
