# QSS - Estilos do QT for Python
# https://doc.qt.io/qtforpython/tutorials/basictutorial/widgetstyling.html

# Dark Theme
# https://pyqtdarktheme.readthedocs.io/en/latest/how_to_use.html

import qdarktheme
from variaveis import COR_PRIMARIA, COR_SECUNDARIA, COR_TERCIARIA
qss = f"""
    PushButton[cssClass="specialButton"] {{
        color: #fff;
        background: {COR_PRIMARIA};
    }}
    PushButton[cssClass="specialButton"]:hover {{
        color: #fff;
        background: {COR_SECUNDARIA};
    }}
    PushButton[cssClass="specialButton"]:pressed {{
        color: #fff;
        background: {COR_TERCIARIA};
    }}
"""


def addTema():
    qdarktheme.setup_theme(
        theme='dark',
        corner_shape='rounded',
        custom_colors={
            "[dark]": {
                "primary": f"{COR_PRIMARIA}",
            },
            "[light]": {
                "primary": f"{COR_PRIMARIA}",
            },
        },
        additional_qss=qss
    )
