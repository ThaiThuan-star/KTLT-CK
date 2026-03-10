class SinhVien:
    def __init__(self, ten, mssv, lop, khoa, gpa):
        self.ten = ten
        self.mssv = mssv
        self.lop = lop
        self.khoa = khoa
        self.gpa = gpa

    def cap_nhat_thong_tin(self, ten_moi, mssv_moi, lop_moi, khoa_moi, gpa_moi):
        self.ten = ten_moi
        self.mssv = mssv_moi
        self.lop = lop_moi
        self.khoa = khoa_moi
        self.gpa = float(gpa_moi)

    def __str__(self):
        return f"{self.ten} - {self.mssv} - Lớp: {self.lop} - Khoa: {self.khoa} - GPA: {self.gpa} - Xếp loại: {self.xep_loai()}"

class Lop:
    def __init__(self, ten_lop):
        self.ten_lop = ten_lop
        self.ds_sv = {}

    def them_sv(self, sv):
        if sv.mssv not in self.ds_sv:
            self.ds_sv[sv.mssv] = sv
            return True
        else:
            print(f"Sinh viên có MSSV {sv.mssv} đã tồn tại")
            return False
    """ CHỈ GIỮ LẠI Ở CLASS SINHVIEN, CÁC THAO TÁC SẼ ĐƯA QUA CLASS QUANLYSINHVIEN """
    def sua_sv(self, mssv, ten_moi=None, mssv_moi=None, lop_moi=None, khoa_moi=None, gpa_moi=None):
        if mssv in self.ds_sv:
            self.ds_sv[mssv].cap_nhat_thong_tin(ten_moi=ten_moi, mssv_moi=mssv_moi,lop_moi=lop_moi, khoa_moi=khoa_moi, gpa_moi=gpa_moi)
            return True
        else:
            print(f"Không tìm thấy sinh viên có MSSV {mssv}")
            return False
    def xoa_sv(self, mssv):
        if mssv in self.ds_sv:
            del self.ds_sv[mssv]
            return True
        else:
            print(f"Không tìm thấy sinh viên có MSSV {mssv}")
            return False

    # def lay_ds_sv(self):
    #     return list(self.ds_sv.values())

    def lay_ds_sv(self): #Lấy ra danh sách các object
        return list(self.ds_sv.values())

    def tim_kiem_nhi_phan(self, mssv):
        ds_sorted = self.sap_xep_theo_mssv()   # lấy danh sách đã sắp xếp theo MSSV
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
    
    def ham_sap_xep (self, arr, ham_lay_gia_tri):  #Theo Quick_Sort
        if len(arr) <= 1:
            return arr
        pivot = arr[-1]
        left = []
        for x in arr[::]:
            if ham_lay_gia_tri(x) < ham_lay_gia_tri(pivot):
                left.append(x)
        #[x for x in arr[::] if ham_lay_gia_tri(x) < ham_lay_gia_tri(pivot) ]
        right = []
        for x in arr[::]:
            if ham_lay_gia_tri(x) > ham_lay_gia_tri(pivot):
                right.append(x)

        return self.ham_sap_xep(left, ham_lay_gia_tri) + [int(pivot.mssv)] + self.ham_sap_xep(right, ham_lay_gia_tri)

    def sap_xep_theo_mssv(self):
        ds = self.lay_ds_sv()
        return self.ham_sap_xep(ds, lambda sv: int(sv.mssv) )

    def sap_xep_theo_gpa(self):
        ds = self.lay_ds_sv()
        return self.ham_sap_xep(ds, lambda sv: sv.gpa)

    def hien_thi_ds(self):
        if not self.ds_sv:
            print("Lớp chưa có sinh viên nào")
        else:
            print(f"Danh sách lớp {self.ten_lop}:")
            for sv in self.ds_sv.values():
                print(sv)
if __name__ == '__main__':
    sv=SinhVien("Thái Thuận","K254161803","416","HTTT","8")
    lop_416=Lop("416")
    lop_416.them_sv(sv)
    print(lop_416.ds_sv)
