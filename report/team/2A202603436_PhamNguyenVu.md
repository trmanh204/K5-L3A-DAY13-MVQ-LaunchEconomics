# Báo cáo cá nhân — PhamNguyenVu-2A202603436

## 1. Thông tin thành viên

- Họ tên: Phạm Nguyên Vũ
- MSSV: 2A202603436
- Email:26ai.vupn@vinuni.edu.vn
- Vai trong nhóm: Người viết code (CP1–CP2) & Người kiểm số

## 2. Phần việc phụ trách

- **CP1 (Nhiệm vụ A):** Cài đặt môi trường Python, viết các hàm xác suất chạy lại (A1), mô hình chi phí mỗi việc thành công từ trace (A2), tách chi phí theo loại yêu cầu (A3) và tính chi phí cố định (A4) trong `src/lab13.py`.
- **CP2 (Nhiệm vụ B):** Chạy phân tích độ nhạy 9 kịch bản đơn (B1), kịch bản cặp (B2), chi phí cả hệ thống theo giới hạn chạy lại (B3) và kịch bản xem lại 100% (B4); hoàn thiện `report/team/bang_chi_phi.md`.

## 3. Đóng góp cụ thể

- Viết đầy đủ các hàm `so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong` và `mo_hinh` trong `src/lab13.py`, vượt qua cả 3 phép thử đáp án biết trước (`1,20 · 1,25 · 1,25`).
- Tính và điền toàn bộ bảng A1, A2, A3, A4, B1, B2, B3, B4 kèm các câu trả lời ngắn (≤ 3 dòng, có số liệu và nhãn `simulated`) vào `report/team/bang_chi_phi.md`.
- Cung cấp Context Snapshot #1 và #2 (CPS tổng `4.472 đ`, phạm vi nên chọn `noi_dia` + `hang_nang`, Top 3 yếu tố nhạy nhất) để các thành viên làm tiếp CP3–CP5.

## 4. Bằng chứng

- `src/lab13.py`: In ra `Ba phép thử đáp án biết trước: ĐẠT` và toàn bộ bảng số liệu A2, A3, A4, B1–B4.
- `report/team/bang_chi_phi.md`: Đủ 9 dòng A2, 4 dòng A3, 2 dòng A4, 9 dòng B1, B2, B3, B4 với đầy đủ nhãn `simulated`.

## 5. Công cụ AI đã dùng

- Trợ lý AI hỗ trợ triển khai code `src/lab13.py` và định dạng bảng `report/team/bang_chi_phi.md`.
- Tự kiểm tra: chạy trực tiếp `python lab13.py` trong `src/`, xác nhận 3 phép thử A1 đạt và đối chiếu từng con số với công thức trong `docs/du_lieu_va_cong_thuc.md` và `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (khớp trong ngưỡng ≤ 2%).

## 6. Tự đánh giá

- Hoàn thành đúng tiến độ CP1 và CP2, không gây conflict Git với các thành viên còn lại và bàn giao `src/lab13.py` sạch sẽ cho thành viên phụ trách CP4.
