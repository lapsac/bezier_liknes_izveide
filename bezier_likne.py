# Programmējamais kods
import numpy as np
import matplotlib.pyplot as plt
img=np.ones((600,600,3))#Height, width, 3-rgb kanali
def DrawBezier(x0,y0,x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7): # jāmaina atkaribā no varianta
    x=x0#sākumpunkts (sākotnējais pikselis)
    y=y0
    ts=0.001 # SOLIS norāda no cik pikseļiem sanāks likne <- no 100 pikseļiem / līknes precizitāte
    t=0 #parametrs kas mainās intervālā no 0 līdz 1
    while t<=1.0: # mainam atkarībā no varianta
        B0=(1-t)**7# 2. pakāpe
        B1=7*t*(1-t)**6
        B2=21*t**2*(1-t)**5
        B3=35*t**3*(1-t)**4
        B4=35*t**4*(1-t)**3
        B5=21*t**5*(1-t)**2
        B6=7*t**5*(1-t)**1
        B7=t**7 
        
        
        x=int(x0*B0+x1*B1+x2*B2+x3*B3+x4*B4+x5*B5+x6*B6+x7*B7) # funkcija bezier līkņu zīmēšanai grafika x vērtībās
        y=int(y0*B0+y1*B1+y2*B2+y3*B3+y4*B4+y5*B5+y6*B6+y7*B7) #  funkcija bezier līkņu zīmēšanai grafika y vērtībās
        img[y,x]=(1,0,1) #magenta pixel
        t=t+ts

DrawBezier(300,100,200,200,200,350,200,400,350,500,200,500,400,300,200,300) #kontrol punkti x y, x y, x y, utt katram punktam
#             1       2       3       4       5       6       7       8  <- kontrolpunkti, virs tiem x un y koordinātes
plt.figure(figsize=(5,5),dpi=100,facecolor='w') # loga mērogs un diazins
plt.imshow(img) #izvade
plt.show()#atspoguļojums
