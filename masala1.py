import os
os.system("cls")
from json import dumps

son = int(input("Son kiriting : "))
raqam =[0,1,2,3,4,5,6,7,8,9]

raqamlar_soni = []
qaysi_raqam = []
natija = {}

for i in raqam:
    if str(son).count(str(i)) >= 1:
        raqamlar_soni.append(str(son).count(str(i)))
        qaysi_raqam.append(i)

natija = dict(zip(qaysi_raqam,raqamlar_soni))
print(dumps(natija, indent=4))
