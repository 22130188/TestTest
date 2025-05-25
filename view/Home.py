import sys

from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import (
    QApplication, QWidget, QGridLayout, QTabWidget, QPushButton, QLabel, QFrame, QHBoxLayout, QVBoxLayout, QStackedWidget
)
from PyQt6.QtCore import Qt, QTimer, QTime, QDate, QSize


import Global
from RecognitionStudentView import RecognitionStudentView
from StudentInformationManagement import StudentInformationManagement
from SystemStatistics import SystemStatistics
from ClassManagementView import ClassManagementView

    # 6.1.0. Giáo viên đang đứng tại giao diện Home (lớp Home), nơi hiển thị danh sách các chức năng chính của hệ thống dưới dạng các tab.
class Home(QWidget):
    def __init__(self,stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.setWindowTitle('Face Recognition System')
        self.setGeometry(0, 0, 1200, 700)
        self.setStyleSheet("color: black;")
        self.init_ui()

    def init_ui(self):
        # Một QVBoxLayout (self.main_layout) được tạo và gán cho main_widget.
        self.central_widget = QWidget(self)
        self.central_widget.setFixedSize(1200, 700)
        self.central_widget.setStyleSheet("background-color: lightblue;")

        self.panel = QFrame(self.central_widget)
        self.panel.setGeometry(15, 15, 1150, 650)
        self.panel.setStyleSheet("""
                           background-color: white;
                           border-radius: 10px;
                       """)
        self.header_panel = QFrame(self.panel)
        self.header_panel.setGeometry(0, 0, 1150, 50)
        self.header_panel.setStyleSheet("""
                            background-color: white;
                            border-top-right-radius: 10px;
                            border-top-left-radius: 10px;
                            border-bottom: 1px solid black;
                        """)


        self.clock_icon = QLabel()
        self.clock_icon.setPixmap(QPixmap('../Image/clock-icon.png').scaled(35, 30))
        self.clock_icon.setStyleSheet("border: none;")

        self.time_date_panel = QFrame(self.header_panel)
        self.time_date_panel.setGeometry(50, 5, 150, 40)
        self.time_date_layout = QVBoxLayout(self.time_date_panel)
        self.time_date_layout.setContentsMargins(0, 0, 0, 0)
        self.time_date_panel.setStyleSheet("border: none;")

        self.time_label = QLabel()
        self.time_label.setStyleSheet("font-size: 12px; font-weight: bold; border: none;")
        self.time_date_layout.addWidget(self.time_label)

        self.date_label = QLabel()
        self.date_label.setStyleSheet("font-size: 12px; font-weight: bold; border: none;")
        self.time_date_layout.addWidget(self.date_label)


        self.title_label = QLabel("Hệ thống nhận diện khuôn mặt")
        self.title_label.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.title_panel = QFrame(self.header_panel)
        self.title_panel.setGeometry(400, 5, 550, 40)
        self.title_panel.setStyleSheet("border: none;")

        self.title_layout = QHBoxLayout(self.title_panel)
        self.title_layout.setContentsMargins(0, 0, 0, 0)
        self.title_layout.addWidget(self.title_label)

        # Tạo nút logout
        self.logout_button = QPushButton(self.header_panel)
        self.logout_button.setIcon(QIcon("../Image/logout_icon.png"))  # Đường dẫn đến icon
        self.logout_button.setIconSize(QSize(30, 30))  # Kích thước icon
        self.logout_button.setStyleSheet("font-size: 14px; font-weight: bold; padding: 5px;")
        self.logout_button.setStyleSheet("border: none;")
        self.logout_button.clicked.connect(self.logout_action)

        # Sử dụng QHBoxLayout cho header_panel
        self.header_layout = QHBoxLayout(self.header_panel)
        self.header_layout.setContentsMargins(10, 5, 10, 5)  # Căn chỉnh lề
        self.header_layout.setSpacing(10)

        # Thêm các phần tử vào header_layout
        self.header_layout.addWidget(self.clock_icon)  # Đồng hồ
        self.header_layout.addWidget(self.time_date_panel)  # Ngày tháng
        self.header_layout.addStretch()  # Đẩy các phần tử còn lại sang trái
        self.header_layout.addWidget(self.title_panel)  # Tiêu đề
        self.header_layout.addStretch()  # Đẩy nút logout sang phải
        self.header_layout.addWidget(self.logout_button)  # Nút logout

        self.main_widget = QWidget(self.panel)
        self.main_widget.setStyleSheet("background-color: white;")
        self.main_widget.setGeometry(0, 50, 1150, 600)

        # Layout chính cho main_widget
        self.main_layout = QVBoxLayout(self.main_widget)
        self.main_widget.setLayout(self.main_layout)

        # Tạo QTabWidget
        self.header_layout = QHBoxLayout(self.header_panel)
        self.header_layout.setContentsMargins(10, 5, 10, 5)
        self.header_layout.setSpacing(10)
        self.header_layout.addWidget(self.clock_icon)
        self.header_layout.addWidget(self.time_date_panel)
        self.header_layout.addStretch()
        self.header_layout.addWidget(self.title_panel)
        self.header_layout.addStretch()

        #Tạo main_widget và gán layout
        self.main_widget = QWidget(self.panel)
        self.main_widget.setStyleSheet("background-color: white;")
        self.main_widget.setGeometry(0, 50, 1150, 600)
        self.main_layout = QVBoxLayout(self.main_widget)

        # Tạo một QTabWidget (self.tab) và thiết lập style cho nó với CSS để hiển thị tab đang chọn với nền trắng và đường viền màu xanh (#0078D7).
        self.tab = QTabWidget(self.main_widget)
        self.tab.setStyleSheet("""
            QTabBar::tab:selected { 
                background: white; 
                border-bottom: 1px solid #0078D7;
                padding: 5px;
            }
        """)
        self.ClassManagementView = ClassManagementView(self)

        # Thêm các trang vào tab
        # self.RecognitionStudent_page = RecognitionStudentView(self)
        self.StudentInformationManagement = StudentInformationManagement(self)
        self.SystemStatistics = SystemStatistics(self)

        self.tab.addTab(self.SystemStatistics, 'Thống kê')
        self.tab.addTab(self.StudentInformationManagement, 'Quản lí học sinh')
        # self.tab.addTab(self.RecognitionStudent_page, 'Nhận diện')

        # Thêm QTabWidget vào layout chính
        self.main_layout.addWidget(self.tab)

        # Đồng hồ cập nhật
        timer = QTimer(self)
        timer.timeout.connect(self.update_time)
        timer.start(1000)

        self.update_time()

    def logout_action(self):

        self.stacked_widget.setCurrentIndex(0)
        Global.GLOBAL_ACCOUNT = None
        Global.GLOBAL_ACCOUNTID = None

    def update_time(self):
        self.time_label.setText(QTime.currentTime().toString("hh:mm:ss"))
        self.date_label.setText(QDate.currentDate().toString("dd/MM/yyyy"))
        # Khởi tạo một đối tượng StudentInformationManagement.
        self.StudentInformationManagement = StudentInformationManagement(self)
        # Khởi tạo một đối tượng SystemStatistics.
        self.SystemStatistics = SystemStatistics(self)

        self.tab.addTab(self.ClassManagementView, 'Quản lí lớp học')

        # QTabWidget thêm StudentInformationManagement làm tab mới với tên "Quản lí sinh viên" thông qua phương thức addTab.
        self.tab.addTab(self.StudentInformationManagement, 'Quản lí sinh viên')

    # 6.1.1. Giáo viên chọn tab "Thống kê" trên QTabWidget (self.tab) của giao diện Home.
        self.tab.addTab(self.SystemStatistics, 'Thống kê')


        # QTabWidget được thêm vào main_layout thông qua phương thức addWidget.
        self.main_layout.addWidget(self.tab)

        timer = QTimer(self)
        timer.timeout.connect(self.update_time)
        timer.start(1000)
        self.update_time()

    def update_time(self):
        self.time_label.setText(QTime.currentTime().toString("hh:mm:ss"))
        self.date_label.setText(QDate.currentDate().toString("dd/MM/yyyy"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    from PyQt6.QtWidgets import QStackedWidget
    stacked = QStackedWidget()
    home = Home(stacked)
    home.show()
    sys.exit(app.exec())

    
