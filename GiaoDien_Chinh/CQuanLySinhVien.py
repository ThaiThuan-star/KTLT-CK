from CSinhVien import *
from CLop import *
from CKhoa import *
import json

class QuanLySinhVien:
    def __init__(self):

        # Khởi tạo các class để qly khoa
        self.Khoa_HTTT = Khoa("HTTT")
        self.Khoa_TCNH = Khoa("TCNH")

        # Khởi tạo các class để qly lớp
        self.lop_416 = Lop("416")
        self.lop_417 = Lop("417")

        self.load_json()

    def load_json(self):
        ds_sv={}
        with open("ds_sv.json", "r", encoding="utf-8") as f:
            ds_sv = json.load(f)

        #Thêm sinh viên theo lớp
        for i,j in ds_sv.items(): #Chỉ chạy các value:
            if j["Lớp"]== "416":
                self.lop_416.them_sv(SinhVien(j["Tên"],i,j["Lớp"],j["Khoa"],j["Gpa"]))
            elif j["Lớp"]=="417":
                self.lop_417.them_sv(SinhVien(j["Tên"], i, j["Lớp"], j["Khoa"], j["Gpa"]))

    #Thêm sinh viên theo khoa
    def add_lop(self):
        self.Khoa_HTTT.add_lop(self.lop_416)
        self.Khoa_TCNH.add_lop(self.lop_417)

    def update_info(self,lop_hientai,mssv_hientai,ten_moi,mssv_moi,lop_moi,khoa_moi,gpa_moi):
        if lop_hientai== lop_moi:
            if lop_hientai == "416":
                self.lop_416.ds_sv[mssv_hientai].update_info(ten_moi,mssv_moi,lop_moi,khoa_moi,gpa_moi)
            elif lop_hientai == "417":
                self.lop_417.ds_sv[mssv_hientai].update_info(ten_moi, mssv_moi, lop_moi, khoa_moi, gpa_moi)
        else:
            if lop_hientai == "416":
                self.lop_416.xoa_sv(mssv_hientai)
                if lop_moi=="417":
                    self.lop_417.ds_sv[mssv_hientai].update_info(ten_moi, mssv_moi, lop_moi, khoa_moi, gpa_moi)

            elif lop_hientai == "417":
                self.lop_417.xoa_sv(mssv_hientai)
                if lop_moi=="416":
                    self.lop_416.ds_sv[mssv_hientai].update_info(ten_moi, mssv_moi, lop_moi, khoa_moi, gpa_moi)

    def save_json(self):

        data = {}

        for lop in [self.lop_416, self.lop_417]:
            for sv in lop.ds_sv.values():
                data[sv.mssv] = {
                    "Tên": sv.ten,
                    "Lớp": sv.lop,
                    "Khoa": sv.khoa,
                    "Gpa": sv.gpa
                }

        with open("ds_sv.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)