from PySide6.QtWidgets import (QMainWindow, QVBoxLayout, QWidget)


class JanelaPrincipal(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # criando widget central do programa
        self.central_widget = QWidget()

        # creiando o layout do widget central(forma da janela central)
        self.v_layout = QVBoxLayout()

        # setando o layout do widget central(forma da janela central)
        self.central_widget.setLayout(self.v_layout)

        # setando o widget central no topo da hierarquia de widgets
        self.setCentralWidget(self.central_widget)

        self.setWindowTitle("Calculadora")

        # tamanho da janela
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())
