#from cvzone.HandTrackingModule import HandDetector
from HandTrackingModule import *
import cv2
import numpy as np
import serial

#COM = '/dev/cu.usbserial-14120'
COM = 'COM4'
BAUD = 9600
ser = serial.Serial(COM, BAUD)

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=2)
while True:
    # Get image frame
    success, img = cap.read()
    # Find the hand and its landmarks
    img = cv2.flip(img, 1)      #hacer un reflejo de la imagen (funciona bien )
    hands, img = detector.findHands(img)  # with draw

    if hands:
        # Hand 1
        hand1 = hands[0]
        centerPoint1 = hand1['center']  # center of the hand cx,cy
        x = centerPoint1[0]; y = centerPoint1[1]
        cv2.circle(img, (x,y), 7, (0,0,255), -1)      #realizar un circulo sobre la imagen(frame), dado el centro de este(x,y), de radio 7, de color azul(0,0,255) y rellenado(-1)
        font = cv2.FONT_HERSHEY_SIMPLEX

        #valor = 360
        valor = 240
        if x < valor:
          print("Mover a la izquierda 100%")
          cv2.putText(img, 'izquierda', (x+10, y), font, 1.2, (0,0,255), 2, cv2.LINE_AA)
          ser.write(b"izquierda\n")
        elif valor <= x < valor*2:      #720
          print("Mover al centro")
          cv2.putText(img, 'centro', (x+10, y), font, 1.2, (0,0,255), 2, cv2.LINE_AA)
          ser.write(b"centro\n")
        elif valor*2 <= x <= valor*3:       #1080
          print("Mover a la derecha 100%")
          cv2.putText(img, 'derecha', (x+10, y), font, 1.2, (0,0,255), 2, cv2.LINE_AA)
          ser.write(b"derecha\n")
    
    # Display
    cv2.imshow("Image", img)
    cv2.waitKey(1)
cap.release()
cv2.destroyAllWindows()
