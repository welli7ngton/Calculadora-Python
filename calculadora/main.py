from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtGui import QIcon
from main_window import JanelaPrincipal
from variaveis import CAMINHO_ICONE
import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)

    janela = JanelaPrincipal()

    label1 = QLabel("Texto texto texto")

    janela.vLayout.addWidget(label1)

    icone = QIcon(str(CAMINHO_ICONE))

    janela.setWindowIcon(icone)
    janela.setWindowIconText("Calculadora")

    janela.show()
    app.exec()
