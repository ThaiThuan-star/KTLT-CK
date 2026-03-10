from CSinhVien import *
class Lop:
    def __init__(self,ten_lop):
        self.ds_sv={}
        self.ten_lop=ten_lop
    def them_sv(self,sv):
        if sv.mssv not in self.ds_sv:
            self.ds_sv[sv.mssv] = sv
            return True
        else:
            print(f"Sinh viên có MSSV {sv.mssv} đã tồn tại")
            return False
    def xoa_sv(self, mssv):
        if mssv in self.ds_sv:
            del self.ds_sv[mssv]
            return True
        else:
            print(f"Không tìm thấy sinh viên có MSSV {mssv}")
            return False
    def ten(self):
        return self.ten_lop

    def lay_ds_sv(self):
        return list(self.ds_sv.values())

    def tim_kiem_nhi_phan(self, mssv):
        ds_sorted = self.sap_xep_theo_mssv()  # lấy danh sách đã sắp xếp theo MSSV
        left, right = 0, len(ds_sorted) - 1
        while left <= right:
            mid = (left + right) // 2
            if ds_sorted[mid].mssv == mssv:
                return ds_sorted[mid]
            elif ds_sorted[mid].mssv < mssv:
                left = mid + 1
            else:
                right = mid - 1
        print(f"Không tìm thấy sinh viên có MSSV {mssv}")
        return None

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
    print(lop_416.sap_xep_theo_gpa())
    print(lop_416.sap_xep_theo_mssv())