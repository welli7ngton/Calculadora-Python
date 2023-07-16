from PySide6.QtWidgets import QPushButton, QGridLayout
from variaveis import MEDIUM_FONT
from utils import isEmpty, isNumOrDot, isValidNumber
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from display import Display


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
    def __init__(self,
                 dp: 'Display',
                 info: 'Display',
                 *args,
                 **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._grid_mask = [
            ["C", "DEL", "^", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["", "0", ".", "="]
        ]
        self.display = dp
        self.info = info
        self._equacao = ""

        self.make_grid()

    @property
    def equacao(self):
        return self._equacao

    @equacao.setter
    def equacao(self, valor: str):
        self._equacao = valor
        self.info.setText(valor)

    def make_grid(self):
        for i, linha in enumerate(self._grid_mask):
            for j, texto_botao in enumerate(linha):
                b = Botao(texto_botao)

                if not isNumOrDot(texto_botao) and not isEmpty(texto_botao):
                    b.setProperty("cssClass", "specialButton")
                    self._configBotaoEspecial(b)
                self.addWidget(b, i, j)
                slot = self.fazSlotBotao(self._addTextoDisplay, b)
                self._connectButtonClicked(b, slot)

    def _connectButtonClicked(self, botao, slot):
        botao.clicked.connect(slot)

    def _configBotaoEspecial(self, botao):
        texto = botao.text()

        if texto == "C":
            slot = self.fazSlotBotao(self.display.clear)
            self._connectButtonClicked(botao, slot)

    def fazSlotBotao(self, func, *args, **kwargs):
        def _slot():
            func(*args, **kwargs)
        return _slot

    def _addTextoDisplay(self, b):
        texto_botao = b.text()
        novoValorDisplay = self.display.text() + texto_botao

        if not isValidNumber(novoValorDisplay):
            return

        self.display.insert(texto_botao)
