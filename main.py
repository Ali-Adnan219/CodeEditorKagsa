from random import choices
import sys
from PySide6 import QtWidgets
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile, QIODevice
from PySide6 import QtCore, QtGui, QtWidgets
import subprocess
from pathlib import Path

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)

from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableView,
    QWidget,QPlainTextEdit,QFileDialog)
import datetime
from datetime import datetime
import os

from subprocess import PIPE, run


if __name__ == "__main__":
    app = QApplication(sys.argv)
    pathnow='not find path'

    ui_file_name = "./code editor/des.ui"
    ui_file = QFile(ui_file_name)
    if not ui_file.open(QIODevice.ReadOnly):
        print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
        sys.exit(-1)
    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()
    if not window:
        print(loader.errorString())
        sys.exit(-1)
    window.show()
    #Run code
    window.pushButton.clicked.connect(lambda: savetxt(window.plainTextEdit_2.toPlainText()))
    #other
    window.comboBox.currentIndexChanged.connect(lambda: shwocop())
    def shwocop():
        global pathnow
        choicess=window.comboBox.currentText()
        if choicess=='Open file':
            #print(window.comboBox.currentText())
            path_to_file = QFileDialog.getOpenFileName ()
            #print(path_to_file )
            f = open(path_to_file[0], "r")
            #print(f.read())
            window.plainTextEdit_2.clear()
            window.plainTextEdit_2.appendPlainText(str(f.read()))
            pathnow=path_to_file[0]
        elif choicess=='Save as':
            #print("h")
            path_to_file = QFileDialog.getSaveFileName ()
            #print(path_to_file )
            f = open(path_to_file[0], "w",encoding='utf-8')
            #print(f.read())
            f.write(str(window.plainTextEdit_2.toPlainText()))
            pathnow=path_to_file[0]
        elif choicess=='Save output':
            path_to_file = QFileDialog.getSaveFileName ()
            #print(path_to_file )
            f = open(path_to_file[0], "w")
            #print(f.read())
            f.write(str(window.plainTextEdit_3.toPlainText()))
            pathnow=path_to_file[0]
    def savetxt(txt):
        global pathnow
        if 'not find path'== pathnow:
            path_to_file = QFileDialog.getSaveFileName ()
            print(path_to_file )
            with open(path_to_file[0], 'w') as f:
                f.write(str(txt))
            command = ['kagsa', path_to_file[0]]
            result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True)
            window.plainTextEdit_3.clear()
            window.plainTextEdit_3.appendPlainText(str(result.stdout))
            pathnow=path_to_file[0]
        else:
            with open(pathnow, 'w') as f:
                f.write(str(txt))
            command = ['kagsa', pathnow]
            result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True)
            window.plainTextEdit_3.clear()
            window.plainTextEdit_3.appendPlainText(str(result.stdout))
    sys.exit(app.exec())