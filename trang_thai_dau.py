def trang_thai_dau(nghieng_1, nghieng_2,cui_1, cui_2):
    if 0.5 < nghieng_2 < 1.5:    
        if 0.6 < nghieng_1 < 1.5:
            if cui_1 >= 0.75 and cui_2 >= 0.75:
                trang_thai = 'Cui'
                mode = 1
            else:
                trang_thai = 'Thang'
                mode = 0

        elif nghieng_1 <= 0.6:
            if cui_1 < 1:
                if nghieng_2 > 0.55:
                    trang_thai = 'Nghieng phai'
                    mode = 2
                else:
                    trang_thai = 'Cui nghieng phai'
                    mode = 4
            else:
                if nghieng_2 < 0.55:
                    trang_thai = 'Cui nghieng phai'
                    mode = 4
                else:
                    trang_thai = 'Nghieng phai'
                    mode = 2

        elif nghieng_1 >= 1.5:
            if cui_2 < 1:
                if nghieng_2 < 1.25:
                    trang_thai = 'Nghieng trai'
                    mode = 3
                else:
                    trang_thai = 'Cui nghieng trai'
                    mode = 5 
            else:
                if nghieng_2 > 0.75:
                    trang_thai = 'Nghieng trai'
                    mode = 3
                else:
                    trang_thai = 'Cui nghieng trai'
                    mode = 5
    elif nghieng_2 >= 1.5:
        trang_thai = 'Nhin Trai'
        mode = 7
    elif nghieng_2 <= 0.5:
        trang_thai = 'Nhin Phai'
        mode = 6
    return trang_thai, mode



def trang_thai_mat(ty_le_mat, dem, mode, canh_bao, trang_thai_trc):
    if mode == 0:
        if ty_le_mat <= 0.25:
            trang_thai = 'Nham'
            dem += 1
            if dem >= 20:
                canh_bao = True
        else:
            trang_thai = 'Mo'
            dem = 0
            canh_bao = False
    elif mode == 1:
        if ty_le_mat <= 0.3:
            trang_thai = 'Nham'
            dem += 1
            if dem >= 20:
                canh_bao = True
        else:
            trang_thai = 'Mo'
            dem = 0
            canh_bao = False
    elif mode == 2:
        if ty_le_mat <= 0.28:
            trang_thai = 'Nham'
            dem += 1
            if dem >= 20:
                    larm = True
        else:
            trang_thai = 'Mo'
            dem = 0
            canh_bao = False
    elif mode == 3:
        if ty_le_mat <= 0.28:
            trang_thai = 'Nham'
            dem += 1
            if dem >= 20:
                canh_bao = True
        else:
            trang_thai = 'Mo'
            dem = 0
            canh_bao = False
    elif mode == 4:
        if ty_le_mat <= 0.35:
            trang_thai = 'Nham'
            dem += 1
            if dem >= 20:
                canh_bao = True
        else:
            trang_thai = 'Open'
            dem = 0
            canh_bao = False
    elif mode == 5:
        if ty_le_mat <= 0.3:
            trang_thai = 'Nham'
            dem += 1
            if dem >= 20:
                canh_bao = True
        else:
            trang_thai = 'Open'
            dem = 0
            canh_bao = False
    elif mode == 6:
        if ty_le_mat <= 0.35:
            trang_thai = 'Nham'
            dem += 1
            if dem >= 20:
                    canh_bao = True
        else:
            trang_thai = 'Mo'
            dem = 0
            canh_bao = False
    elif mode == 7:
        if ty_le_mat <= 0.33:
            trang_thai = 'Nham'
            dem += 1
            if dem >= 20:
                canh_bao = True
        else:
            trang_thai = 'Mo'
            dem = 0
            canh_bao = False
    trang_thai_trc = trang_thai
    return trang_thai, trang_thai_trc, dem, canh_bao


def gat_dau(trang_thai_truoc, mode, dem, gat_num, trang_thai):
    if trang_thai_truoc == 0 and (mode == 0 or mode == 2 or mode == 3):
        trang_thai_truoc == mode
    if mode == 1 or mode == 6 or mode == 7 and (trang_thai_truoc == 0 or trang_thai_truoc == 2 or trang_thai_truoc == 3):
        if trang_thai == "Nham":
            dem += 1
            trang_thai_truoc = mode
    if (mode == 0 or mode == 2 or mode == 3) and (trang_thai_truoc == 1 or trang_thai_truoc == 6 or trang_thai_truoc == 7):  
        if dem <= 15 and dem != 0:
            gat_num += 1
            dem = 0
    return gat_num, dem, trang_thai_truoc