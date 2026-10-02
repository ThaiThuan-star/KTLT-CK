from google import genai 
import json

FILENAME = "ds_sv.json"

# 1. Khởi tạo Client (Thay API Key của bạn vào đây)
client = genai.Client(api_key="AIzaSyDBNtCQtBqlU3n3lWwYvd_XUzfpayhyD3M")
MODEL_ID = "models/gemini-flash-lite-latest" 

# 2. Logic lấy dữ liệu: Đọc file hoặc Tạo ngẫu nhiên
def tai_tao_data():

    with open(FILENAME, 'r', encoding='utf-8') as f:
        data = json.load(f)
        source="DỮ LIỆU TỪ MÁY"
    return data,source

def hoi_ai(user):
    data,source = tai_tao_data()
    json_string = json.dumps(data, ensure_ascii=False)

    prompt = f"""
    <SYSTEM>
    Bạn là chuyên gia phân tích dữ liệu học thuật cao cấp. 
    Nhiệm vụ: Phân tích dữ liệu JSON và trả về câu trả lời dưới dạng HTML để hiển thị trên ứng dụng Desktop.
    </SYSTEM>

    <DATA source="{source}">
    {json_string}
    </DATA>

    <RULES_FOR_CLASSIFICATION>
    - 🔴 NGUY CẤP: (fail_ratio > 0.5) HOẶC (khoảng cách điểm spread >= 6).
    - 🔴 NGUY CƠ: Có xu hướng giảm điểm hoặc spread cao nhưng chưa tới mức nguy cấp.
    - 🟡 CÓ NGUY CƠ: Điểm trung bình thấp (5-6).
    - 🟢 TRUNG BÌNH: Điểm ổn định (6-8).
    - 🔵 CẦN THÚC ĐẨY: Điểm khá nhưng cần đẩy lên giỏi.
    </RULES_FOR_CLASSIFICATION>

    <OUTPUT_STYLE_GUIDE>
    1. LUÔN trả về bảng bằng thẻ <table> nếu có dữ liệu danh sách.
    2. Sử dụng Inline CSS để làm đẹp:
       - Table: border-collapse: collapse; width: 100%; margin: 10px 0;
       - Th/Td: border: 1px solid #A0C4FF; padding: 10px; text-align: center;
       - Header (Th): background-color: #2196F3; color: white;
    3. TÔ MÀU chữ cho cột "Phân loại":
       - Nguy cấp/Nguy cơ: color: red; font-weight: bold;
       - Có nguy cơ: color: orange;
       - Trung bình: color: green;
    4. Nếu người dùng hỏi câu hỏi ngoài việc lập bảng, hãy trả lời bằng văn bản HTML có các thẻ <p>, <b>, <ul> để dễ đọc.
    </OUTPUT_STYLE_GUIDE>

    Câu hỏi của người dùng: {user}
    """

# 4. Thực thi
    try:
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=[prompt, f"Người dùng hỏi: {user}"]
        )
        return response.text if response.text else "AI không có phản hồi."
    except Exception as e:
        return f"Lỗi kết nối AI: {str(e)}"
    
