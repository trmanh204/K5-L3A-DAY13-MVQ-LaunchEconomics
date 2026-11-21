# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | **82,83%** (994 / 1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại (`duoc_xem_lai == 1`) | **27,12%** (48 / 177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | **4,25%** (51 / 1.200; trong phạm vi `noi_dia` + `hang_nang`: **3,97%**, 39 / 982) |
| Dùng | Nhóm tự đề xuất: % yêu cầu đủ điều kiện trong nhóm can thiệp mà nhân viên mở gợi ý của trợ lý | Số `request_id` duy nhất có event `agent_suggestion_shown` chia tổng số `request_id` đủ điều kiện phân cho nhóm can thiệp (`arm == 'treatment'`) | Không cần tính |
| An toàn | Nhóm tự đề xuất: % đơn hoàn sai tiền hoặc lệch bảng giá qua kiểm tra mẫu hằng tuần | Số đơn có `lech_tien == true` trong `tariff_audit_result` chia tổng số đơn được hậu kiểm (mẫu 100 đơn/tuần) | Không cần tính |

> **Lưu ý diễn giải:** Chỉ số chính **trong đợt chạy thử là 82,83%** (chỉ số an toàn mở lại 7 ngày là **4,25%**), **không kết luận** "trợ lý đã nâng chỉ số so với mức nền 70%" vì đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Mười event dưới đây đều gắn `trace_id` để nối xuyên suốt với trace của agent, đồng bộ với các event giám sát trong `bang_loi.md` và `pilot_plan.yaml`:

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | `request_id`, `loai`, `so_tien_vnd`, `depot`, `arm`, `trace_id` | Khi khách gửi yêu cầu hoàn phí |
| `agent_run_completed` | Dịch vụ agent | `request_id`, `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status`, `tariff_version`, `trace_id` | Sau mỗi lần chạy agent, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | `request_id`, `staff_id`, `so_tien_de_xuat`, `trace_id` | Khi gợi ý hiện ra (kiêm `access_event` kiểm soát chia sẻ tài khoản) |
| `review_decision` | Giao diện nhân viên | `request_id`, `staff_id`, `quyet_dinh` (`giu`/`sua`/`bo`), `phut_xem_lai_thuc`, `trace_id` | Khi nhân viên bấm giữ, sửa hoặc bỏ gợi ý |
| `staff_rework_completed` | Hệ thống CSKH | `request_id`, `staff_id`, `phut_lam_lai_thuc`, `ly_do`, `trace_id` | Khi nhân viên hoàn tất xử lý lại ca lỗi |
| `ledger_write_result` | Dịch vụ sổ cái | `request_id`, `idempotency_key`, `so_tien_vnd`, `status`, `trace_id` | Khi ghi giao dịch hoàn tiền (đối soát với `refund_success_notified` bắt Ca 7, Ca 20) |
| `handoff_to_staff` | Dịch vụ agent | `request_id`, `reason`, `tom_tat`, `trace_id` | Khi chuyển yêu cầu sang nhân viên (ngoài phạm vi hoặc quá 2 lần chạy) |
| `ticket_closed` | Hệ thống ticket | `request_id`, `closed_at`, `trace_id` | Khi đóng yêu cầu hoàn phí |
| `request_reopened` | App khách / CSKH | `request_id`, `reopened_at`, `reason`, `audit_result`, `trace_id` | Khi khách mở lại yêu cầu trong vòng 7 ngày |
| `tariff_audit_result` | Hệ thống hậu kiểm kế toán | `request_id`, `so_tien_da_hoan`, `so_tien_dung`, `tariff_version`, `lech_tien`, `trace_id` | Hằng tuần khi kế toán kiểm tra mẫu 100 đơn (bắt lỗi ngầm Ca 5, Ca 17) |

**Kiểm tra chéo (mọi chỉ số ở bảng E1 đều tính được từ danh sách event trên):**

- **Chỉ số chính (% đóng trong 24h & không mở lại 7 ngày):** ghép `refund_request_created` (mẫu số, thời điểm tạo) với `ticket_closed` (kiểm tra `closed_at - created_at <= 24h`) và `request_reopened` (không xuất hiện trong 7 ngày sau đóng) theo `request_id` và `trace_id`.
- **Chỉ số dùng (tỉ lệ bỏ qua gợi ý):** lấy từ `review_decision` — tử số là số `request_id` duy nhất có `quyet_dinh` là `sua` hoặc `bo`, mẫu số là tổng `request_id` duy nhất có `review_decision`.
- **Chỉ số an toàn (tỉ lệ lỗi lọt đến khách — mở lại 7 ngày):** tử số là số `request_id` có `request_reopened` trong 7 ngày, mẫu số là tổng `request_id` từ `refund_request_created` thuộc cohort đã đủ 7 ngày theo dõi.
- **Chỉ số dùng tự đề xuất (% yêu cầu mở gợi ý trợ lý):** tử số là số `request_id` duy nhất có `agent_suggestion_shown`, mẫu số là tổng `request_id` đủ điều kiện từ `refund_request_created` có `arm == 'treatment'`.
- **Chỉ số an toàn tự đề xuất (% đơn hoàn sai tiền qua kiểm tra mẫu):** lấy trực tiếp từ `tariff_audit_result` — tử số là số đơn `lech_tien == true`, mẫu số là tổng số đơn kiểm tra mẫu trong tuần.

## E2 · Rủi ro kinh tế

Số liệu tác động lấy trực tiếp từ bảng độ nhạy và phân tích cố định trong `report/team/bang_chi_phi.md` (các con số dựa trên phút nhân viên đều là `simulated`):

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi (yếu tố nhạy nhất bảng B1) | Chi phí mỗi việc thành công tăng **+51,8%**, từ 4.472 đ lên **6.787 đ** `[simulated]` | Tỉ lệ ca `lam_lai` hằng tuần vượt **7%** (mức đợt chạy thử: **4,89%** trong phạm vi `noi_dia` + `hang_nang`, **6,17%** toàn mẫu) | Khóa mở rộng bước rollout, rà 20 trace `lam_lai` gần nhất để sửa quy tắc tính tiền và prompt trước khi chạy tiếp | PM trợ lý hoàn phí |
| Phải duy trì xem lại 100% kéo dài (B4, áp dụng trong kỳ đo pilot) | Chi phí mỗi việc thành công trong phạm vi đạt **11.743 đ = 0,98×** (với 9 phút làm lại) hoặc **12.415 đ = 1,03×** (với trung bình thực tế 15,3 phút) so với baseline 12.000 đ `[simulated]`; hoà vốn yêu cầu xem lại ≤ **4,8–5,1 phút** | Chi phí thực đo từ `review_decision` + `staff_rework_completed` vượt **12.000 đ/việc** trong 2 báo cáo tuần liên tiếp, hoặc thời gian xem lại thực đo > **5 phút/ca** | Kích hoạt luật dừng chi phí trong `pilot_plan.yaml`; tối ưu giao diện xem lại để rút ngắn thời gian và lập kế hoạch thử giảm tỉ lệ xem lại ở giai đoạn sau ngày quyết định `2027-01-05` | Trưởng nhóm CSKH |
| Khối lượng yêu cầu thấp hơn dự kiến (A4, chi phí cố định 40 triệu đ/tháng) | Chi phí cố định mỗi việc tăng gấp đôi từ **+1.185 đ** (tổng **4.599 đ = 0,38×** ở 45.000 yc/tháng) lên **+2.370 đ** (tổng **5.784 đ = 0,48×** khi khối lượng giảm một nửa) `[simulated]` | Số việc thành công hằng tuần thấp hơn **50%** kế hoạch hoặc số yêu cầu đạt điều kiện không đủ 299 ca/nhân viên | Giữ nguyên quy mô, chưa mở rộng thêm depot/nhân viên và rà soát lại cơ cấu chi phí cố định 40 triệu đ/tháng trước ngày quyết định | PM trợ lý hoàn phí |
