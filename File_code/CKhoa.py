from CLop import Lop
from CSinhVien import SinhVien
class Khoa:
    def __init__(self,ten_khoa):
        self.ds_lop={}
        self.ten_khoa=ten_khoa
    def them_lop(self, lop): #lop là đối tượng (class Lop)
        if lop.ten_lop in self.ds_lop:
            return "Lớp đã tồn tại"
        self.ds_lop[lop.ten_lop] = lop
        return "Thêm lớp thành công"
    def lay_ds_sv(self):  # Lấy ra danh sách các object
        ds_sv_khoa=[]
        for lop in self.ds_lop.values(): # Đọc các lớp
            # ds_sv_khoa.append(i.ds_sv.values())
            for sv in lop.ds_sv.values(): #Đọc các object SinhVien
                ds_sv_khoa.append(sv)
        return ds_sv_khoa
    def ham_sap_xep(self, arr, ham_lay_gia_tri):  # Quick Sort
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
        return self.ham_sap_xep(ds, lambda sv: int(sv.mssv))

    def sap_xep_theo_gpa(self):
        ds = self.lay_ds_sv()
        return self.ham_sap_xep(ds, lambda sv: sv.gpa)
