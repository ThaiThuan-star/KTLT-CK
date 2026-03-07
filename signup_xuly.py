import json
import os #kiểm tra file đã tồn tại chưa
import hashlib

DATA_FILE = "users.jsonl" #lưu trữ dữ liệu người dùng theo định dạng JSON 

class User:
    def __init__(self, username, password, salt):
        self.username = username
        self.password = password
        self.salt = salt

    def dinh_dang_du_lieu(self):
        return {
            "username": self.username,
            "hash": self.password,
            "salt": self.salt
        }

class quanlydanhtinh:
    def __init__(self):
        self.users = {}  # dùng dict để lưu trong ram
        self.quet_users()

    def hash_password(self, password, salt): #băm hàm sha256 với salt để tăng cường bảo mật, tránh bị tấn công bằng cách sử dụng bảng băm sẵn 
        return hashlib.sha256((password + salt).encode()).hexdigest()

    def quet_users(self):
        if not os.path.exists(DATA_FILE): #check if file data tồn tại 
            return

        with open(DATA_FILE, "r") as f: # r means chỉ đọc, dùng with để đọc sau r đóng sách lại (lịch sự chưa các cvo)
            for line in f:
                record = json.loads(line.strip())
                doi_tuong_user = User(record["username"], record["hash"], record["salt"])
                self.users[doi_tuong_user.username] = doi_tuong_user.dinh_dang_du_lieu() #lưu vào dict users với key là username và value là dict chứa hash và salt
    

    def Dangki(self, username, password):
        if username in self.users: #có thể trùng mk nhưng ko đc trùng username
            return False, "ten da ton tai"

    #bảo mật
        salt = os.urandom(16).hex() #tạo salt ngẫu nhiên -> ko bị hack bằng bảng băm sẵn.
        hashed = self.hash_password(password, salt)

    #make a new record
        record = User(username, hashed, salt).dinh_dang_du_lieu()

    #append vào file
        with open(DATA_FILE, "a") as f: # a means append
            f.write(json.dumps(record) + "\n")

    #lưu vào dict
        self.users[username] = record
        return True, "Dang ki thanh cong"

    def Dangnhap(self, username, password):
        if username not in self.users:
            return False, "ko thay tai khoan ku"

        record = self.users[username]
        salt = self.users[username]["salt"]
        hashed = self.hash_password(password, salt)

        if hashed == self.users[username]["hash"]:
            return True, "Dang nhap thanh cong"
        else:
            return False, "Sai mat khau roi ku"

