from PyQt6.QtWidgets import QApplication,QMainWindow
from MainWindow_Ext import MainWindow
app=QApplication([])
w=QMainWindow()
f=MainWindow()
f.setupUi(w)
w.show()
app.exec()