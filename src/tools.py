"""
🛠️ TOOL DEFINITIONS & EXECUTION BACKEND
Mã nguồn chứa danh sách Tool Schemas (JSON Schema) và Execution Layer phục vụ cho MCP Server.
"""

import json
from typing import Dict, Any

# ==============================================================================
# 1. KHAI BÁO TOOL SCHEMAS CHUẨN NATIVE JSON SCHEMA (TASK 1.2)
# ==============================================================================

TOOLS_SCHEMA = [
    {
        "name": "doctor_schedule_query",
        "description": "Tra cứu lịch làm việc và khung giờ khám còn trống của bác sĩ tại Vinmec.",
        "parameters": {
            "type": "object",
            "properties": {
                "specialty": {
                    "type": "string",
                    "description": "Tên chuyên khoa cần khám, ví dụ: Tim mạch"
                },
                "doctor_name": {
                    "type": "string",
                    "description": "Tên bác sĩ cần tra cứu"
                },
                "facility": {
                    "type": "string",
                    "description": "Cơ sở Vinmec cần tra cứu"
                },
                "date": {
                    "type": "string",
                    "description": "Ngày cần tra cứu, ví dụ: 20/09/2026"
                }
            },
            "required": ["specialty", "doctor_name", "facility", "date"]
        }
    },
    {
        "name": "book_appointment",
        "description": "Đặt lịch khám tại Vinmec theo bác sĩ, chuyên khoa, cơ sở và thời gian đã chọn.",
        "parameters": {
            "type": "object",
            "properties": {
                "patient_name": {
                    "type": "string",
                    "description": "Họ tên người bệnh"
                },
                "specialty": {
                    "type": "string",
                    "description": "Tên chuyên khoa cần khám"
                },
                "advisor_name": {
                    "type": "string",
                    "description": "Tên bác sĩ"
                },
                "facility": {
                    "type": "string",
                    "description": "Cơ sở Vinmec"
                },
                "datetime_str": {
                    "type": "string",
                    "description": "Thời gian khám, ví dụ: 09:00 ngày 20/09/2026"
                }
            },
            "required": ["specialty", "doctor_name", "facility", "datetime_str"]
        }
    }
]

# ==============================================================================
# 2. MÔ PHỎNG DỮ LIỆU & HÀM THỰC THI TOOL (EXECUTION LAYER)
# ==============================================================================

MOCK_DOCTOR_SCHEDULES = {
    "Nguyễn Minh Anh": {
        "specialty": "Tim mạch",
        "facility": "Vinmec Central Park",
        "available_slots": ["09:00 ngày 20/09/2026", "10:30 ngày 20/09/2026"]
    }
}


def execute_doctor_schedule_query(specialty: str, doctor_name: str, facility: str, date: str) -> str:
    """Tra cứu lịch làm việc và khung giờ khám của bác sĩ tại Vinmec."""
    doctor = MOCK_DOCTOR_SCHEDULES.get(doctor_name.strip())
    if doctor and specialty.lower() in doctor["specialty"].lower():
        return json.dumps({
            "status": "SUCCESS",
            "doctor_name": doctor_name,
            "specialty": doctor["specialty"],
            "facility": doctor["facility"],
            "date": date,
            "available_slots": doctor["available_slots"]
        }, ensure_ascii=False)
    return json.dumps({
        "status": "NOT_FOUND",
        "message": f"Không tìm thấy lịch làm việc phù hợp của bác sĩ '{doctor_name}' tại Vinmec."
    }, ensure_ascii=False)


def execute_book_appointment(
    specialty: str,
    doctor_name: str,
    facility: str,
    datetime_str: str,
    patient_name: str = "Bệnh nhân"
) -> str:
    """Thực thi đặt lịch khám tại Vinmec."""
    doctor = MOCK_DOCTOR_SCHEDULES.get(doctor_name.strip())
    if not doctor or datetime_str not in doctor["available_slots"]:
        return json.dumps({
            "status": "NOT_AVAILABLE",
            "message": f"Khung giờ {datetime_str} của bác sĩ {doctor_name} hiện không còn trống."
        }, ensure_ascii=False)
    return json.dumps({
        "status": "SUCCESS",
        "booking_id": f"VMC-{doctor_name.replace(' ', '')}-20260920",
        "patient_name": patient_name,
        "specialty": specialty,
        "doctor_name": doctor_name,
        "facility": facility,
        "datetime": datetime_str,
        "message": f"Đặt lịch khám thành công tại {facility} với bác sĩ {doctor_name} vào {datetime_str}."
    }, ensure_ascii=False)


# Router gọi tool thực tế
TOOL_ROUTER = {
    "doctor_schedule_query": execute_doctor_schedule_query,
    "book_appointment": execute_book_appointment
}

def dispatch_tool_call(tool_name: str, arguments: Dict[str, Any]) -> str:
    """Hàm trung chuyển thực thi tool"""
    if tool_name in TOOL_ROUTER:
        try:
            if tool_name == "book_appointment" and "advisor_name" in arguments:
                arguments = dict(arguments)
                arguments["doctor_name"] = arguments.pop("advisor_name")
            return TOOL_ROUTER[tool_name](**arguments)
        except Exception as e:
            return json.dumps({"status": "EXECUTION_ERROR", "error": str(e)}, ensure_ascii=False)
    return json.dumps({"status": "UNKNOWN_TOOL", "error": f"Tool '{tool_name}' không tồn tại!"}, ensure_ascii=False)
