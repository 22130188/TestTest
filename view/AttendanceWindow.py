from BaseTableWindow import BaseTableWindow
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QPushButton, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QHBoxLayout, QWidget, QLineEdit, QHeaderView
)
from PyQt6.QtCore import Qt
import sys
import os

# Thêm thư mục gốc vào PYTHONPATH
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)
from model.DatabaseManagement import DatabaseManagement


class AttendanceWindow(BaseTableWindow):
    def __init__(self):
        super().__init__("Học sinh có điểm danh")

        # Khởi tạo DatabaseManagement
        self.db_manager = DatabaseManagement()

        # Lấy dữ liệu từ DatabaseManagement

    # 6.1.14. AttendanceWindow khởi tạo và gọi get_attendance_data() của DatabaseManagement để lấy danh sách học sinh có điểm danh.
        data = self.db_manager.get_attendance_data()

    # 6.1.17  Hệ thống kiểm tra kết quả từ get_attendance_data(), nếu không có dữ liệu
        if not data or not isinstance(data, (list, tuple)):
            # 6.3.1. Bảng (self.table) sẽ không hiển thị hàng nào (setRowCount(0)) trên QTableWidget
            self.table.setRowCount(0)
        else:
    # 6.1.18. Hệ thống hiển thị dữ liệu vào bảng (self.table) bằng cách gọi setItem() để gán giá trị vào từng ô trên QTableWidget
            self.table.setRowCount(len(data))  # Đặt số hàng bằng độ dài data
            for i, row in enumerate(data):
                for j, value in enumerate(row):
                    self.table.setItem(i, j, QTableWidgetItem(str(value)))



