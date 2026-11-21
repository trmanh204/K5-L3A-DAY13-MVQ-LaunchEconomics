# Team

## Thông tin nhóm

- Tên nhóm: MVQ
- Lớp: L3A
- Repo nhóm: https://github.com/trmanh204/K5-L3A-DAY13-MVQ-LaunchEconomics
- URL repo, nhánh nộp, commit chốt:

## Thành viên

| STT | Họ tên      | MSSV        | Email                     | GitHub                      | Vai trò                                                                                             |
| --: | ----------- | ----------- | ------------------------- | --------------------------- | --------------------------------------------------------------------------------------------------- |
|   1 | Lê Anh Quân | 2A202603576 | 26ai.quanla@vinuni.edu.vn | https://github.com/quanle28 | Phụ trách bảng phân loại lỗi và phương án khắc phục (CP3); phụ trách cỡ mẫu và kế hoạch pilot (CP4) |
|   2 |             |             |                           |                             |                                                                                                     |
|   3 |             |             |                           |                             |                                                                                                     |
|   4 |             |             |                           |                             |                                                                                                     |

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

## HoVaTen-MSSV

### Phần việc phụ trách

-

### Đóng góp cụ thể

-

### Bằng chứng

-
