from cvzone.HandTrackingModule import HandDetector
import cv2

cap = cv2.VideoCapture(1)           #here you need to specify which camera use (ex: 0 or 1)
detector = HandDetector(detectionCon=0.8, maxHands=2)
while True:
    # Get image frame
    success, img = cap.read()
    # Find the hand and its landmarks
    hands, img = detector.findHands(img, draw=True)  # with draw

    if hands:
        # Hand 1
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # List of 21 Landmark points
        bbox1 = hand1["bbox"]  # Bounding box info x,y,w,h
        centerPoint1 = hand1['center']  # center of the hand cx,cy
        handType1 = hand1["type"]  # Handtype Left or Right

        fingers1 = detector.fingersUp(hand1)

        if len(hands) == 2:
            # Hand 2
            hand2 = hands[1]
            lmList2 = hand2["lmList"]  # List of 21 Landmark points
            bbox2 = hand2["bbox"]  # Bounding box info x,y,w,h
            centerPoint2 = hand2['center']  # center of the hand cx,cy
            handType2 = hand2["type"]  # Hand Type "Left" or "Right"

            fingers2 = detector.fingersUp(hand2)

            # Find Distance between two Landmarks. Could be same hand or different hands
            index_finger1 = lmList1[8][:2]      # 8 is the index of the forefinger according to MediaPipe hands keypoints 
            index_finger2 = lmList2[8][:2]
            length, info, img = detector.findDistance(index_finger1, index_finger2, img)  # with draw
            print("Distance(pixels): ", round(length, 2))

    # Display
    cv2.imshow("Image", img)
    cv2.waitKey(1)