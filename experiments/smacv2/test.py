import cv2
import numpy as np
x = np.zeros((1440,1920*3,3))
imgs = ["terran_3_vs_4","terran_3_vs_4_p1_","terran_5_vs_5"]
for i,img in enumerate(imgs) :
    img = cv2.imread(img+".png")
    print(img.shape)
    r = i//3
    c = i%3
    x[1440*r:1440*(r+1),1920*c:1920*(c+1),:] = img
x = cv2.resize(x,(1920*3,1440))
cv2.imwrite("result_addition_smacv2.png",x)