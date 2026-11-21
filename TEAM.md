# Team

## Thông tin nhóm

- Tên nhóm: MVQ
- Lớp: L3A
- Repo nhóm: https://github.com/trmanh204/K5-L3A-DAY13-MVQ-LaunchEconomics
- URL repo, nhánh nộp, commit chốt: https://github.com/trmanh204/K5-L3A-DAY13-MVQ-LaunchEconomics · nhánh `main`

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
| 1 | Lê Anh Quân | 2A202603576 | 26ai.quanla@vinuni.edu.vn | https://github.com/quanle28 | Người gắn nhãn 1 (CP3) & Phụ trách cỡ mẫu, kế hoạch pilot (CP4) |
| 2 | Phạm Nguyên Vũ | 2A202603436 | 26ai.vupn@vinuni.edu.vn | https://github.com/phamvu65 | Người viết code & Người kiểm số: mô hình chi phí (CP1) và bảng độ nhạy (CP2) |
| 3 | Trần Đức Mạnh | 2A202603615 | 26ai.manhtd5@vinuni.edu.vn | https://github.com/trmanh204 | Người gắn nhãn 2 (CP3), người giữ hồ sơ (CP5) & đóng gói, kiểm tra, nộp bài |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## Lê Anh Quân — 2A202603576

### Phần việc phụ trách

- **CP3 — Nhiệm vụ C:** phụ trách phân loại 20 ca lỗi, tổng hợp nhãn, tính đồng thuận, xử lý bất đồng và hoàn thiện bảng khắc phục 5 loại lỗi.
- **CP4 — Nhiệm vụ D:** bổ sung tính cỡ mẫu D1 và tỉ lệ mở lại D3 trong `src/lab13.py`; phân tích cách chia nhóm D2 và hoàn thiện `report/team/pilot_plan.yaml`.

### Đóng góp cụ thể

- Cập nhật hai bộ nhãn trong `bang_loi.md`: trùng **18/20 = 90%**; ghi quy tắc phân biệt cho ca **8 và 15**, chốt nhãn Hệ thống.
- Hoàn thiện bảng khắc phục cho ca **9, 7, 18, 4, 17**, đủ 5 loại lỗi; mỗi dòng có event, ngưỡng, tần suất phát hiện và vai trò phụ trách.
- Bổ sung `co_mau` và `co_mau_pilot`, tính đủ D1 a–e; chọn **20 nhân viên/nhóm**, **299 yêu cầu/người**, **5.980 yêu cầu thực/nhóm**, **DE = 6,96**, tương đương **859,20 hiệu dụng** cho mức chênh 6 điểm.
- Ghi rõ đánh đổi: power cho tác động thật 5 điểm chỉ **0,642**; tính tỉ lệ mở lại **4,25%** toàn mẫu và **3,97%** trong phạm vi trước khi đặt ngưỡng an toàn.
- Hoàn thiện kế hoạch pilot có đối chứng, phân nhóm ngẫu nhiên, phạm vi `noi_dia` + `hang_nang`, **4 luật dừng**, rollback trong **30 phút** và ngày quyết định **05/01/2027**.
- Sử dụng Codex hỗ trợ phân tích, viết code và rà soát; bàn giao kết quả CP3–CP4 cho Mạnh làm tiếp CP5. Các số chi phí dựa trên thời gian giả lập được ghi nhãn `simulated`; kế hoạch chưa được triển khai thực tế.

### Bằng chứng

- [Bảng lỗi CP3](report/team/bang_loi.md): 20 ca, hai bộ nhãn, đồng thuận 90%, quy tắc cho ca bất đồng và 5 phương án khắc phục.
- [Code tính toán](src/lab13.py): kết quả D1 a–e, power và tỉ lệ mở lại; đã được chạy kiểm tra trong phiên rà soát bằng Codex.
- [Kế hoạch pilot CP4](report/team/pilot_plan.yaml): đủ trường, đọc được bằng `yaml.safe_load`, không còn dấu hỏi.
- [Báo cáo cá nhân](report/team/2A202603576_LeAnhQuan.md): phần việc, kết quả, bằng chứng và công cụ AI đã dùng.

## Phạm Nguyên Vũ — 2A202603436

### Phần việc phụ trách

- **CP1 — Nhiệm vụ A:** Cài đặt môi trường, viết 3 hàm A1, mô hình chi phí từ trace A2, tách chi phí theo loại yêu cầu A3 và chi phí cố định A4 trong `src/lab13.py`.
- **CP2 — Nhiệm vụ B:** Chạy phân tích độ nhạy 9 kịch bản đơn (B1), kịch bản cặp (B2), chi phí cả hệ thống theo giới hạn chạy lại (B3), kịch bản xem lại 100% (B4) và hoàn thiện `report/team/bang_chi_phi.md`.

### Đóng góp cụ thể

- Hoàn thiện `so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong` và `mo_hinh` trong `src/lab13.py`, vượt qua cả 3 phép thử A1 (`1,20 · 1,25 · 1,25`).
- Tính toàn bộ bảng A1–A4, B1–B4 (CPS tổng `4.472 đ` `[simulated]`, gấp 16,3× hoá đơn; xác định phạm vi `noi_dia` + `hang_nang`; Top 3 yếu tố nhạy nhất; giới hạn 2 lần chạy rẻ nhất toàn hệ thống `6.901.220 đ` `[simulated]`; B4 xem lại 100% lên `11.743–12.415 đ` `[simulated]`).

### Bằng chứng

- [Code tính toán](src/lab13.py): đạt 3/3 phép thử A1 và in đủ bảng A2–A4, B1–B4.
- [Bảng chi phí CP1–CP2](report/team/bang_chi_phi.md): đủ các bảng và câu trả lời có nhãn `simulated`.
- [Báo cáo cá nhân](report/team/2A202603436_PhamNguyenVu.md): chi tiết phần việc, bằng chứng và kiểm tra.

## Trần Đức Mạnh — 2A202603615

### Phần việc phụ trách

- **Hỗ trợ CP3:** Đóng vai Người gắn nhãn 2, gắn nhãn độc lập 20 ca lỗi cùng Lê Anh Quân.
- **CP5 — Nhiệm vụ E:** Tính thử chỉ số, đề xuất 2 chỉ số mới, thiết kế danh sách event có `trace_id`, phân tích rủi ro kinh tế (`report/team/chi_so.md`) và tổng hợp hồ sơ launch v0 (`report/team/ho_so_launch_v0.md`).
- **Duyệt chéo & Đóng gói:** Ghi nhận phiếu chấm chéo (`report/team/phieu_cham.md`), hoàn thiện `TEAM.md`, `report/team/group_report.md`, kiểm tra toàn bộ checklist nộp bài.

### Đóng góp cụ thể

- Hoàn thành bộ nhãn độc lập 20 ca lỗi (đồng thuận **18/20 = 90%** với Lê Anh Quân).
- Tính 3 chỉ số E1 (`82,83%`, `27,12%`, `4,25%`), thiết kế 10 event có `trace_id` đồng bộ với CP3–CP4, kiểm tra chéo 5/5 chỉ số và viết 3 dòng rủi ro kinh tế trong `chi_so.md`.
- Tổng hợp hồ sơ 1 trang `ho_so_launch_v0.md` đủ 7 mục, gắn đúng trạng thái `Giả lập` và chốt đề xuất **Go có điều kiện** kèm 4 điều kiện cụ thể và đánh đổi bất lợi.

### Bằng chứng

- [Chỉ số, event & rủi ro E1–E2](report/team/chi_so.md)
- [Hồ sơ launch v0](report/team/ho_so_launch_v0.md)
- [Phiếu chấm chéo Gate 2a](report/team/phieu_cham.md)
- [Báo cáo cá nhân](report/team/2A202603615_TranDucManh.md)
