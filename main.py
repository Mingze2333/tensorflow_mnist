import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from GUI import MainWidget
from PyQt5.QtWidgets import QApplication
import sys

app = QApplication(sys.argv)
mainWidget = MainWidget()
mainWidget.show()
exit(app.exec_())
