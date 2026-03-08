from PyQt6.QtWidgets import QTableWidgetItem,QMessageBox,QMainWindow
from MainWindow import Ui_MainWindow
from datetime import datetime
import json
import os

class MainWindow(Ui_MainWindow,QMainWindow):
    def setupUi(self,MainWindow): # Ghi đè từ hàm setup của class cha
         super().setupUi(MainWindow) # Gọi hàm setup của class cha và thêm vào MainWindow vào đó để chạy giao diện
                                     # Phải thêm vào MainWindow để cái Widget biết nó cần được gắn vào đâu (MainWindow)
         self.stackedWidget.hide()
         self.MainWindow=MainWindow # Dòng này lưu lại cửa sổ chính vào biến của class
         # Ẩn cái "khay" chứa các bảng khi vừa mở app
         self.process()
    def process(self):
        self.btn_add_sv.clicked.connect(self.add_sv)
        self.btn_search.clicked.connect(self.search_sv)
        self.btn_confirm.clicked.connect(self.confirm_sv)
    def add_sv(self):

        ten = self.txt_ho_ten.text().strip()
        mssv = self.txt_mssv.text().strip()
        lop = self.txt_lop.text().strip()
        gpa = self.txt_gpa.text().strip()
        khoa = self.comboBox.currentText().strip()
        ngay = datetime.now().strftime("%d/%m/%Y")
        if (not self.txt_ho_ten.text() or not self.txt_gpa.text() or not self.txt_lop.text() or not self.txt_mssv.text() ) :
            QMessageBox.warning(self, "Lỗi nhập liệu", "Nhập thiếu dữ liệu")
            return
        try:
            kt_gpa=float(gpa) #Phải tách biệt ra riêng vì QTable chỉ nhận str
        except ValueError:
            QMessageBox.warning(self, "Lỗi", "GPA phải là số")
            return

        # Hiện lại cái khay
        self.stackedWidget.show()
        # Chuyển sang trang chứa bảng tìm kiếm
        self.stackedWidget.setCurrentIndex(0)

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
        self.tbl_ds_them.setItem(row, 5, QTableWidgetItem(ngay))

        QMessageBox.information(self, "Thông báo", "Thêm sinh viên thành công!")
        self.clear_input()

    #Xóa các dữ liệu trên thanh nhập sau khi thêm
    def clear_input(self):
        self.txt_ho_ten.setText("")
        self.txt_mssv.setText("")
        self.txt_lop.setText("")
        self.txt_gpa.setText("")

    def search_sv(self):
        ma_sv = self.txt_search.text().strip()
        if not ma_sv:
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng nhập mã số sinh viên cần tìm!")
            return
        filename = "ds_sv.json"
        try:
            # Mở và đọc dữ liệu từ file JSON
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)

            # Vì cấu trúc JSON giờ là dictionary với key là MSSV, ta chỉ cần kiểm tra key
            if ma_sv in data:
                student_info = data[ma_sv]

                # Cập nhật thông tin lên giao diện
                self.txt_ten_search.setText(student_info.get("Tên"))
                self.txt_mssv_search.setText(ma_sv)  # Mã SV chính là từ khóa tìm kiếm
                self.txt_lop_search.setText(student_info.get("Lớp", ""))
                self.txt_khoa_search.setText(student_info.get("Khoa", ""))
                self.txt_gpa_search.setText(str(student_info.get("Gpa", "")))

                # Hiện lại cái khay
                self.stackedWidget.show()
                # Chuyển sang trang chứa bảng tìm kiếm
                self.stackedWidget.setCurrentIndex(1)

                QMessageBox.information(self, "Thông báo", "Đã tìm thấy sinh viên!")
            else:
                QMessageBox.warning(self, "Lỗi", f"Không tìm thấy sinh viên có mã {ma_sv}!")
        except json.JSONDecodeError:
            QMessageBox.warning(self, "Lỗi", "File dữ liệu JSON bị lỗi định dạng hoặc đang trống!")
        return
    def confirm_sv(self):

        row = self.tbl_ds_them.rowCount()
        existing_data = {}
        filename="ds_sv.json"
        if os.path.exists(filename):
            try:
                with open(filename, "r", encoding="utf-8") as file:
                    existing_data = json.load(file)
            except json.JSONDecodeError:
                # Bỏ qua nếu file rỗng hoặc lỗi định dạng, khởi tạo lại dictionary rỗng
                existing_data = {}
            for i in range(row):
                ten= self.tbl_ds_them.item(i, 0).text()
                mssv= self.tbl_ds_them.item(i, 1).text()
                lop= self.tbl_ds_them.item(i, 2).text()
                khoa= self.tbl_ds_them.item(i, 3).text()
                gpa= self.tbl_ds_them.item(i, 4).text()
                ngay_them= self.tbl_ds_them.item(i, 5).text()
                existing_data[mssv]={
                    "Tên":ten,
                    "Lớp":lop,
                    "Khoa":khoa,
                    "Gpa":float(gpa),
                    "Ngày thêm":ngay_them
                    }
        with open("ds_sv.json", "w", encoding="utf-8") as file:
            json.dump(existing_data, file, indent=4, ensure_ascii=False)
        QMessageBox.information(self, "Thông báo", "Thêm thành công!")
        self.stackedWidget.hide()
        return