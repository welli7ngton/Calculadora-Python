from PySide6.QtWidgets import QApplication, QLabel
import sys
from main_window import JanelaPrincipal

if __name__ == "__main__":
    app = QApplication(sys.argv)

    janela = JanelaPrincipal()

    label1 = QLabel("Texto texto texto")

    janela.v_layout.addWidget(label1)

    janela.show()

    app.exec()
