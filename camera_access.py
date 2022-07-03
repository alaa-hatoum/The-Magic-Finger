# import the opencv library
import cv2

vid = cv2.VideoCapture(0)

while(True):
    #capture the video frame by frame
    ret, frame = vid.read()
    
    #displat the resulting frame
    cv2.imshow('Reflection', frame)
    
    #makes the loop end if you press 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object 
vid.release()

# Destroy all the windows
cv2.destroyAllWindows()
