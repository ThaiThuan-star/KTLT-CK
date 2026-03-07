from CSinhVien import *
from CLop import *
from CKhoa import *
import json

class QuanLySinhVien:
    def __init__(self):
        pass
        self.load_json()

    def load_json(self):

        with open("ds_sv.json", "r", encoding="utf-8") as f:
            ds_sv = json.load(f)

        # Khởi tạo các class để qly khoa
        Khoa_HTTT = Khoa("HTTT")
        Khoa_TCNH = Khoa("TCNH")

        # Khởi tạo các class để qly lớp
        lop_416 = Lop("416")
        lop_417 = Lop("411")
        #Thêm sinh viên theo lớp
        for i,j in ds_sv.items(): #Chỉ chạy các value:
            if j["Lớp"]== "416":
                lop_416.them_sv(SinhVien(j["Tên"],i,j["Lớp"],j["Khoa"],j["Gpa"]))
            elif j["Lớp"]=="417":
                lop_417.them_sv(SinhVien(j["Tên"], i, j["Lớp"], j["Khoa"], j["Gpa"]))
        #Thêm sinh viên theo khoa
        Khoa_HTTT.add_lop(lop_416)
        Khoa_TCNH.add_lop(lop_417)