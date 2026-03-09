class sinhvien:
    def __init__(self, mssv, ten, gpa):
        self.mssv = mssv
        self.ten = ten
        self.gpa = gpa

class lop:
    def __init__(self, tenlop):
        self.ten_lop = tenlop
        self.ds_sv = {}

    def them_sinh_vien(self, sv):
        if sv.mssv in self.ds_sv:
            return "MSSV đã tồn tại"
        self.ds_sv[sv.mssv] = sv
        return "Thêm sinh viên thành công"
    
    def xoa_sinh_vien(self, mssv):
        if mssv not in self.ds_sv:
            return "Không tìm thấy sinh viên"
        del self.ds_sv[mssv]
        return "Xóa sinh viên thành công"
    
    def xap_xep_sinh_vien(self, ds_sv = None):
        if ds_sv is None:
            ds_sv = list(self.ds_sv.values())
        if len(ds_sv) <= 1:
            return ds_sv
        pivot = ds_sv[len(ds_sv) // 2]
        trai = [x for x in ds_sv if x.mssv.lower() < pivot.mssv.lower()]
        giua = [x for x in ds_sv if x.mssv.lower() == pivot.mssv.lower()]
        phai = [x for x in ds_sv if x.mssv.lower() > pivot.mssv.lower()]
        return self.xap_xep_sinh_vien(trai) + giua + self.xap_xep_sinh_vien(phai)
    
    def tim_sinh_vien(self, mssv):
        return self.ds_sv.get(mssv, None)
    
    def hien_thi_sinh_vien(self):
        if not self.ds_sv:
            return "Chưa có sinh viên nào"
        result = f"Danh sách sinh viên của lớp {self.ten_lop}:\n"
        for sv in self.ds_sv.values():
            result += f"- MSSV: {sv.mssv}, Tên: {sv.ten}\n"
        return result

class khoa:
    def __init__(self, tenkhoa):
        self.tenkhoa = tenkhoa
        self.ds_lop = {}

    def them_lop(self, tenlop):
        if tenlop in self.ds_lop:
            return "Lớp đã tồn tại"
        self.ds_lop[tenlop] = lop(tenlop)
        return "Thêm lớp thành công"
    
    def xoa_lop(self, tenlop):
        if tenlop not in self.ds_lop:
            return "Không tìm thấy lớp"
        del self.ds_lop[tenlop]
        return "Xóa lớp thành công"
    
    def xap_xep_lop(self, ds_lop = None):
        if ds_lop is None:
            ds_lop = list(self.ds_lop.values())
        if len(ds_lop) <= 1:
            return ds_lop
        pivot = ds_lop[len(ds_lop) // 2]
        trai = [x for x in ds_lop if x.ten_lop.lower() < pivot.ten_lop.lower()]
        giua = [x for x in ds_lop if x.ten_lop.lower() == pivot.ten_lop.lower()]
        phai = [x for x in ds_lop if x.ten_lop.lower() > pivot.ten_lop.lower()]
        return self.xap_xep_lop(trai) + giua + self.xap_xep_lop(phai)
    
    def tim_lop(self, tenlop):
        return self.ds_lop.get(tenlop, None)
    
    def hien_thi_lop(self):
        if not self.ds_lop:
            return "Chưa có lớp nào"
        result = f"Danh sách lớp của khoa {self.tenkhoa}:\n"
        for lop in self.ds_lop.values():
            result += f"- {lop.ten_lop}\n"
        return result
    
class truong:
    def __init__(self):
        self.ds_khoa = []

    def them_khoa(self, tenkhoa):
        if any(khoa.tenkhoa == tenkhoa for khoa in self.ds_khoa):
            return "Khoa đã tồn tại"
        self.ds_khoa.append(khoa(tenkhoa))
        return "Thêm khoa thành công"
    
    def xoa_khoa(self, tenkhoa):
        khoa = self.tim_khoa(tenkhoa)
        if not khoa:
            return "Không tìm thấy khoa"
        self.ds_khoa.remove(khoa)
        return "Xóa khoa thành công"
    
    def tim_khoa(self, tenkhoa):
        for khoa in self.ds_khoa:
            if khoa.tenkhoa == tenkhoa:
                return khoa
        return None
    
    def hien_thi_khoa(self):
        if not self.ds_khoa:
            return "Chưa có khoa nào"
        result = "Danh sách khoa:\n"
        for khoa in self.ds_khoa:
            result += f"- {khoa.tenkhoa}\n"
        return result
    
    def xap_xep_khoa(self, ds_khoa = None):
        if ds_khoa is None:
            ds_khoa = self.ds_khoa
        if len(ds_khoa) <= 1:
            return ds_khoa
        pivot = ds_khoa[len(ds_khoa) // 2]
        trai = [x for x in ds_khoa if x.tenkhoa.lower() < pivot.tenkhoa.lower()]
        giua = [x for x in ds_khoa if x.tenkhoa.lower() == pivot.tenkhoa.lower()]
        phai = [x for x in ds_khoa if x.tenkhoa.lower() > pivot.tenkhoa.lower()]
        return self.xap_xep_khoa(trai) + giua + self.xap_xep_khoa(phai)
    
    def xap_xep_sinh_vien(self):
        danh_sach_tong_hop = []
        for khoa in self.ds_khoa:
            for lop in khoa.ds_lop.values():
                for sv in lop.ds_sv.values():
                    thong_tin = {
                        "mssv": sv.mssv,
                        "ten": sv.ten,
                        "lop": lop.ten_lop,
                        "khoa": khoa.tenkhoa
                    }
                    danh_sach_tong_hop.append(thong_tin)
        danh_sach_tong_hop.sort(key=lambda x: x["mssv"].lower())
        return danh_sach_tong_hop
    
    def hien_thi_sinh_vien(self):
        danh_sach_tong_hop = self.xap_xep_sinh_vien()
        if not danh_sach_tong_hop:
            return "Chưa có sinh viên nào"
        result = "Danh sách sinh viên:\n"
        for sv in danh_sach_tong_hop:
            result += f"- MSSV: {sv['mssv']}, Tên: {sv['ten']}, Lớp: {sv['lop']}, Khoa: {sv['khoa']}\n"
        return result
    

    
