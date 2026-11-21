# Bảng lỗi và cách khắc phục · Nhiệm vụ C

Nguồn: [20 ca trong đề gốc](../../docs/Ngay13_Lab13_De_bai_hoc_vien.docx), [định nghĩa và nhãn tham khảo](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md).
Nhãn dựa trên nguyên nhân gốc; “Ngầm” chỉ dùng khi chưa ai nhận ra sai sót trước kiểm tra.

- **Người gắn nhãn 1:** Lê Anh Quân
- **Người gắn nhãn 2 (kiêm giữ hồ sơ):** Trần Đức Mạnh

## Hai bộ nhãn độc lập và đối chiếu (20 ca)

Hai người gắn nhãn ngồi tách nhau, gắn độc lập cả 20 ca trong 8 phút trước khi so sánh.

|  Ca | Tóm tắt tình huống                                                 | Nhãn 1 (Lê Anh Quân) | Nhãn 2 (Trần Đức Mạnh) | Trùng nhau | Nhãn chốt         |
| --: | ------------------------------------------------------------------ | -------------------- | ---------------------- | :--------: | ----------------- |
|   1 | Số tài khoản thiếu 2 chữ số; ngân hàng trả lỗi.                    | Do người dùng        | Do người dùng          |     Có     | Do người dùng     |
|   2 | Kiện 28 kg dùng bảng hàng thường, hoàn thiếu 45.000 đ.             | Hệ thống             | Hệ thống               |     Có     | Hệ thống          |
|   3 | Tiền về ví trong 5 phút nhưng khách chờ ở ngân hàng.               | Ngữ cảnh             | Ngữ cảnh               |     Có     | Ngữ cảnh          |
|   4 | Không có dữ liệu chặng nước ngoài, chuyển nhân viên.               | Giới hạn hệ thống    | Giới hạn hệ thống      |     Có     | Giới hạn hệ thống |
|   5 | Kiểm tra thấy 14 đơn hoàn thừa trung bình 12.000 đ do mã giảm giá. | Ngầm                 | Ngầm                   |     Có     | Ngầm              |
|   6 | Khách chọn giao trễ nhưng mô tả hàng vỡ.                           | Do người dùng        | Do người dùng          |     Có     | Do người dùng     |
|   7 | Ghi sổ lỗi 503 sau 3 lần nhưng vẫn báo hoàn thành.                 | Hệ thống             | Hệ thống               |     Có     | Hệ thống          |
|   8 | Dẫn điều 7.2 không tồn tại dù số tiền đúng.                        | Hệ thống             | Ngầm                   | **Không**  | Hệ thống          |
|   9 | Nhập mã sàn thay mã vận đơn; trợ lý dừng.                          | Do người dùng        | Do người dùng          |     Có     | Do người dùng     |
|  10 | Từ chối đúng điều khoản bão nhưng ứng dụng cam kết 24 giờ.         | Ngữ cảnh             | Ngữ cảnh               |     Có     | Ngữ cảnh          |
|  11 | Không xử lý được tin thoại 40 giây.                                | Giới hạn hệ thống    | Giới hạn hệ thống      |     Có     | Giới hạn hệ thống |
|  12 | D05 có tiền token gấp 3 suốt 3 tuần mà không ai thấy.              | Ngầm                 | Ngầm                   |     Có     | Ngầm              |
|  13 | Bảo hiểm đối tác ngoài phạm vi, trả lời chung chung.               | Giới hạn hệ thống    | Giới hạn hệ thống      |     Có     | Giới hạn hệ thống |
|  14 | Khách bấm nhầm xác nhận nhận tiền.                                 | Do người dùng        | Do người dùng          |     Có     | Do người dùng     |
|  15 | Trễ 26 giờ hoàn 100% thay vì 50%; nhân viên bắt được.              | Hệ thống             | Ngầm                   | **Không**  | Hệ thống          |
|  16 | Thông báo đúng thiết kế lúc 2:14 sáng gây phiền.                   | Ngữ cảnh             | Ngữ cảnh               |     Có     | Ngữ cảnh          |
|  17 | Bảng giá cache cũ làm lệch 212 đơn trong 9 ngày.                   | Ngầm                 | Ngầm                   |     Có     | Ngầm              |
|  18 | Hoàn đúng 15.000 đ nhưng không giải thích cách tính.               | Ngữ cảnh             | Ngữ cảnh               |     Có     | Ngữ cảnh          |
|  19 | Đơn 14 tháng vượt cửa sổ dữ liệu 12 tháng.                         | Giới hạn hệ thống    | Giới hạn hệ thống      |     Có     | Giới hạn hệ thống |
|  20 | Khách gửi lại sau 10 phút gây hoàn 2 lần.                          | Hệ thống             | Hệ thống               |     Có     | Hệ thống          |

- **Tỉ lệ đồng thuận:** **18 / 20 = 90%** (đạt ngưỡng $\ge 80\%$ của CP3).
- **Phân bố nhãn chốt:** Do người dùng: 4 · Hệ thống: 5 · Ngữ cảnh: 4 · Giới hạn hệ thống: 4 · Ngầm: 3 (tổng 20 ca).

## Quy tắc phân biệt cho các ca không trùng

- **Ca 8 (Dẫn điều 7.2 không tồn tại dù số tiền đúng):** Trích dẫn sai nằm trực tiếp trên nội dung phản hồi nhìn thấy được nên xếp vào **Hệ thống**, không phải Ngầm.
- **Ca 15 (Trễ 26 giờ hoàn 100% thay vì 50%; nhân viên bắt được):** Sai quy tắc tính tiền đã bị nhân viên phát hiện trước khi gửi cho khách nên xếp vào **Hệ thống**, chỉ dùng **Ngầm** khi sai sót lọt qua và chỉ lộ ra khi kiểm tra hậu kiểm.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Mọi event đều gắn kèm `request_id`, `trace_id`, `staff_id`, `depot` và thời điểm.

|  Ca | Loại lỗi          | Phát hiện bằng gì (event, ngưỡng, tần suất)                                                                                                                       | Khắc phục thế nào                                                                                                                                 | Ai phụ trách       |
| --: | ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
|   9 | Do người dùng     | Event `input_validation_failed` (`reason=marketplace_code`); thống kê hằng ngày, cảnh báo khi tỉ lệ vượt **2%** tổng yêu cầu.                                     | Nhận dạng định dạng mã sàn và ánh xạ tự động sang mã vận đơn; nếu không tra được thì hướng dẫn khách nhập đúng trước khi tạo lệnh.                | PM trợ lý hoàn phí |
|   7 | Hệ thống          | Đối soát `refund_success_notified` với `ledger_write_result` mỗi giờ theo `trace_id`; cảnh báo ngay khi có **$\ge 1$ ca** báo thành công nhưng thiếu `status=ok`. | Chỉ gửi thông báo hoàn tiền sau khi sổ cái trả `ok`; lỗi 503 sau tối đa 2 lần chạy thì báo "đang xử lý" và chuyển nhân viên kèm khóa chống trùng. | Kỹ sư trưởng agent |
|  18 | Ngữ cảnh          | Event `request_reopened` (`reason=amount_dispute`, `audit_result=correct`); kiểm tra hằng tuần, **$\ge 1$ ca** thì rà soát mẫu câu trả lời.                       | Bắt buộc hiển thị rõ phí gốc, tỉ lệ hoàn, phép tính (`30.000 đ × 50% = 15.000 đ`) và kênh nhận tiền trong mọi thông báo hoàn phí.                 | Trưởng nhóm CSKH   |
|   4 | Giới hạn hệ thống | Event `handoff_to_staff` (`reason=missing_foreign_leg_data`); kiểm hằng ngày, **$\ge 1$ ca** `quoc_te` lọt vào luồng tự động thì khóa định tuyến.                 | Loại nhóm `quoc_te` khỏi phạm vi pilot; thông báo rõ thiếu dữ liệu chặng ngoại và chuyển nhân viên cùng tóm tắt `trace_id`, không suy đoán.       | PM trợ lý hoàn phí |
|  17 | Ngầm              | Event `tariff_audit_result`: đối soát ngẫu nhiên **100 đơn/tuần** với bảng giá hiệu lực; **$\ge 1$ đơn** lệch tiền hoặc phiên bản thì báo động trong ngày.        | Tự động xóa cache khi cập nhật bảng giá và lưu `tariff_version` vào trace; rà soát và bù/thu hồi đơn lệch trước khi mở lại luồng.                 | Kế toán trưởng     |
