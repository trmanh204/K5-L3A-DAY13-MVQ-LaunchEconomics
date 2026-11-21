# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): **MVQ (Lớp L3A)**
- Nhóm được chấm: **lucky (Lớp L3A — Repo: `K5-L3A-DAY13-lucky-LaunchEconomics`)**

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | **10** | Đề xuất **Go có điều kiện** khớp toàn bộ số liệu CP1–CP4 (CPS toàn mẫu 4.472 đ, trong phạm vi 3.414 đ, cộng cố định 4.599 đ = 0,38× `[simulated]`). Hồ sơ nêu thẳng 3 điểm bất lợi lớn kèm 4 điều kiện xử lý có người phụ trách và hạn kiểm tra (`2026-12-01` đến `2026-12-15`): (1) lỗi sổ cái & hoàn trùng Ca 7, 20; (2) đánh đổi MDE 6 điểm khiến power ở mức +5 điểm chỉ còn ~**0,62**; (3) xem lại 100% đẩy chi phí lên **11.743–12.516 đ (0,98×–1,04×)** `[simulated]`. |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | **10** | Gắn đầy đủ nhãn `[simulated]` ở mọi con số tính từ cột `_simulated` trong `bang_chi_phi.md`, `chi_so.md`, `ho_so_launch_v0.md` (đúng trạng thái `Giả lập` ở mục 1, 2, 3, 7) và `simulated_inputs` trong `pilot_plan.yaml`. Phạm vi thu hẹp rõ về `noi_dia` (**0,22×**, 2.696 đ) và `hang_nang` (**0,69×**, 8.221 đ), loại `quoc_te` (**1,88×**, 22.515 đ, thành công 27,3%) và `doi_tac` (**0,85×**, 10.215 đ) `[simulated]`. Không dùng từ cấm hay vai trò chung chung. |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | **10** | Có đối chứng song song (**20 vs 20** nhân viên tại 12 depot, phân tầng ngẫu nhiên có seed, kiểm soát spillover theo `staff_id`, công bố trước ngày quyết định `2027-01-05`). Tính đủ D1 a–e (`1.251`, `3.103`, trần `1.000`/`300`), chọn MDE `0,06`, `m >= 299`, `DE = 6,96`, `n_per_arm = 859` hiệu dụng; YAML hợp lệ, không còn dấu `?`. Đủ **3 luật dừng** đúng mẫu NẾU–TRONG–THÌ–KHÔNG THÌ có ngưỡng dựa trên nền mở lại `4,25%` (`>= 2 điểm` hoặc `> 6,0%`), thời hạn rõ và vai trò dừng cụ thể (rollback 30 phút). |
| **Tổng** | | | | **30 / 30** | |

**Quyết định của hội đồng:** **Go có điều kiện**

**Lý do:** Hồ sơ của nhóm `lucky` nhất quán từ dữ liệu trace đến kế hoạch pilot, thu hẹp phạm vi có căn cứ bằng số, minh bạch nhãn `simulated` và nêu đầy đủ các con số bất lợi (power ~0,62 ở mức +5 điểm; chi phí xem lại 100% lên 11.743–12.516 đ `[simulated]`). Hội đồng đồng ý duyệt kế hoạch pilot với 4 điều kiện nhóm đã đặt ra, đồng thời khuyến nghị làm rõ 2 điểm vận hành trước khi chạy: (1) tách lỗi `>= 1 ca hoàn trùng` khỏi cửa sổ 3 ngày để kích hoạt dừng ngay trong 30 phút; (2) điều chỉnh hoặc ghi rõ ngoại lệ cho luật dừng chi phí `> 8.000 đ` trong 2 tuần đầu rollout khi còn xem lại 100%.

**Một câu hỏi cho đội trình:** Trong `pilot_plan.yaml`, luật dừng số 2 yêu cầu thu hẹp phạm vi nếu chi phí mỗi việc thành công vượt **8.000 đ trong 2 tuần liên tiếp**, nhưng ở 2 tuần rollout đầu (`0.10` và `0.25`) nhóm vẫn duy trì **xem lại 100%** với chi phí ước tính **11.743–12.516 đ/việc `[simulated]`** — vậy luật dừng này có tự động kích hoạt ngay sau tuần 2 hay không, và nhóm xử lý xung đột ngưỡng này thế nào?

**Câu trả lời của đội trình (ghi lại tại buổi):** Chấm chéo trực tiếp trên hồ sơ repo của nhóm `lucky` (`K5-L3A-DAY13-lucky-LaunchEconomics`); chưa có phiên hỏi đáp trực tiếp tại lớp để ghi nhận câu trả lời miệng của đội trình.
