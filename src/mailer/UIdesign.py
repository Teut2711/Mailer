# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mailer.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(752, 484)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(90, 255, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(90, 255, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(90, 255, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(90, 255, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(90, 255, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(90, 255, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(90, 255, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(90, 255, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(90, 255, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        MainWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("index.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("\n"
"background-color:rgb(90, 255, 90);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, -1, 221, 491))
        font = QtGui.QFont()
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("\n"
"background-color:rgb(53, 74, 122);\n"
"color:rgb(220, 255, 10);\n"
"height:100%;\n"
"font-size:20px;\n"
"")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(60, 50, 71, 31))
        font = QtGui.QFont()
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("border: 2px solid transparent;\n"
"color:white;\n"
"font-size:20px;")
        self.label_7.setObjectName("label_7")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(50, 170, 101, 31))
        font = QtGui.QFont()
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("border: 2px solid transparent;\n"
"color:white;\n"
"font-size:20px;")
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QtCore.QRect(20, 100, 171, 31))
        self.lineEdit.setMouseTracking(False)
        self.lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit.setStyleSheet("border:none;\n"
"border-bottom:2px solid red;\n"
"color:rgb(251, 255, 157);\n"
"height:18px;\n"
"width:30px;")
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhEmailCharactersOnly|QtCore.Qt.ImhLowercaseOnly|QtCore.Qt.ImhNoAutoUppercase)
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 220, 171, 31))
        self.lineEdit_2.setStyleSheet("border:none;\n"
"border-bottom:2px solid red;\n"
"color:rgb(251, 255, 157);\n"
"height:18px;\n"
"width:30px;")
        self.lineEdit_2.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(70, 300, 51, 31))
        font = QtGui.QFont()
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("border: 2px solid transparent;\n"
"color:white;\n"
"font-size:20px;")
        self.label_6.setObjectName("label_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 350, 171, 31))
        self.lineEdit_3.setStyleSheet("border:none;\n"
"border-bottom:2px solid red;\n"
"color:rgb(251, 255, 157);\n"
"height:18px;\n"
"width:30px;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5.raise_()
        self.label_7.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.label_6.raise_()
        self.lineEdit_3.raise_()
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(219, -1, 531, 491))
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet("background:rgb(238, 255, 83);\n"
"border-radius:4px;\n"
"border-top:2px solid red;\n"
"border-right:2px solid green;\n"
"")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(130, 90, 271, 61))
        font = QtGui.QFont()
        font.setFamily("Miriam Mono CLM")
        font.setPointSize(50)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(99)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("\n"
"font: 50pt \"Miriam Mono CLM\";\n"
"background:transparent;\n"
"color:rgb(55, 57, 177);\n"
"font-weight:1000;\n"
"padding-right:0px;\n"
"padding-bottom:1px;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(10, 190, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(62)
        font.setStrikeOut(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background:rgb(74, 86, 253);\n"
"color:rgb(1, 15, 44);\n"
"font: bold italic large \"Times New Roman\" ;\n"
"font-size:16px;\n"
"font-weight:500;\n"
"padding:3px;\n"
"text-decoration:none;\n"
"border-bottom:2px red;\n"
"\n"
"")
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setGeometry(QtCore.QRect(110, 190, 281, 31))
        self.textEdit.setStyleSheet("height:30px;\n"
"background-color:transparent;\n"
"border:none;\n"
"border-bottom:2px double rgb(12, 12, 255);\n"
"font-size:15px;\n"
"color:rgb(34, 4, 156);\n"
"padding:2px;")
        self.textEdit.setFrameShadow(QtWidgets.QFrame.Raised)
        self.textEdit.setLineWidth(20)
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit.setObjectName("textEdit")
        self.FileBrowse = QtWidgets.QPushButton(self.widget)
        self.FileBrowse.setGeometry(QtCore.QRect(400, 190, 91, 31))
        self.FileBrowse.setStyleSheet("QObject{background:rgb(90, 101, 255);\n"
"font-style:italic;\n"
"font-size:14px;}\n"
"\n"
"QObject:pressed{\n"
"\n"
"background:rgb(211, 255, 143);\n"
"}\n"
"\n"
"")
        self.FileBrowse.setObjectName("FileBrowse")
        self.Fire = QtWidgets.QPushButton(self.widget)
        self.Fire.setGeometry(QtCore.QRect(210, 230, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.Fire.setFont(font)
        self.Fire.setStyleSheet("QPushButton{background:rgb(158, 37, 16);\n"
"color:white;\n"
"}\n"
"QPushButton:pressed{\n"
"\n"
"background:rgb(255, 131, 29);\n"
"}")
        self.Fire.setObjectName("Fire")
        self.textBrowser = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 310, 481, 131))
        font = QtGui.QFont()
        font.setFamily("Noto Kufi Arabic")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background:white;\n"
"font: 12pt \"Noto Kufi Arabic\";\n"
"color:rgb(255, 39, 125);")
        self.textBrowser.setObjectName("textBrowser")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(180, 10, 151, 31))
        self.label_3.setStyleSheet("font-size:20px;\n"
"color:rgb(3, 3, 58);\n"
"border:2px solid red;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(0, 50, 531, 31))
        self.label_4.setStyleSheet("color:rgb(11, 6, 84);\n"
"font-size:12px;\n"
"background:rgb(165, 179, 255);\n"
"")
        self.label_4.setObjectName("label_4")
        self.progressBar = QtWidgets.QProgressBar(self.widget)
        self.progressBar.setGeometry(QtCore.QRect(10, 280, 481, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet("text-align:center;\n"
"background:white;\n"
"border:3px solid gray;\n"
"border-radius:0;\n"
"")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mailer"))
        self.groupBox.setTitle(_translate("MainWindow", "User Info"))
        self.label_7.setText(_translate("MainWindow", "E-Mail"))
        self.label_5.setText(_translate("MainWindow", "Password"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Enter E-mail"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Enter Password"))
        self.label_6.setText(_translate("MainWindow", "Host"))
        self.lineEdit_3.setText(_translate("MainWindow", "mail.masserv.com"))
        self.label.setText(_translate("MainWindow", "Mailer"))
        self.label_2.setText(_translate("MainWindow", "File Name"))
        self.FileBrowse.setText(_translate("MainWindow", "Browse"))
        self.Fire.setText(_translate("MainWindow", "Send Emails"))
        self.label_3.setText(_translate("MainWindow", "Excel  Columns"))
        self.label_4.setText(_translate("MainWindow", "| E-Mail Addresses(seperated by comma) | Files(Path) |  Subject(text) |  Message(.htm/.html)|"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
