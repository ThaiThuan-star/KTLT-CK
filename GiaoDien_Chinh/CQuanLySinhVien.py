from CSinhVien import *
from CLop import *
from CKhoa import *
import json

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

        self.load_json()

    def load_json(self):
        with open("ds_sv.json", "r", encoding="utf-8") as f:
            ds_sv = json.load(f)

        for mssv, data in ds_sv.items():
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
    #Thêm sinh viên theo khoa
    def add_lop(self):
        self.Khoa_HTTT.add_lop(self.ds_lop["416"])
        self.Khoa_TCNH.add_lop(self.ds_lop["417"])

    def update_info(self, lop_hientai, mssv_hientai, ten_moi, mssv_moi, lop_moi, khoa_moi, gpa_moi):

        lop_cu = self.ds_lop[lop_hientai]
        sv = lop_cu.ds_sv[mssv_hientai]

        # nếu không đổi lớp
        if lop_hientai == lop_moi:
            sv.update_info(ten_moi, mssv_moi, lop_hientai, khoa_moi, gpa_moi)

        # nếu đổi lớp
        else:
            lop_cu.xoa_sv(mssv_hientai)
            sv.update_info(ten_moi, mssv_moi, lop_moi, khoa_moi, gpa_moi)

            lop_moi_obj = self.ds_lop[lop_moi]
            lop_moi_obj.them_sv(sv)

    def tim_kiem(self,mssv_tim):
        data = {}
        for lop in self.ds_lop.values():
            for sv in lop.ds_sv.values():
                data[sv.mssv] = {
                    "Tên": sv.ten,
                    "Lớp": sv.lop,
                    "Khoa": sv.khoa,
                    "Gpa": sv.gpa
                }

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