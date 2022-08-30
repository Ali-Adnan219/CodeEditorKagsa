import sys
from PySide6 import QtWidgets
from PySide6 import QtCore, QtGui
from PySide6.QtCore import Qt
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile, QIODevice
from PySide6.QtCore import QProcess

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform,QKeyEvent)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QPlainTextEdit, QPushButton, QSizePolicy, QWidget,QFileDialog)
import os
import subprocess
from subprocess import Popen, PIPE
import shlex
import re
pathnow='not find path'

# A regular expression, to extract the % complete.
progress_re = re.compile("Total complete: (\d+)%")

def simple_percent_parser(output):
    """
    Matches lines using the progress_re regex,
    returning a single integer for the % progress.
    """
    m = progress_re.search(output)
    if m:
        pc_complete = m.group(1)
        return int(pc_complete)




class Ui_CodeEditorkagsa(object):
    def setupUi(self, CodeEditorkagsa):
        if not CodeEditorkagsa.objectName():
            CodeEditorkagsa.setObjectName(u"CodeEditorkagsa")
        CodeEditorkagsa.resize(1134, 577)
        CodeEditorkagsa.setStyleSheet(u"\n"
"background-color: rgb(208, 199, 255);")
        self.pushButton = QPushButton(CodeEditorkagsa)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(570, 10, 151, 41))
        self.pushButton.setMinimumSize(QSize(141, 41))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.plainTextEdit_2 = QPlainTextEdit(CodeEditorkagsa)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setGeometry(QRect(10, 60, 711, 441))
        self.comboBox = QComboBox(CodeEditorkagsa)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(10, 10, 111, 41))
        self.comboBox.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(130, 28, 255);")
        self.plainTextEdit_3 = QPlainTextEdit(CodeEditorkagsa)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")
        self.plainTextEdit_3.setGeometry(QRect(730, 60, 391, 441))
        self.label = QLabel(CodeEditorkagsa)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(250, 10, 211, 41))
        self.label.setStyleSheet(u"background-color: rgb(85, 85, 127);\n"
"font: 12pt \"MS Reference Sans Serif\";")
        self.label_2 = QLabel(CodeEditorkagsa)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(830, 10, 211, 41))
        self.label_2.setStyleSheet(u"background-color: rgb(85, 85, 127);\n"
"font: 12pt \"MS Reference Sans Serif\";")

        self.retranslateUi(CodeEditorkagsa)
        self.pushButton.clicked.connect(lambda: self.savetxt(self.plainTextEdit_2.toPlainText()))
        self.comboBox.currentIndexChanged.connect(lambda: self.shwocop())

        QMetaObject.connectSlotsByName(CodeEditorkagsa)
    # setupUi

    def retranslateUi(self, CodeEditorkagsa):
        CodeEditorkagsa.setWindowTitle(QCoreApplication.translate("CodeEditorkagsa", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("CodeEditorkagsa", u"Run code", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("CodeEditorkagsa", u"Options", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("CodeEditorkagsa", u"Open file", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("CodeEditorkagsa", u"Save as", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("CodeEditorkagsa", u"Save output", None))

        self.label.setText(QCoreApplication.translate("CodeEditorkagsa", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#0c79ff;\">Code</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("CodeEditorkagsa", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#0c79ff;\">Output</span></p></body></html>", None))
    #Run code
    def shwocop(self):
        global pathnow
        choicess=self.comboBox.currentText()
        if choicess=='Open file':
            #print(window.comboBox.currentText())
            path_to_file = QFileDialog.getOpenFileName ()
            #print(path_to_file )
            f = open(path_to_file[0], "r")
            #print(f.read())
            self.plainTextEdit_2.clear()
            self.plainTextEdit_2.appendPlainText(str(f.read()))
            pathnow=path_to_file[0]
        elif choicess=='Save as':
            #print("h")
            path_to_file = QFileDialog.getSaveFileName ()
            #print(path_to_file )
            f = open(path_to_file[0], "w",encoding='utf-8')
            #print(f.read())
            f.write(str(self.plainTextEdit_2.toPlainText()))
            pathnow=path_to_file[0]
        elif choicess=='Save output':
            path_to_file = QFileDialog.getSaveFileName ()
            #print(path_to_file )
            f = open(path_to_file[0], "w")
            #print(f.read())
            f.write(str(self.plainTextEdit_3.toPlainText()))
            pathnow=path_to_file[0]
    def handle_stdout(self):
        data = self.p.readAllStandardOutput()
        stdout = bytes(data).decode("utf8")
        self.plainTextEdit_3.appendPlainText(stdout)
    def message(self, s):
        self.plainTextEdit_3.appendPlainText(s)
    def handle_stderr(self):
        data = self.p.readAllStandardError()
        stderr = bytes(data).decode("utf8")
        # Extract progress if it is in the data.
        progress = simple_percent_parser(stderr)
        if progress:
            self.progress.setValue(progress)
        self.plainTextEdit_3.appendPlainText(stderr)


    def handle_state(self, state):
        states = {
            QProcess.NotRunning: 'Not running',
            QProcess.Starting: 'Starting',
            QProcess.Running: 'Running',
        }
        state_name = states[state]
        self.plainTextEdit_3.appendPlainText(f"State changed: {state_name}")

    def process_finished(self):
        self.plainTextEdit_3.appendPlainText("Process finished.")
        self.p = None
    def savetxt(self,txt):
        global pathnow
        if 'not find path'== pathnow:
            path_to_file = QFileDialog.getSaveFileName ()
            print(path_to_file )
            with open(path_to_file[0], 'w') as f:
                f.write(str(txt))
            command =  path_to_file[0]
            self.p = QProcess() 
            self.p.readyReadStandardOutput.connect(self.handle_stdout)
            self.p.readyReadStandardError.connect(self.handle_stderr)
            self.p.stateChanged.connect(self.handle_state)
            self.p.finished.connect(self.process_finished)  # Clean up once complete.
            self.p.start("kagsa", [path_to_file[0]])
            self.plainTextEdit_3.clear()
            #self.plainTextEdit_3.appendPlainText(str( out.decode("utf-8")))
            pathnow=path_to_file[0]
        else:
            with open(pathnow, 'w') as f:
                f.write(str(txt))
            command = pathnow
            self.p = QProcess() 
            self.p.readyReadStandardOutput.connect(self.handle_stdout)
            self.p.readyReadStandardError.connect(self.handle_stderr)
            self.p.stateChanged.connect(self.handle_state)
            self.p.finished.connect(self.process_finished)  # Clean up once complete.
            self.p.start("kagsa", [command])
            self.plainTextEdit_3.clear()
            #self.plainTextEdit_3.appendPlainText(str(out.decode("utf-8")))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_CodeEditorkagsa()
    w = QtWidgets.QMainWindow()
    ex.setupUi(w)
    w.show()
    sys.exit(app.exec_())