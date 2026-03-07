class SinhVien:
    def __init__(self,ten,mssv,lop,khoa,gpa):
        self.ten = ten
        self.mssv = mssv
        self.lop = lop
        self.khoa=khoa
        self.gpa=float(gpa)
    def xep_loai(self):
        if self.gpa <4:
            return "Kém"
        elif 4<=self.gpa <5:
            return "Yếu"
        elif 5<=self.gpa <7:
            return "Trung bình"
        elif 7<=self.gpa <8:
            return "Khá"
        elif 8<=self.gpa <9:
            return "Giỏi"
        else:
            return "Xuất sắc"

    def __str__(self):
        return f"{self.ten} {self.mssv} {self.lop} {self.khoa} {self.gpa}"