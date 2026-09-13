# 📊 BÁO CÁO THU HOẠCH NGHIỆM THU BÀI LAB 3 (BƯỚC 3 — SUBMISSION ARTIFACT)

> **Họ và Tên Học viên:** [Hoàng Trung Hiếu]  
> **Mã Sinh Viên / Mã Học viên:** [2A202602945]  
> **Chủ đề Lựa chọn:** [*Trợ lý Tư vấn Sức khỏe Vinmec:* Tra cứu lịch làm việc bác sĩ chuyên khoa và đặt lịch khám bệnh.]  

---

## 1. BẢNG CHẤM ĐIỂM AGENTIC FIT SCORING MATRIX (ĐÁNH GIÁ CHỦ ĐỀ)

| Tiêu chí Đánh giá | Mức độ (1 - 5) | Giải trình chi tiết lý do chọn điểm |
| :--- | :---: | :--- |
| **1. Multi-step Reasoning** | 4 / 5 | Agent cần xác định chuyên khoa, tra cứu bác sĩ và lịch trống, sau đó đề xuất hoặc đặt lịch phù hợp cho người bệnh. |
| **2. Tool Interaction** | 4 / 5 | Hệ thống cần gọi công cụ tra cứu lịch làm việc bác sĩ và công cụ đặt lịch khám, có thể kết nối với MCP Server hoặc cơ sở dữ liệu bệnh viện. |
| **3. Dynamic Decision** | 4 / 5 | Bước đặt lịch phụ thuộc vào kết quả tra cứu: bác sĩ có làm việc không, còn khung giờ hay không, thông tin bệnh nhân đã đầy đủ chưa. |
| **4. Long Horizon Goal** | 3 / 5 | Agent cần duy trì mục tiêu đặt lịch qua một chuỗi xử lý ngắn, nhưng hiện tại chỉ giới hạn ở hai chức năng, chưa phải quy trình chăm sóc sức khỏe dài hạn |
| **TỔNG ĐIỂM AGENTIC FIT** | ** 15 / 20** | *Nếu tổng điểm > 12/20: Bài toán rất phù hợp triển khai Agentic System.* |

---

## 2. TRÍCH XUẤT KẾT QUẢ WATERFALL TRACE LOG (SAU KHI CHẠY TEST SUITE TRÊN API THẬT)

> ⚠️ **YÊU CẦU NGHIỆM THU:** Mở tệp `.env` điền `GEMINI_API_KEY` (hoặc `OPENAI_API_KEY`) để kết nối LLM thật trước khi thực thi `python src/app.py --all`. Bài nộp chỉ dùng Mock Offline Provider sẽ không đạt điểm nghiệm thực tế.

Dán 1 đoạn trích xuất log tiêu biểu từ file `docs/trace_waterfall.json` sinh ra từ phản hồi LLM API thật:

```json
[
  {
    "step": 1,
    "query": "Tôi cần khám Tim mạch tại Vinmec. Hãy tra cứu lịch làm việc của bác sĩ Nguyễn Minh Anh, tìm khung giờ còn trống gần nhất rồi đặt lịch lúc 09:00 ngày 20/09/2026 nếu còn chỗ.",
    "action_type": "TOOL_EXECUTION",
    "tool_name": "doctor_schedule_query",
    "arguments": {
      "specialty": "Tim mạch",
      "doctor_name": "Nguyễn Minh Anh",
      "facility": "Vinmec",
      "date": "20/09/2026"
    },
    "observation": {
      "status": "SUCCESS",
      "doctor_name": "Nguyễn Minh Anh",
      "specialty": "Tim mạch",
      "facility": "Vinmec Central Park",
      "date": "20/09/2026",
      "available_slots": [
        "09:00 ngày 20/09/2026",
        "10:30 ngày 20/09/2026"
      ]
    },
    "latency_ms": 2128.7
  }
]
```

---

## 3. TỔNG KẾT KẾT QUẢ NGHIỆM THU & NỘP BÀI

- [x] Đã điền API Key thật trong `.env` và xác nhận Agent chạy mượt mà trên LLM API thật (Gemini/OpenAI).
- **Tổng số Test Cases đã chạy thành công:** 5 / 5 test cases.
- **Số lượt gọi Tool qua MCP Server chính xác:** 5 lượt.
- **Kết quả đẩy Repo nộp bài:** [x] Đã Commit và Push mã nguồn thành công lên GitHub cá nhân.

---

> ✅ **HOÀN TẤT NỘP BÀI:** Sao chép đường link GitHub Repository cá nhân của bạn và dán vào ô nộp bài trên hệ thống LMS VLearn để hoàn tất Bài Lab 3!
