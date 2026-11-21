"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
from statistics import NormalDist
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    return 1 / p if k is None else (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    return 1.0 if k is None else 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0
    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = (reqs['ket_qua'] == 'thanh_cong').sum()
    return dict(
        token=tien_token.sum(),
        tool=tien_tool.sum(),
        chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
        xem_lai=xem_lai,
        lam_lai=lam_lai,
        tong=tong,
        thanh_cong=thanh_cong,
        cps=tong / thanh_cong,
        hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs),
    )


def co_mau(p1, p2, alpha=0.05, power=0.8):
    """D1: so hai ti le, hai phia; cong thuc trong de, lam tron len."""
    za = NormalDist().inv_cdf(1 - alpha / 2)
    zb = NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    return math.ceil((za * math.sqrt(2 * pb * (1 - pb))
                      + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2
                     / (p2 - p1) ** 2)


def co_mau_pilot(icc=0.02):
    """Tra ca co mau tho va hieu dung de tranh nham 859 voi 5.980."""
    n5 = co_mau(0.70, 0.75)
    de75 = 1 + (75 - 1) * icc
    n_tho75 = math.ceil(n5 * de75)
    # Cau e cho san 859; giu so nay thay vi thay bang cach xap xi khac.
    n6 = 859
    m = math.ceil(n6 * (1 - icc) / (20 - n6 * icc))
    de = 1 + (m - 1) * icc
    return dict(n5=n5, de75=de75, n_tho75=n_tho75,
                staff75=math.ceil(n_tho75 / 75), tran_staff=20 / icc,
                tran_depot=6 / icc, n6=n6, m=m, de=de,
                n_tho=20 * m, n_hieu_dung=20 * m / de)


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    print('\n--- A2 · Mô hình chi phí tổng ---')
    for ten, gia_tri in ket_qua.items():
        if ten == 'hoa_don_moi_yc':
            print(f'{ten:15s} {gia_tri:>14,.1f}')
        else:
            print(f'{ten:15s} {gia_tri:>14,.0f}')
    print(f'So với hoá đơn/yc: {ket_qua["cps"] / ket_qua["hoa_don_moi_yc"]:.1f}x')
    print(f'Tỉ trọng xem lại: {ket_qua["xem_lai"] / ket_qua["tong"] * 100:.1f}%, làm lại: {ket_qua["lam_lai"] / ket_qua["tong"] * 100:.1f}%')
    khong_tc = len(reqs) - ket_qua['thanh_cong']
    he_thong_a2 = (ket_qua['tong'] + khong_tc * BASELINE) / len(reqs)
    print(f'Chi phí cả hệ thống/yc: {he_thong_a2:,.0f} đ ({he_thong_a2 / BASELINE:.2f}x của 12.000 đ)')

    # Nhiệm vụ A3: tính lại theo từng giá trị của cột loai.
    print('\n--- A3 · Tách theo loại yêu cầu ---')
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        sub = reqs[reqs['loai'] == loai]
        kq = mo_hinh(runs, sub)
        tl_tc = kq['thanh_cong'] / len(sub) * 100
        lan_tb = sub['so_lan_chay'].mean()
        print(f'{loai:10s} | n={len(sub):3d} | TC={tl_tc:5.1f}% | Lần={lan_tb:.2f} | CPS={kq["cps"]:7,.0f} đ ({kq["cps"] / BASELINE:.2f}x)')

    runs_loai = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    runs_loai['is_ok'] = (runs_loai['status'] == 'ok').astype(float)
    piv = runs_loai.pivot_table(index='loai', columns='attempt', values='is_ok', aggfunc='mean') * 100
    print('\n--- A3 · Tỉ lệ ok (%) theo attempt ---')
    print(piv.round(1).to_string())

    # Nhiệm vụ A4: chi phí cố định (noi_dia + hang_nang)
    print('\n--- A4 · Chi phí cố định (noi_dia + hang_nang) ---')
    pv_reqs = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    kq_pv = mo_hinh(runs, pv_reqs)
    tl_pv = kq_pv['thanh_cong'] / len(reqs)
    for ten_kl, kl_thang in [('45.000/tháng', 45_000), ('22.500/tháng', 22_500)]:
        viec_tc_thang = kl_thang * tl_pv
        co_dinh_moi_viec = 40_000_000 / viec_tc_thang
        tong_cps = kq_pv['cps'] + co_dinh_moi_viec
        print(f'{ten_kl:12s} | TC/tháng={viec_tc_thang:7,.0f} | Cố định={co_dinh_moi_viec:6,.0f} đ | Tổng={tong_cps:6,.0f} đ ({tong_cps / BASELINE:.2f}x)')

    # Nhiệm vụ B1: đổi từng yếu tố
    print('\n--- B1 · Độ nhạy ---')
    kich_ban = {
        'Giá token gấp đôi': dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa': dict(gia_vao=13, gia_ra=65),
        'Tỉ lệ xem lại gấp đôi': dict(he_so_xem_lai=2.0),
        'Tỉ lệ xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
        'Số ca làm lại gấp đôi': dict(he_so_lam_lai=2.0),
        'Số ca làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
        'Lương nhân viên tăng 25%': dict(luong_phut=2500),
        'Chỉ cho chạy tối đa 2 lần': dict(max_lan_chay=2),
        'Chỉ cho chạy 1 lần': dict(max_lan_chay=1),
    }
    goc = ket_qua['cps']
    for ten, kw in kich_ban.items():
        cps_kb = mo_hinh(runs, reqs, **kw)['cps']
        print(f'{ten:28s} {cps_kb:8,.0f} đ ({(cps_kb / goc - 1) * 100:+6.1f}%)')

    # Nhiệm vụ B2: đổi một cặp
    cps_cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2.0)['cps']
    print(f'\n--- B2 · Giá token x2 + Xem lại x2: {cps_cap:,.0f} đ ({(cps_cap / goc - 1) * 100:+.1f}%) ---')

    # Nhiệm vụ B3: giới hạn chạy lại và chi phí cả hệ thống
    print('\n--- B3 · Giới hạn chạy lại ---')
    for k in [1, 2, 3]:
        kq_k = mo_hinh(runs, reqs, max_lan_chay=k)
        khong_tc_k = len(reqs) - kq_k['thanh_cong']
        ca_ht = kq_k['tong'] + khong_tc_k * BASELINE
        print(f'{k} lần | Trợ lý={kq_k["tong"]:9,.0f} đ | Không TC={khong_tc_k:3d} | Cả hệ thống={ca_ht:9,.0f} đ | CPS={kq_k["cps"]:6,.0f} đ')

    # Nhiệm vụ B4: xem lại 100% (noi_dia + hang_nang)
    print('\n--- B4 · Xem lại 100% (noi_dia + hang_nang) ---')
    pv_runs = runs[runs['request_id'].isin(pv_reqs['request_id'])]
    so_co_ok = pv_runs[pv_runs['status'] == 'ok']['request_id'].nunique()
    so_lam_lai = (pv_reqs['ket_qua'] == 'lam_lai').sum()
    tien_xem_100 = so_co_ok * 5 * LUONG_PHUT
    tien_tt_pv = kq_pv['token'] + kq_pv['tool']
    tb_phut_lam_lai = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean()
    for phut_ll in [9.0, tb_phut_lam_lai]:
        tien_ll_100 = so_lam_lai * phut_ll * LUONG_PHUT
        tong_100 = tien_tt_pv + tien_xem_100 + tien_ll_100
        cps_100 = tong_100 / kq_pv['thanh_cong']
        hoa_von = (kq_pv['thanh_cong'] * BASELINE - tien_tt_pv - tien_ll_100) / (so_co_ok * LUONG_PHUT)
        print(f'Làm lại {phut_ll:4.1f}p | Tổng={tong_100:10,.0f} đ | CPS={cps_100:6,.0f} đ ({cps_100 / BASELINE:.2f}x) | Hoà vốn xem lại <= {hoa_von:.1f}p')

    # Nhiệm vụ D1: tính đủ năm câu trước khi chọn cách chia.
    d = co_mau_pilot()
    print('\n--- D1 · Cỡ mẫu pilot (giả định của lab) ---')
    print(f'a) Theo yêu cầu, +5 điểm: {d["n5"]:,} yêu cầu/nhóm')
    print(f'b) m=75: DE={d["de75"]:.2f}; {d["n_tho75"]:,} yêu cầu/nhóm; '
          f'{d["staff75"]} nhân viên/nhóm, tổng {2 * d["staff75"]} > 40')
    print(f'c) 20 nhân viên/nhóm: n hiệu dụng < {d["tran_staff"]:,.0f} < {d["n5"]:,}; không đạt +5 điểm')
    print(f'd) 6 depot/nhóm: n hiệu dụng < {d["tran_depot"]:,.0f}; chỉ 6 cụm/nhóm')
    print(f'e) +6 điểm, cần {d["n6"]} hiệu dụng/nhóm (đề cho): '
          f'm={d["m"]}; DE={d["de"]:.2f}; {d["n_tho"]:,} yêu cầu thực/nhóm; '
          f'n hiệu dụng={d["n_hieu_dung"]:.2f}')
    from statsmodels.stats.proportion import proportion_effectsize
    from statsmodels.stats.power import NormalIndPower
    power5 = NormalIndPower().power(
        effect_size=proportion_effectsize(0.75, 0.70),
        nobs1=d['n_hieu_dung'], alpha=0.05, ratio=1, alternative='two-sided')
    print(f'Đánh đổi: power với tác động thật +5 điểm chỉ {power5:.3f}, không đạt 0,80')
    print('\n--- D3 · Tỉ lệ mở lại trước khi đặt ngưỡng ---')
    for ten, tap in [('Toàn mẫu', reqs), ('noi_dia + hang_nang', pv_reqs)]:
        mo_lai = int((tap['mo_lai_trong_7_ngay'] == 1).sum())
        print(f'{ten}: {mo_lai}/{len(tap)} = {mo_lai / len(tap):.2%}')
    print('Ngưỡng đề xuất: mở lại >6% hoặc cao hơn đối chứng >=2 điểm; '
          'so trên cohort đã đủ 7 ngày theo dõi.')
