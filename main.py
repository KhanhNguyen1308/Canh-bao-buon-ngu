import cv2
import time
import numpy as np
import mediapipe as mp
from threading import Thread
from ty_le_dau import ty_le_dau
from ham import play_sound, draw_point, ty_le_mat
from trang_thai_dau import gat_dau, trang_thai_dau, trang_thai_mat

a = open("Text/n1.txt", "+w")
b = open("Text/n2.txt", "+w")
c = open("Text/c1.txt", "+w")
d = open("Text/c2.txt", "+w")
e = open("Text/avg.txt", "+w")
f = open("Text/mode.txt", "+w")
wav_path = '/home/pi/Documents/Drowsy_detect/alarm.wav'
dem = 0
gat_num = 0
ty_le_tb_mat = 0
trang_thai_trc = 0
dem_gat = 0
tt_mat = ''
tt_mat_trc = ''
tt_dau = ''
Drowsy_mode = ''
mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh()
drawSpec = mpDraw.DrawingSpec(thickness=1, circle_radius=2)
cap = cv2.VideoCapture("Video/final_test.mp4")
canh_bao = False
while True:
    ret, img = cap.read()
    pTime = time.time()
    key = cv2.waitKey(50)
    ih, iw = img.shape[0], img.shape[1]
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceMesh.process(imgRGB)
    if results:
        face = []
        Left_eye = []
        Right_eye = []
        try:
            for face_lms in results.multi_face_landmarks:
                for lm in face_lms.landmark:
                    x, y = int(lm.x * iw), int(lm.y * ih)
                    face.append([x, y])

            nose = face[5]
            Left_eye.append([face[249], face[374], face[380], face[382], face[385], face[386]])
            Right_eye.append([face[7], face[145], face[153], face[155], face[158], face[159]])
            img = draw_point(img, nose, Left_eye, Right_eye)
            ty_le_tb_mat = ty_le_mat(Left_eye, Right_eye)
            nghieng_1, nghieng_2, cui_1, cui_2 = ty_le_dau(nose, Left_eye, Right_eye)
            tt_dau, mode = trang_thai_dau(nghieng_1, nghieng_2, cui_1, cui_2)
            tt_mat, tt_mat_trc, dem, canh_bao= trang_thai_mat(ty_le_tb_mat, dem, mode, canh_bao, tt_mat_trc)
            gat_num, dem_gat, trang_thai_trc = gat_dau(trang_thai_trc, mode, dem_gat, gat_num, tt_mat)
            a.write(str(round(nghieng_1,3))+"\n")
            b.write(str(round(nghieng_2,3))+"\n")
            c.write(str(round(cui_1,3))+"\n")
            d.write(str(round(cui_2,3))+"\n")
            e.write(str(round(ty_le_tb_mat,3))+"\n")
            f.write(str(mode/10)+"\n")
            z = "n1:"+str(round(nghieng_1,3))+"  n2:"+str(round(nghieng_2,3))+"  c1:"+str(round(cui_1,3))+"  c2:"+str(round(cui_2,3))
            if canh_bao == True:
                color = (0, 0, 255)
                cv2.putText(img, "CANH BAO!!!", (int(iw/2-250),int(ih/2)), cv2.FONT_HERSHEY_SIMPLEX, 3, color, 2)
                t = Thread(target=play_sound, args=(wav_path,))
                t.deamon = True
                t.start()
            elif canh_bao == False:
                color = (255, 0, 0)
        except Exception:
            color = (0, 255, 0)
    cTime = time.time()
    fps = int(1 / (cTime - pTime))
    cv2.putText(img, str(fps), (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
    cv2.putText(img, "Tu the: " + tt_dau, (10,40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
    cv2.putText(img, "Trang thai mat: " + tt_mat, (10,60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
    cv2.putText(img, "Gat dau: " + str(gat_num), (10,80), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
    pTime = cTime
    cv2.imshow('results', img)
    if key == ord('q'):
        break
    if key == ord('a'):
        print(z)

a.close()
b.close()
c.close()
d.close()
e.close()
f.close()
cap.release()
cv2.destroyAllWindows()
