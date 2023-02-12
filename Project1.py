import numpy as np
import matplotlib.pyplot as plt
import cv2
import pyautogui
pyautogui.FAILSAFE=False
pyautogui.leftClick()
pyautogui.screenshot('1.png')
img = cv2.imread('1.png')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


_, binary = cv2.threshold(gray, 10 ,250, cv2.THRESH_BINARY)


#plt.imshow(binary, cmap="gray")
#plt.show()

contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#img = cv2.drawContours(img, contours, -1, (0,255,0),2)
#plt.imshow(img)
#plt.show()

if len(contours) !=0:
    for contour in contours:
        if cv2.contourArea((contour)) > 150:
            x,y,w,h = cv2.boundingRect(contour)
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,),1)
            pyautogui.moveTo(x, y)
            pyautogui.keyDown('ctrl')
            pyautogui.press('q')
            pyautogui.keyUp('ctrl')
            #print(x, y)




