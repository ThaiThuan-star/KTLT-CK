from quanlysinhvien import QuanLySinhVien, SinhVien

class Khoa:
    def __init__(self, tenkhoa):
        self.tenkhoa = tenkhoa
        self.ds_lop = []

    def cau_tru_du_lieu_khoa(self):
        return {
            "tenkhoa": self.tenkhoa,
            "ds_lop": self.ds_lop
        }


class QuanLyKhoa:
    def __init__(self):
        self.ds_khoa = []
    
    # Quản lý khoa
    def them_khoa(self, tenkhoa):
        for k in self.ds_khoa:
            if k.tenkhoa == tenkhoa:
                return "Khoa đã tồn tại"
        self.ds_khoa.append(Khoa(tenkhoa))
        return "Thêm khoa thành công"

    def tim_khoa(self, tenkhoa):
        for k in self.ds_khoa:
            if k.tenkhoa == tenkhoa:
                return k
        return None

    def xoa_khoa(self, tenkhoa):
        khoa = self.tim_khoa(tenkhoa)
        if not khoa:
            return "Không tìm thấy khoa"
        self.ds_khoa.remove(khoa)
        return "Xóa khoa thành công"

    def hien_thi_khoa(self):
        if not self.ds_khoa:
            return "Chưa có khoa nào"
        result = "Danh sách khoa:\n"
        for khoa in self.ds_khoa:
            result += f"- {khoa.tenkhoa}\n"
        return result
    
    def hien_thi_danh_sach_lop_khoa(self, tenkhoa): #rỗng vì chưa có danh sách sinh viên nào, sau này sẽ sửa lại để hiển thị danh sách sinh viên của lớp đó
        khoa = self.tim_khoa(tenkhoa)
        if not khoa:
            return "Không tìm thấy khoa"
        if not khoa.ds_lop:
            return "Chưa có lớp nào"
        result = f"Danh sách lớp của khoa {tenkhoa}:\n"
        for lop in khoa.ds_lop:
            result += f"- {lop}\n"
        return result
    
    #quản lý lớp học trong khoa
    def tim_lop(self, tenkhoa, tenlop):
        khoa = self.tim_khoa(tenkhoa)
        if not khoa:
            return None
        for lop in khoa.ds_lop:
            if lop == tenlop:
                return lop
        return None

    def them_lop(self, tenkhoa, tenlop):
        khoa = self.tim_khoa(tenkhoa)
        if not khoa:
            return "Không tìm thấy khoa"
        if tenlop in khoa.ds_lop:
            return "Lớp đã tồn tại"
        khoa.ds_lop.append(tenlop)
        return "Thêm lớp thành công"
    
    def xoa_lop(self, tenkhoa, tenlop):
        khoa = self.tim_khoa(tenkhoa)
        if not khoa:
            return "Không tìm thấy khoa"
        if tenlop not in khoa.ds_lop:
            return "Không tìm thấy lớp"
        khoa.ds_lop.remove(tenlop)
        return "Xóa lớp thành công"

    def hien_thi_lop(self, tenkhoa):
        khoa = self.tim_khoa(tenkhoa)
        if not khoa:
            return "Không tìm thấy khoa"
        if not khoa.ds_lop:
            return "Chưa có lớp"
        result = f"Danh sách lớp khoa {tenkhoa}:\n"
        for lop in khoa.ds_lop:
            result += f"- {lop}\n"
        return result
    
    def hien_thi_danh_sach_sinh_vien_lop(self, tenkhoa, tenlop): #rỗng vì chưa có danh sách sinh viên nào, sau này sẽ sửa lại để hiển thị danh sách sinh viên của lớp đó
        khoa = self.tim_khoa(tenkhoa)
        if not khoa:
            return "Không tìm thấy khoa"
        if tenlop not in khoa.ds_lop:
            return "Không tìm thấy lớp"
        qlsv = QuanLySinhVien()
        return qlsv.hien_thi_sinh_vien()


qlk = QuanLyKhoa()

print(qlk.hien_thi_danh_sach_sinh_vien_lop("CNTT","KTPM"))
print(qlk.them_khoa("Công Nghệ Thông Tin"))
print(qlk.them_lop("Công Nghệ Thông Tin", "Kỹ Thuật Phần Mềm"))
print(qlk.them_lop("Công Nghệ Thông Tin", "Mạng Máy Tính"))
print(qlk.hien_thi_lop("Công Nghệ Thông Tin"))
print(qlk.xoa_lop("Công Nghệ Thông Tin", "Mạng Máy Tính"))
print(qlk.hien_thi_lop("Công Nghệ Thông Tin"))
print(qlk.xoa_khoa("Công Nghệ Thông Tin"))
print(qlk.hien_thi_khoa())
print(qlk.hien_thi_danh_sach_sinh_vien_lop("Công Nghệ Thông Tin", "Kỹ Thuật Phần Mềm"))

