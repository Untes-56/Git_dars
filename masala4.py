import os
os.system("cls")

matn = open("istalgan.txt", "r")
malumot = matn.read()
matn.close()

chap_qol = "1QAZ2WSX3EDC45RTFGVB"
ong_qol = "67YUHJNM8IK,9OL.0P;:?/'_-"

count_ong = 0
count_chap = 0

for belgi in malumot:
    if belgi.capitalize() in chap_qol:
        count_chap += 1
    if belgi.capitalize() in ong_qol:
        count_ong += 1

print("Ong qo'l belgi soni:", count_ong) 
print("Chap qo'l belgi soni:", count_chap)
