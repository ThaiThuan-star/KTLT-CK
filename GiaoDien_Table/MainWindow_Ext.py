from PyQt6.QtWidgets import QTableWidgetItem,QMessageBox,QMainWindow
from MainWindow import Ui_MainWindow
from datetime import datetime
from CSinhVien import *
from CLop import *
from CKhoa import *
from CQuanLySinhVien import *
import json
import os

class MainWindow(Ui_MainWindow,QMainWindow):
    def setupUi(self,MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow

        # Khởi tạo đối tượng quản lý (Tự động load JSON và phân khoa/lớp)
        self.qly=QuanLySinhVien()

        self.process()
    def process(self):

        #Hiển thị danh sách sinh viên (Khang làm)

        self.btn_delete_sv.clicked.connect(self.delete_sv)
        self.btn_add_sv.clicked.connect(self.add_sv)
        self.btn_edit_sv.clicked.connect(self.edit_sv)
        self.btn_loc.clicked.connect(self.loc_sv)
        self.btn_search.clicked.connect(self.search_sv)

    def add_sv(self):
        ten = self.txt_ho_ten.text().strip()
        mssv = self.txt_mssv.text().strip()
        lop = self.box_lop.currentText().strip()
        gpa = self.txt_gpa.text().strip()
        khoa = self.comboBox.currentText().strip()
        ngay_them = datetime.now().strftime("%d/%m/%Y")
        if (not self.txt_ho_ten.text() or not self.txt_gpa.text()
                or not self.box_lop.currentText() or not self.txt_mssv.text() ) :
            QMessageBox.warning(self, "Lỗi nhập liệu", "Nhập thiếu dữ liệu")
            return
        try:
            kt_gpa=float(gpa) #Phải tách biệt ra riêng vì QTable chỉ nhận str
        except ValueError:
            QMessageBox.warning(self, "Lỗi", "GPA phải là số")
            return

        #Kiểm tra xem sinh viên đã có trong ds chưa
        existing_data = {}
        filename = "ds_sv.json"
        if os.path.exists(filename):
            try:
                with open(filename, "r", encoding="utf-8") as file:
                    existing_data = json.load(file)
            except json.JSONDecodeError:
                # Bỏ qua nếu file rỗng hoặc lỗi định dạng, khởi tạo lại dictionary rỗng
                existing_data = {}
        if mssv in existing_data:
            QMessageBox.warning(self, "Lỗi", "Sinh viên đã tồn tại")
            return

        """Set thông tin vào bảng"""

        # Đếm số dòng hiện tại
        row = self.tbl_ds_them.rowCount()

        # Thêm dòng mới dựa trên số dòng vì chỉ số dòng bắt đầu từ 0
        self.tbl_ds_them.insertRow(row)

        # Set dữ liệu đúng cột
        # Phải dùng QTableWidgetItem vì các ô không chỉ chứa vban mà còn chứa nhiều dl như font-size,...

        self.tbl_ds_them.setItem(row, 0, QTableWidgetItem(ten))
        self.tbl_ds_them.setItem(row, 1, QTableWidgetItem(mssv))
        self.tbl_ds_them.setItem(row, 2, QTableWidgetItem(lop))
        self.tbl_ds_them.setItem(row, 3, QTableWidgetItem(khoa))
        self.tbl_ds_them.setItem(row, 4, QTableWidgetItem(gpa))
        self.tbl_ds_them.setItem(row, 5, QTableWidgetItem(ngay_them))

        existing_data[mssv] = {
            "Tên": ten,
            "Lớp": lop,
            "Khoa": khoa,
            "Gpa": float(gpa),
            "Ngày thêm": ngay_them
        }
        with open("ds_sv.json", "w", encoding="utf-8") as file:
            json.dump(existing_data, file, indent=4, ensure_ascii=False)
        QMessageBox.information(self, "Thông báo", "Thêm thành công!")
        self.clear_input()
        return
    def clear_input(self):
        self.txt_ho_ten.setText("")
        self.txt_mssv.setText("")
        self.txt_gpa.setText("")
    def delete_sv(self):
        pass
    def edit_sv(self):
        pass
    def loc_sv(self):
        pass
    def search_sv(self):
        pass
