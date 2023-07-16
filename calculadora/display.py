from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt
from variaveis import BIG_FONT, MARGEM, LARGURA_MINIMA


# função para criar o dislay do histórico da calculadora
def cria_infor_display():
    # criando widget
    infor_display = Display()
    # setando estilos do display
    infor_display.setStyleSheet("font-size: 15px;")
    infor_display.setMinimumHeight(5)
    infor_display.setTextMargins(7, 2, 7, 2)
    infor_display.setPlaceholderText("Histórico")
    return infor_display


class Display(QLineEdit):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.setStyleSheet(f"font-size: {BIG_FONT}px;")
        self.setMinimumHeight(BIG_FONT*2)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*[MARGEM for _ in range(4)])
        self.setMinimumWidth(LARGURA_MINIMA)
