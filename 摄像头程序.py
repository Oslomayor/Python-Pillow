# 摄像头程序
import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while(1):    # get a frame and show   
    ret, frame = cap.read()   
    cv2.imshow('Capture', frame)        
    if cv2.waitKey(1) & 0xFF == ord('q'):      
        breakcap.release()
cv2.destroyAllWindows()
