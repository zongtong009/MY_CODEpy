import sys
import PySide2
import os

# dirname = os.path.dirname(PySide2.__file__)
# plugin_path = os.path.join(dirname, 'plugins', 'platforms')
# os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

from PySide2 import QtWidgets


app = QtWidgets.QApplication(sys.argv)

hello = QtWidgets.QPushButton("Hello world!")
hello.resize(100, 30)

hello.show()

sys.exit(app.exec_())
