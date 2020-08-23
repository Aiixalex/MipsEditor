# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QMdiArea, QMdiSubWindow, QFileDialog, QInputDialog

from Assmbler.assemble import assemble
from Dissembler.dissemble import dissemble
from EditorSubWindow import EditorSubWindow


class MainWindow(QMainWindow):
    PagesCount = 0
    def __init__(self, parent=None) :
        super().__init__(parent)
        self.setupUi(self)

    @pyqtSlot()
    def on_actionNew_File_triggered(self):
        filename, _ = QFileDialog.getSaveFileName(self, 'New File',
                                                  filter="All Files (*.*);;ASM Files (*.asm *.s);;Text Files (*.txt)")
        if filename:
            with open(filename, 'w+', encoding="UTF8") as f :
                self.addSubPage(self.mdi_Editor)
                SubPage = self.mdi_Editor.currentSubWindow()
                SubPage.setWindowTitle(filename)
                SubPage.path = filename
        f.close()

    @ pyqtSlot()
    def on_actionOpen_File_triggered(self):
        filename, _ = QFileDialog.getOpenFileName(self, 'Open File',
                                                  filter="All Files (*.*);;ASM Files (*.asm *.s);;Text Files (*.txt)")
        if filename:
            with open(filename, 'r+', encoding="UTF8") as f:
                self.addSubPage(self.mdi_Editor)
                SubPage = self.mdi_Editor.currentSubWindow()
                SubPage.setWindowTitle(filename)
                SubPage.Editor.setText(f.read())
                SubPage.path = filename
        f.close()

    @pyqtSlot()
    def on_actionSave_File_triggered(self):
        SubPage = self.mdi_Editor.currentSubWindow()
        with open(SubPage.path, 'w+', encoding="UTF8") as f:
            f.write(SubPage.Editor.text())
        f.close()

    @pyqtSlot()
    def on_actionSave_as_triggered(self) :
        SubPage = self.mdi_Editor.currentSubWindow()
        filename, _ = QFileDialog.getSaveFileName(self, 'Save File',
                                                  filter="All Files (*.*);;ASM Files (*.asm *.s);;Text Files (*.txt)")
        if filename :
            with open(filename, 'w+', encoding="UTF8") as f :
                f.write(SubPage.Editor.text())

    # @pyqtSlot()
    # def on_actionPrint_triggered(self):

    @pyqtSlot()
    def on_actionExit_triggered(self):
        self.close()

    @pyqtSlot()
    def on_actionUndo_triggered(self):
        SubPage = self.mdi_Editor.currentSubWindow()
        SubPage.Editor.undo()

    @pyqtSlot()
    def on_actionRedo_triggered(self):
        SubPage = self.mdi_Editor.currentSubWindow()
        SubPage.Editor.redo()

    @pyqtSlot()
    def on_actionCut_triggered(self):
        SubPage = self.mdi_Editor.currentSubWindow()
        SubPage.Editor.cut()

    @pyqtSlot()
    def on_actionCopy_triggered(self):
        SubPage = self.mdi_Editor.currentSubWindow()
        SubPage.Editor.copy()

    @pyqtSlot()
    def on_actionPaste_triggered(self):
        SubPage = self.mdi_Editor.currentSubWindow()
        SubPage.Editor.paste()

    @pyqtSlot()
    def on_actionDelete_triggered(self) :
        SubPage = self.mdi_Editor.currentSubWindow()
        SubPage.Editor.removeSelectedText()

    @pyqtSlot()
    def on_actionFind_triggered(self):
        SubPage = self.mdi_Editor.currentSubWindow()
        text, ok = QInputDialog.getText(self, 'Find', 'Search Target:')
        if ok:
            SubPage.Editor.findFirst(text, 0, 0, 0, 0)

    @pyqtSlot()
    def on_actionSelect_All_triggered(self) :
        SubPage = self.mdi_Editor.currentSubWindow()
        SubPage.Editor.selectAll()

    @pyqtSlot()
    def on_actionAssemble_triggered(self):
        SubPage = self.mdi_Editor.currentSubWindow()
        input = SubPage.Editor.text()
        assemble(input)
        self.Output.append('Output : Successfully assemble the file.\n'
                           'The result has been writen in \'asm_Result.txt\'\n')

    @pyqtSlot()
    def on_actionDissemble_triggered(self):
        SubPage = self.mdi_Editor.currentSubWindow()
        input = SubPage.Editor.text()
        dissemble(input)
        self.Output.append('Output : Successfully dissemble the file.\n'
                           'The result has been writen in \'dis_Result.txt\'\n')

    # @pyqtSlot()
    # def on_actionHelp_triggered(self):

    def addSubPage(self, MdiArea):
        SubPage = EditorSubWindow()
        SubPage.setWindowTitle("Untitled.txt")
        self.Pages.append(SubPage)
        MdiArea.addSubWindow(SubPage)

        self.PagesCount += 1
        return SubPage


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1141, 756)
        MainWindow.setToolTipDuration(-1)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser_Debug = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_Debug.setObjectName("textBrowser_Debug")
        self.gridLayout.addWidget(self.textBrowser_Debug, 1, 1, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Output = QtWidgets.QTextEdit(self.tab)
        self.Output.setObjectName("Output")
        self.horizontalLayout.addWidget(self.Output)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textBrowser_Terminal = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_Terminal.setObjectName("textBrowser_Terminal")
        self.horizontalLayout_2.addWidget(self.textBrowser_Terminal)
        self.horizontalLayout_2.setStretch(0, 30)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 2, 0, 1, 2)
        self.label_Debug = QtWidgets.QLabel(self.centralwidget)
        self.label_Debug.setObjectName("label_Debug")
        self.gridLayout.addWidget(self.label_Debug, 0, 1, 1, 1)
        self.mdi_Editor = QtWidgets.QMdiArea(self.centralwidget)
        self.mdi_Editor.setObjectName("mdi_Editor")
        self.mdi_Editor.setViewMode(QMdiArea.TabbedView)
        self.mdi_Editor.setTabsClosable(False)
        self.Pages = []
        # self.addSubPage(self.mdi_Editor)
        self.gridLayout.addWidget(self.mdi_Editor, 0, 0, 2, 1)
        self.gridLayout.setColumnStretch(0, 5)
        self.gridLayout.setColumnStretch(1, 3)
        self.gridLayout.setRowStretch(1, 3)
        self.gridLayout.setRowStretch(2, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1141, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuRun = QtWidgets.QMenu(self.menubar)
        self.menuRun.setObjectName("menuRun")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")

        MainWindow.setMenuBar(self.menubar)
        self.actionNew_File = QtWidgets.QAction(MainWindow)
        self.actionNew_File.setObjectName("actionNew_File")
        self.actionSave_File = QtWidgets.QAction(MainWindow)
        self.actionSave_File.setObjectName("actionSave_File")
        self.actionPrint = QtWidgets.QAction(MainWindow)
        self.actionPrint.setObjectName("actionPrint")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAssemble = QtWidgets.QAction(MainWindow)
        self.actionAssemble.setObjectName("actionAssemble")
        self.actionDissemble = QtWidgets.QAction(MainWindow)
        self.actionDissemble.setObjectName("actionDissemble")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionOpen_File = QtWidgets.QAction(MainWindow)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionDebug = QtWidgets.QAction(MainWindow)
        self.actionDebug.setObjectName("actionDebug")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        self.actionRedo.setObjectName("actionRedo")
        self.actionCut = QtWidgets.QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionDelete = QtWidgets.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.actionFind = QtWidgets.QAction(MainWindow)
        self.actionFind.setObjectName("actionFind")
        self.actionSelect_All = QtWidgets.QAction(MainWindow)
        self.actionSelect_All.setObjectName("actionSelect_All")

        self.menuFile.addAction(self.actionNew_File)
        self.menuFile.addAction(self.actionOpen_File)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave_File)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addAction(self.actionPrint)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)

        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionDelete)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionFind)
        self.menuEdit.addAction(self.actionSelect_All)

        self.menuRun.addAction(self.actionAssemble)
        self.menuRun.addAction(self.actionDissemble)
        self.menuRun.addSeparator()
        self.menuRun.addAction(self.actionDebug)

        self.menuHelp.addAction(self.actionHelp)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuRun.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Output"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Terminal"))
        self.label_Debug.setText(_translate("MainWindow", "Debug"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuRun.setTitle(_translate("MainWindow", "Run"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionNew_File.setText(_translate("MainWindow", "New File"))
        self.actionSave_File.setText(_translate("MainWindow", "Save File"))
        self.actionPrint.setText(_translate("MainWindow", "Print"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionAssemble.setText(_translate("MainWindow", "Assemble"))
        self.actionDissemble.setText(_translate("MainWindow", "Dissemble"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as"))
        self.actionOpen_File.setText(_translate("MainWindow", "Open File"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionDebug.setText(_translate("MainWindow", "Debug"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionDelete.setText(_translate("MainWindow", "Delete"))
        self.actionFind.setText(_translate("MainWindow", "Find"))
        self.actionSelect_All.setText(_translate("MainWindow", "Select All"))
