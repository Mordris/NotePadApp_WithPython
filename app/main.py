import sys
from PyQt5.QtWidgets import QApplication
from app.views import NotepadApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    notepad = NotepadApp()
    notepad.show()
    sys.exit(app.exec_())
