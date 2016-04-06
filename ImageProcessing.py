import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
import random 
import numpy as np
imagePath = 'TestPhoto.jpg'
image = cv2.imread(imagePath)

# #source, start ,end, color ,size
# cv2.line(image, (0,0), (150,150), (255,0,0), 10)
# cv2.rectangle(image, (100,0), (150,150), (255,255,0), 5)
# cv2.circle(image, (400,400), 50,  (0,0,255))

# #add text on it
# font = cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(image,'OpenCV Tuts!',(10,500), font, 6, (200,255,155), 13)

# #cut and paste
# pasteImg = image[300:400,300:400]
# image[0:100,0:100] = pasteImg

# # two return one is threshold value input (source, threshold, tobe value ,cv2.THRESH_BINARY)
# grayscaled = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# retval, threshold = cv2.threshold(grayscaled, 130, 255, cv2.THRESH_BINARY)
# cv2.imshow('Threshold Drawing', threshold);

# cv2.imshow('TEST Drawing', image);

# getVideoSource from webcam!
cap = cv2.VideoCapture(0)

while(1):
    _, frame = cap.read()

    #convert to HSV Hue, Saturation, Lightness
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([30,150,50])
    upper_red = np.array([255,255,180])
    
    #create mask in range
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame,frame, mask= mask)

    # #gaussian blu
    # blur = cv2.GaussianBlur(res,(15,15),0)
    # cv2.imshow('Gaussian Blurring',blur)

    # #Simple image processing
    # kernel = np.ones((5,5),np.uint8)
    # erosion = cv2.erode(mask, kernel, iterations = 1)
    # dilation = cv2.dilate(mask, kernel, iterations = 1)
    # opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    # closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    # cv2.imshow('opening',opening)
    # cv2.imshow('closing',closing)

    # edge detect
    edges = cv2.Canny(frame,100,200)
    cv2.imshow('Edges',edges)
    # cv2.imshow('frame',frame)
    # cv2.imshow('mask',mask)
    # cv2.imshow('res',res)
   

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cap.release()

#wait for any key to close window
cv2.waitKey(0)
cv2.destroyAllWindows()