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
        return self.ham_sap_xep(ds, lambda sv: sv.mssv)

    def sap_xep_theo_gpa(self):
        ds = self.lay_ds_sv()
        return self.ham_sap_xep(ds, lambda sv: sv.gpa)
if __name__ == '__main__':
    sv1 = SinhVien("Thái Thuận", "1799", "416", "HTTT", 4)
    sv2 = SinhVien("Đạt", "1800", "416", "HTTT", 1)
    sv3 = SinhVien("Dũng", "1801", "416", "HTTT", 2)
    sv4 = SinhVien("Lâm", "1802", "416", "HTTT", 3)
    sv5 = SinhVien("Khang", "1804", "416", "HTTT", 5)
    lop_416 = Lop("416")
    lop_416.them_sv(sv1)
    lop_416.them_sv(sv2)
    lop_416.them_sv(sv3)
    lop_416.them_sv(sv4)
    lop_416.them_sv(sv5)
    # print(lop_416.sap_xep_theo_gpa())
    # print(lop_416.sap_xep_theo_mssv())

    sv6 = SinhVien("A ", "1799", "416", "HTTT", 4)
    sv7 = SinhVien("B", "1800", "416", "HTTT", 1)
    sv8 = SinhVien("C", "1801", "416", "HTTT", 2)
    sv9 = SinhVien("D", "1802", "416", "HTTT", 3)
    sv10 = SinhVien("E", "1804", "416", "HTTT", 5)
    lop_417 = Lop("417")
    lop_417.them_sv(sv6)
    lop_417.them_sv(sv7)
    lop_417.them_sv(sv8)
    lop_417.them_sv(sv9)
    lop_417.them_sv(sv10)
    # print(lop_417.sap_xep_theo_gpa())
    # print(lop_417.sap_xep_theo_mssv())

    khoa=Khoa("HTTT")
    khoa.them_lop(lop_417)
    khoa.them_lop(lop_416)

    print(khoa.lay_ds_sv())

    print(khoa.sap_xep_theo_gpa())
    print(khoa.sap_xep_theo_mssv())