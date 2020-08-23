# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qsci import QsciScintilla
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self, parent=None) :
        super().__init__(parent)
        self.setupUi(self)

        ##self.scintilla

    @pyqtSlot()
    def on_actionNew_File_N_triggered(self):
        if (self.unsaved) :
            answer = QMessageBox.question(self, 'Warning', 'The open file is unsaved, still open another file?', QMessageBox.Yes | QMessageBox.No)
            return
        self.current_filename = 'untitled.asm'
        self.label.setText('untitled.asm')
        self.textEdit.setText('')
        self.unsaved = False

    # @ pyqtSlot()
    # def on_actionOpen_File_triggered(self):
    #
    #
    # @pyqtSlot()
    # def on_actionSave_File_triggered(self):
    #
    # @pyqtSlot()
    # def on_actionSave_as_triggered(self) :
    #
    #
    # @pyqtSlot()
    # def on_actionPrint_triggered(self):


    @pyqtSlot()
    def on_actionExit_triggered(self) :
        self.close()

    # @pyqtSlot()
    # def on_actionAssemble(self):
    #
    #
    # @pyqtSlot()
    # def on_actionDissemble(self):
    #
    #
    # @pyqtSlot()
    # def on_actionHelp(self) :


    def setupUi(self, MainWindow):
        self.current_filename = ''
        self.unsaved = False

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1141, 756)
        MainWindow.setToolTipDuration(-1)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.textEdit = QsciScintilla(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 1, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 1, 1, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textEdit_2 = QsciScintilla(self.tab)
        self.textEdit_2.setObjectName("textEdit_2")
        self.horizontalLayout.addWidget(self.textEdit_2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.horizontalLayout_2.addWidget(self.textBrowser_2)
        self.horizontalLayout_2.setStretch(0, 30)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 2, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 5)
        self.gridLayout.setColumnStretch(1, 3)
        self.gridLayout.setRowStretch(1, 3)
        self.gridLayout.setRowStretch(2, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1141, 26))
        self.menubar.setObjectName("menubar")
        self.menuMipsAssembler = QtWidgets.QMenu(self.menubar)
        self.menuMipsAssembler.setObjectName("menuMipsAssembler")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuDebug = QtWidgets.QMenu(self.menubar)
        self.menuDebug.setObjectName("menuDebug")
        MainWindow.setMenuBar(self.menubar)
        self.actionNew_File_N = QtWidgets.QAction(MainWindow)
        self.actionNew_File_N.setObjectName("actionNew_File_N")
        self.actionSave_File = QtWidgets.QAction(MainWindow)
        self.actionSave_File.setObjectName("actionSave_File")
        self.actionPrint = QtWidgets.QAction(MainWindow)
        self.actionPrint.setObjectName("actionPrint")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.action_asm = QtWidgets.QAction(MainWindow)
        self.action_asm.setObjectName("action_asm")
        self.action_bin = QtWidgets.QAction(MainWindow)
        self.action_bin.setObjectName("action_bin")
        self.action_coe = QtWidgets.QAction(MainWindow)
        self.action_coe.setObjectName("action_coe")
        self.action_asm_2 = QtWidgets.QAction(MainWindow)
        self.action_asm_2.setObjectName("action_asm_2")
        self.action_bin_2 = QtWidgets.QAction(MainWindow)
        self.action_bin_2.setObjectName("action_bin_2")
        self.action_coe_2 = QtWidgets.QAction(MainWindow)
        self.action_coe_2.setObjectName("action_coe_2")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        self.actionRedo.setObjectName("actionRedo")
        self.actionCut = QtWidgets.QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionDelete = QtWidgets.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.actionDelete_2 = QtWidgets.QAction(MainWindow)
        self.actionDelete_2.setObjectName("actionDelete_2")
        self.actionFind = QtWidgets.QAction(MainWindow)
        self.actionFind.setObjectName("actionFind")
        self.actionGo_to = QtWidgets.QAction(MainWindow)
        self.actionGo_to.setObjectName("actionGo_to")
        self.actionSelect_All = QtWidgets.QAction(MainWindow)
        self.actionSelect_All.setObjectName("actionSelect_All")
        self.actionAssemble = QtWidgets.QAction(MainWindow)
        self.actionAssemble.setObjectName("actionAssemble")
        self.actionCoe = QtWidgets.QAction(MainWindow)
        self.actionCoe.setObjectName("actionCoe")
        self.actionDissemble = QtWidgets.QAction(MainWindow)
        self.actionDissemble.setObjectName("actionDissemble")
        self.actionStep = QtWidgets.QAction(MainWindow)
        self.actionStep.setObjectName("actionStep")
        self.actionStep_2 = QtWidgets.QAction(MainWindow)
        self.actionStep_2.setObjectName("actionStep_2")
        self.actionyunxingdao = QtWidgets.QAction(MainWindow)
        self.actionyunxingdao.setObjectName("actionyunxingdao")
        self.actionstop = QtWidgets.QAction(MainWindow)
        self.actionstop.setObjectName("actionstop")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionOpen_File = QtWidgets.QAction(MainWindow)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.actionDebug = QtWidgets.QAction(MainWindow)
        self.actionDebug.setObjectName("actionDebug")
        self.actionUndo_2 = QtWidgets.QAction(MainWindow)
        self.actionUndo_2.setObjectName("actionUndo_2")
        self.actionRedo_2 = QtWidgets.QAction(MainWindow)
        self.actionRedo_2.setObjectName("actionRedo_2")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.menuMipsAssembler.addAction(self.actionNew_File_N)
        self.menuMipsAssembler.addAction(self.actionOpen_File)
        self.menuMipsAssembler.addSeparator()
        self.menuMipsAssembler.addAction(self.actionSave_File)
        self.menuMipsAssembler.addAction(self.actionSave_as)
        self.menuMipsAssembler.addAction(self.actionPrint)
        self.menuMipsAssembler.addSeparator()
        self.menuMipsAssembler.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionHelp)
        self.menuDebug.addAction(self.actionAssemble)
        self.menuDebug.addAction(self.actionDissemble)
        self.menubar.addAction(self.menuMipsAssembler.menuAction())
        self.menubar.addAction(self.menuDebug.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Terminal"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Debug"))
        self.label_2.setText(_translate("MainWindow", "Output"))
        self.menuMipsAssembler.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuDebug.setTitle(_translate("MainWindow", "Build"))
        self.actionNew_File_N.setText(_translate("MainWindow", "New File"))
        self.actionSave_File.setText(_translate("MainWindow", "Save File"))
        self.actionPrint.setText(_translate("MainWindow", "Print"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.action_asm.setText(_translate("MainWindow", ".asm"))
        self.action_bin.setText(_translate("MainWindow", ".bin"))
        self.action_coe.setText(_translate("MainWindow", ",coe"))
        self.action_asm_2.setText(_translate("MainWindow", ".asm"))
        self.action_bin_2.setText(_translate("MainWindow", ".bin"))
        self.action_coe_2.setText(_translate("MainWindow", ".coe"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionDelete.setText(_translate("MainWindow", "Paste"))
        self.actionDelete_2.setText(_translate("MainWindow", "Delete"))
        self.actionFind.setText(_translate("MainWindow", "Find"))
        self.actionGo_to.setText(_translate("MainWindow", "Go to"))
        self.actionSelect_All.setText(_translate("MainWindow", "Select All"))
        self.actionAssemble.setText(_translate("MainWindow", "Assemble"))
        self.actionCoe.setText(_translate("MainWindow", "Coe"))
        self.actionDissemble.setText(_translate("MainWindow", "Dissemble"))
        self.actionStep.setText(_translate("MainWindow", "Debug"))
        self.actionStep_2.setText(_translate("MainWindow", "Step()"))
        self.actionyunxingdao.setText(_translate("MainWindow", "yunxingdao"))
        self.actionstop.setText(_translate("MainWindow", "Stop"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as"))
        self.actionOpen_File.setText(_translate("MainWindow", "Open File"))
        self.actionDebug.setText(_translate("MainWindow", "Debug"))
        self.actionUndo_2.setText(_translate("MainWindow", "Undo"))
        self.actionRedo_2.setText(_translate("MainWindow", "Redo"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
