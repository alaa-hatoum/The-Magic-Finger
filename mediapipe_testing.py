import cv2
from matplotlib import colors
import numpy as np
import mediapipe as mp
import math



mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

cap=cv2.VideoCapture(0)

with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
    
    
    while cap.isOpened():
        ret, frame = cap.read()
        
        
        if not ret:
            print("Ignoring empty camera frame.")
            continue
        
        #converts from BGR to RGB, array switch is neccesary for input into hands.process
        image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        
        # flip image on the horizontal
        image = cv2.flip(image,1)

        #set flag (flag can be thought of as the status of an image)
        image.flags.writeable = False
        
        #detects the joints on the hand 
        results = hands.process(image)
        
        image_height, image_width, _ = image.shape

        #set flag to true
        image.flags.writeable = True
        
        #convert image back to BGR
        image= cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        print(results)
        
        # rendering results 
        if results.multi_hand_landmarks:
            for num, hand in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS,
                                          mp_drawing.DrawingSpec(color=(250,0,0),thickness=4, circle_radius = 3),
                                          mp_drawing.DrawingSpec(color=(250,250,250),thickness=4, circle_radius = 3),
                                          )
                
        cv2.imshow('Magic Finger', image)
        counter = 0
        calibration = True
        wrstx=wrsty=thmx=thmy=indx=indy=midx=midy=rngx=rngy=pnkx=pnky = []
        wrstxi=wrstyi=thmxi=thmyi=indxi=indyi=midxi=midyi=rngxi=rngyi=pnkxi=pnkyi = 0
        while calibration:
            for hand_landmarks in results.multi_hand_landmarks:
            # Here is How to Get All the Coordinates
                for ids, landmrk in enumerate(hand_landmarks.landmark):
                    #print(ids, landmrk)
                    if ids == 0:
                        wrstxi,wrstyi = landmrk.x * image_width, landmrk.y*image_height
                        wrstx.append(wrstxi)
                        wrsty.append(wrstyi)
                    elif ids == 4:
                        thmxi,thmyi = landmrk.x * image_width, landmrk.y*image_height
                        thmx.append(thmxi)
                        thmx.append(thmyi)
                    elif ids == 8:
                        indxi, indyi = landmrk.x * image_width, landmrk.y*image_height
                        indx.append(indxi)
                        indy.append(indyi)
                    elif ids == 12:
                        midxi, midyi = landmrk.x * image_width, landmrk.y*image_height
                        midx.append(midxi)
                        midy.append(midyi)
                    elif ids == 16:
                        rngxi,rngyi = landmrk.x * image_width, landmrk.y*image_height
                        rngx.append(rngxi)
                        rngy.append(rngyi)
                    elif ids == 20:
                        pnkxi, pnkyi = landmrk.x * image_width, landmrk.y*image_height
                        pnkx.append(pnkxi)
                        pnky.append(pnkyi)      
        if counter>= 1000:
            calibration == False
        else:
            counter += 1
            
        wrstx = wrstx/len(wrstx)
        wrsty = wrsty/len(wrsty)
        thmx = thmx/len(thmx)
        thmy = thmy/len(thmy)
        indx = indx/len(indx)
        indy = indy/len(indy)
        midx = midx/len(midx)
        midy = midy/len(midy)
        rngx = rngx/len(rngx)
        rngy = rngy/len(rngy)
        pnkx = pnkx/len(pnkx)
        pnky = pnky/len(pnky)

        
        ind_rat = math.sqrt((indx-wrstx)^2 + (indy-wrsty)^2)
        
        print(ind_rat)

        
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
        
    cap.release()
    cv2.destroyAllWindows()
