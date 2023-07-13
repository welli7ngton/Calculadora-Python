# QMainWindow e centralWidget
# -> QApplication (app)
#   -> QmainWindow (window -> setCentralWidget)
#   -> CentralWidget (central_widget)
#       -> Layout (layout)
#           -> Widget (botao1)
#           -> Widget (botao2)
#           -> Widget (botao3)
#    -> show
# -> exec

import sys
import datetime
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication,
                               QGridLayout,
                               QPushButton,
                               QWidget,
                               QMainWindow)

data_atual = datetime.datetime.now()
app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle(f"{data_atual.day}/{data_atual.month:02d}")
# criação dos botões
botao1 = QPushButton('Texto do botão')
botao1.setStyleSheet('font-size: 80px;')

botao2 = QPushButton('Botão 2')
botao2.setStyleSheet('font-size: 40px;')

botao3 = QPushButton('Botão 3')
botao3.setStyleSheet('font-size: 40px;')


@Slot()
def exemplo_slot():
    print(1234567810)


@Slot()
def outro_slot(checked):
    print("está marcado?", checked)


@Slot()
def terceiro_slot(acao):
    def interna():
        outro_slot(acao.isChecked())
    return interna


# criando widget central
central_widget = QWidget()
window.setCentralWidget(central_widget)
# criando layout
layout = QGridLayout()

# setando layout do widget central(janela central)
central_widget.setLayout(layout)

# adicionando os botões no layout
layout.addWidget(botao1, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 3, 1, 1, 2)

# menu bar
menu = window.menuBar()
primeiro_menu = menu.addMenu("Menu")
primeira_acao = primeiro_menu.addAction("Primeira Ação")
primeira_acao.triggered.connect(exemplo_slot)

segunda_acao = primeiro_menu.addAction("Segunda acao")
segunda_acao.setCheckable(True)
segunda_acao.toggled.connect(outro_slot)
# segunda_acao.hovered.connect(terceiro_slot(segunda_acao))

botao1.clicked.connect(terceiro_slot(segunda_acao))

# status bar
status_bar = window.statusBar()
status_bar.showMessage("Barra de status")

window.show()
app.exec()  # O loop da aplicação
