# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Mon Oct 15 16:55:55 2012
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_pyglatin(object):
    def setupUi(self, pyglatin):
        pyglatin.setObjectName("pyglatin")
        pyglatin.resize(322, 303)
        self.centralWidget = QtGui.QWidget(pyglatin)
        self.centralWidget.setObjectName("centralWidget")
        self.pushButton = QtGui.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 200, 83, 25))
        self.pushButton.setObjectName("pushButton")
        self.textEdit_2 = QtGui.QTextEdit(self.centralWidget)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 100, 301, 81))
        self.textEdit_2.setObjectName("textEdit_2")
        self.lineEdit = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 20, 281, 51))
        self.lineEdit.setObjectName("lineEdit")
        pyglatin.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(pyglatin)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 322, 22))
        self.menuBar.setObjectName("menuBar")
        pyglatin.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(pyglatin)
        self.mainToolBar.setObjectName("mainToolBar")
        pyglatin.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(pyglatin)
        self.statusBar.setObjectName("statusBar")
        pyglatin.setStatusBar(self.statusBar)

        self.retranslateUi(pyglatin)
        QtCore.QMetaObject.connectSlotsByName(pyglatin)

    def retranslateUi(self, pyglatin):
        pyglatin.setWindowTitle(QtGui.QApplication.translate("pyglatin", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("pyglatin", "PushButton", None, QtGui.QApplication.UnicodeUTF8))

