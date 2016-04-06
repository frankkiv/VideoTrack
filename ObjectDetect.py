import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
import numpy as np
imagePath = 'TestPhoto2.jpg'
img_rgb = cv2.imread(imagePath)
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

template = cv2.imread('shape.jpg',0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)

# #study
# abc = [('a','b','c','d','e'),('f','g','h','i','j')]
# print zip(abc)
# print zip(*abc)
# print zip(*abc[::-1])
# # [(('a', 'b', 'c', 'd', 'e'),), (('f', 'g', 'h', 'i', 'j'),)]
# # [('a', 'f'), ('b', 'g'), ('c', 'h'), ('d', 'i'), ('e', 'j')]
# # [('f', 'a'), ('g', 'b'), ('h', 'c'), ('i', 'd'), ('j', 'e')]


for pt in zip(*loc[::-1]):
    print pt
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)

small = cv2.resize(img_rgb, (0,0), fx=0.5, fy=0.5) 
cv2.imshow('Detected',small)

cv2.waitKey(0)
cv2.destroyAllWindow()