from PyQt5.Qsci import QsciScintilla
from PyQt5.QtWidgets import QMdiSubWindow


class EditorSubWindow(QMdiSubWindow):
    def __init__(self, parent=None) :
        super().__init__(parent)
        self.Editor = QsciScintilla()
        self.setWidget(self.Editor)
        self.unsaved = False
        self.path = ''
