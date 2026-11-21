# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: **MVQ**
- Lớp: **L3A**
- Thành viên: Phạm Nguyên Vũ (`2A202603436`), Lê Anh Quân (`2A202603576`), Trần Đức Mạnh (`2A202603615`) — chi tiết xem [TEAM.md](../../TEAM.md).

## 2. Mục tiêu và cách tiếp cận

Nhóm xây dựng bộ **hồ sơ launch v0** cho trợ lý hoàn phí của LogiX-VN nhằm trình duyệt kế hoạch pilot tại cổng **Gate 2a**. Toàn bộ dữ liệu 1.200 yêu cầu và 1.624 lần chạy là dữ liệu giả lập; nhóm tiếp cận theo trình tự 5 checkpoint (A → E), thống nhất quy trình làm tuần tự trên nhánh `main` và kiểm tra chéo toàn bộ số liệu bằng `src/lab13.py` trước khi tổng hợp hồ sơ.

## 3. Giải pháp

- **Nhiệm vụ A & B (Chi phí & Độ nhạy):** Cài đặt 3 hàm xác suất chạy lại A1 (đạt 3/3 phép thử `1,20 · 1,25 · 1,25`), xây dựng hàm `mo_hinh` tính chi phí mỗi việc thành công từ trace (tử số tính mọi lần chạy kể cả lỗi, mẫu số chỉ đếm `thanh_cong`), tách 4 loại yêu cầu, cộng chi phí cố định 40 triệu đ/tháng và chạy 9 kịch bản độ nhạy + giới hạn chạy lại + kịch bản xem lại 100%. Xem [bang_chi_phi.md](bang_chi_phi.md) và [src/lab13.py](../../src/lab13.py).
- **Nhiệm vụ C (Bảng lỗi):** Hai thành viên (Lê Anh Quân, Trần Đức Mạnh) gắn nhãn độc lập 20 ca lỗi theo 5 loại Google PAIR trong 8 phút, đạt đồng thuận **18/20 = 90%**, thống nhất quy tắc cho 2 ca lệch (Ca 8, Ca 15) và lập bảng khắc phục đo được cho 5 ca đại diện. Xem [bang_loi.md](bang_loi.md).
- **Nhiệm vụ D (Kế hoạch pilot):** Tính đủ 5 câu cỡ mẫu D1 và tỉ lệ mở lại nền D3 trong `src/lab13.py`, chọn chia ngẫu nhiên theo nhân viên (20 + 20 cụm, phân tầng 12 depot, seed `20261121`), thu hẹp phạm vi về `noi_dia` + `hang_nang`, viết 4 luật dừng đủ 4 vế `NẾU – TRONG – THÌ – KHÔNG THÌ`. Xem [pilot_plan.yaml](pilot_plan.yaml).
- **Nhiệm vụ E (Chỉ số, rủi ro & Hồ sơ launch v0):** Tính thử 3 chỉ số, đề xuất 2 chỉ số mới, thiết kế 10 event có `trace_id` kèm kiểm tra chéo, lập bảng 3 rủi ro kinh tế và tổng hợp hồ sơ 1 trang 7 mục. Xem [chi_so.md](chi_so.md) và [ho_so_launch_v0.md](ho_so_launch_v0.md).

## 4. Kết quả

- **Chi phí (simulated):** CPS toàn mẫu **4.472 đ/việc** (gấp **16,3×** hoá đơn 274,7 đ/yc; làm lại 51,8%, xem lại 40,7%). Chi phí cả hệ thống là **5.865 đ/yc = 0,49×** baseline 12.000 đ; giới hạn **2 lần chạy** rẻ nhất toàn hệ thống (**6.901.220 đ**). Trong phạm vi `noi_dia` + `hang_nang`, cộng cố định 40 triệu/tháng đạt **4.599 đ (0,38×)** ở 45.000 yc/tháng và **5.784 đ (0,48×)** khi giảm nửa khối lượng. Tuy nhiên, nếu xem lại 100%, chi phí lên **11.743 đ (0,98×)** (9p làm lại) hoặc **12.415 đ (1,03×)** (15,3p làm lại).
- **Chỉ số đợt chạy thử (không đối chứng):** Chính **82,83%** (994/1.200); bỏ qua gợi ý **27,12%** (48/177); mở lại 7 ngày **4,25%** (51/1.200; trong phạm vi **3,97%**).
- **Đề xuất cuối của [ho_so_launch_v0.md](ho_so_launch_v0.md):** **Go có điều kiện** cho kế hoạch pilot `noi_dia` + `hang_nang` (tối đa 2 lần chạy) với 4 điều kiện cụ thể trước ngày `2026-11-23`.
- **Kết quả duyệt chéo Gate 2a:** Nhóm MVQ đã hoàn thành chấm chéo hồ sơ của nhóm `lucky` (Lớp L3A, repo `K5-L3A-DAY13-lucky-LaunchEconomics`) với tổng điểm **30/30**, quyết định **Go có điều kiện** kèm 1 câu hỏi phản biện về xung đột ngưỡng dừng 8.000 đ trong giai đoạn xem lại 100% — chi tiết xem [phieu_cham.md](phieu_cham.md).

## 5. Khó khăn và cách xử lý

- **Nhóm có 3 thành viên (ít hơn mẫu 4 người):** Phân công Vũ phụ trách CP1–CP2, Quân phụ trách CP3–CP4, Mạnh hỗ trợ gắn nhãn độc lập CP3, phụ trách CP5 và đóng gói; làm tuần tự trên `main` nên không phát sinh xung đột Git.
- **Không đủ số cụm cho MDE 5 điểm:** 40 nhân viên chia đôi chỉ cho cỡ mẫu hiệu dụng tối đa < 1.000 < 1.251; nhóm minh bạch đánh đổi sang MDE 6 điểm (`m = 299`, `DE = 6,96`) và ghi rõ power cho +5 điểm chỉ còn **0,642** trong cả `pilot_plan.yaml` và `ho_so_launch_v0.md`.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp và bằng chứng của từng thành viên nằm trong [TEAM.md](../../TEAM.md) và 3 file báo cáo cá nhân trong `report/team/`.

## 7. Hạn chế và hướng cải thiện

- Thời gian xem lại và làm lại hiện là dữ liệu `simulated` (chiếm 92,5% tổng chi phí); cần thay bằng thời gian đo thực tế từ `review_decision` và `staff_rework_completed` ngay từ bước rollout 10%.
- Giữ xem lại 100% trong kỳ đo pilot khiến bài toán kinh tế sát hoặc vượt baseline 12.000 đ; sau ngày quyết định `2027-01-05`, cần thiết kế một thí nghiệm riêng để kiểm chứng mức giảm tỉ lệ xem lại an toàn.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, https://arxiv.org/abs/2504.13359
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure", https://pair.withgoogle.com
- Tài liệu `statsmodels` (`NormalIndPower`, `proportion_effectsize`) và tài liệu đề bài Lab 13 trong thư mục `docs/`.
