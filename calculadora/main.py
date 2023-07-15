import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from main_window import JanelaPrincipal
from display import Display, cria_infor_display
from variaveis import CAMINHO_ICONE
from styles import addTema
from buttons import GridBotoes


if __name__ == "__main__":
    app = QApplication(sys.argv)
    addTema()
    janela = JanelaPrincipal()

    info = cria_infor_display()
    janela.addToWidgetVLayout(info)
    display = Display()
    # display.setPlaceholderText("0")
    janela.addToWidgetVLayout(display)

    grid_botoes = GridBotoes()
    janela.vLayout.addLayout(grid_botoes)

    icone = QIcon(str(CAMINHO_ICONE))
    janela.setWindowIcon(icone)
    janela.setWindowIconText("Calculadora")

    janela.adjustFixedSize()
    janela.show()
    app.exec()
