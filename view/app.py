import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import io
from PIL import Image
import Global

# Import dữ liệu giả
from mock_data import (
    mock_classes, mock_students, mock_class_statistics, 
    mock_attendance_data, mock_no_attendance_data, 
    mock_student_details, mock_sessions
)

# Thiết lập tiêu đề và giao diện chính
st.set_page_config(page_title="Face Recognition System", layout="wide")
st.title("Hệ thống nhận diện khuôn mặt")

# Hiển thị thời gian và ngày
current_time = datetime.now().strftime("%H:%M:%S")
current_date = datetime.now().strftime("%d/%m/%Y")
col1, col2, col3 = st.columns([1, 3, 1])
with col1:
    st.write(f"**Thời gian:** {current_time}")
    st.write(f"**Ngày:** {current_date}")
with col2:
    st.empty()
with col3:
    if st.button("Đăng xuất"):
        Global.GLOBAL_ACCOUNT = None
        Global.GLOBAL_ACCOUNTID = None
        st.session_state["logged_in"] = False
        st.experimental_rerun()

# Tạo các tab chính
tabs = st.tabs(["Thống kê", "Quản lý học sinh", "Quản lý lớp học", "Nhận diện"])

# Tab 1: Thống kê
with tabs[0]:
    st.header("Thống kê học sinh theo lớp học")
    class_names, hoc_sinh_co_diem_danh, hoc_sinh_vang = mock_class_statistics
    x = [name for name in class_names.values()]
    sumst = [hoc_sinh_co_diem_danh.get(class_name, 0) for class_name in class_names.values()]
    miss = [hoc_sinh_vang.get(class_name, 0) for class_name in class_names.values()]

    if not x:
        st.write("Không có dữ liệu để hiển thị")
    else:
        fig, ax = plt.subplots()
        indices = range(len(x))
        width = 0.35
        if any(sumst):
            ax.bar([i - width / 2 for i in indices], sumst, width, color="#F29CA3", label="Số học sinh điểm danh")
        if any(miss):
            ax.bar([i + width / 2 for i in indices], miss, width, color="#64113F", label="Số học sinh vắng")
        ax.set_xticks(indices)
        ax.set_xticklabels(x, rotation=45, ha="right")
        ax.set_title("Thống kê học sinh theo lớp học")
        ax.set_ylabel("Số học sinh")
        ax.set_xlabel("Lớp học")
        ax.legend()
        st.pyplot(fig)

    # Sub-tabs cho danh sách học sinh điểm danh và vắng
    sub_tabs = st.tabs(["Học sinh đã điểm danh", "Học sinh vắng"])
    with sub_tabs[0]:
        st.subheader("Học sinh đã điểm danh")
        if not mock_attendance_data:
            st.write("Không có dữ liệu để hiển thị")
        else:
            df = pd.DataFrame(mock_attendance_data, columns=["Tên lớp", "ID SV", "Tên Học sinh", "Buổi", "Ngày"])
            st.dataframe(df)

            # Tìm kiếm và xuất Excel
            search_text = st.text_input("Tìm kiếm ID học sinh hoặc tên lớp (Đã điểm danh):", key="attendance_search")
            if search_text:
                filtered_df = df[df["ID SV"].astype(str).str.contains(search_text, case=False) | 
                                df["Tên lớp"].str.contains(search_text, case=False)]
                st.dataframe(filtered_df)
            if st.button("Xuất Excel (Đã điểm danh)"):
                buffer = io.BytesIO()
                with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
                    df.to_excel(writer, index=False, sheet_name="HocSinhDiemDanh")
                st.download_button(
                    label="Tải xuống file Excel",
                    data=buffer.getvalue(),
                    file_name="hoc_sinh_diem_danh.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )

    with sub_tabs[1]:
        st.subheader("Học sinh vắng")
        if not mock_no_attendance_data:
            st.write("Không có dữ liệu để hiển thị")
        else:
            df = pd.DataFrame(mock_no_attendance_data, columns=["Tên lớp", "ID SV", "Tên Học sinh", "Buổi", "Ngày"])
            st.dataframe(df)

            # Tìm kiếm và xuất Excel
            search_text = st.text_input("Tìm kiếm ID học sinh hoặc tên lớp (Vắng):", key="no_attendance_search")
            if search_text:
                filtered_df = df[df["ID SV"].astype(str).str.contains(search_text, case=False) | 
                                df["Tên lớp"].str.contains(search_text, case=False)]
                st.dataframe(filtered_df)
            if st.button("Xuất Excel (Vắng)"):
                buffer = io.BytesIO()
                with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
                    df.to_excel(writer, index=False, sheet_name="HocSinhVang")
                st.download_button(
                    label="Tải xuống file Excel",
                    data=buffer.getvalue(),
                    file_name="hoc_sinh_vang.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )

# Tab 2: Quản lý học sinh
with tabs[1]:
    st.header("Quản lý thông tin sinh viên")
    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("Thông tin học sinh")
        student_id = st.text_input("ID Học sinh", key="student_id")
        name = st.text_input("Tên Học sinh", key="student_name")
        cccd = st.text_input("CCCD", key="student_cccd")
        gender = st.selectbox("Giới tính", ["nam", "nữ"], key="student_gender")
        dob = st.date_input("Ngày sinh", value=datetime.today(), key="student_dob")
        class_name = st.text_input("Lớp học", key="student_class")
        
        if st.button("Sửa học sinh"):
            if student_id and name and cccd and class_name:
                st.success(f"Đã sửa thông tin học sinh với ID {student_id} thành công (giả lập).")
            else:
                st.error("Vui lòng nhập đầy đủ thông tin!")

        if st.button("Xóa học sinh"):
            if student_id:
                st.success(f"Đã xóa học sinh với ID {student_id} thành công (giả lập).")
            else:
                st.error("Vui lòng nhập ID học sinh để xóa!")

    with col2:
        st.subheader("Hệ thống tìm kiếm")
        class_options = ["Tất cả các lớp"] + [c[1] for c in mock_classes]
        selected_class = st.selectbox("Chọn lớp:", class_options, key="class_select")
        search_id = st.text_input("Tìm kiếm theo ID:", key="search_student_id")
        
        if st.button("Tìm kiếm học sinh"):
            if search_id:
                if selected_class == "Tất cả các lớp":
                    results = [s for s in mock_students if str(s[0]) == search_id]
                else:
                    results = [s for s in mock_students if str(s[0]) == search_id and s[4] == selected_class]
                
                if results:
                    df = pd.DataFrame(results, columns=["ID Học sinh", "Họ tên", "CCCD", "Giới tính", "Lớp"])
                    st.dataframe(df)
                else:
                    st.error(f"Không tìm thấy học sinh với ID {search_id}.")
            else:
                st.error("Vui lòng nhập ID học sinh để tìm kiếm!")

        if selected_class == "Tất cả các lớp":
            results = mock_students
        else:
            results = [s for s in mock_students if s[4] == selected_class]

        if results:
            df = pd.DataFrame(results, columns=["ID Học sinh", "Họ tên", "CCCD", "Giới tính", "Lớp"])
            st.dataframe(df)

# Tab 3: Quản lý lớp học
with tabs[2]:
    st.header("Quản lý thông tin lớp học")
    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("Thông tin buổi học")
        session_id = st.text_input("ID Buổi học", key="session_id")
        session_name = st.text_input("Tên Buổi học", key="session_name")
        start_time = st.text_input("Giờ bắt đầu", key="start_time")
        end_time = st.text_input("Giờ kết thúc", key="end_time")
        session_date = st.date_input("Ngày", value=datetime.today(), key="session_date")
        class_names = [c[1] for c in mock_classes]
        class_name = st.selectbox("Lớp", class_names, key="session_class")

        if st.button("Lưu buổi học"):
            if session_id and session_name and start_time and end_time:
                st.success("Buổi học đã được lưu thành công (giả lập).")
            else:
                st.error("Vui lòng nhập đầy đủ thông tin!")

        if st.button("Sửa buổi học"):
            if not session_id:
                st.error("ID buổi học không được để trống!")
            else:
                st.success(f"Sửa thông tin buổi học với ID {session_id} thành công (giả lập).")

        if st.button("Xóa buổi học"):
            if session_id:
                st.success(f"Đã xóa buổi học với ID {session_id} thành công (giả lập).")
            else:
                st.error("Vui lòng nhập ID buổi học để xóa!")

        if st.button("Thêm lớp học"):
            new_class_name = st.text_input("Nhập tên lớp học mới:", key="new_class_name")
            if new_class_name:
                st.success("Lớp học đã được thêm thành công (giả lập).")

    with col2:
        st.subheader("Hệ thống tìm kiếm")
        search_keyword = st.text_input("Tìm kiếm theo tên lớp:", key="search_session")
        if st.button("Tìm kiếm buổi học"):
            if search_keyword:
                results = [s for s in mock_sessions if search_keyword.lower() in s[2].lower()]
                if results:
                    df = pd.DataFrame(results, columns=["ID", "Tên buổi học", "Lớp", "Ngày", "Giờ bắt đầu", "Giờ kết thúc"])
                    st.dataframe(df)
                else:
                    st.error("Không tìm thấy buổi học nào với từ khóa này.")
            else:
                st.error("Vui lòng nhập từ khóa để tìm kiếm!")

        if st.button("Xem tất cả buổi học"):
            if mock_sessions:
                df = pd.DataFrame(mock_sessions, columns=["ID", "Tên buổi học", "Lớp", "Ngày", "Giờ bắt đầu", "Giờ kết thúc"])
                st.dataframe(df)
            else:
                st.error("Không có buổi học nào trong hệ thống.")

# Tab 4: Nhận diện
with tabs[3]:
    st.header("Nhận diện sinh viên")
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("Màn hình nhận diện")
        class_name = st.text_input("Lớp:", value="Lớp 10A", key="recognition_class", disabled=True)
        session_name = st.text_input("Buổi:", value="Buổi 1", key="recognition_session", disabled=True)

        uploaded_file = st.file_uploader("Tải ảnh lên", type=["png", "jpg", "jpeg", "bmp"])
        if uploaded_file:
            image = Image.open(uploaded_file)
            st.image(image, caption="Ảnh đã tải lên", use_column_width=True)

    with col2:
        st.subheader("Nhận diện sinh viên")
        st.image([], caption="Khuôn mặt nhận diện", use_column_width=True)
        st.text_input("ID sinh viên:", value="1", disabled=True, key="recognition_id")
        st.text_input("Tên sinh viên:", value="Nguyễn Văn A", disabled=True, key="recognition_name")
        st.text_input("Thời gian:", value=current_time, disabled=True, key="recognition_time")

    st.subheader("Thông tin điểm danh")
    if "attendance_data" not in st.session_state:
        st.session_state["attendance_data"] = []
    if st.button("Nhận diện lại"):
        st.session_state["attendance_data"] = []
    df = pd.DataFrame(st.session_state["attendance_data"], columns=["ID", "Tên sinh viên", "Thời gian"])
    st.dataframe(df)

    if st.button("Lưu danh sách"):
        st.success("Danh sách đã được lưu (giả lập)!")
        st.session_state["attendance_data"] = []