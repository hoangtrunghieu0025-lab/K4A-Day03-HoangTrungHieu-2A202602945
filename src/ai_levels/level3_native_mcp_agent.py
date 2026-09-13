"""
📚 [REFERENCE ONLY / CODE MẪU THAM KHẢO]
🧠 CẤP ĐỘ 3: NATIVE MCP AGENT (Native Tool Calling + MCP Server Integration)
⚠️ Lưu ý: File này chỉ dùng để đọc tham khảo kiến trúc. Không chỉnh sửa hay debug file này.
"""

import json

def get_weather(city: str) -> str:
    return f"Thời tiết {city}: 28°C, Nắng nhẹ."

def run_level3_demo():
    print("=== DEMO CẤP ĐỘ 3: NATIVE MCP AGENT ===")
    user_goal = "Tra cứu lịch làm việc của bác sĩ Nguyễn Minh Anh tại Vinmec"
    print(f"🎯 Goal: {user_goal}")
    print("🧠 [Thought]: Phát sinh Native Tool Call 'doctor_schedule_query'...")
    print("🛠️ [Native Tool Call]: doctor_schedule_query({'specialty': 'Tim mạch', 'doctor_name': 'Nguyễn Minh Anh', 'facility': 'Vinmec Central Park', 'date': '20/09/2026'})")
    print("👁️ [MCP Server Observation]: {'doctor_name': 'Nguyễn Minh Anh', 'specialty': 'Tim mạch', 'available_slots': ['09:00 ngày 20/09/2026']}")
    print("🏁 [Final Answer]: Bác sĩ Nguyễn Minh Anh có khung giờ trống lúc 09:00 ngày 20/09/2026 tại Vinmec Central Park.")

if __name__ == "__main__":
    run_level3_demo()
