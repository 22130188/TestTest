import sys
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QFrame, QTabWidget,
    QStackedWidget
)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import sys
import os

# Thêm thư mục gốc vào PYTHONPATH
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)
from model.DatabaseManagement import DatabaseManagement

from AttendanceWindow import AttendanceWindow
from NoAttendanceWindow import NoAttendanceWindow
import os

# 6.1.2. QTabWidget tự động chuyển đến widget SystemStatistics đã được khởi tạo và thêm vào tab trước đó
class SystemStatistics(QMainWindow):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = QStackedWidget()
        self.stacked_widget = stacked_widget
        self.setWindowTitle("Thống kê hệ thống")
        self.setGeometry(100, 100, 1200, 700)
        self.db_manager = DatabaseManagement()  # Khởi tạo DatabaseManagement
        self.setup_ui()
        self.setStyleSheet("background-color: white; color:black;")
        self.chart_canvas = QWidget()

    # 6.1.3. Hệ thống khởi tạo giao diện SystemStatistics, bao gồm ba tab con: "Thống kê", "Học sinh vắng", và "Học sinh đã điểm danh" bằng phương thức setup_ui()
    def setup_ui(self):
        main_layout = QVBoxLayout()

        tab_widget = QTabWidget(self)
        tab_widget.clear()
        tab_widget.addTab(self.create_statistics_tab(), "Thống kê")

    # 6.1.12 Giáo viên chọn tab Học sinh đã điểm danh trong SystemStatistics
        tab_widget.addTab(self.create_attendance_tab(), "Học sinh đã điểm danh")

    # 6.1.19 Giáo viên chọn tab Học sinh vắng trong SystemStatistics
        tab_widget.addTab(self.create_no_attendance_tab(), "Học sinh vắng")


        main_layout.addWidget(tab_widget)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    # 6.1.4. Trong SystemStatistics, hệ thống gọi phương thức create_statistics_tab() để tạo giao diện thống kê
    def create_statistics_tab(self):
        statistics_tab = QWidget()
        layout = QHBoxLayout()

        chart_widget = self.create_chart_with_border()
        layout.addWidget(chart_widget)

        statistics_tab.setLayout(layout)
        return statistics_tab

    # 6.1.13. Hệ thống gọi phương thức create_attendance_tab() để tạo giao diện AttendanceWindow.
    def create_attendance_tab(self):
        attendance_tab = QWidget()
        layout = QVBoxLayout()

        self.attendance_window_widget = AttendanceWindow()
        layout.addWidget(self.attendance_window_widget)

        attendance_tab.setLayout(layout)
        return attendance_tab

    # 6.1.20. Hệ thống gọi phương thức create_no_attendance_tab() để tạo giao diện NoAttendanceWindow.
    def create_no_attendance_tab(self):
        no_attendance_tab = QWidget()
        layout = QVBoxLayout()

        self.no_attendance_window_widget = NoAttendanceWindow()
        layout.addWidget(self.no_attendance_window_widget)

        no_attendance_tab.setLayout(layout)
        return no_attendance_tab

    def create_chart_with_border(self):
        chart_container = QFrame()
        chart_container.setStyleSheet("""
            QFrame {
                background-color: #ffffff;
                border: 2px solid #4faaff;
                border-radius: 10px;
                padding: 10px;
                box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
            }
        """)

        self.chart_layout = QVBoxLayout()
        self.chart_canvas = self.create_area_chart()
        self.chart_layout.addWidget(self.chart_canvas)

        chart_container.setLayout(self.chart_layout)
        return chart_container

    def shorten_class_name(self, name, max_length=10):
        """Hàm rút ngắn tên môn học nếu quá dài"""
        if len(name) <= max_length:
            return name
        words = name.split()
        if len(words) == 1:
            return name[:max_length - 3] + "..."
        short_name = "".join(word[0] for word in words if word)
        if len(short_name) > max_length:
            return short_name[:max_length - 3] + "..."
        return short_name

    # 6.1.5.  Hệ thống gọi phương thức create_area_chart() để tạo biểu đồ thống kê điểm danh trong SystemStatistics

    def create_area_chart(self):
        figure = Figure(figsize=(10, 6))
        ax = figure.add_subplot(111)

    # 6.1.6. Hệ thống gọi get_class_statistics() của đối tượng DatabaseManagement để lấy dữ liệu thống kê.
        class_names, hoc_sinh_co_diem_danh, hoc_sinh_vang = self.db_manager.get_class_statistics()

        # 6.1.9. DatabaseManagement trả dữ liệu thống kê về cho SystemStatistics thông qua các biến x, sumst, miss
        x = [self.shorten_class_name(name) for name in class_names.values()]
        # 6.1.10. Trong tab SystemStatistics, create_area_chart() kiểm tra nếu không có dữ liệu lớp học x (x rỗng)
        if not x:
            #6.2.1 Hiển thị thông báo "Không có dữ liệu để hiển thị" trên biểu đồ ax : Figure
            ax.text(0.5, 0.5, "Không có dữ liệu để hiển thị",
                    horizontalalignment='center', verticalalignment='center',
                    transform=ax.transAxes, fontsize=12)
            ax.set_xticks([])
            ax.set_yticks([])
            figure.tight_layout()
            return FigureCanvas(figure)

        sumst = [hoc_sinh_co_diem_danh.get(class_name, 0) for class_name in class_names.values()]
        miss = [hoc_sinh_vang.get(class_name, 0) for class_name in class_names.values()]

        indices = list(range(len(x)))
        width = 0.35

        # 6.1.11. Phương thức bar() sử dụng dữ liệu trả về để vẽ biểu đồ cột hiển thị số học sinh có điểm danh và vắng theo từng lớp trên ax:Figure
        # Vẽ biểu đồ
        if any(sumst):
            ax.bar([i - width / 2 for i in indices], sumst, width=width, color="#F29CA3", label="Số học sinh điểm danh")
        if any(miss):
            ax.bar([i + width / 2 for i in indices], miss, width=width, color="#64113F", label="Số học sinh vắng")

        ax.set_xticks(indices)
        ax.set_xticklabels(x, rotation=45, ha="right", fontsize=10)
        ax.set_title("Thống kê học sinh theo lớp học", fontsize=18, fontweight="bold", pad=20)
        ax.set_ylabel("Số học sinh", fontsize=12, labelpad=10)
        ax.set_xlabel("Lớp học", fontsize=12, labelpad=10)
        ax.tick_params(axis="both", labelsize=10)

        ax.legend(
            loc="upper right",
            bbox_to_anchor=(1.0, -0.2),
            ncol=1,
            fontsize=10,
            frameon=True
        )

        ax.set_facecolor("#ffffff")
        figure.subplots_adjust(bottom=0.25, left=0.1, right=0.9, top=0.9)
        figure.set_facecolor("#ffffff")
        ax.grid(color="#0E131F", linestyle="--", linewidth=0.5, alpha=0.3)
        figure.tight_layout()

        canvas = FigureCanvas(figure)
        return canvas

    def reload_chart(self):
        while self.chart_layout.count() > 0:
            widget = self.chart_layout.takeAt(0).widget()
            if widget is not None:
                widget.deleteLater()
        self.chart_canvas = self.create_area_chart()
        self.chart_layout.addWidget(self.chart_canvas)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SystemStatistics(None)
    window.show()
    sys.exit(app.exec())