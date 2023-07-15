from PySide6.QtWidgets import QPushButton, QGridLayout
from variaveis import MEDIUM_FONT
from utils import isEmpty, isNumOrDot


class Botao(QPushButton):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.configStyles()

    def configStyles(self):
        fonte = self.font()
        fonte.setPixelSize(MEDIUM_FONT)
        fonte.setBold(True)
        fonte.setItalic(True)
        self.setMinimumSize(75, 75)
        self.setFont(fonte)


class GridBotoes(QGridLayout):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        # matriz para facilitar a adição de botoes por item/linha/coluna
        self._grid_mask = [
            ["C", "DEL", "^", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            [" ", "0", ".", "="]
        ]

        for i, linha in enumerate(self._grid_mask):
            for j, texto_botao in enumerate(linha):
                b = Botao(texto_botao)

                if not isNumOrDot(texto_botao) and not isEmpty(texto_botao):
                    b.setProperty("cssClass", "specialButton")
                self.addWidget(b, i, j)
