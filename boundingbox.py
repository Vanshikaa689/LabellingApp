import os
import cv2


imagefol=r"C:\VANSHIKA\UNIVERSITY\COURSES\YEAR 3\EDGE AI\LABELING_APP\images"
annotationfol=r"C:\VANSHIKA\UNIVERSITY\COURSES\YEAR 3\EDGE AI\LABELING_APP\labels"


imlist=os.listdir(imagefol)

font = cv2.FONT_HERSHEY_SIMPLEX 
fontScale = 1
color = (0, 0, 255) 
thickness = 2

for im in imlist:
    img=cv2.imread(os.path.join(imagefol,im))
    (r,c,ch)=img.shape

    org = (00, 20) 
    img = cv2.putText(img, "next", org, font, fontScale,  color, thickness, cv2.LINE_AA)

    org = (500, 20) 
    img = cv2.putText(img, "car", org, font, fontScale,  color, thickness, cv2.LINE_AA)


    org = (1000, 20) 
    img = cv2.putText(img, "person", org, font, fontScale,  color, thickness, cv2.LINE_AA)


    frame= im[:-4]
    dst_txt =  frame + '.txt'

    with open(os.path.join(annotationfol, dst_txt), 'a') as f:

        while(1):
            r = cv2.selectROI(img) 

            if r[0]< 50 and r[1] < 50:  
                break
            
            
            r1 = cv2.selectROI(img)

            if r1[0]>500 and r1[0] < 520 and r1[1]> 20 and r1[1] < 40: 
                s="car" 

            if r1[0]> 1000 and r1[0] < 1020 and r1[1]> 20 and r1[1] < 40: 
                s="person" 
            line= s + " " + str(r[0]) + " " + str(r[1]) + " " + str(r[2]) + " " + str(r[3]) + "\n"
            f.write(line)
    f.close()


