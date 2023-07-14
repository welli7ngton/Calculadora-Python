import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from main_window import JanelaPrincipal
from display import Display, cria_infor_display
from variaveis import CAMINHO_ICONE
from styles import addTema

if __name__ == "__main__":
    app = QApplication(sys.argv)
    addTema()
    janela = JanelaPrincipal()

    info = cria_infor_display()
    janela.addToVLayout(info)
    display = Display()
    # display.setPlaceholderText("0")
    janela.addToVLayout(display)

    icone = QIcon(str(CAMINHO_ICONE))
    janela.setWindowIcon(icone)
    janela.setWindowIconText("Calculadora")

    janela.adjustFixedSize()
    janela.show()
    app.exec()
