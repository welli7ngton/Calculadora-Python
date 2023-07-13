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


def exemplo_slot():
    print(1234567810)


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

# status bar
status_bar = window.statusBar()
status_bar.showMessage("Barra de status")

window.show()
app.exec()  # O loop da aplicação
