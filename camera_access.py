# import the opencv library
import cv2
#importing os module
import os

#Image name 
filename = 'test.jpg'

#image directory
directory = r'C:\Users\alaah\OneDrive\Desktop\Personal Software Projects\The-Magic-Finger'


vid = cv2.VideoCapture(0)

while(True):
    #capture the video frame by frame
    ret, frame = vid.read()
    
    #display the resulting frame
    cv2.imshow('Reflection', frame)
    
    
    #makes the loop end if you press 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
#changes location of directory
os.chdir(directory)

#saves the last frame of the video
cv2.imwrite(filename, frame)

# After the loop release the cap object 
vid.release()

# Destroy all the windows
cv2.destroyAllWindows()
