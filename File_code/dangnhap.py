import json
import os #kiểm tra file đã tồn tại chưa

DATA_FILE = "users.jsonl" #lưu trữ dữ liệu người dùng theo định dạng JSON 

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


    def dinh_dang_du_lieu(self):
        return {
            "username": self.username,
            "password": self.password
        }
    
class quanlydanhtinh:
    def __init__(self):
        self.users = {}
        self.quet_users()

    def quet_users(self):
        if not os.path.exists(DATA_FILE):
            return
        
        with open(DATA_FILE, "r") as f:
            for line in f:
                record = json.loads(line.strip())
                doi_tuong_user = User(record["username"], record["password"])
                self.users[doi_tuong_user.username] = doi_tuong_user.dinh_dang_du_lieu()

    def dangki(self, username, password):
        if username in self.users:
                return False, "Tên Người Dùng Đã Tồn Tại"
            
        record = User(username, password).dinh_dang_du_lieu()

        with open(DATA_FILE, "a") as f:
                f.write(json.dumps(record) + "\n")

        self.users[username] = record
        return True, "Đăng Ký Thành Công"
        
    def dangnhap(self, username, password):
        if username not in self.users:
            return False, "Tên Người Dùng Không Tồn Tại"
            
        if self.users[username]["password"] != password:
            return False, "Mật Khẩu Không Chính Xác"
            
        return True, "Đăng Nhập Thành Công"
        

if __name__ == "__main__":
    ql = quanlydanhtinh()
    print(ql.dangki("user1", "pass1"))
    print(ql.dangki("user2", "pass2"))
    print(ql.dangnhap("user1", "pass1"))
    print(ql.dangnhap("user2", "wrongpass"))