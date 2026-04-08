a = 50
b = 20
c = a + b
print(a, b, c)
print('a =', a, 'b =', b, 'c = ', c)

name = "소마고 친구들"
print(name, "반과워요!")

a = input("첫번째 수 : ")
a = int(a)
b = input("두번째 수 : ")
b = int(b)
c = a + b
print("두 수의 합은 : ", c)

print("안녕하세요.")
name = input("이름이 뭐에요? >>> ")
print(f'{name}님 반가워요!')
age = int(input("몇 살이세요? >>> "))
print(f"십년 뒤에는 {10 + age}살이 되겠군요!")
food = input("가장 좋아하는 음식이 뭐애요? >>> ")
print(f"저도 {food} 좋아해요!")

price = 800
count = 10
total = price * count
print(f'전체 빵값 : {total - 1}')

price = int(input("빵의 단가 입력 >>> "))
count = int(input("빵의 갯수 입력 >>> "))
print(f'전체 빵값 : {(price - 1) * count}원')

h = int(input("키 입력 >>> "))
w = int(input("몸무게 입력 >>> "))
print(f"체질량 지수 : {w / (h * h) * 10000}")

a = int(input("연필 핀매 갯수 >>> "))
b = int(input("지우개 핀매 갯수 >>> "))
c = int(input("공책 핀매 갯수 >>> "))

print(f"""
연필의 판매 갯수 : {a}
지우개 핀매 갯수 : {b}
공책 핀매 갯수 : {c}
------------------------
파이썬 문방구 오늘의 판매내역
------------------------
1. 연필 : {a}개, {a * 700}원
2. 연필 : {b}개, {b * 500}원
3. 연필 : {c}개, {c * 2500}원
------------------------
오늘 총 판매 금액 : {(a * 700) + (b * 500) + (c * 2500)}원
------------------------
""")

sco = int(input("점수를 입력해주세요. >>> "))
if sco >= 60:
    print("합격입니다.")
else:
    print("불합격입니다.")

card = int(input("잔액 입력 >>> "))
if card >= 1000:
    print("반갑습니다.")

else:
    print("잔액이 부족합니다.")

capt = input("보안 문자 입력 >>> ")
if capt == "FaSHoiN":
    print("확인")

else:
    print("다시 입력하세요")

base = 270 
use = int(input("전기 사용량 입력 >>> "))
if (use > 100):
    cost = (use * base) * 1.2

else:
    print(f'전기 사용량 : {use}kW')
    print(f'요금 : {cost}원')

id = input("id를 입력하세요 >> ")
pwd = input("패스워드를 입력하세요. >> ")
if (id == "info" and pwd == "edu"):
    print('로그인 되었습니다.')
else:
    print("로그인에 실패했습니다.")

kind = input("당신의 승객 유형은 (임산부, 노약자, 장애인, 해당 사항 없음) >>> ")
if (kind == "임산부" or kind == "노약자" or kind == "장애인"):
    print("좌석 이용 가능")

else:
    print("좌석 이용 불가능")


p = int(input("점수를 입력하세요. >>> "))

if p >= 90:
    print("당신의 등급은 A입니다.")

elif p >= 80:
    print("당신의 등급은 B입니다.")

elif p >= 70:
    print("당신의 등급은 C입니다.")

elif p >= 60:
    print("당신의 등급은 D입니다.")

else:
    print("당신의 등급은 E입니다.")

num = int(input("정수를 입력해주세요."))

if num % 2 == 0:
    print("짝수입니다")
else:
    print("홀수입니다")

a = int(input("정수를 입력하세요. >> "))
if a > 0:
    print("양수입니다.")

elif a == 0:
    print('0입니다.')

else:
    print("음수입니다.")

age = int(input("정수를 입력하세요. >> "))
cost = 14000

if age <= 10:
    print(f'20% 할인 대상입니다. \n {14000 * 0.2}원입니다.')

elif age >= 60:
    print(f'30% 할인 대상입니다. \n {14000 * 0.3}원입니다.')

else:
    print(f'할인 대상이 아닙니다. \n {cost}원입니다.')

i = 1
while i < 5:
    print("Hello World")
    i += 1
    
i = 1
hap = 0
while i <= 5:
    print(i)
    hap += i
    i += 1
print(hap)

sum = 0

while True:
    n = int(input("숫자 입력: "))
    sum += n
    
    if sum > 20:
        break

print(f"합 : {sum}")

total = 0

while True:
    score = int(input("점수 입력: "))
    total += score

    if total > 20:
        print("합:", total)
        break

for i in range(5):
    print('Hello World')

for i in range(1, 6):
    print(i, "Hello World")

sum = 0
for i in range(1, 6):
    sum += i
    print(i, end=" ")
print(sum)

for i in range(10):
    print(i, end=" ")

for i in range(0,10):
    print(i, end=" ")
print()

for i in range(1, 11, 2):
    print(i, end=" ")   
print()

for i in range(10, 0, -2):
    print(i, end=" ")
print()

