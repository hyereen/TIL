import cv2

print('Hello, OpenCV', cv2.__version__)

img = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE) # 그레이스케일로 출력

if img is None:
    print('image load failed')
    sys.exit()

cv2.namedWindow('image')
cv2.imshow('image', img)
cv2.waitKey(3000) # 3초후에 창 닫힘

cv2.destroyWindow('image')
