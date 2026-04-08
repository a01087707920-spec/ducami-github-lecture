con = "sweet"
if con == "sweet":
    print("삼키다.")
else:
    [print("뱉는다.")]

season = "summer"

if season =="spring":
    print("Flower blooming.")

elif season == "summer":
    print("Too warm")

elif season == "fall":
    print("The season of reading")

else:
    print("Too cold.")

season = "winter"

if season =="spring":
    print("Flower blooming.")

elif season == "summer":
    print("Too warm")

elif season == "fall":
    print("The season of reading")

elif season == "winter":
    print("Too cold.")

temp = 18

if temp < 26:
    pass

else:
    print("에어컨을 켠다.")

age = 19
height = 150

if height >= 150 and age < 10:
    print("놀이기구를 탈 수 있습니다.")

else:
    print("놀이기구를 탈 수 없습니다")

num = input('Choose the number.')
if "3" in num or "6" in num or "9" in num:
    print("짝")

else:
    print("369숫자가 아닙니다.")

i = 1

while i < 11: #조건식
    print("파이썬" + str(i))
    i = i + 1 #탈출조건

s = 0
while ():
    num = input("숫자 입력 (종료는 n) >>> ")
    if num == "n":
        break
    s = 
print("합계 : ", s)

for i in range(1, 101):
    if i % 10 == 0:
        print(i)
print("종료합니다.")

count = 0
for s in 'banana':
    if s == 'a':
        count = count + 1
print("a문자 포함 횟수는", count)

num = int(input("숫자를 입력하세요. >>> "))
sum = 1
for i in range(1, num + 1):
    sum = sum * i
print(num,"! = ", sum)

def list_avg(s_list):
    sum = 0
    for i in s_list:
        sum = sum + i
    result = sum/len(s_list)
    print("점수의 평균 : ", result)

score = [90, 80, 70, 50, 60]
list_avg(score) #함수호출


