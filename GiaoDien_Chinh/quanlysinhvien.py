class SinhVien:
    def __init__(self, ten, lop, mssv, gpa):
        self.ten = ten
        self.lop = lop
        self.mssv = mssv
        self.gpa = gpa
        self.xep_loai = None
    def xep_loai_sinh_vien(self, gpa):
        if gpa >= 9.0:
            return "Xuất Sắc"
        elif gpa >= 8.0:
            return "Giỏi"
        elif gpa >= 7.0:
            return "Khá"
        elif gpa >= 5.0:
            return "Trung Bình"
        else:
            return "Yếu"
    def sua_sinh_vien(self, mssv, ten=None, tuoi=None, lop=None, gpa=None):
        for sv in self.sinhvien:
            if sv.mssv == mssv:
                if ten:
                    sv.ten = ten
                if tuoi:
                    sv.tuoi = tuoi
                if lop:
                    sv.lop = lop
                if gpa is not None:
                    sv.gpa = gpa
                    sv.xep_loai = self.xep_loai_sinh_vien(gpa)
                return "Sửa Sinh Viên Thành Công"
        return "Không Tìm Thấy Sinh Viên"



class QuanLySinhVien:
    def __init__(self):
        self.sinhvien = []

    def kiem_tra_mssv(self, mssv):
        for sv in self.sinhvien:
            if sv.mssv == mssv:
                return True
        return False

    def xep_loai_sinh_vien(self, gpa):
        if gpa >= 9.0:
            return "Xuất Sắc"
        elif gpa >= 8.0:
            return "Giỏi"
        elif gpa >= 7.0:
            return "Khá"
        elif gpa >= 5.0:
            return "Trung Bình"
        else:
            return "Yếu"

    def them_sinh_vien(self, ten, tuoi, lop, mssv, gpa):
        for sv in self.sinhvien:
            if sv.mssv == mssv:
                return "MSSV đã tồn tại"
        sv = SinhVien(ten, tuoi, lop, mssv, gpa)
        sv.xep_loai = self.xep_loai_sinh_vien(gpa)
        self.sinhvien.append(sv)
        return "Thêm Sinh Viên Thành Công"

    def xoa_sinh_vien(self, mssv):
        for sv in self.sinhvien:
            if sv.mssv == mssv:
                self.sinhvien.remove(sv)
                return "Xóa Sinh Viên Thành Công"
        return "Không Tìm Thấy Sinh Viên"

    def sua_sinh_vien(self, mssv, ten=None, tuoi=None, lop=None, gpa=None):
        for sv in self.sinhvien:
            if sv.mssv == mssv:
                if ten:
                    sv.ten = ten
                if tuoi:
                    sv.tuoi = tuoi
                if lop:
                    sv.lop = lop
                if gpa is not None:
                    sv.gpa = gpa
                    sv.xep_loai = self.xep_loai_sinh_vien(gpa)
                return "Sửa Sinh Viên Thành Công"
        return "Không Tìm Thấy Sinh Viên"

    def hien_thi_sinh_vien(self):
        if not self.sinhvien:
            return "Chưa Có Sinh Viên Nào"
        result = "Danh Sách Sinh Viên:\n"
        for sv in self.sinhvien:
            result += (
                f"MSSV: {sv.mssv}, "
                f"Tên: {sv.ten}, "
                f"Tuổi: {sv.tuoi}, "
                f"Lớp: {sv.lop}, "
                f"GPA: {sv.gpa}, "
                f"Xếp Loại: {sv.xep_loai}\n"
            )
        return result


qlsv = QuanLySinhVien()
print(qlsv.them_sinh_vien("Nguyen Van A", 20, "CNTT", "SV001", 10))
print(qlsv.hien_thi_sinh_vien())
print(qlsv.sua_sinh_vien("SV001", gpa=8.5))
print(qlsv.hien_thi_sinh_vien())