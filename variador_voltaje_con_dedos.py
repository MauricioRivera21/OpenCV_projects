from cvzone.HandTrackingModule import HandDetector
import cv2
#from HandTrackingModule import *
import numpy as np
import serial

COM = 'COM4'
BAUD = 9600
ser = serial.Serial(COM, BAUD)

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=2)
while True:
    # Get image frame
    success, img = cap.read()
    # Find the hand and its landmarks
    #img = cv2.flip(img, 1)      #hacer un reflejo de la imagen
    hands, img = detector.findHands(img)  # This does everything

    # If I need the extected information:
    if hands:
        # Hand 1
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # List of 21 Landmark points
        #print(lmList1)
        bbox1 = hand1["bbox"]  # Bounding box info x,y,w,h
        centerPoint1 = hand1['center']  # center of the hand cx,cy
        handType1 = hand1["type"]  # Handtype Left or Right
        fingers1 = detector.fingersUp(hand1)
        print(fingers1)

        x = centerPoint1[0]; y = centerPoint1[1]
        font = cv2.FONT_HERSHEY_SIMPLEX

        if fingers1[1]*fingers1[2]*fingers1[3]*fingers1[4]*fingers1[0] == 1:
            print("5v")
            cv2.putText(img, '5v', (x+10, y), font, 1.2, (0,0,255), 2, cv2.LINE_AA)
            ser.write(b"5_voltio\n")
        elif fingers1[1]*fingers1[2]*fingers1[3]*fingers1[4] == 1:
            print("4v")
            cv2.putText(img, '4v', (x+10, y), font, 1.2, (0,0,255), 2, cv2.LINE_AA)
            ser.write(b"4_voltio\n")
        elif fingers1[1]*fingers1[2]*fingers1[3] == 1:
            print("3v")
            cv2.putText(img, '3v', (x+10, y), font, 1.2, (0,0,255), 2, cv2.LINE_AA)
            ser.write(b"3_voltio\n")
        elif fingers1[1]*fingers1[2] == 1:
            print("2v")
            cv2.putText(img, '2v', (x+10, y), font, 1.2, (0,0,255), 2, cv2.LINE_AA)
            ser.write(b"2_voltio\n")
        elif fingers1[1] == 1:
            #print("Indice levantado -> 1v")
            cv2.putText(img, '1v', (x+10, y), font, 1.2, (0,0,255), 2, cv2.LINE_AA)
            ser.write(b"1_voltio\n")
        else:
            print("dedos abajo -> 0v")
            cv2.putText(img, '0v', (x+10, y), font, 1.2, (0,0,255), 2, cv2.LINE_AA)
            ser.write(b"0_voltio\n")

        # Find Distance between two Landmarks. Could be same hand or different hands
        #length, info, img = detector.findDistance(lmList1[0][:2], lmList1[8][:2], img)

    # Display
    cv2.imshow("Image", img)
    cv2.waitKey(1)
cap.release()
cv2.destroyAllWindows()