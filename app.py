from src.model.juego import Juego

from src.view.menu import Menu

def main():
    """
    Función principal que inicializa el juego del Ahorcado.
    """
    juego = Juego()
    menu = Menu(juego)
    menu.iniciar()

if __name__ == "__main__":
    main()
