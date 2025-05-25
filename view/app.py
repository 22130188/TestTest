import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import io
from PIL import Image
import Global
from mock_data import (
    mock_classes, mock_students, mock_class_statistics, 
    mock_attendance_data, mock_no_attendance_data, 
    mock_student_details, mock_sessions, mock_recognition_data
)

# CSS tùy chỉnh để tái tạo giao diện PyQt6
st.markdown("""
    <style>
    /* Màu nền tổng thể */
    .main {
        background-color: lightblue;
        padding: 0;
        margin: 0;
        min-height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    
    /* Panel chính */
    .panel {
        background-color: white;
        border-radius: 10px;
        width: 1200px;
        height: 700px;
        box-sizing: border-box;
        display: flex;
        flex-direction: column;
    }
    
    /* Header panel */
    .header-panel {
        background-color: white;
        border-top-right-radius: 10px;
        border-top-left-radius: 10px;
        border-bottom: 1px solid black;
        display: flex;
        align-items: center;
        padding: 5px 10px;
        height: 50px;
        box-sizing: border-box;
    }
    
    .header-panel .time-date {
        font-size: 12px;
        font-weight: bold;
        width: 150px;
    }
    
    .header-panel .title {
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        flex-grow: 1;
    }
    
    .header-panel .logout-btn {
        width: 100px;
        text-align: right;
    }
    
    .header-panel .logout-btn button {
        font-size: 14px;
        font-weight: bold;
        padding: 5px 10px;
        background-color: transparent;
        border: none;
        cursor: pointer;
    }
    
    /* Main widget */
    .main-widget {
        background-color: white;
        width: 1150px;
        height: 600px;
        margin: 25px auto 0 auto;
        box-sizing: border-box;
        overflow-y: auto;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        padding: 0 25px;
    }
    
    .stTabs [data-baseweb="tab"] {
        padding: 5px 10px;
        border-bottom: 1px solid transparent;
        font-size: 14px;
        font-weight: bold;
    }
    
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background-color: white;
        border-bottom: 1px solid #0078D7;
    }
    
    /* Sub-tabs */
    .sub-tabs .stTabs [data-baseweb="tab-list"] {
        padding: 0 10px;
    }
    
    .sub-tabs .stTabs [data-baseweb="tab"] {
        padding: 5px 10px;
        font-size: 12px;
    }
    
    /* Biểu đồ */
    .chart-container {
        background-color: #ffffff;
        border: 2px solid #4faaff;
        border-radius: 10px;
        padding: 10px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
        margin: 10px;
        width: fit-content;
        height: fit-content;
    }
    
    /* Bảng dữ liệu */
    .stDataFrame {
        width: 100%;
        margin: 10px 0;
    }
    
    .stDataFrame table {
        width: 100%;
        border-collapse: collapse;
        font-size: 12px;
    }
    
    .stDataFrame th, .stDataFrame td {
        border: 1px solid #CCCCCC;
        padding: 4px;
        text-align: center;
    }
    
    .stDataFrame tr:nth-child(even) {
        background-color: #f6f6f6;
    }
    
    /* Nút */
    button[kind="primary"] {
        background-color: black;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 5px 10px;
        font-size: 12px;
        width: 100%;
        box-sizing: border-box;
    }
    
    button[kind="primary"]:hover {
        background-color: #333333;
        color: white;
    }
    
    /* Input */
    .stTextInput > div > input {
        border: 1px solid #CCCCCC;
        border-radius: 4px;
        padding: 5px;
        font-size: 12px;
        width: 100%;
        box-sizing: border-box;
    }
    
    /* Selectbox */
    .stSelectbox > div > div {
        border: 1px solid #CCCCCC;
        border-radius: 4px;
        padding: 4px;
        font-size: 12px;
    }
    
    /* DateInput */
    .stDateInput > div > input {
        border: 1px solid #CCCCCC;
        border-radius: 4px;
        padding: 5px;
        font-size: 12px;
        width: 100%;
    }
    
    /* Group box */
    .group-box {
        border: 1px solid gray;
        padding: 10px;
        margin: 10px;
        border-radius: 5px;
        background-color: white;
        height: calc(100% - 40px);
        box-sizing: border-box;
    }
    
    .group-box-title {
        font-weight: bold;
        font-size: 14px;
        margin-bottom: 10px;
        text-align: center;
    }
    
    /* Khu vực ảnh nhận diện */
    .recognition-image {
        width: 700px;
        height: 360px;
        border: 1px solid black;
        margin: 10px 0;
        display: flex;
        justify-content: center;
        align-items: center;
        background-color: #f0f0f0;
    }
    
    .recognition-image img {
        max-width: 100%;
        max-height: 100%;
        object-fit: contain;
    }
    
    /* Khu vực ảnh khuôn mặt */
    .face-image {
        width: 150px;
        height: 150px;
        border: 1px solid gray;
        margin: 10px auto;
        display: block;
        object-fit: cover;
    }
    
    /* Thanh tìm kiếm */
    .search-bar {
        display: flex;
        gap: 10px;
        margin-bottom: 10px;
        align-items: center;
    }
    
    .search-bar .stTextInput {
        flex-grow: 1;
    }
    
    /* Cột trong group box */
    .group-box-col {
        height: 100%;
    }
    
    /* Khoảng cách giữa các phần tử */
    .spacer {
        height: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Thiết lập giao diện chính
st.markdown('<div class="main">', unsafe_allow_html=True)
st.markdown('<div class="panel">', unsafe_allow_html=True)

# Header panel
st.markdown('<div class="header-panel">', unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 3, 1])
with col1:
    current_time = datetime.now().strftime("%H:%M:%S")
    current_date = datetime.now().strftime("%d/%m/%Y")
    st.markdown(f'<div class="time-date">{current_time}<br>{current_date}</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="title">Hệ thống nhận diện khuôn mặt</div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="logout-btn">', unsafe_allow_html=True)
    if st.button("Đăng xuất", key="logout"):
        Global.GLOBAL_ACCOUNT = None
        Global.GLOBAL_ACCOUNTID = None
        st.session_state["logged_in"] = False
        st.experimental_rerun()
    st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Main widget
st.markdown('<div class="main-widget">', unsafe_allow_html=True)

# Tạo các tab chính
tabs = st.tabs(["Thống kê", "Quản lý học sinh", "Quản lý lớp học", "Nhận diện"])

# Tab 1: Thống kê
with tabs[0]:
    st.markdown('<div class="sub-tabs">', unsafe_allow_html=True)
    sub_tabs = st.tabs(["Thống kê", "Học sinh đã điểm danh", "Học sinh vắng"])

    # Tab Thống kê
    with sub_tabs[0]:
        st.subheader("Thống kê học sinh theo lớp học")
        class_names, hoc_sinh_co_diem_danh, hoc_sinh_vang = mock_class_statistics
        x = [name for name in class_names.values()]
        sumst = [hoc_sinh_co_diem_danh.get(class_name, 0) for class_name in class_names.values()]
        miss = [hoc_sinh_vang.get(class_name, 0) for class_name in class_names.values()]

        if not x:
            st.write("Không có dữ liệu để hiển thị")
        else:
            st.markdown('<div class="chart-container">', unsafe_allow_html=True)
            fig, ax = plt.subplots(figsize=(10, 6))
            indices = range(len(x))
            width = 0.35
            if any(sumst):
                ax.bar([i - width / 2 for i in indices], sumst, width, color="#F29CA3", label="Số học sinh điểm danh")
            if any(miss):
                ax.bar([i + width / 2 for i in indices], miss, width, color="#64113F", label="Số học sinh vắng")
            ax.set_xticks(indices)
            ax.set_xticklabels(x, rotation=45, ha="right", fontsize=10)
            ax.set_title("Thống kê học sinh theo lớp học", fontsize=18, fontweight="bold", pad=20)
            ax.set_ylabel("Số học sinh", fontsize=12, labelpad=10)
            ax.set_xlabel("Lớp học", fontsize=12, labelpad=10)
            ax.legend(loc="upper right", bbox_to_anchor=(1.0, -0.2), ncol=1, fontsize=10, frameon=True)
            ax.set_facecolor("#ffffff")
            fig.subplots_adjust(bottom=0.25, left=0.1, right=0.9, top=0.9)
            fig.set_facecolor("#ffffff")
            ax.grid(color="#0E131F", linestyle="--", linewidth=0.5, alpha=0.3)
            st.pyplot(fig)
            st.markdown('</div>', unsafe_allow_html=True)

    # Tab Học sinh đã điểm danh
    with sub_tabs[1]:
        st.subheader("Học sinh đã điểm danh")
        if not mock_attendance_data:
            st.write("Không có dữ liệu để hiển thị")
        else:
            df = pd.DataFrame(mock_attendance_data, columns=["Tên lớp", "ID SV", "Tên Học sinh", "Buổi", "Ngày"])
            
            st.markdown('<div class="search-bar">', unsafe_allow_html=True)
            search_col, button_col1, button_col2, button_col3 = st.columns([3, 1, 1, 1])
            with search_col:
                search_text = st.text_input("ID Học sinh hoặc tên lớp học", key="attendance_search")
            with button_col1:
                st.button("Tìm kiếm", key="attendance_search_btn")
            with button_col2:
                st.button("Xem tất cả", key="attendance_view_all")
            with button_col3:
                if st.button("Xuất Excel", key="attendance_export"):
                    buffer = io.BytesIO()
                    with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
                        df.to_excel(writer, index=False, sheet_name="HocSinhDiemDanh")
                    st.download_button(
                        label="Tải xuống file Excel",
                        data=buffer.getvalue(),
                        file_name="hoc_sinh_diem_danh.xlsx",
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    )
            st.markdown('</div>', unsafe_allow_html=True)
            
            if search_text:
                filtered_df = df[df["ID SV"].astype(str).str.contains(search_text, case=False) | 
                                df["Tên lớp"].str.contains(search_text, case=False)]
                st.dataframe(filtered_df, use_container_width=True)
            else:
                st.dataframe(df, use_container_width=True)

    # Tab Học sinh vắng
    with sub_tabs[2]:
        st.subheader("Học sinh vắng")
        if not mock_no_attendance_data:
            st.write("Không có dữ liệu để hiển thị")
        else:
            df = pd.DataFrame(mock_no_attendance_data, columns=["Tên lớp", "ID SV", "Tên Học sinh", "Buổi", "Ngày"])
            
            st.markdown('<div class="search-bar">', unsafe_allow_html=True)
            search_col, button_col1, button_col2, button_col3 = st.columns([3, 1, 1, 1])
            with search_col:
                search_text = st.text_input("ID Học sinh hoặc tên lớp học", key="no_attendance_search")
            with button_col1:
                st.button("Tìm kiếm", key="no_attendance_search_btn")
            with button_col2:
                st.button("Xem tất cả", key="no_attendance_view_all")
            with button_col3:
                if st.button("Xuất Excel", key="no_attendance_export"):
                    buffer = io.BytesIO()
                    with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
                        df.to_excel(writer, index=False, sheet_name="HocSinhVang")
                    st.download_button(
                        label="Tải xuống file Excel",
                        data=buffer.getvalue(),
                        file_name="hoc_sinh_vang.xlsx",
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    )
            st.markdown('</div>', unsafe_allow_html=True)
            
            if search_text:
                filtered_df = df[df["ID SV"].astype(str).str.contains(search_text, case=False) | 
                                df["Tên lớp"].str.contains(search_text, case=False)]
                st.dataframe(filtered_df, use_container_width=True)
            else:
                st.dataframe(df, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Tab 2: Quản lý học sinh
with tabs[1]:
    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown('<div class="group-box group-box-col">', unsafe_allow_html=True)
        st.markdown('<div class="group-box-title">Thông tin Học sinh</div>', unsafe_allow_html=True)
        
        st.text_input("ID Học sinh:", key="student_id")
        st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
        st.text_input("Tên Học sinh:", key="student_name")
        st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
        st.text_input("Lớp học:", key="student_class")
        st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
        st.text_input("CCCD:", key="student_cccd")
        st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
        st.selectbox("Giới tính:", ["male", "female"], key="student_gender")
        st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
        st.date_input("Ngày sinh:", value=datetime.today(), key="student_dob")
        st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
        
        btn_col1, btn_col2 = st.columns(2)
        with btn_col1:
            if st.button("Sửa", key="edit_student"):
                st.success("Đã sửa thông tin học sinh (giả lập).")
        with btn_col2:
            if st.button("Xóa", key="delete_student"):
                st.success("Đã xóa học sinh (giả lập).")
        
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="group-box group-box-col">', unsafe_allow_html=True)
        st.markdown('<div class="group-box-title">Hệ Thống Tìm kiếm</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="search-bar">', unsafe_allow_html=True)
        filter_col, search_col, btn_col = st.columns([2, 2, 1])
        with filter_col:
            class_options = ["Tất cả các lớp"] + [c[1] for c in mock_classes]
            selected_class = st.selectbox("Chọn lớp:", class_options, key="class_select")
        with search_col:
            search_id = st.text_input("Tìm kiếm theo ID:", key="search_student_id")
        with btn_col:
            st.button("Tìm kiếm", key="search_student_btn")
        st.markdown('</div>', unsafe_allow_html=True)
        
        if search_id:
            if selected_class == "Tất cả các lớp":
                results = [s for s in mock_students if str(s[0]) == search_id]
            else:
                results = [s for s in mock_students if str(s[0]) == search_id and s[4] == selected_class]
        else:
            if selected_class == "Tất cả các lớp":
                results = mock_students
            else:
                results = [s for s in mock_students if s[4] == selected_class]

        if results:
            df = pd.DataFrame(results, columns=["ID Học sinh", "Họ tên", "CCCD", "Giới tính", "Lớp"])
            st.dataframe(df, use_container_width=True)
        else:
            st.write("Không có dữ liệu để hiển thị")
        
        st.markdown('</div>', unsafe_allow_html=True)

# Tab 3: Quản lý lớp học
with tabs[2]:
    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown('<div class="group-box group-box-col">', unsafe_allow_html=True)
        st.markdown('<div class="group-box-title">Thông tin buổi học</div>', unsafe_allow_html=True)
        
        st.text_input("ID Buổi học:", key="session_id")
        st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
        st.text_input("Tên Buổi học:", key="session_name")
        st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
        st.text_input("Giờ bắt đầu:", key="start_time")
        st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
        st.text_input("Giờ kết thúc:", key="end_time")
        st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
        st.date_input("Ngày:", value=datetime.today(), key="session_date")
        st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
        class_names = [c[1] for c in mock_classes]
        st.selectbox("Lớp:", class_names, key="session_class")
        st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

        btn_col1, btn_col2, btn_col3 = st.columns(3)
        with btn_col1:
            if st.button("Import", key="import_session"):
                st.success("Dữ liệu đã được import (giả lập).")
        with btn_col2:
            if st.button("Thêm lớp học", key="add_class"):
                new_class_name = st.text_input("Nhập tên lớp học mới:", key="new_class_name")
                if new_class_name:
                    st.success("Lớp học đã được thêm (giả lập).")
        with btn_col3:
            if st.button("Lưu", key="save_session"):
                st.success("Buổi học đã được lưu (giả lập).")

        st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
        btn_col4, btn_col5 = st.columns(2)
        with btn_col4:
            if st.button("Sửa", key="edit_session"):
                st.success("Đã sửa buổi học (giả lập).")
        with btn_col5:
            if st.button("Xóa", key="delete_session"):
                st.success("Đã xóa buổi học (giả lập).")

        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="group-box group-box-col">', unsafe_allow_html=True)
        st.markdown('<div class="group-box-title">Hệ Thống Tìm kiếm</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="search-bar">', unsafe_allow_html=True)
        search_col, btn_col1, btn_col2 = st.columns([3, 1, 1])
        with search_col:
            search_keyword = st.text_input("Tìm kiếm theo tên lớp:", key="search_session")
        with btn_col1:
            st.button("Tìm kiếm", key="search_session_btn")
        with btn_col2:
            st.button("Xem tất cả", key="view_all_sessions")
        st.markdown('</div>', unsafe_allow_html=True)

        if search_keyword:
            results = [s for s in mock_sessions if search_keyword.lower() in s[2].lower()]
        else:
            results = mock_sessions

        if results:
            df = pd.DataFrame(results, columns=["ID", "Tên buổi học", "Lớp", "Ngày", "Giờ bắt đầu", "Giờ kết thúc"])
            st.dataframe(df, use_container_width=True)
        else:
            st.write("Không có dữ liệu để hiển thị")

        st.markdown('</div>', unsafe_allow_html=True)

# Tab 4: Nhận diện
with tabs[3]:
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown('<div class="group-box group-box-col">', unsafe_allow_html=True)
        st.markdown('<div class="group-box-title">Màn hình nhận diện</div>', unsafe_allow_html=True)
        
        col_class, col_session = st.columns(2)
        with col_class:
            st.text_input("Lớp:", value="Cau truc du lieu", key="recognition_class", disabled=True)
        with col_session:
            st.text_input("Buổi:", value="Buoi 1", key="recognition_session", disabled=True)

        sub_tabs = st.tabs(["Nhận diện", "Thông tin điểm danh"])
        with sub_tabs[0]:
            uploaded_file = st.file_uploader("Tải ảnh lên", type=["png", "jpg", "jpeg", "bmp"])
            st.markdown('<div class="recognition-image">', unsafe_allow_html=True)
            if uploaded_file:
                image = Image.open(uploaded_file)
                st.image(image, use_column_width=True)
            else:
                st.write("Chưa có ảnh được tải lên")
            st.markdown('</div>', unsafe_allow_html=True)

        with sub_tabs[1]:
            if "attendance_data" not in st.session_state:
                st.session_state["attendance_data"] = []
            df = pd.DataFrame(st.session_state["attendance_data"], columns=["ID", "Tên sinh viên", "Thời gian"])
            st.dataframe(df, use_container_width=True)

        btn_col1, btn_col2, btn_col3 = st.columns(3)
        with btn_col1:
            if st.button("Tải Ảnh", key="load_image"):
                pass  # Đã xử lý ở file uploader
        with btn_col2:
            if st.button("Nhận diện lại", key="reset_recognition"):
                st.session_state["attendance_data"] = []
        with btn_col3:
            if st.button("Lưu danh sách", key="save_recognition"):
                st.success("Danh sách đã được lưu (giả lập)!")
                st.session_state["attendance_data"] = []

        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="group-box group-box-col">', unsafe_allow_html=True)
        st.markdown('<div class="group-box-title">Nhận diện sinh viên</div>', unsafe_allow_html=True)
        
        # Hiển thị ảnh khuôn mặt
        selected_student = mock_student_details[0]  # Giả lập học sinh đầu tiên
        if selected_student[6]:  # Kiểm tra photo_path
            st.image(selected_student[6], caption="Khuôn mặt nhận diện", width=150, output_format="auto", use_column_width=False, clamp=True)
        else:
            st.markdown('<div class="face-image"></div>', unsafe_allow_html=True)
        
        st.markdown('<div class="group-box">', unsafe_allow_html=True)
        st.markdown('<div class="group-box-title">Điểm danh thành công</div>', unsafe_allow_html=True)
        current_time = datetime.now().strftime("%H:%M:%S")
        st.text_input("ID sinh viên:", value=str(selected_student[0]), disabled=True, key="recognition_id")
        st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
        st.text_input("Tên sinh viên:", value=selected_student[1], disabled=True, key="recognition_name")
        st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
        st.text_input("Thời gian:", value=current_time, disabled=True, key="recognition_time")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # Đóng main-widget
st.markdown('</div>', unsafe_allow_html=True)  # Đóng panel
st.markdown('</div>', unsafe_allow_html=True)  # Đóng main