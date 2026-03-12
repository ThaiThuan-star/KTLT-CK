
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit
from log_in import Ui_MainWindow
from dangnhap import quanlydanhtinh

from MainWindow_Ext import  MainWindow


class MainApp(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.user_manager = quanlydanhtinh()

        # Kết nối các nút chuyển trang
        self.btn_dk.clicked.connect(self.show_register)
        self.btn_dktd.clicked.connect(self.show_register)
        self.btn_dn2.clicked.connect(self.show_login)
        # Nút chính
        self.btn_dnc.clicked.connect(self.handle_login)
        self.btn_dkc.clicked.connect(self.handle_register)

        # Nút ẩn/hiện mật khẩu
        self.btn_eyemk.clicked.connect(lambda: self.toggle_password_visibility(self.txt_mk))  #Nếu k dùng thì nó tự chạy hàm toggle...
        self.btn_eyemk2.clicked.connect(lambda: self.toggle_password_visibility(self.txt_mk2))
        self.btn_eyenlmk.clicked.connect(lambda: self.toggle_password_visibility(self.txt_nlmk))
        # Đặt trang hiển thị ban đầu là đăng nhập (index 0)
        self.stackedWidget.setCurrentIndex(0)

    def show_register(self):
        self.stackedWidget.setCurrentIndex(1)
        self.lbl_smk.clear() # Xóa thông báo lỗi cũ

    def show_login(self):
        self.stackedWidget.setCurrentIndex(0)
        self.lbl_smk.clear()

    def toggle_password_visibility(self, line_edit):
        # Chuyển chế độ hiển thị của ô mật khẩu (ẩn hoặc hiện)
        if line_edit.echoMode() == QLineEdit.EchoMode.Password:
            line_edit.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            line_edit.setEchoMode(QLineEdit.EchoMode.Password)

    def handle_login(self):
        username = self.txt_tk.text().strip()
        password = self.txt_mk.text()

        if not username or not password:
            self.lbl_smk.setText("Vui lòng nhập đầy đủ tài khoản và mật khẩu")
            return

        # Kiểm tra đăng nhập
        success, message = self.user_manager.dangnhap(username, password) #Lấy 2 giá trị từ hàm dangnhap

        if success:
            # TẠO ĐỐI TƯỢNG MÀN HÌNH CHÍNH
            self.main_window = MainWindow()

            # Kích hoạt giao diện (setupUi) cho màn hình chính
            self.main_window.setupUi(self.main_window)

            # Hiển thị màn hình chính
            self.main_window.show()

            # Đóng màn hình đăng nhập hiện tại
            self.close()
        else:
            self.lbl_smk.setText(message)

    def handle_register(self):
        username = self.txt_tk2.text().strip()
        password = self.txt_mk2.text()
        repassword = self.txt_nlmk.text()

        if not username or not password or not repassword:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin")
            return
        if password != repassword:
            QMessageBox.warning(self, "Lỗi", "Mật khẩu nhập lại không khớp")
            return

        success, message = self.user_manager.dangki(username, password)

        if success:
            QMessageBox.information(self, "Thành công", message)
            self.show_login()                 # Quay về trang đăng nhập
            self.txt_tk.setText(username)      # Điền sẵn tên đăng nhập
        else:
            QMessageBox.critical(self, "Lỗi", message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())