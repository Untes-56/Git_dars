import os
os.system("cls")

son = input("Son kiriting: ")
nol_soni = 0
for i in son:
    if int(i) == 0:
        nol_soni += 1
    else:
        break
print(nol_soni)
