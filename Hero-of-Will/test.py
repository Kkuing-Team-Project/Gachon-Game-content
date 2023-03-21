import cv2

path = 'video/RPReplay_Final1678908123 2.MP4'
cap = cv2.VideoCapture(path)

# 이미지 크기 확인
height, width = 886, 1920

while cap.isOpened():
    ret, image = cap.read()
    if not ret:
        break
    # 콤보
    cv2.rectangle(image, (100, 130), (250, 190), (0, 0, 255), 3)

    # 점수
    cv2.rectangle(image, (width//2-100, 30), (width//2+40, 100), (255, 0, 0), 3)
    cv2.imshow('test', image)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()