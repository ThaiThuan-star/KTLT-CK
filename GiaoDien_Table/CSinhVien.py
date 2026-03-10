class SinhVien:
    def __init__(self,ten,mssv,lop,khoa,gpa):
        self.ten = ten
        self.mssv = mssv
        self.lop = lop
        self.khoa=khoa
        self.gpa=float(gpa)
    def update_info(self,ten_moi,mssv_moi,lop_moi,khoa_moi,gpa_moi):
        self.ten = ten_moi
        self.mssv = mssv_moi
        self.lop = lop_moi
        self.khoa = khoa_moi
        self.gpa = float(gpa_moi)

    def __str__(self):
        return f"{self.ten} {self.mssv} {self.lop} {self.khoa} {self.gpa}"
    def __repr__(self):
        return f"{self.ten} {self.mssv} {self.lop} {self.khoa} {self.gpa}"