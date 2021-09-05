def so_sanh_va_canh_bao(ty_le, moc, dem):
    if ty_le <= moc:
        trang_thai = 'Nham'
        dem += 1
        if dem >= 20:
            canh_bao = True
    elif ty_le > moc:
        trang_thai = 'Mo'
        dem = 0
        canh_bao = False
    return trang_thai, canh_bao, dem


def trang_thai_dau(nghieng_1, nghieng_2,cui_1, cui_2):
    if 0.4 < nghieng_2 < 2:    
        if 0.5 < nghieng_1 < 1.5:
            if cui_1 <= 0.75: 
                if cui_2 <= 0.75:
                    trang_thai = 'Thang'
                    mode = 0
                elif cui_2 > 0.75:
                    trang_thai = 'Cui'
                    mode = 1
            elif cui_1 > 0.75:
                if cui_2 <= 0.75:
                    trang_thai = 'Thang'
                    mode = 0
                elif cui_2 > 0.75:
                    trang_thai = 'Cui'
                    mode = 1

        elif nghieng_1 <= 0.5:
            if cui_1 <= 0.3:
                trang_thai = 'Nghieng phai'
                mode = 2
            elif cui_1 > 0.3:
                trang_thai = 'Cui_Nghieng phai'
                mode = 4

        elif nghieng_1 >= 1.5:
            if cui_2 <= 0.3:
                trang_thai = 'Nghieng Trai'
                mode = 3
            elif cui_2 > 0.3:
                trang_thai = 'Cui_Nghieng Trai'
                mode = 5
    elif nghieng_2 >= 2:
        trang_thai = 'Nhin Trai'
        mode = 7
    elif nghieng_2 <= 0.4:
        trang_thai = 'Nhin Phai'
        mode = 6
    return trang_thai, mode



def trang_thai_mat(ty_le_mat, dem, mode, canh_bao, trang_thai_trc):
    if mode == 0:
        if ty_le_mat <= 0.25:
            trang_thai = 'Nham'
            dem += 1
            if dem >= 20:
                Alarm = True
        else:
            trang_thai = 'Mo'
            dem = 0
            Alarm = False
    elif mode == 1:
        if ty_le_mat <= 0.3:
            trang_thai = 'Nham'
            dem += 1
            if dem >= 20:
                Alarm = True
        else:
            trang_thai = 'Mo'
            dem = 0
            Alarm = False
    elif mode == 2:
        if ty_le_mat <= 0.28:
            trang_thai = 'Nham'
            dem += 1
            if dem >= 20:
                    larm = True
        else:
            trang_thai = 'Mo'
            dem = 0
            Alarm = False
    elif mode == 3:
        if ty_le_mat <= 0.28:
            trang_thai = 'Nham'
            dem += 1
            if dem >= 20:
                Alarm = True
        else:
            trang_thai = 'Mo'
            dem = 0
            Alarm = False
    elif mode == 4:
        if ty_le_mat <= 0.35:
            trang_thai = 'Nham'
            dem += 1
            if dem >= 20:
                Alarm = True
        else:
            trang_thai = 'Open'
            dem = 0
            Alarm = False
    elif mode == 5:
        if ty_le_mat <= 0.3:
            trang_thai = 'Nham'
            dem += 1
            if dem >= 20:
                Alarm = True
        else:
            trang_thai = 'Open'
            dem = 0
            Alarm = False
    elif mode == 6:
        if ty_le_mat <= 0.35:
            trang_thai = 'Nham'
            dem += 1
            if dem >= 20:
                    Alarm = True
        else:
            trang_thai = 'Mo'
            dem = 0
            Alarm = False
    elif mode == 7:
        if ty_le_mat <= 0.33:
            trang_thai = 'Nham'
            dem += 1
            if dem >= 20:
                Alarm = True
        else:
            trang_thai = 'Mo'
            dem = 0
            Alarm = False
    trang_thai_trc = trang_thai
    return trang_thai, trang_thai_trc, dem, canh_bao


def gat_dau(prev_status, mode, dem, gat_num, trang_thai):
    if prev_status == 0 and (mode == 0 or mode == 2 or mode == 3):
        prev_status == mode
    if mode == 1 or mode == 6 or mode == 7 and (prev_status == 0 or prev_status == 2 or prev_status == 3):
        if trang_thai == "Nham":
            dem += 1
            prev_status = mode
    if (mode == 0 or mode == 2 or mode == 3) and (prev_status == 1 or prev_status == 6 or prev_status == 7):  
        if dem <= 10 and dem != 0:
            gat_num += 1
            dem = 0
    return gat_num, dem, prev_status