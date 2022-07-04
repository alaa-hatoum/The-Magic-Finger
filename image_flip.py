import cv2
import os



directory_name = r"C:\Users\alaah\OneDrive\Desktop\Personal Software Projects\The-Magic-Finger"

img_path = r"C:\Users\alaah\OneDrive\Desktop\Personal Software Projects\The-Magic-Finger\test.jpg"

image = cv2.imread(img_path)

name = 'Display'

os.chdir(directory_name)

image_flip = cv2.flip(image,-1)

cv2.imwrite("test_flip.jpg",image_flip)

# Destroy all the windows
cv2.destroyAllWindows()