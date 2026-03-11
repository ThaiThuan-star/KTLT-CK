# from PyQt6.QtWidgets import QApplication,QMainWindow
# from MainWindow_Ext import MainWindow
# app=QApplication([])
# w=QMainWindow()
# f=MainWindow()
# f.setupUi(w)
# w.show()
# app.exec()


from PyQt6.QtWidgets import QApplication
from MainWindow_Ext import MainWindow
import sys

app = QApplication(sys.argv)
window = MainWindow()
window.setupUi(window) # Thiết lập giao diện lên chính nó
window.show()

sys.exit(app.exec())