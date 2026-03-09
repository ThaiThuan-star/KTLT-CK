from CSinhVien import *
class Lop:
    def __init__(self,ten_lop):
        self.ds_sv={}
        self.ten_lop=ten_lop
    def them_sv(self,sv):
        self.ds_sv[sv.mssv]=sv
    def ten(self):
        return self.ten_lop
    def xoa_sv(self,mssv_xoa):
        del self.ds_sv[mssv_xoa]

if __name__ == '__main__':
    sv1=SinhVien("Thái Thuận","K254161803","416","HTTT",3)
    sv2 = SinhVien("Đạt", "K254161801", "416", "HTTT", 3)
    lop_416=Lop("416")
    lop_416.them_sv(sv1)
    lop_416.them_sv(sv2)
    print(lop_416.ds_sv)