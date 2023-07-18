from PySide6.QtWidgets import QPushButton, QGridLayout
from variaveis import MEDIUM_FONT
from utils import isEmpty, isNumOrDot, isValidNumber
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from display import Display
    from main_window import JanelaPrincipal


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
                 window: 'JanelaPrincipal',
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
        self.window = window
        self.display = dp
        self.info = info
        self._equacao = ""
        self.esquerda = None
        self.direita = None
        self.operador = None
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
            # jeito 1
            # slot = self.fazSlotBotao(self.display.clear)
            # self._connectButtonClicked(botao, slot)
            # slot2 = self.fazSlotBotao(self.info.clear)
            # self._connectButtonClicked(botao, slot2)

            # jeito 2
            # botao.clicked.connect(self.display.clear)
            # botao.clicked.connect(self.info.clear)

            # funcao
            self._connectButtonClicked(botao, self.limpaDisplay)

        if texto == "DEL":
            self._connectButtonClicked(botao, self.display.backspace)

        if texto in "+-*/^":
            self._connectButtonClicked(
                botao,
                self.fazSlotBotao(self.operadorClicado, botao)
                )

        if texto == "=":
            self._connectButtonClicked(botao, self.igual)

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

    def operadorClicado(self, botao):
        texto_botao = botao.text()
        texto_display = self.display.text()
        self.display.clear()

        if not isValidNumber(texto_display) and self.esquerda is None:
            self._mostraErro("Você não digitou nada.")
            return

        if self.esquerda is None:
            self.esquerda = float(texto_display)

        self.operador = texto_botao

        self.equacao = f"{self.esquerda} {self.operador} ??"

    def limpaDisplay(self):
        self.equacao = ""
        self.esquerda = None
        self.direita = None
        self.operador = None
        self.display.clear()

    def igual(self):
        texto_display = self.display.text()
        if not isValidNumber(texto_display):
            self._mostraErro("Você não digitou nada.")
            return

        self.direita = float(self.display.text())
        self.equacao = f"{self.esquerda} {self.operador} {self.direita}"

        if "^" in self.equacao:
            self.equacao = self.equacao.replace("^", "**")

        try:
            resultado = eval(self.equacao)
            self.equacao = f"{self.equacao} = {resultado}"
            self.esquerda = resultado
        except SyntaxError:
            self.equacao = ""
            self.display.clear()
            resultado = ""
        except ZeroDivisionError:
            self.equacao = "error"
            self._mostraErro("Erro: Divisão por zero.")
            self.esquerda = None
        except OverflowError:
            self.equacao = "error"
            self._mostraErro("Erro: Número muito grande.")
            self.esquerda = None

        self.display.clear()
        self.direita = None

    def _mostraErro(self, texto):
        msgBox = self.window.fazMsgBox()
        msgBox.setText(texto)
        msgBox.setIcon(msgBox.Icon.Warning)
        msgBox.exec()
