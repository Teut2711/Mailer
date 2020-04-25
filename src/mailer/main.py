import os
import smtplib
import subprocess
import sys
from time import sleep

from PyQt5 import QtWidgets
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog, QToolTip
from PyQt5.QtGui import QFont, QValidator

from mailer.sendmailer import sendMail
from mailer.UIdesign import Ui_MainWindow


def authenticateuser(host, port, user, passwd):

    with smtplib.SMTP(host,
                        port) as smtp:
        smtp.login(user=user,
                    password=passwd)

class MainMailer(Ui_MainWindow):
    
    def __init__(self, MainWindow):
        super().setupUi(MainWindow)

        MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint
                                  | QtCore.Qt.WindowMinimizeButtonHint)
        MainWindow.show()

        self.textBrowser.setStyleSheet(
            "color:#1A1B41;font-size:14px;background:white;")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Fire.setDisabled(True)
        self.FileBrowse.clicked.connect(self.browse_File)  # Browse Button
        self.textEdit.textChanged.connect(self.activateredbtn)

    def browse_File(self):
        self.textBrowser.setText("")
        self.progressBar.setValue(0)
        file_name, _ = QFileDialog.getOpenFileName(
            filter="Excel (*.xlsx);;CSV (*.csv) ")

        if file_name:
            self.textEdit.setText(file_name)
            subprocess.run(["start", "excel", file_name], shell=True)
            self.Fire.setEnabled(True)
            self.Fire.clicked.connect(self.executeMailer)
    
    def activateredbtn(self):
        if self.textEdit.toPlainText().endswith(".csv") or  self.textEdit.toPlainText().endswith(".xlsx") :
            self.Fire.setEnabled(True)
            self.Fire.clicked.connect(self.executeMailer)
    


    def print_send(self, value1, value2):
        if value2 > 0:
            self.progressBar.setValue(value2)
        self.textBrowser.append(f"<em>{value1}</em>")

    def executeMailer(self):
        if self.lineEdit.text() and self.lineEdit_2.text():
            try:
                authenticateuser(host=self.lineEdit_3.text(),
                                        port=587,
                                        user=self.lineEdit.text(),
                                        passwd=self.lineEdit_2.text())
            except smtplib.SMTPAuthenticationError:
                self.textBrowser.setHtml(
                    "<strong>Invalid Username or Password !!</strong>")
            except Exception as e:
                self.textBrowser.setText(getattr(e, 'message', repr(e)))
            else:
                self.textEdit.disconnect()
                self.textEdit.setReadOnly(True)
                self.Fire.setEnabled(False)
                self.Fire.clicked.disconnect()
                self.FileBrowse.clicked.disconnect()
                self.FileBrowse.setDisabled(True)
                self.textBrowser.setText("Process Started...")
                self.obj = sendMail(settings={
                    "smtphost": self.lineEdit_3.text(),
                    "smtpuser": self.lineEdit.text(),
                    "smtppass": self.lineEdit_2.text(),
                    "mailfrom": self.lineEdit.text(),
                    "smtpport": 587
                },
                                    excel_file=self.textEdit.toPlainText())
                self.obj.sent_to.connect(self.print_send)
                self.obj.finished.connect(self.obj.deleteLater)
                self.obj.finished.connect(self.finished_sending)
                self.obj.start()

    def finished_sending(self):
        self.textEdit.setReadOnly(False)
        self.textEdit.textChanged.connect(self.activateredbtn)
        self.FileBrowse.setEnabled(True)
        self.FileBrowse.clicked.connect(self.browse_File)
        self.textBrowser.append("<strong>Process Finished...<strong>")


def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainMailer(MainWindow)
    return app.exec()
