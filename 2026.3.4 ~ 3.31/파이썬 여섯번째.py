gas_list = [10, 7, 8, 6, 15]  # 각 호의 7월 가스 사용량

for i in range(len(gas_list)):
    gas = gas_list[i]
    totalPrice = 50000 + gas * 3000

    print(f"{i+1}호: {totalPrice}원")

word = input("문자 입력 >> ")

for i in range(-1, -1-len(word), -1):
    print(word[i], end = '')

import random
d = ["cream", "pancakes", "brownies", "cookies", "candy"]
random.shuffle(d) 
print(d)  

import random
rps = ["가위", "바위", "보"]
choice = random.choice(rps)
print(choice)

import random

print("컴퓨터를 이겨라 [가위바위보]")

i_cho = input('나의 선택 >>> ')

com = ["가위", "바위", "보"]
com_cho = random.choice(com)
print('컴퓨터의 선택 :', com_cho)

if i_cho == com_cho:
    print("비김 😐")
elif (i_cho == "가위" and com_cho == "보") or \
     (i_cho == "바위" and com_cho == "가위") or \
     (i_cho == "보" and com_cho == "바위"):
    print("이김 ^^")
else:
    print("짐 ㅠ")


