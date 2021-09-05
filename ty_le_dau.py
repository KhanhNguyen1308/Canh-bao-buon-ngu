import numpy as np
import math
from ham import khoang_cach, mid_point


def ty_le_dau(mui, mat_trai, mat_phai):
    g_t = mid_point(mat_trai[0][0], mat_trai[0][3])
    g_p = mid_point(mat_phai[0][0], mat_phai[0][3])
    x2 = (g_t[0], mui[1])
    x1 = (g_p[0], mui[1])
    y2 = (mui[0], g_t[1])
    y1 = (mui[0], g_p[1])
    kc_gt_x2 = khoang_cach(g_t, x2)
    if kc_gt_x2 == 0:
        kc_gt_x2 = 1
    kc_gp_x1 = khoang_cach(g_p, x1)
    if kc_gp_x1 == 0:
        kc_gp_x1 = 1
    kc_gt_y2 = khoang_cach(g_t, y2)
    if kc_gt_y2 == 0:
        kc_gt_y2 = 1
    kc_gp_y1 = khoang_cach(g_p, y1)
    if kc_gp_y1 == 0:
        kc_gp_y1 = 1
    nghieng_1 = kc_gp_x1/kc_gt_x2
    nghieng_2 = kc_gp_y1/kc_gt_y2
    cui_1 = kc_gp_x1/kc_gp_y1
    cui_2 = kc_gt_x2/kc_gt_y2
    if nghieng_1 < 0:
        nghieng_1 = nghieng_1 * (-1)
    if nghieng_2 < 0:
        nghieng_2 = nghieng_2 * (-1)
    if cui_1 < 0:
        cui_1 = cui_1 * (-1)
    if cui_2 < 0:
        cui_2 = cui_2 * (-1)
    return nghieng_1, nghieng_2, cui_1, cui_2

