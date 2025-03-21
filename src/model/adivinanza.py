class Adivinanza:
    """
        Representa una palabra a adivinar en el juego del ahorcado.

        Attributes:
            __letras (list[str]): Lista de caracteres que conforman la palabra a adivinar.
            __posiciones (list[bool]): Lista de booleanos que indican si cada letra ha sido adivinada.
    """

    def __init__(self, palabra: str):
        """
        Inicializa una instancia de Adivinanza.

        Args:
            palabra (str): La palabra a adivinar.
        """
        self.__letras: list[str] = list(palabra)
        self.__posiciones: list[bool] = [False] * len(self.__letras)

    def adivinar(self, letra: str) -> list[int]:
        """
        Marca las posiciones donde la letra aparece en la palabra y actualiza el estado.

        Args:
            letra (str): La letra a adivinar.

        Returns:
            list[int]: Lista de índices donde la letra fue encontrada; lista vacía si no está.
        """
        if letra not in self.__letras:
            return []
        posiciones_donde_esta_la_letra = []
        for i in range(len(self.__letras)):
            if self.__letras[i] == letra:
                posiciones_donde_esta_la_letra.append(i)
                self.__posiciones[i] = True
        return posiciones_donde_esta_la_letra

    def obtener_letras(self) -> list[str]:
        """
        Retorna la lista de letras que conforman la palabra.

        Returns:
            list[str]: Lista de caracteres de la palabra.
        """
        return self.__letras

    def obtener_posiciones(self) -> list[bool]:
        """
        Devuelve el estado actual de adivinación para cada letra.

        Returns:
            list[bool]: Lista de booleanos que indica si cada letra ha sido adivinada.
        """
        return self.__posiciones

    def obtener_cantidad_posiciones(self) -> int:
        """
        Retorna la cantidad total de letras de la palabra.

        Returns:
            int: Número de letras.
        """
        return len(self.__letras)

    def verificar_si_hay_triunfo(self) -> bool:
        """
        Verifica si todas las letras han sido adivinadas.

        Returns:
            bool: True si se ha adivinado la palabra completa, de lo contrario False.
        """
        return all(self.__posiciones)