import sys

import sintactico as lexsint
import lexico as lexlex


from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from PyQt5.QtWidgets import QErrorMessage
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPlainTextEdit

from PyQt5.QtWidgets import QSizePolicy


#def window():
app = QApplication(sys.argv)
wind = QWidget()
wind.setWindowTitle('Analizador')
wind.setGeometry(350,100,1150,950)


verificar = QPushButton('Verificar')

limpiar = QPushButton('Limpiar')



lblCodigo = QLabel()
lblCodigo.setText("Escriba su código:")

codigo = QPlainTextEdit()
texto = codigo.sizePolicy()
texto.setHorizontalPolicy(QSizePolicy.Expanding)
codigo.setSizePolicy(texto)

lblAnalisis = QLabel()
lblAnalisis.setText("Análisis")
lblAnalisis.setAlignment(Qt.AlignCenter)

lblLex = QLabel()
lblLex.setText("Lexer: ")

lexer = QPlainTextEdit()
lex = lexer.sizePolicy()
lex.setHorizontalPolicy(QSizePolicy.Expanding)
lexer.setSizePolicy(lex)

lblLexErr = QLabel()
lblLexErr.setText("Errores: ")

errorLex = QPlainTextEdit()
errLex = errorLex.sizePolicy()
errLex.setHorizontalPolicy(QSizePolicy.Expanding)
errorLex.setSizePolicy(errLex)


lblSint = QLabel()
lblSint.setText("Sintáctico: ")

sintactico = QPlainTextEdit()
#sintactico = QLineEdit()
sint = sintactico.sizePolicy()
sint.setHorizontalPolicy(QSizePolicy.Expanding)
sintactico.setSizePolicy(sint)

lblSintErr = QLabel()
lblSintErr.setText("Errores: ")

errorSint = QPlainTextEdit()
errSint = errorSint.sizePolicy()
errSint.setHorizontalPolicy(QSizePolicy.Expanding)
errorSint.setSizePolicy(errSint)


def clearAll():
    codigo.clear()
    lexer.clear()
    errorLex.clear()
    sintactico.clear()
    errorSint.clear()

limpiar.clicked.connect(clearAll)


def analisis():
    cdg = codigo.toPlainText()
    val = len(cdg)
    #print(cdg)
    #print(val)
    if(val == 0):
        errorM()

    lexer.clear()
    sintactico.clear()
    errorSint.clear()
    errorLex.clear()

    lexVal = lexlex.lexenizador(cdg)
    #print(lexVal)
    for linea in lexVal:
        if( "Caracter" not in linea ):
            lexer.appendPlainText(linea)
        else:
            errorLex.appendPlainText(linea)


    #var = '"'
    #res = cdg
    #res = var + var + var + res + var + var + var

    #print(res)
    #lexsint.sintactico('''var set = new Set(['a',5]);''')
    #lexsint.sintactico("""var i;""")
    lexSint = lexsint.sintactico(cdg)

    if len(lexSint)==1:
        sintactico.appendPlainText(lexSint[0])
    else:
        sintactico.appendPlainText(lexSint[0])
        errorSint.appendPlainText(lexSint[1])


verificar.clicked.connect(analisis)



def errorM():
    wind.setGeometry(350, 100, 1150, 950)
    buttonReply = QMessageBox.warning(wind,'¡Advertencia!', "No hay texto.", QMessageBox.Ok, QMessageBox.Ok)






layoutGeneral = QVBoxLayout()

layoutCod = QVBoxLayout()
layoutUno = QHBoxLayout()
layoutDos = QHBoxLayout()
layoutTres = QHBoxLayout()

layoutButtons = QVBoxLayout()

layoutButtons.addWidget(verificar)
layoutButtons.addWidget(limpiar)


layoutCod.addWidget(lblCodigo)
layoutCod.addWidget(codigo)

layoutUno.addLayout(layoutButtons)
layoutUno.addLayout(layoutCod)

layoutAnalisis = QVBoxLayout()


layoutLS = QHBoxLayout()
layoutLex = QVBoxLayout()
layoutSint = QVBoxLayout()


layoutLex.addWidget(lblLex)
layoutLex.addWidget(lexer)
layoutLex.addWidget(lblLexErr)
layoutLex.addWidget(errorLex)


layoutSint.addWidget(lblSint)
layoutSint.addWidget(sintactico)
layoutSint.addWidget(lblSintErr)
layoutSint.addWidget(errorSint)


layoutLS.addLayout(layoutLex)
layoutLS.addLayout(layoutSint)


layoutAnalisis.addWidget(lblAnalisis)
layoutAnalisis.addLayout(layoutLS)


layoutGeneral.addLayout(layoutUno)
layoutGeneral.addLayout(layoutAnalisis)

wind.setStyleSheet("""
        QWidget > QPushButton{
            background-color: blue;
            border-style: outset;
            border-width: 2px;
            border-radius: 10px;
            border-color: beige;
            font: bold 14px;
            min-width: 10em;
            padding: 6px;
            color: white;
        }
        
    QWidget > QLabel{
        font-family: Verdana;
        font: 16px;
    }
    
    QWidget > QPlainTextEdit {
        background-color: black;
        font-family: Consolas;
        color: #a6fd42;
        font: 18px;
        padding: 8px;
    }
    
    QWidget {
        background-color: #8ecafe;
    }
        """)

wind.setLayout(layoutGeneral)
wind.show()
sys.exit(app.exec_())