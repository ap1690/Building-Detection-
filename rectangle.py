import cv2 
import numpy as np 
import matplotlib.pyplot as plt
  
image = cv2.imread('30dff8c4-0465-41a7-856e-4aabfcde26d2.jpg')  
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
edged = cv2.Canny(gray, 0, 30) 
contours, hierarchy = cv2.findContours(edged,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)   
print("Number of Contours found = " + str(len(contours))) 

cv2.imshow("edges",cv2.resize(edged,(500,500)))
cv2.waitKey(0)
xc=0
for i in contours:
            (x, y, w, h) = cv2.boundingRect(i)
            try:
                if gray[int(y+h/3),int(x+h/3)]==243 and cv2.contourArea(i)>100:
                    print("rectangle")
                    cv2.putText(image, 'Building', (x,y), cv2.FONT_HERSHEY_SIMPLEX,1, (0,0,255), 1, cv2.LINE_AA)
                    cv2.drawContours(image, i, -1, (0, 255, 0), 3) 
            except:
                continue
plt.imshow(image)
plt.show()
print("total rectangle",xc)
cv2.imshow('Contours', cv2.resize(image,(500,500))) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 
