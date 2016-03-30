import matplotlib.pyplot as plt
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
import random 

imagePath = 'TestPhoto.jpg'
image = cv2.imread(imagePath)

#load opencv training data
faceCascade = cv2.CascadeClassifier('/usr/local/Cellar/opencv/2.4.12_2/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml') 
#eyeCascade = cv2.CascadeClassifier('/usr/local/Cellar/opencv/2.4.12_2/share/OpenCV/haarcascades/haarcascade_eye.xml')

#image2gray
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
font = cv2.FONT_HERSHEY_SIMPLEX
faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=8, minSize=(80, 80), flags = cv2.CASCADE_SCALE_IMAGE)
#faces = faceCascade.detectMultiScale(gray, 1.3, 5)
#eyes = eyeCascade.detectMultiScale(gray)
#print faces

for (x, y, w, h) in faces:
    
    #add rect (sourceimage,lefttop, rightbottom, color, size)
    cv2.rectangle(image, (x,y), (x+w,y+h), (14,201,255), 5)
    #(video source, string, TopLeft, font, font-size, font-color, font-weight)
    cv2.putText(image, str(random.randrange(20,30)), (x+(w/2)-30,y-10), font, 2, (14,201,255), 7)

plt.imshow(cv2.cvtColor(image,cv2.COLOR_RGB2BGR))


import imutils

camera = cv2.VideoCapture(0)
# keep looping
while True:
    # grab the current frame
    (grabbed, frame) = camera.read()
 
    # resize the frame, blur it, and convert it to the HSV
    # color space
    frame = imutils.resize(frame, width=600)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    font = cv2.FONT_HERSHEY_SIMPLEX
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=8, minSize=(100, 100), flags = cv2.CASCADE_SCALE_IMAGE)
    for (x, y, w, h) in faces:
    
        #(sourceimage,lefttop, rightbottom, color, size)
        cv2.rectangle(frame, (x,y), (x+w,y+h), (14,201,255), 5)
        cv2.putText(frame, "Frank", (x,y-10), font, 2, (14,201,255), 7)

    # show the frame to our screen
    cv2.imshow("Frame", frame)
 
    # if the 'q' key is pressed, stop the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()
