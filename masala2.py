import os
os.system("cls")

def funk(son:int, royhat:list):
    new_list = sorted(royhat, key=lambda qiymat: qiymat["Narxi"], reverse=True)
    for i in range(son):
        print(new_list[i])

list1=[
    {"Mahsulot nomi":"Non", "Narxi":3500},
    {"Mahsulot nomi":"Go'sht", "Narxi":80000},
    {"Mahsulot nomi":"Suv", "Narxi":11000},
    {"Mahsulot nomi":"Kartoshka", "Narxi":10000},
    {"Mahsulot nomi":"Sabzi", "Narxi":8000},
]

son = int(input("Qimmat mahsulot sonini kiriting: "))
funk(son, list1)
