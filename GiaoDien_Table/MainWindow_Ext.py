from PyQt6.QtWidgets import QTableWidgetItem,QMessageBox,QMainWindow,QHeaderView

from MainWindow import Ui_MainWindow
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

        self.tbl_ds_them.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch) #Căn chỉnh bảng
        # Khởi tạo đối tượng quản lý (Tự động load JSON và phân khoa/lớp)
        self.qly=QuanLySinhVien()

        self.tbl_ds_them.itemClicked.connect(self.hien_thi_thong_tin)
        self.btn_clear.clicked.connect(self.clear_input)

        self.process()

        self.cb_loc_khoa.currentTextChanged.connect(self.loc_lop)
        self.comboBox.currentTextChanged.connect(self.phatsinh)

    def closeEvent(self, event):
        try:
            self.qly.save_json()
            QMessageBox.information(self, "Thông báo", "Đã lưu dữ liệu thành công")
        except:
            QMessageBox.warning(self, "Cảnh báo", "Lưu dữ liệu không thành công")

        event.accept()

    def process(self):
        """ Hiển thị danh sách sinh viên"""
        # Xóa trắng bảng trước khi bỏ dữ liệu vào ==> tránh trùng lặp
        self.tbl_ds_them.setRowCount(0)

        # Dựa vào class qly, lặp qua tất cả các lớp và sinh viên để đưa lên bảng
        for lop in self.qly.ds_lop.values():
            for sv in lop.ds_sv.values():
                row = self.tbl_ds_them.rowCount()
                self.tbl_ds_them.insertRow(row)

                # Nạp thông tin từ đối tượng SinhVien (sv) lên Table
                self.tbl_ds_them.setItem(row, 0, QTableWidgetItem(sv.mssv))
                self.tbl_ds_them.setItem(row, 1, QTableWidgetItem(sv.ten))
                self.tbl_ds_them.setItem(row, 2, QTableWidgetItem(sv.lop))
                self.tbl_ds_them.setItem(row, 3, QTableWidgetItem(sv.khoa))
                self.tbl_ds_them.setItem(row, 4, QTableWidgetItem(str(sv.gpa)))

        self.btn_delete_sv.clicked.connect(self.delete_sv)
        self.btn_add_sv.clicked.connect(self.add_sv)
        self.btn_edit_sv.clicked.connect(self.edit_sv)
        self.btn_loc.clicked.connect(self.loc_sv)
        self.btn_search.clicked.connect(self.search_sv)

    def loc_lop(self):
        self.cb_loc_lop.setCurrentIndex(0)
        khoa=self.cb_loc_khoa.currentText()
        view=self.cb_loc_lop.view() #Lấy danh sách hiển thị của comboBox : 411,412,413...

        # hiện lại toàn bộ lớp trước
        for i in range(self.cb_loc_lop.count()):
            view.setRowHidden(i, False)

        if khoa=="Tất cả Khoa":
            pass
        if khoa=="Hệ thống thông tin":
            view.setRowHidden(1, True)
            view.setRowHidden(2, True)
            view.setRowHidden(3, True)
            view.setRowHidden(4, True)
            view.setRowHidden(7, True)
            view.setRowHidden(8, True)
        if khoa=="Kinh tế đối ngoại":
            view.setRowHidden(3, True)
            view.setRowHidden(4, True)
            view.setRowHidden(5, True)
            view.setRowHidden(6, True)
            view.setRowHidden(7, True)
            view.setRowHidden(8, True)
        if khoa=="Tài chính ngân hàng":
            view.setRowHidden(1, True)
            view.setRowHidden(2, True)
            view.setRowHidden(5, True)
            view.setRowHidden(6, True)
            view.setRowHidden(7, True)
            view.setRowHidden(8, True)
        if khoa =="Toán kinh tế":
            view.setRowHidden(1, True)
            view.setRowHidden(2, True)
            view.setRowHidden(3, True)
            view.setRowHidden(4, True)
            view.setRowHidden(5, True)
            view.setRowHidden(6, True)

    def add_sv(self):
        ten = self.txt_ho_ten.text().strip()
        mssv = self.txt_mssv.text().strip()
        lop = self.box_lop.currentText().strip()
        gpa = self.txt_gpa.text().strip()
        khoa = self.comboBox.currentText().strip()
        if (not self.txt_ho_ten.text() or not self.txt_gpa.text()
              or not self.txt_mssv.text() or self.box_lop.currentText()=="Lớp"
                or self.comboBox.currentText()=="Khoa" ) :
            QMessageBox.warning(self, "Lỗi nhập liệu", "Nhập thiếu dữ liệu")
            return
        try:
            kt_gpa=float(gpa) #Phải tách biệt ra riêng vì QTable chỉ nhận str
            kt_mssv=int(mssv)
        except ValueError:
            QMessageBox.warning(self, "Lỗi", "GPA và MSSV phải là số")
            return

        #Kiểm tra xem sinh viên đã có trong ds chưa
        if mssv in self.qly.ds_sv:
            QMessageBox.warning(self, "Lỗi", "Sinh viên đã tồn tại")
            return

        """Set thông tin vào bảng"""

        # Đếm số dòng hiện tại
        row = self.tbl_ds_them.rowCount()

        # Thêm dòng mới dựa trên số dòng vì chỉ số dòng bắt đầu từ 0
        self.tbl_ds_them.insertRow(row)

        # Set dữ liệu đúng cột
        # Phải dùng QTableWidgetItem vì các ô không chỉ chứa vban mà còn chứa nhiều dl như font-size,...

        self.tbl_ds_them.setItem(row, 0, QTableWidgetItem(mssv))
        self.tbl_ds_them.setItem(row, 1, QTableWidgetItem(ten))
        self.tbl_ds_them.setItem(row, 2, QTableWidgetItem(lop))
        self.tbl_ds_them.setItem(row, 3, QTableWidgetItem(khoa))
        self.tbl_ds_them.setItem(row, 4, QTableWidgetItem(gpa))

        QMessageBox.information(self, "Thông báo", "Thêm thành công!")

        """LƯU THAY ĐỔI"""
        #Ghi thay đổi vào ds_sv và ds_sv_obj của CQuanLySinhVien
        self.qly.ds_sv[mssv] = {"Tên":ten,"Lớp":lop,"Khoa":khoa,"Gpa":float(gpa)}

        #Ghi thay đổi vào đối tượng Lop
        self.qly.them_sv(ten,mssv,lop,khoa,gpa)

        #Ghi thay đổi vào hàm lưu sv dưới dạng obj
        self.qly.ds_sv_obj[mssv]=SinhVien(ten,mssv,lop,khoa,gpa)

        self.clear_input()
        return
    def clear_input(self):
        self.txt_ho_ten.setText("")
        self.txt_mssv.setText("")
        self.txt_gpa.setText("")

    def delete_sv(self):

        row = self.tbl_ds_them.currentRow()
        if row == -1:
            QMessageBox.warning(self, "Thông báo", "Hãy chọn sinh viên cần xóa")
            return

        mssv = self.tbl_ds_them.item(row, 0).text()
        lop = self.tbl_ds_them.item(row, 2).text()

        reply = QMessageBox.question(
            self,
            "Xác nhận xóa",
            f"Bạn có chắc muốn xóa sinh viên {mssv} ?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if reply == QMessageBox.StandardButton.Yes:

            # xóa trong bảng
            self.tbl_ds_them.removeRow(row)
            QMessageBox.information(self, "Thông báo", "Đã xóa sinh viên")

            """LƯU THAY ĐỔI TRONG DỮ LIỆU"""

            # Ghi thay đổi vào đối tượng QuanLySinhVien
            del self.qly.ds_sv[mssv]

            # Ghi thay đổi vào đối tượng QuanLySinhVien
            del self.qly.ds_sv_obj[mssv]

            # Ghi thay đổi vào đối tượng Lop
            self.qly.xoa_sv(mssv,lop)

            return
    def edit_sv(self):
        row = self.tbl_ds_them.currentRow()
        lop_hien_tai=self.tbl_ds_them.item(row, 2).text()
        mssv_hientai=self.tbl_ds_them.item(row, 0).text()

        ten_moi=self.txt_ho_ten.text()
        mssv_moi=self.txt_mssv.text()
        lop_moi=self.box_lop.currentText()
        khoa_moi=self.comboBox.currentText()
        gpa_moi=self.txt_gpa.text()

        #set lại trên table
        if (not self.txt_ho_ten.text() or not self.txt_gpa.text()
              or not self.txt_mssv.text() or self.box_lop.currentText()=="Lớp"
                or self.comboBox.currentText()=="Khoa" ) :
            QMessageBox.warning(self, "Lỗi nhập liệu", "Nhập thiếu dữ liệu")
            return
        try:
            kt_gpa=float(gpa_moi) #Phải tách biệt ra riêng vì QTable chỉ nhận str
            kt_mssv=int(mssv_moi)
        except ValueError:
            QMessageBox.warning(self, "Lỗi", "GPA và MSSV phải là số")
            return

        #Kiểm tra xem sinh viên đã có trùng không
        if mssv_moi != mssv_hientai:
            if mssv_moi in self.qly.ds_sv:
                QMessageBox.warning(self, "Lỗi", "MSSV đã tồn tại")
                return

        self.tbl_ds_them.setItem(row, 0, QTableWidgetItem(mssv_moi))
        self.tbl_ds_them.setItem(row, 1, QTableWidgetItem(ten_moi))
        self.tbl_ds_them.setItem(row, 2, QTableWidgetItem(lop_moi))
        self.tbl_ds_them.setItem(row, 3, QTableWidgetItem(khoa_moi))
        self.tbl_ds_them.setItem(row, 4, QTableWidgetItem(gpa_moi))

        QMessageBox.information(self,"Thông báo", "Cập nhật thành công")
        self.clear_input()

        #Thay đổi trong đối tượng Lop
        self.qly.update_info(lop_hien_tai,mssv_hientai, ten_moi, mssv_moi, lop_moi, khoa_moi, gpa_moi)

        #Thay đổi trong đối tượng QuanLySinhVien
        #Xóa cái cũ thêm cái mới để đỡ mắc công chỉnh
        del self.qly.ds_sv[mssv_hientai]
        del self.qly.ds_sv_obj[mssv_hientai]

        self.qly.ds_sv[mssv_moi]={"Tên":ten_moi,"Lớp":lop_moi,"Khoa":khoa_moi,"Gpa":float(gpa_moi)}
        self.qly.ds_sv_obj[mssv_moi]=SinhVien(ten_moi,mssv_moi,lop_moi,khoa_moi,gpa_moi)

    def hien_thi_thong_tin(self):
        # 1. Lấy vị trí dòng (row) đang được người dùng click
        row = self.tbl_ds_them.currentRow()

        # Nếu chưa chọn dòng nào hợp lệ thì bỏ qua
        if row < 0:
            return

        # Lấy nội dung từng cột trong dòng đó
        mssv = self.tbl_ds_them.item(row, 0).text()
        ten = self.tbl_ds_them.item(row, 1).text()
        lop = self.tbl_ds_them.item(row, 2).text()
        khoa = self.tbl_ds_them.item(row, 3).text()
        gpa = self.tbl_ds_them.item(row, 4).text()

        # Đẩy dữ liệu lên các ô TextBox
        self.txt_mssv.setText(mssv)
        self.txt_ho_ten.setText(ten)
        self.txt_gpa.setText(gpa)

        # Đẩy dữ liệu lên ComboBox Khoa
        self.comboBox.setCurrentText(khoa)
        self.box_lop.setCurrentText(lop)

    def phatsinh(self):
        self.box_lop.setCurrentIndex(0)
        khoa = self.comboBox.currentText()
        view = self.box_lop.view()  # Lấy danh sách hiển thị của comboBox : 411,412,413...
        # hiện lại toàn bộ lớp trước
        for i in range(self.box_lop.count()):
            view.setRowHidden(i, False)

        if khoa == "Khoa":
            pass
        if khoa == "Hệ thống thông tin":
            view.setRowHidden(1, True)
            view.setRowHidden(2, True)
            view.setRowHidden(3, True)
            view.setRowHidden(4, True)
            view.setRowHidden(7, True)
            view.setRowHidden(8, True)
        if khoa == "Kinh tế đối ngoại":
            view.setRowHidden(3, True)
            view.setRowHidden(4, True)
            view.setRowHidden(5, True)
            view.setRowHidden(6, True)
            view.setRowHidden(7, True)
            view.setRowHidden(8, True)
        if khoa == "Tài chính ngân hàng":
            view.setRowHidden(1, True)
            view.setRowHidden(2, True)
            view.setRowHidden(5, True)
            view.setRowHidden(6, True)
            view.setRowHidden(7, True)
            view.setRowHidden(8, True)
        if khoa == "Toán kinh tế":
            view.setRowHidden(1, True)
            view.setRowHidden(2, True)
            view.setRowHidden(3, True)
            view.setRowHidden(4, True)
            view.setRowHidden(5, True)
            view.setRowHidden(6, True)

    def loc_sv(self):
        # 1. Lấy giá trị người dùng đang chọn ở các ô ComboBox
        khoa_chon = self.cb_loc_khoa.currentText().strip()
        lop_chon = self.cb_loc_lop.currentText().strip()
        tieu_chi = self.cb_loc_GPA.currentText().strip()

        # 2. Xóa trắng bảng trước khi hiển thị kết quả lọc
        self.tbl_ds_them.setRowCount(0)

        #Xét các trường hợp để sắp xếp
        if khoa_chon == "Tất cả Khoa" and lop_chon=="Tất cả Lớp":
            if tieu_chi=="Xếp theo GPA":
                danh_sach_loc=(self.qly.sap_xep_theo_gpa())
            elif tieu_chi=="Xếp theo MSSV":
                danh_sach_loc = (self.qly.sap_xep_theo_mssv())
            elif tieu_chi=="Thêm":
                danh_sach_loc=[x for x in self.qly.ds_sv_obj.values()]
        elif lop_chon !="Tất cả Lớp":
            if tieu_chi=="Xếp theo GPA":
                danh_sach_loc=self.qly.ds_lop[lop_chon].sap_xep_theo_gpa()
            elif tieu_chi=="Xếp theo MSSV":
                danh_sach_loc = self.qly.ds_lop[lop_chon].sap_xep_theo_mssv()
            elif tieu_chi == "Thêm":
                danh_sach_loc=self.qly.ds_lop[lop_chon].lay_ds_sv()
        elif lop_chon=="Tất cả Lớp":
            if khoa_chon=="Hệ thống thông tin":
                if tieu_chi=="Xếp theo GPA":
                    danh_sach_loc=self.qly.Khoa_HTTT.sap_xep_theo_gpa()
                elif tieu_chi=="Xếp theo MSSV":
                    danh_sach_loc=self.qly.Khoa_HTTT.sap_xep_theo_mssv()
                elif tieu_chi == "Thêm":
                    danh_sach_loc= self.qly.Khoa_HTTT.lay_ds_sv()
            elif khoa_chon=="Kinh tế đối ngoại":
                if tieu_chi=="Xếp theo GPA":
                    danh_sach_loc=self.qly.Khoa_KTDN.sap_xep_theo_gpa()
                elif tieu_chi=="Xếp theo MSSV":
                    danh_sach_loc=self.qly.Khoa_KTDN.sap_xep_theo_mssv()
                elif tieu_chi == "Thêm":
                    danh_sach_loc= self.qly.Khoa_KTDN.lay_ds_sv()
            elif khoa_chon=="Tài chính ngân hàng":
                if tieu_chi=="Xếp theo GPA":
                    danh_sach_loc=self.qly.Khoa_TCNH.sap_xep_theo_gpa()
                elif tieu_chi=="Xếp theo MSSV":
                    danh_sach_loc=self.qly.Khoa_TCNH.sap_xep_theo_mssv()
                elif tieu_chi == "Thêm":
                    danh_sach_loc= self.qly.Khoa_TCNH.lay_ds_sv()
            else:
                if tieu_chi=="Xếp theo GPA":
                    danh_sach_loc=self.qly.Khoa_TKT.sap_xep_theo_gpa()
                elif tieu_chi=="Xếp theo MSSV":
                    danh_sach_loc=self.qly.Khoa_TKT.sap_xep_theo_mssv()
                elif tieu_chi == "Thêm":
                    danh_sach_loc= self.qly.Khoa_TKT.lay_ds_sv()

        # 6. IN DANH SÁCH LÊN BẢNG
        for sv in danh_sach_loc:
            row = self.tbl_ds_them.rowCount()
            self.tbl_ds_them.insertRow(row)   #Thêm hàng dựa vào chỉ số

            # Nạp thông tin lên các ô của bảng
            self.tbl_ds_them.setItem(row, 0, QTableWidgetItem(sv.mssv))
            self.tbl_ds_them.setItem(row, 1, QTableWidgetItem(sv.ten))
            self.tbl_ds_them.setItem(row, 2, QTableWidgetItem(sv.lop))
            self.tbl_ds_them.setItem(row, 3, QTableWidgetItem(sv.khoa))
            self.tbl_ds_them.setItem(row, 4, QTableWidgetItem(str(sv.gpa)))
    def search_sv(self):
        mssv_tim_kiem=self.txt_search.text().strip()
        ds_mssv=[]
        for i in self.qly.ds_sv.keys():
            ds_mssv.append(i)

        #Phần này áp dụng kiến thức về thuật toán tìm kiếm
        if Binary_Search(ds_mssv,mssv_tim_kiem):
            self.txt_ho_ten.setText(str(self.qly.ds_sv[mssv_tim_kiem]["Tên"]))
            self.txt_mssv.setText(str(mssv_tim_kiem))
            self.txt_gpa.setText(str(self.qly.ds_sv[mssv_tim_kiem]["Gpa"]))
            self.box_lop.setCurrentText(str(self.qly.ds_sv[mssv_tim_kiem]["Lớp"]))
            self.comboBox.setCurrentText(str(self.qly.ds_sv[mssv_tim_kiem]["Khoa"]))
        else:
            QMessageBox.warning(self, "Lỗi", "Không tìm thấy sinh viên")

