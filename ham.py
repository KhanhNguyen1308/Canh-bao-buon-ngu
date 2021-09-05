import cv2
import numpy as np
import os


def play_sound(path):
	os.system('aplay ' + path)


def list2point(list):
    point = (list[0], list[1])
    return point


def mid_point(p1, p2):
    mp = (int((p1[0]+p2[0])/2), int((p1[1]+p2[1])/2))
    return mp


def khoang_cach(p1, p2):
    a = np.array(p1)
    b = np.array(p2)
    return np.linalg.norm(a-b)


def draw_point(img, mui_list, mat_trai_list, mat_phai_list):
    mat_trai0 = list2point(mat_trai_list[0][0])
    mat_trai1 = list2point(mat_trai_list[0][1])
    mat_trai2 = list2point(mat_trai_list[0][2])
    mat_trai3 = list2point(mat_trai_list[0][3])
    mat_trai4 = list2point(mat_trai_list[0][4])
    mat_trai5 = list2point(mat_trai_list[0][5])

    mat_phai0 = list2point(mat_phai_list[0][0])
    mat_phai1 = list2point(mat_phai_list[0][1])
    mat_phai2 = list2point(mat_phai_list[0][2])
    mat_phai3 = list2point(mat_phai_list[0][3])
    mat_phai4 = list2point(mat_phai_list[0][4])
    mat_phai5 = list2point(mat_phai_list[0][5])

    mui = list2point(mui_list)

    giua_trai = mid_point(mat_trai0, mat_trai3)
    giua_phai = mid_point(mat_phai0, mat_phai3)

    trai_x = (giua_trai[0], mui[1])
    phai_x = (giua_phai[0], mui[1])

    trai_y = (mui[0], giua_trai[1])
    phai_y = (mui[0], giua_phai[1])

    cv2.circle(img, giua_trai, 2, (0, 255, 0), -1)
    cv2.circle(img, giua_phai, 2, (0, 255, 0), -1)
    cv2.circle(img, trai_x, 2, (0, 255, 0), -1)
    cv2.circle(img, phai_x, 2, (0, 255, 0), -1)
    cv2.circle(img, trai_y, 2, (0, 255, 0), -1)
    cv2.circle(img, phai_y, 2, (0, 255, 0), -1)

    cv2.circle(img, mui, 3, (255, 0, 0), -1)

    cv2.circle(img, mat_trai0, 2, (0, 255, 0), -1)
    cv2.circle(img, mat_trai1, 2, (0, 255, 0), -1)
    cv2.circle(img, mat_trai2, 2, (0, 255, 0), -1)
    cv2.circle(img, mat_trai3, 2, (0, 255, 0), -1)
    cv2.circle(img, mat_trai4, 2, (0, 255, 0), -1)
    cv2.circle(img, mat_trai5, 2, (0, 255, 0), -1)

    cv2.circle(img, mat_phai0, 2, (0, 255, 0), -1)
    cv2.circle(img, mat_phai1, 2, (0, 255, 0), -1)
    cv2.circle(img, mat_phai2, 2, (0, 255, 0), -1)
    cv2.circle(img, mat_phai3, 2, (0, 255, 0), -1)
    cv2.circle(img, mat_phai4, 2, (0, 255, 0), -1)
    cv2.circle(img, mat_phai5, 2, (0, 255, 0), -1)

    cv2.line(img, mui, trai_x, (0, 255, 255), 1)
    cv2.line(img, mui, phai_x, (0, 255, 255), 1)
    cv2.line(img, mui, trai_y, (0, 255, 255), 1)
    cv2.line(img, mui, phai_y, (0, 255, 255), 1)

    cv2.line(img, giua_trai, trai_x, (0, 255, 255), 1)
    cv2.line(img, giua_phai, phai_x, (0, 255, 255), 1)
    cv2.line(img, giua_trai, trai_y, (0, 255, 255), 1)
    cv2.line(img, giua_phai, phai_y, (0, 255, 255), 1)

    return img


def ty_le_mat(mat_trai_list, mat_phai_list):
    mat_trai0 = list2point(mat_trai_list[0][0])
    mat_trai1 = list2point(mat_trai_list[0][1])
    mat_trai2 = list2point(mat_trai_list[0][2])
    mat_trai3 = list2point(mat_trai_list[0][3])
    mat_trai4 = list2point(mat_trai_list[0][4])
    mat_trai5 = list2point(mat_trai_list[0][5])

    mat_phai0 = list2point(mat_phai_list[0][0])
    mat_phai1 = list2point(mat_phai_list[0][1])
    mat_phai2 = list2point(mat_phai_list[0][2])
    mat_phai3 = list2point(mat_phai_list[0][3])
    mat_phai4 = list2point(mat_phai_list[0][4])
    mat_phai5 = list2point(mat_phai_list[0][5])

    khoang_cach1 = khoang_cach(mat_trai5, mat_trai1)
    khoang_cach2 = khoang_cach(mat_trai4, mat_trai2)
    khoang_cach3 = khoang_cach(mat_trai3, mat_trai0)
    khoang_cach4 = khoang_cach(mat_phai5, mat_phai1)
    khoang_cach5 = khoang_cach(mat_phai4, mat_phai2)
    khoang_cach6 = khoang_cach(mat_phai3, mat_phai0)
    ty_le_mat_trai = (khoang_cach1+khoang_cach2)/(2*khoang_cach3)
    ty_le_mat_phai = (khoang_cach4+khoang_cach5)/(2*khoang_cach6)
    ty_le_tb = (ty_le_mat_trai+ty_le_mat_phai)/2
    return ty_le_tb

