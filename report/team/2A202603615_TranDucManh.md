# Báo cáo cá nhân — TranDucManh-2A202603615

## 1. Thông tin thành viên

- Họ tên: Trần Đức Mạnh
- MSSV: 2A202603615
- Email: 26ai.manhtd5@vinuni.edu.vn
- Vai trong nhóm: Người gắn nhãn 2 (CP3), phụ trách CP5 (Chỉ số, rủi ro kinh tế, hồ sơ launch v0, duyệt chéo Gate 2a) và đóng gói, kiểm tra, nộp bài.

## 2. Phần việc phụ trách

- **Hỗ trợ CP3 (Nhiệm vụ C):** Đóng vai Người gắn nhãn 2, gắn nhãn độc lập 20 ca lỗi theo 5 loại của Google PAIR trong 8 phút để đối chiếu đồng thuận cùng Lê Anh Quân.
- **CP5 (Nhiệm vụ E):** Tính thử 3 chỉ số chính/dùng/an toàn từ `src/logix_requests.csv`, đề xuất thêm 2 chỉ số, thiết kế danh sách 10 event có `trace_id` kèm bảng kiểm tra chéo, lập bảng rủi ro kinh tế trong `report/team/chi_so.md` và tổng hợp hồ sơ 1 trang `report/team/ho_so_launch_v0.md`.
- **Duyệt chéo Gate 2a & Đóng gói:** Điều phối chấm chéo (`report/team/phieu_cham.md`), hoàn thiện `TEAM.md`, `report/team/group_report.md`, kiểm tra toàn bộ checklist trước khi push và nộp bài.

## 3. Đóng góp cụ thể

- Hoàn thành bộ nhãn độc lập 20 ca lỗi cho CP3 (đồng thuận **18/20 = 90%** với Lê Anh Quân; thảo luận chốt nhãn Hệ thống cho ca 8 và ca 15).
- Chạy kiểm chứng toàn bộ đầu ra CP1–CP4 trên máy cá nhân (`src/lab13.py` đạt 3/3 phép thử A1; `pilot_plan.yaml` hợp lệ với `yaml.safe_load`, không còn dấu `?`).
- Tính 3 chỉ số E1 trên `logix_requests.csv` (`keep_default_na=False`): chỉ số chính **82,83%** (994/1.200), tỉ lệ bỏ qua gợi ý **27,12%** (48/177), tỉ lệ mở lại 7 ngày **4,25%** (51/1.200; trong phạm vi `noi_dia` + `hang_nang` là **3,97%**).
- Đề xuất 2 chỉ số bổ sung (tỉ lệ mở gợi ý trợ lý ở nhóm can thiệp; tỉ lệ lệch tiền qua hậu kiểm mẫu 100 đơn/tuần), xây dựng bảng **10 event** có `trace_id` đồng bộ với `bang_loi.md` và `pilot_plan.yaml`, hoàn thiện bảng kiểm tra chéo 5/5 chỉ số.
- Xây dựng bảng **3 rủi ro kinh tế** trong `chi_so.md` dựa trên số liệu độ nhạy của CP2 (`+51,8%` khi làm lại gấp đôi; `11.743–12.415 đ` khi xem lại 100%; `+2.370 đ/việc` chi phí cố định khi khối lượng giảm nửa — đều gắn nhãn `simulated`).
- Tổng hợp hồ sơ 1 trang `ho_so_launch_v0.md` đủ 7 mục, gắn đúng trạng thái `Giả lập` cho các mục 1, 2, 3, 7 và chốt đề xuất **Go có điều kiện** kèm 4 điều kiện cụ thể (có vai trò phụ trách và ngày kiểm tra), nêu trung thực hai đánh đổi bất lợi (power 0,642 ở mức +5 điểm và rủi ro kinh tế khi xem lại 100%).

## 4. Bằng chứng

- `report/team/chi_so.md`: Đầy đủ bảng E1 (5 chỉ số), danh sách 10 event có `trace_id`, kiểm tra chéo và bảng E2 (3 rủi ro kinh tế có nhãn `simulated`).
- `report/team/ho_so_launch_v0.md`: Hồ sơ launch v0 dài 1 trang, đủ 7 mục, đúng quy ước trạng thái, đề xuất Go có điều kiện với 4 điều kiện đo được.
- `report/team/bang_loi.md`: Cột nhãn độc lập của Người gắn nhãn 2 (Trần Đức Mạnh) cho 20 ca lỗi.
- `report/team/phieu_cham.md`: Phiếu chấm chéo Gate 2a cho nhóm `lucky` (`K5-L3A-DAY13-lucky-LaunchEconomics`, 30/30 điểm, quyết định Go có điều kiện và câu hỏi phản biện bằng số).
- `TEAM.md` và `report/team/group_report.md`: Cập nhật đầy đủ thông tin nhóm 3 thành viên và tổng hợp kết quả.

## 5. Công cụ AI đã dùng

- Sử dụng trợ lý AI (Antigravity / Gemini) để phân tích yêu cầu đề bài, rà soát tính nhất quán giữa CP1–CP4 và CP5, hỗ trợ trình bày `chi_so.md`, `ho_so_launch_v0.md` và soát checklist nộp bài.
- **Cách tự kiểm tra:** Chạy trực tiếp Python trên `src/logix_requests.csv` để xác nhận 3 chỉ số E1 (`82,83%`, `27,12%`, `4,25%`); chạy `python lab13.py` và `yaml.safe_load` đối chiếu lại toàn bộ số liệu CP1–CP4; quét toàn bộ thư mục `report/team/` đảm bảo không có từ cấm, không còn dấu `?` và mọi con số giả lập đều gắn nhãn `simulated`.

## 6. Tự đánh giá

- Hoàn thiện đầy đủ và nhất quán phần CP5 trước mốc 17:00 để nhóm kịp duyệt chéo Gate 2a; bảo đảm hồ sơ nêu rõ cả bằng chứng thuận lợi lẫn con số bất lợi để hội đồng đánh giá khách quan.
