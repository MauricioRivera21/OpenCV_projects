from cvzone.FaceDetectionModule import FaceDetector
import cv2

cap = cv2.VideoCapture(1)           #here you need to specify which camera use (ex: 0 or 1)
detector = FaceDetector()

while True:
    success, img = cap.read()
    img, bboxs = detector.findFaces(img)

    if bboxs:
        # bboxInfo - "id","bbox","score","center"
        center = bboxs[0]["center"]
        cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
