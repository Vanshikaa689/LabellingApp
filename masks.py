import os
import sys
  

import numpy as np

import cv2   
import matplotlib.pyplot as plt


imagefol=r"C:\VANSHIKA\UNIVERSITY\COURSES\YEAR 3\EDGE AI\LABELING_APP\images"
annotationfol=r"C:\VANSHIKA\UNIVERSITY\COURSES\YEAR 3\EDGE AI\LABELING_APP\labels"
segfol= r"C:\VANSHIKA\UNIVERSITY\COURSES\YEAR 3\EDGE AI\LABELING_APP\segfol"

if not os.path.exists(segfol): 
    os.makedirs(segfol)


imlist=os.listdir(imagefol)

font = cv2.FONT_HERSHEY_SIMPLEX 
fontScale = 1
color = (0, 0, 255) 
thickness = 2
org1 = (0,50)
org2 = (500,50)

org3 = (1000,50)
org4 = (1500,50)

colorcar=(255,150,255)
colorperson=(255,150,15)

for im in imlist:
    img=cv2.imread(os.path.join(imagefol,im))
    img = cv2.putText(img, "next_image", org2, font, fontScale,  color, thickness, cv2.LINE_AA)
    img = cv2.rectangle(img, (500,10), (530,30), color, -1)

    img = cv2.putText(img, "car", org3, font, fontScale,  color, thickness, cv2.LINE_AA)
    img = cv2.rectangle(img, (1000,10), (1030,30), color, -1)

    img = cv2.putText(img, "person", org4, font, fontScale,  color, thickness, cv2.LINE_AA)
    img = cv2.rectangle(img, (1500,10), (1530,30), color, -1)

    


    plt.imshow(img)
    imb=np.zeros_like(img)
    l=0
    
    dst_txt=annotationfol + "/" + im[:-3] + 'txt'
    with open( dst_txt, 'w') as f:
        flag=1
        while(1): 
            pl=[] 

            if flag==0:
                break
            
            while(1):
                
                p=plt.ginput(1)
                (px,py)=p[0][0],p[0][1]
                
                if px >1000 and py >10 and px<1030 and py<30:
                    cls="car"
                    col=colorcar
                    break

                if px >1500 and py >10 and px<1530 and py<30:
                    cls="person"
                    col=colorperson
                    break

                if px >500 and py >10 and px<530 and py<30:
                    plt.close()
                    flag=0
                    break
                l+=1



                pl.append((int(px),int(py)))


            if flag:
                cv2.fillPoly(imb, [np.array(pl)], col)
                f.write(cls + " ")
                for a in pl:
                    
                    f.write("("+str(a[0]) + "," + str(a[1])+ ") ")
                f.write("\n")

        
        cv2.imwrite(os.path.join(segfol,im),imb)
        cv2.imshow('win',imb)
        cv2.waitKey()
        cv2.destroyAllWindows()

            
                    

            

#run for multiple images
#save the segmented image using cv2.imwrite
#try to save multiple polygons in the same image



#Take an image and its label (txt file you created with selectroi)
#Display the bb on the image using the txt file using cv2.rectangle..
#Now allow the user to add more bb and edit the file...