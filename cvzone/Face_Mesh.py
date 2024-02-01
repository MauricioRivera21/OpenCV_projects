from cvzone.FaceMeshModule import FaceMeshDetector
import cv2

cap = cv2.VideoCapture(1)           #here you need to specify which camera use (ex: 0 or 1)
detector = FaceMeshDetector(maxFaces=2)
while True:
    success, img = cap.read()
    img, faces = detector.findFaceMesh(img)
    #if faces:
    #    print(faces[0])
    cv2.imshow("Image", img)
    cv2.waitKey(1)
