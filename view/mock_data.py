# Dữ liệu giả cho các lớp học (dựa trên bảng classes)
mock_classes = [
    (1, "Cau truc du lieu"),
    (2, "Toan roi rac"),
    (3, "Python"),
    (4, "Lap trinh mang"),
    (5, "Lap trinh web"),
    (6, "OOP"),
    (7, "Ly thuyet do thi"),
    (8, "AI"),
    (9, "Chuyen de Java"),
    (10, "Co so du lieu"),
]

# Dữ liệu giả cho danh sách học sinh (dựa trên bảng students và studentsofclass)
mock_students = [
    (1, "Dang Anh Nguyen", "123456709", "male", "Cau truc du lieu"),
    (2, "Le Thi Thuy Kieu", "987654321", "female", "Cau truc du lieu"),
    (3, "Dang Tran Tan Luc", "112233445", "male", "Cau truc du lieu"),
    (4, "Do Van Minh Tai", "112233", "male", "Cau truc du lieu"),
]

# Dữ liệu giả cho thông tin chi tiết của học sinh (dựa trên bảng students, với photo_path là URL ảnh từ internet)
mock_student_details = [
    (1, "Dang Anh Nguyen", "123456709", "male", "Cau truc du lieu", "2005-05-18", "https://images.unsplash.com/photo-1506794778202-cad84cf45f1d"),
    (2, "Le Thi Thuy Kieu", "987654321", "female", "Cau truc du lieu", "2005-05-15", "https://images.unsplash.com/photo-1494790108377-be9c29b29330"),
    (3, "Dang Tran Tan Luc", "112233445", "male", "Cau truc du lieu", "2005-05-15", "https://images.unsplash.com/photo-1500648767791-00dcc994a43e"),
    (4, "Do Van Minh Tai", "112233", "male", "Cau truc du lieu", "2005-05-15", "https://images.unsplash.com/photo-1519085360753-af0119f7cbe7"),
]

# Dữ liệu giả cho thống kê điểm danh (dựa trên bảng studentsInSessions và classes)
mock_class_statistics = (
    {1: "Cau truc du lieu", 2: "Toan roi rac", 3: "Python", 4: "Lap trinh mang", 5: "Lap trinh web", 6: "OOP", 7: "Ly thuyet do thi", 8: "AI", 9: "Chuyen de Java", 10: "Co so du lieu"},
    {
        "Cau truc du lieu": 3,  # Số học sinh điểm danh (tính từ studentsInSessions với attendance="present")
        "Toan roi rac": 6,
        "Python": 6,
        "Lap trinh mang": 6,
        "Lap trinh web": 0,
        "OOP": 1,
        "Ly thuyet do thi": 0,
        "AI": 0,
        "Chuyen de Java": 0,
        "Co so du lieu": 0,
    },
    {
        "Cau truc du lieu": 9,  # Số học sinh vắng (tính từ studentsInSessions với attendance="absent")
        "Toan roi rac": 6,
        "Python": 6,
        "Lap trinh mang": 6,
        "Lap trinh web": 12,
        "OOP": 11,
        "Ly thuyet do thi": 12,
        "AI": 12,
        "Chuyen de Java": 12,
        "Co so du lieu": 12,
    }
)

# Dữ liệu giả cho danh sách học sinh đã điểm danh (dựa trên bảng studentsInSessions với attendance="present")
mock_attendance_data = [
    ("Toan roi rac", 1, "Dang Anh Nguyen", "Buoi 1", "2024-11-08"),
    ("Toan roi rac", 2, "Le Thi Thuy Kieu", "Buoi 1", "2024-11-08"),
    ("Toan roi rac", 3, "Dang Tran Tan Luc", "Buoi 1", "2024-11-08"),
    ("Toan roi rac", 1, "Dang Anh Nguyen", "Buoi 2", "2024-11-09"),
    ("Toan roi rac", 2, "Le Thi Thuy Kieu", "Buoi 2", "2024-11-09"),
    ("Toan roi rac", 3, "Dang Tran Tan Luc", "Buoi 2", "2024-11-09"),
    ("Python", 1, "Dang Anh Nguyen", "Buoi 1", "2024-11-14"),
    ("Python", 2, "Le Thi Thuy Kieu", "Buoi 1", "2024-11-14"),
    ("Python", 3, "Dang Tran Tan Luc", "Buoi 1", "2024-11-14"),
    ("Python", 1, "Dang Anh Nguyen", "Buoi 2", "2024-11-15"),
    ("Python", 2, "Le Thi Thuy Kieu", "Buoi 2", "2024-11-15"),
    ("Python", 3, "Dang Tran Tan Luc", "Buoi 2", "2024-11-15"),
    ("Lap trinh mang", 1, "Dang Anh Nguyen", "Buoi 1", "2024-11-20"),
    ("Lap trinh mang", 2, "Le Thi Thuy Kieu", "Buoi 1", "2024-11-20"),
    ("Lap trinh mang", 3, "Dang Tran Tan Luc", "Buoi 1", "2024-11-20"),
    ("Lap trinh mang", 1, "Dang Anh Nguyen", "Buoi 2", "2024-11-21"),
    ("Lap trinh mang", 2, "Le Thi Thuy Kieu", "Buoi 2", "2024-11-21"),
    ("Lap trinh mang", 3, "Dang Tran Tan Luc", "Buoi 2", "2024-11-21"),
    ("OOP", 4, "Do Van Minh Tai", "Buoi 8", "2024-12-08"),
]

# Dữ liệu giả cho danh sách học sinh vắng (dựa trên bảng studentsInSessions với attendance="absent")
mock_no_attendance_data = [
    ("Cau truc du lieu", 1, "Dang Anh Nguyen", "Buoi 1", "2024-11-01"),
    ("Cau truc du lieu", 2, "Le Thi Thuy Kieu", "Buoi 1", "2024-11-01"),
    ("Cau truc du lieu", 3, "Dang Tran Tan Luc", "Buoi 1", "2024-11-01"),
    ("Cau truc du lieu", 1, "Dang Anh Nguyen", "Buoi 2", "2024-11-02"),
    ("Cau truc du lieu", 2, "Le Thi Thuy Kieu", "Buoi 2", "2024-11-02"),
    ("Cau truc du lieu", 3, "Dang Tran Tan Luc", "Buoi 2", "2024-11-02"),
    ("Cau truc du lieu", 1, "Dang Anh Nguyen", "Buoi 3", "2024-11-03"),
    ("Cau truc du lieu", 2, "Le Thi Thuy Kieu", "Buoi 3", "2024-11-03"),
    ("Cau truc du lieu", 3, "Dang Tran Tan Luc", "Buoi 3", "2024-11-03"),
    ("Cau truc du lieu", 4, "Do Van Minh Tai", "Buoi 1", "2024-11-01"),
    ("Cau truc du lieu", 4, "Do Van Minh Tai", "Buoi 2", "2024-11-02"),
    ("Cau truc du lieu", 4, "Do Van Minh Tai", "Buoi 3", "2024-11-03"),
    ("Toan roi rac", 4, "Do Van Minh Tai", "Buoi 1", "2024-11-08"),
    ("Toan roi rac", 4, "Do Van Minh Tai", "Buoi 2", "2024-11-09"),
    ("Python", 4, "Do Van Minh Tai", "Buoi 1", "2024-11-14"),
    ("Python", 4, "Do Van Minh Tai", "Buoi 2", "2024-11-15"),
    # Tiếp tục với các buổi khác...
]

# Dữ liệu giả cho các buổi học (dựa trên bảng sessions)
mock_sessions = [
    (1, "Buoi 1", "Cau truc du lieu", "2024-11-01", "08:00:00", "10:00:00"),
    (2, "Buoi 2", "Cau truc du lieu", "2024-11-02", "10:00:00", "12:00:00"),
    (3, "Buoi 3", "Cau truc du lieu", "2024-11-03", "08:00:00", "10:00:00"),
    (4, "Buoi 4", "Cau truc du lieu", "2024-11-04", "10:00:00", "12:00:00"),
    (5, "Buoi 5", "Cau truc du lieu", "2024-11-05", "08:00:00", "10:00:00"),
    (6, "Buoi 6", "Cau truc du lieu", "2024-11-06", "10:00:00", "12:00:00"),
    (7, "Buoi 7", "Cau truc du lieu", "2024-11-07", "08:00:00", "10:00:00"),
    (8, "Buoi 8", "Cau truc du lieu", "2024-11-08", "10:00:00", "12:00:00"),
    (9, "Buoi 1", "Toan roi rac", "2024-11-08", "08:00:00", "10:00:00"),
    (10, "Buoi 2", "Toan roi rac", "2024-11-09", "10:00:00", "12:00:00"),
    (11, "Buoi 3", "Toan roi rac", "2024-11-10", "08:00:00", "10:00:00"),
    (12, "Buoi 4", "Toan roi rac", "2024-11-11", "10:00:00", "12:00:00"),
    (13, "Buoi 5", "Toan roi rac", "2024-11-12", "08:00:00", "10:00:00"),
    (14, "Buoi 6", "Toan roi rac", "2024-11-13", "10:00:00", "12:00:00"),
    (15, "Buoi 7", "Toan roi rac", "2024-11-14", "08:00:00", "10:00:00"),
    (16, "Buoi 8", "Toan roi rac", "2024-11-15", "10:00:00", "12:00:00"),
    (17, "Buoi 1", "Python", "2024-11-14", "08:00:00", "10:00:00"),
    (18, "Buoi 2", "Python", "2024-11-15", "10:00:00", "12:00:00"),
    (19, "Buoi 3", "Python", "2024-11-16", "08:00:00", "10:00:00"),
    (20, "Buoi 4", "Python", "2024-11-17", "10:00:00", "12:00:00"),
    (21, "Buoi 5", "Python", "2024-11-18", "08:00:00", "10:00:00"),
    (22, "Buoi 6", "Python", "2024-11-19", "10:00:00", "12:00:00"),
    (23, "Buoi 7", "Python", "2024-11-20", "08:00:00", "10:00:00"),
    (24, "Buoi 8", "Python", "2024-11-21", "10:00:00", "12:00:00"),
    (25, "Buoi 1", "Lap trinh mang", "2024-11-20", "08:00:00", "10:00:00"),
    (26, "Buoi 2", "Lap trinh mang", "2024-11-21", "10:00:00", "12:00:00"),
    (27, "Buoi 3", "Lap trinh mang", "2024-11-22", "08:00:00", "10:00:00"),
    (28, "Buoi 4", "Lap trinh mang", "2024-11-23", "10:00:00", "12:00:00"),
    (29, "Buoi 5", "Lap trinh mang", "2024-11-24", "08:00:00", "10:00:00"),
    (30, "Buoi 6", "Lap trinh mang", "2024-11-25", "10:00:00", "12:00:00"),
    (31, "Buoi 7", "Lap trinh mang", "2024-11-26", "08:00:00", "10:00:00"),
    (32, "Buoi 8", "Lap trinh mang", "2024-11-27", "10:00:00", "12:00:00"),
    (33, "Buoi 1", "Lap trinh web", "2024-11-26", "08:00:00", "10:00:00"),
    (34, "Buoi 2", "Lap trinh web", "2024-11-27", "10:00:00", "12:00:00"),
    (35, "Buoi 3", "Lap trinh web", "2024-11-28", "08:00:00", "10:00:00"),
    (36, "Buoi 4", "Lap trinh web", "2024-11-29", "10:00:00", "12:00:00"),
    (37, "Buoi 5", "Lap trinh web", "2024-11-30", "08:00:00", "10:00:00"),
    (38, "Buoi 6", "Lap trinh web", "2024-12-01", "10:00:00", "12:00:00"),
    (39, "Buoi 7", "Lap trinh web", "2024-12-02", "08:00:00", "10:00:00"),
    (40, "Buoi 8", "Lap trinh web", "2024-12-03", "10:00:00", "12:00:00"),
    (41, "Buoi 1", "OOP", "2024-12-01", "08:00:00", "10:00:00"),
    (42, "Buoi 2", "OOP", "2024-12-02", "10:00:00", "12:00:00"),
    (43, "Buoi 3", "OOP", "2024-12-03", "08:00:00", "10:00:00"),
    (44, "Buoi 4", "OOP", "2024-12-04", "10:00:00", "12:00:00"),
    (45, "Buoi 5", "OOP", "2024-12-05", "08:00:00", "10:00:00"),
    (46, "Buoi 6", "OOP", "2024-12-06", "10:00:00", "12:00:00"),
    (47, "Buoi 7", "OOP", "2024-12-07", "08:00:00", "10:00:00"),
    (48, "Buoi 8", "OOP", "2024-12-08", "10:00:00", "12:00:00"),
]

# Dữ liệu giả cho nhận diện (dựa trên bảng students)
mock_recognition_data = {
    "ids": [1, 2, 3, 4],
    "names": [
        "Dang Anh Nguyen",
        "Le Thi Thuy Kieu",
        "Dang Tran Tan Luc",
        "Do Van Minh Tai"
    ],
    "mapIdtoName": {
        1: "Dang Anh Nguyen",
        2: "Le Thi Thuy Kieu",
        3: "Dang Tran Tan Luc",
        4: "Do Van Minh Tai"
    }
}