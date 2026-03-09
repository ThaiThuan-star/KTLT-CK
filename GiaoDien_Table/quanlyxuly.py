from quanlydulieu import khoa,lop,sinhvien, truong

class quanlysinhvien:
    def __init__(self):
        self.truong = truong()
        
    def xep_loai_gpa(self, gpa):
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

   #khoa
    def them_khoa(self,tenkhoa):
        return self.truong.them_khoa(tenkhoa)
    def xoa_khoa(self,tenkhoa):
        return self.truong.xoa_khoa(tenkhoa)
    def tim_khoa(self,tenkhoa):
        return self.truong.tim_khoa(tenkhoa)
    def hien_thi_khoa(self):
        return self.truong.hien_thi_khoa()
    def xap_xep_khoa(self):
        return self.truong.xap_xep_khoa()
    
    #lop
    def them_lop(self, tenkhoa, tenlop):
        k = self.tim_khoa(tenkhoa)
        if not k:
            return "Không tìm thấy khoa"
        return k.them_lop(tenlop)

    def tim_lop(self, tenkhoa, tenlop):
        k = self.tim_khoa(tenkhoa)
        if not k:
            return None
        return k.tim_lop(tenlop)
    
    def hien_thi_lop(self, tenkhoa):
        k = self.tim_khoa(tenkhoa)
        if not k:
            return "Không tìm thấy khoa"
        return k.hien_thi_lop()
    
    def xap_xep_lop(self, tenkhoa):
        return self.truong.xap_xep_lop(tenkhoa)
    
    #sinhvien
    def them_sinh_vien(self, ten, khoa, lop, mssv, gpa):
        k = self.tim_khoa(khoa)
        if not k:
            return "Không tìm thấy khoa"
        l = k.tim_lop(lop)
        if not l:
            return "Không tìm thấy lớp"
        sv = sinhvien(mssv, ten, gpa)               
        return l.them_sinh_vien(sv)
    
    def xoa_sinh_vien(self, mssv):
        return self.truong.xoa_sinh_vien(mssv)

    def sua_sinh_vien(self, mssv, ten=None, tuoi=None, lop=None, gpa=None):
        return self.truong.sua_sinh_vien(mssv, ten, tuoi, lop, gpa)
    def lay_sinh_vien_theo_lop(self, tenlop):
        return self.truong.lay_sinh_vien_theo_lop(tenlop)
    def hien_thi_sinh_vien(self):
        return self.truong.hien_thi_sinh_vien()
    
    #hiển thị
    def hien_thi_sv_lop(self, tenkhoa, tenlop):
        k = self.tim_khoa(tenkhoa)
        if not k:
            return "Không tìm thấy khoa"
        l = k.tim_lop(tenlop)
        if not l:
            return "Không tìm thấy lớp"
        return l.hien_thi_sinh_vien()

    def hien_thi_sv_khoa(self, tenkhoa):
        k = self.tim_khoa(tenkhoa)
        if not k:
            return "Không tìm thấy khoa"
        result = f"Danh sách sinh viên của khoa {tenkhoa}\n"
        for l in k.ds_lop.values():
            for sv in l.ds_sv.values():
                result += f"MSSV: {sv.mssv} | Tên: {sv.ten} | GPA: {sv.gpa} | Xếp loại: {self.xep_loai_gpa(sv.gpa)}\n"
        return result

    def hien_thi_sv_truong(self):
        return self.truong.hien_thi_sinh_vien()
    
    #lấy dữ liệu
    def lay_sv_lop(self, tenkhoa, tenlop):
        k = self.tim_khoa(tenkhoa)
        if not k:
            return []
        l = k.tim_lop(tenlop)
        if not l:
            return []
        return list(l.ds_sv.values())

    def lay_sv_khoa(self, tenkhoa):
        k = self.tim_khoa(tenkhoa)
        if not k:
            return []
        ds = []
        for l in k.ds_lop.values():
            ds.extend(l.ds_sv.values())
        return ds

    def lay_sv_truong(self):
        ds = []
        for k in self.truong.ds_khoa:
            for l in k.ds_lop.values():
                ds.extend(l.ds_sv.values())
        return ds

    #xếp theo mssv:
    def xap_xep_mssv(self, ds_sv=None):
        if ds_sv is None:
            ds_sv = self.lay_sv_truong()
        return sorted(ds_sv, key=lambda sv: sv.mssv)

    
    #xếp theo gpa
    def xap_xep_gpa(self, ds_sv=None):
        if ds_sv is None:
            ds_sv = self.lay_sv_truong()
        return sorted(ds_sv, key=lambda sv: sv.gpa, reverse=True)
    
    #sửa thông tin
    def sua_thong_tin_sinh_vien(self, mssv, ten=None, gpa=None, tenlop = None, tenkhoa = None):
        for k in self.truong.ds_khoa:
            for l in k.ds_lop:
                sv = l.tim_sinh_vien(mssv)
                if sv:
                    if ten:
                        sv.ten = ten
                    if tenlop:
                        sv.lop = tenlop
                    if tenkhoa:
                        sv.khoa = tenkhoa
                    if gpa is not None:
                        sv.gpa = gpa
                    return "Sửa thông tin sinh viên thành công"
        return "Không tìm thấy sinh viên"
    
    #hiển thị danh sách sinh viên đã xếp theo mssv hoặc gpa
    def hien_thi_ds(self, ds):
        if not ds:
            return "Danh sách trống"
        result = ""
        for sv in ds:
            result += f"MSSV: {sv.mssv} | Tên: {sv.ten} | GPA: {sv.gpa} | Xếp loại: {self.xep_loai_gpa(sv.gpa)}\n"
        return result

ql = quanlysinhvien()


# =========================
# TẠO KHOA
# =========================

ql.them_khoa("CNTT")
ql.them_khoa("Kinh Te")

# =========================
# TẠO LỚP
# =========================

ql.them_lop("CNTT", "CTK44")
ql.them_lop("CNTT", "CTK45")

ql.them_lop("Kinh Te", "KTK44")

# =========================
# THÊM SINH VIÊN
# =========================

ql.them_sinh_vien("Nguyen Van A", "CNTT", "CTK44", "SV001", 8.5)
ql.them_sinh_vien("Tran Thi B", "CNTT", "CTK44", "SV002", 7.2)
ql.them_sinh_vien("Le Van C", "CNTT", "CTK44", "SV003", 9.1)

ql.them_sinh_vien("Pham Van D", "CNTT", "CTK45", "SV004", 6.8)
ql.them_sinh_vien("Hoang Thi E", "CNTT", "CTK45", "SV005", 8.0)

ql.them_sinh_vien("Vo Van F", "Kinh Te", "KTK44", "SV006", 7.5)
ql.them_sinh_vien("Do Thi G", "Kinh Te", "KTK44", "SV007", 9.3)

# =========================
# HIỂN THỊ
# =========================

print("===== DANH SÁCH KHOA =====")
print(ql.hien_thi_khoa())

print("\n===== SINH VIÊN LỚP CTK44 =====")
print(ql.hien_thi_sv_lop("CNTT", "CTK44"))

print("\n===== SINH VIÊN KHOA CNTT =====")
print(ql.hien_thi_sv_khoa("CNTT"))

print("\n===== SINH VIÊN TOÀN TRƯỜNG =====")
print(ql.hien_thi_sv_truong())

# =========================
# SẮP XẾP
# =========================

print("\n===== SẮP XẾP SV LỚP CTK44 THEO GPA =====")

ds = ql.lay_sv_lop("CNTT", "CTK44")
ds = ql.xap_xep_gpa(ds)

print(ql.hien_thi_ds(ds))


print("\n===== SẮP XẾP SV KHOA CNTT THEO MSSV =====")

ds = ql.lay_sv_khoa("CNTT")
ds = ql.xap_xep_mssv(ds)

print(ql.hien_thi_ds(ds))


print("\n===== SẮP XẾP TOÀN TRƯỜNG THEO GPA =====")

ds = ql.lay_sv_truong()
ds = ql.xap_xep_gpa(ds)

print(ql.hien_thi_ds(ds))
ql.sua_thong_tin_sinh_vien("SV003", ten="Le Van C Updated", gpa=9.5)


ds = ql.lay_sv_truong()
ds = ql.xap_xep_mssv(ds)

print("\n===== DANH SÁCH SAU KHI SỬA =====")
print(ql.hien_thi_ds(ds))