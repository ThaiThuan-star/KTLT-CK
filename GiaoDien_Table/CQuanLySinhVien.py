from CSinhVien import *
from CLop import *
from CKhoa import *
from Functions import *
import json
import os

DATA_FILE= "ds_sv.json"

class QuanLySinhVien:
    def __init__(self):

        # Khởi tạo các class để qly khoa
        self.Khoa_HTTT = Khoa("HTTT")
        self.Khoa_TCNH = Khoa("TCNH")
        self.Khoa_KTDN = Khoa("KTDN")
        self.Khoa_TKT = Khoa("TKT")

        # Khởi tạo các class để qly lớp
        self.ds_lop = {
            "411": Lop("411"),
            "412": Lop("412"),
            "413": Lop("413"),
            "414": Lop("414"),
            "415": Lop("415"),
            "416": Lop("416"),
            "417": Lop("417"),
            "418": Lop("418")
        }
        self.ds_sv={}  #Dùng để save dữ liệu sau cùng lại lên file json
        self.ds_sv_obj={}  #Dùng để xử lý khi cần toàn bộ ds_sv

        self.load_json()
        self.add_lop()

    def load_json(self):
        if not os.path.exists(DATA_FILE):
            return
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                self.ds_sv = json.load(f)
        except json.JSONDecodeError:  #Nếu file json rỗng
            self.ds_sv = {}

        for mssv, data in self.ds_sv.items():
            lop = data["Lớp"]

            if lop in self.ds_lop:
                sv = SinhVien(
                    data["Tên"],
                    mssv,
                    lop,
                    data["Khoa"],
                    data["Gpa"]
                )

                self.ds_lop[lop].them_sv(sv)
                self.ds_sv_obj[mssv] = sv  #Thêm vào ds các obj sinh viên của toàn trường
    #Thêm sinh viên theo khoa
    def add_lop(self):

        self.Khoa_HTTT.them_lop(self.ds_lop["415"])
        self.Khoa_HTTT.them_lop(self.ds_lop["416"])

        self.Khoa_TCNH.them_lop(self.ds_lop["413"])
        self.Khoa_TCNH.them_lop(self.ds_lop["414"])

        self.Khoa_KTDN.them_lop(self.ds_lop["411"])
        self.Khoa_KTDN.them_lop(self.ds_lop["412"])

        self.Khoa_TKT.them_lop(self.ds_lop["417"])
        self.Khoa_TKT.them_lop(self.ds_lop["418"])

    def them_sv(self,ten,mssv,lop,khoa,gpa):
        self.ds_lop[lop].them_sv(SinhVien(ten,mssv,lop,khoa,gpa))

    def xoa_sv(self,mssv,lop):
        self.ds_lop[lop].xoa_sv(mssv)

    def update_info(self, lop_hientai, mssv_hientai, ten_moi, mssv_moi, lop_moi, khoa_moi, gpa_moi):

        lop_cu = self.ds_lop[lop_hientai]
        sv = self.ds_lop[lop_hientai].ds_sv[mssv_hientai]

        # nếu không đổi lớp
        if lop_hientai == lop_moi:
            sv.update_info(ten_moi, mssv_moi, lop_hientai, khoa_moi, gpa_moi)

            # Xóa hẳn đổi tượng cũ, thêm đối tượng mới luôn để đỡ mắc công cập nhật từng thông tin
            del self.ds_lop[lop_hientai].ds_sv[mssv_hientai]
            self.ds_lop[lop_hientai].ds_sv[mssv_moi] = sv

        # nếu đổi lớp mới
        else :
            lop_cu.xoa_sv(mssv_hientai)
            sv.update_info(ten_moi, mssv_moi, lop_moi, khoa_moi, gpa_moi)

            lop_moi_obj = self.ds_lop[lop_moi]
            lop_moi_obj.them_sv(sv)

    def lay_ds_sv(self):
        return list(self.ds_sv_obj.values())

    def ham_sap_xep(self, arr, ham_lay_gia_tri):
        if len(arr) <= 1:
            return arr
        pivot = arr[-1]
        left = []
        for x in arr[:-1]:
            if ham_lay_gia_tri(x) <= ham_lay_gia_tri(pivot):
                left.append(x)
        right = []
        for x in arr[:-1]:
            if ham_lay_gia_tri(x) > ham_lay_gia_tri(pivot):
                right.append(x)

        return self.ham_sap_xep(left, ham_lay_gia_tri) + [pivot] + self.ham_sap_xep(right, ham_lay_gia_tri)

    def sap_xep_theo_mssv(self):
        ds = self.lay_ds_sv()
        return self.ham_sap_xep(ds, lambda sv: sv.mssv)

    def sap_xep_theo_gpa(self):
        ds = self.lay_ds_sv()
        return self.ham_sap_xep(ds, lambda sv: sv.gpa)

    def save_json(self):
        data = {}
        for lop in self.ds_lop.values():
            for sv in lop.ds_sv.values():
                data[sv.mssv] = {
                    "Tên": sv.ten,
                    "Lớp": sv.lop,
                    "Khoa": sv.khoa,
                    "Gpa": sv.gpa
                }

        with open("ds_sv.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)