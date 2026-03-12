import sys
from PyQt6 import QtWidgets, QtCore, QtGui
from ChatAI import Ui_ChatWindow
import modunAi  

class ChatAIApp(QtWidgets.QWidget): 
    def __init__(self):
        super().__init__()
        self.ui = Ui_ChatWindow()
        self.ui.setupUi(self)
        
        # Kết nối sự kiện gửi tin nhắn 
        self.ui.btn_send.clicked.connect(self.gui_cau_hoi)
        self.ui.input_field.returnPressed.connect(self.gui_cau_hoi) 

    def gui_cau_hoi(self):
        cau_hoi = self.ui.input_field.text().strip()
        if not cau_hoi: return
        
        self.ui.chat_display.append(f"<b style='color: #2196F3;'>Bạn:</b> {cau_hoi}")
        self.ui.input_field.clear()
        self.ui.chat_display.append("<i style='color: gray;'>AI đang phân tích...</i>")
        QtWidgets.QApplication.processEvents()
        
        tra_loi = modunAi.hoi_ai(cau_hoi)
        
        # Xóa dòng trạng thái
        cursor = self.ui.chat_display.textCursor()
        cursor.movePosition(QtGui.QTextCursor.MoveOperation.End)
        cursor.select(QtGui.QTextCursor.SelectionType.LineUnderCursor)
        cursor.removeSelectedText()

        # Hiển thị câu trả lời của AI với định dạng HTML 
        self.ui.chat_display.append(f"<div style='font-family: Arial; line-height: 1.5;'>{tra_loi}</div>")
        self.ui.chat_display.append("<br><hr style='border: 0.1px solid #eee;'>")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    font = QtGui.QFont("Times New Roman", 11) # Đặt font chữ chung cho toàn ứng dụng
    app.setFont(font)
    window = ChatAIApp()
    window.show()
    sys.exit(app.exec())