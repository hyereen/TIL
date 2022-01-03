import sys
import glob
import cv2

img_files = glob.glob('.\\images\\*.jpg')

for f in img_files:
    print(f)

# 전체 화면 영상 출력 창 만들기
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN) # 전체 화면을 띄움

cnt = len(img_files)
idx = 0
while True:
    img = cv2.imread(img_files[idx])
    cv2.imshow('image', img)

    if cv2.waitKey(1000) == 27: # ESC
        break

    idx += 1
    if idx >= cnt:
        idx = 0

cv2.destroyAllWindows()