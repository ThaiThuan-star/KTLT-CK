class Khoa:
    def __init__(self,ten_khoa):
        self.ds_lop={}
        self.ten_khoa=ten_khoa
    def add_lop(self,lop):
        self.ds_lop[lop.ten()]=lop
