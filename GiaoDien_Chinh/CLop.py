class Lop:
    def __init__(self,ten_lop):
        self.ds_sv={}
        self.ten_lop=ten_lop
    def them_sv(self,sv):
        self.ds_sv[sv.mssv](sv)
    def ten(self):
        return self.ten_lop
    def xoa_sv(self,mssv_xoa):
        del self.ds_sv[mssv_xoa]