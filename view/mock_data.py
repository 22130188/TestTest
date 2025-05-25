# mock_data.py
from datetime import datetime, date

# Dữ liệu giả cho các lớp học
mock_classes = [
    (1, "Lớp 10A"),
    (2, "Lớp 10B"),
    (3, "Lớp 11A"),
]

# Dữ liệu giả cho danh sách học sinh
mock_students = [
    (1, "Nguyễn Văn A", "123456789", "male", "Lớp 10A"),
    (2, "Trần Thị B", "987654321", "female", "Lớp 10A"),
    (3, "Lê Văn C", "456789123", "male", "Lớp 10B"),
    (4, "Phạm Thị D", "321654987", "female", "Lớp 11A"),
]

# Dữ liệu giả cho thống kê điểm danh
mock_class_statistics = (
    {1: "Lớp 10A", 2: "Lớp 10B", 3: "Lớp 11A"},
    {"Lớp 10A": 15, "Lớp 10B": 12, "Lớp 11A": 18},  # Số học sinh có điểm danh
    {"Lớp 10A": 5, "Lớp 10B": 8, "Lớp 11A": 2},     # Số học sinh vắng
)

# Dữ liệu giả cho danh sách học sinh đã điểm danh
mock_attendance_data = [
    ("Lớp 10A", 1, "Nguyễn Văn A", "Buổi 1", "2025-05-20"),
    ("Lớp 10A", 2, "Trần Thị B", "Buổi 1", "2025-05-20"),
    ("Lớp 10B", 3, "Lê Văn C", "Buổi 2", "2025-05-21"),
]

# Dữ liệu giả cho danh sách học sinh vắng
mock_no_attendance_data = [
    ("Lớp 10A", 5, "Nguyễn Văn E", "Buổi 1", "2025-05-20"),
    ("Lớp 10B", 6, "Trần Văn F", "Buổi 2", "2025-05-21"),
    ("Lớp 11A", 7, "Lê Thị G", "Buổi 3", "2025-05-22"),
]

# Dữ liệu giả cho thông tin chi tiết của học sinh
mock_student_details = [
    (1, "Nguyễn Văn A", "123456789", "male", "Lớp 10A", "2007-01-01", None),
    (2, "Trần Thị B", "987654321", "female", "Lớp 10A", "2007-02-02", None),
    (3, "Lê Văn C", "456789123", "male", "Lớp 10B", "2006-03-03", None),
    (4, "Phạm Thị D", "321654987", "female", "Lớp 11A", "2006-04-04", None),
]

# Dữ liệu giả cho các buổi học
mock_sessions = [
    (1, "Buổi 1", "Lớp 10A", "2025-05-20", "08:00", "10:00"),
    (2, "Buổi 2", "Lớp 10B", "2025-05-21", "10:00", "12:00"),
    (3, "Buổi 3", "Lớp 11A", "2025-05-22", "13:00", "15:00"),
]