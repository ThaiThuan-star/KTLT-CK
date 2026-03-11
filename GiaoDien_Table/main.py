from PyQt6.QtWidgets import QApplication

#QApplication, đối tượng quản lý app: qly click, cửa sổ, vòng lặp chương trình

from MainWindow_Ext import MainWindow
import sys

app = QApplication(sys.argv) #Khởi tạo chương trình
window = MainWindow() #Tạo của sổ chính
window.setupUi(window) #Thiết lập giao diện cho chính nó
window.show()  #Hiển thị cửa sổ lên màn hình

sys.exit(app.exec()) #Chạy vòng lặp chương trình để chờ các thao tác từ người dùng