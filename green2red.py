import cv2
import matplotlib.pyplot as plt

p = cv2.imread('image.jpg')
p = cv2.cvtColor(p, cv2.COLOR_BGR2RGB)

plt.imshow(p)
plt.figure()
q = p.copy()
for w in q:
    for r in w:
        if(r[1]>r[0] and r[1]>r[2]):
            
            if r[1]+100>255:
                r[0],r[1]=255,r[0]
            else:
                r[0],r[1]=r[1],r[0]
            

plt.imshow(q)
plt.show()

