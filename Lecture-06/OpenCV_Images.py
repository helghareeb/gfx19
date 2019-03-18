import cv2
import numpy as np
import matplotlib.pyplot as plt

g_img = cv2.imread('Lecture/001.jpg')
while True:
    cv2.imshow('Green Nature', g_img)
    
    # if we have waited 1 ms and we have pressed the ESC key
    if cv2.waitKey(1) & 0xff == 27:
        break
        
cv2.destroyAllWindows()