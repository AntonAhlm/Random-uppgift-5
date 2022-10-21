
import random

kast=[1,2,3,4,5,6]
antalkast=[]
a=int(input("Antal kast : "))
for i in range(0,a+1):
    b=random.choice(kast)
    print("kast",i,":",b)
    if b <=3:
        antalkast.append(1)
print("Antal kast lika med eller under 3 :",sum(antalkast))