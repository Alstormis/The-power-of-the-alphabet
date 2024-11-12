from PyQt5 import QtWidgets
from src.app.lr1.forms.Lr1_code import Mywindow
import sys

app = QtWidgets.QApplication([])
application = Mywindow()
application.show()
application.language_selection()
sys.exit(app.exec_())
