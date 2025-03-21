from src.model.diccionario import Diccionario
from src.model.adivinanza import Adivinanza
from src.model.error_intentos_insuficientes import ErrorIntentosInsuficientes

class Juego:
    """
    Clase que encapsula la lógica principal del juego del Ahorcado.

    Atributos:
        __dificultad (str): Nivel de dificultad del juego. Puede ser "DIFICULTAD_BAJA", "DIFICULTAD_MEDIA" o "DIFICULTAD_ALTA".
        __intentos_realizados (int): Número de intentos restantes para adivinar la palabra.
        __diccionario (Diccionario): Instancia que provee la palabra a adivinar.
        __adivinanza (Adivinanza): Instancia que representa la palabra oculta y su estado.
    """

    DIFICULTAD_BAJA = "DIFICULTAD_BAJA"
    DIFICULTAD_MEDIA = "DIFICULTAD_MEDIA"
    DIFICULTAD_ALTA = "DIFICULTAD_ALTA"

    def __init__(self):
        """
        Inicializa el juego con dificultad baja por defecto y sin una palabra generada.
        """
        self.__dificultad = Juego.DIFICULTAD_BAJA
        self.__intentos_realizados: int = 0
        self.__diccionario = Diccionario()
        self.__adivinanza: Adivinanza = None

    def obtener_intentos_realizados(self) -> int:
        """
        Retorna la cantidad de intentos restantes.

        Returns:
            int: Número de intentos restantes.
        """
        return self.__intentos_realizados

    def obtener_adivinanza(self) -> Adivinanza:
        """
        Retorna la instancia de Adivinanza que contiene la palabra oculta.

        Returns:
            Adivinanza: Instancia que representa la palabra a adivinar.
        """
        return self.__adivinanza

    def __generar_palabra(self) -> str:
        """
        Genera una palabra a adivinar utilizando el diccionario.

        Returns:
            str: La palabra generada.
        """
        return self.__diccionario.obtener_palabra()

    def calcular_intentos_permitidos(self) -> int:
        """
        Calcula el número de intentos permitidos basado en el nivel de dificultad.

        Returns:
            int: Número de intentos permitidos.
        """
        if self.__dificultad == self.DIFICULTAD_BAJA:
            return 20
        if self.__dificultad == self.DIFICULTAD_MEDIA:
            return 10
        if self.__dificultad == self.DIFICULTAD_ALTA:
            return 5

        return 0

    def modificar_dificultad(self, dificultad: str) -> None:
        """
        Modifica el nivel de dificultad del juego.

        Args:
            dificultad (str): Nuevo nivel de dificultad, debe ser una de las constantes definidas.
        """
        self.__dificultad = dificultad

    def iniciar_partida(self) -> int:
        """
        Inicia una nueva partida generando una palabra oculta y configurando el número de intentos permitidos.

        Returns:
            int: La cantidad de posiciones (letras) de la palabra oculta.
        """
        palabra = self.__generar_palabra()
        self.__adivinanza = Adivinanza(palabra)
        self.__intentos_realizados = self.calcular_intentos_permitidos()
        return self.__adivinanza.obtener_cantidad_posiciones()

    def adivinar(self, letra: str) -> list[int]:
        """
        Intenta adivinar una letra de la palabra.

        Args:
            letra (str): Letra que el jugador quiere adivinar.

        Returns:
            list[int]: Lista con las posiciones donde aparece la letra en la palabra. Vacía si la letra no está.

        Raises:
            ErrorIntentosInsuficientes: Si no quedan intentos disponibles.
        """
        if self.__intentos_realizados < 0:
            raise ErrorIntentosInsuficientes()
        self.__intentos_realizados -= 1
        return self.__adivinanza.adivinar(letra)

    def verificar_si_hay_intentos(self) -> bool:
        """
        Verifica si aún quedan intentos disponibles.

        Returns:
            bool: True si hay intentos disponibles, False de lo contrario.
        """
        return self.__intentos_realizados >= 0

    def verificar_triunfo(self) -> bool:
        """
        Verifica si el jugador ha adivinado la palabra oculta.

        Returns:
            bool: True si se ha adivinado la palabra, False de lo contrario.
        """
        return self.__adivinanza.verificar_si_hay_triunfo()
