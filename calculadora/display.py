from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent
from variaveis import BIG_FONT, MARGEM, LARGURA_MINIMA
from utils import isEmpty, isNumOrDot


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
    igual = Signal()
    backspc = Signal()
    esc_p = Signal()
    numeros = Signal(str)
    operadores = Signal(str)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.setStyleSheet(f"font-size: {BIG_FONT}px;")
        self.setMinimumHeight(BIG_FONT*2)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*[MARGEM for _ in range(4)])
        self.setMinimumWidth(LARGURA_MINIMA)

    def keyPressEvent(self, evento: QKeyEvent) -> None:
        tecla = evento.key()
        nome_tecla = evento.text().strip()

        if tecla in [Qt.Key.Key_Enter, Qt.Key.Key_Return, Qt.Key.Key_Equal]:
            self.igual.emit()
            return evento.ignore()

        if tecla in [Qt.Key.Key_Backspace, Qt.Key.Key_Delete, Qt.Key.Key_D]:
            self.backspc.emit()
            return evento.ignore()

        if tecla in [Qt.Key.Key_Escape, Qt.Key.Key_C]:
            self.esc_p.emit()
            return evento.ignore()
        if tecla in [
            Qt.Key.Key_Equal, Qt.Key.Key_Minus, Qt.Key.Key_P, Qt.Key.Key_Plus,
            Qt.Key.Key_Slash, Qt.Key.Key_multiply, Qt.Key.Key_Asterisk,
        ]:
            if nome_tecla.lower() == "p":
                nome_tecla = "^"
            self.operadores.emit(nome_tecla)
            return evento.ignore()

        if isEmpty(nome_tecla):
            return evento.ignore()

        if isNumOrDot(nome_tecla):
            self.numeros.emit(nome_tecla)
            return evento.ignore()
