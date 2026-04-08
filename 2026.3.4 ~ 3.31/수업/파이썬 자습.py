a = input()
print(a)

a = int(input())
print(a + 10)

a = int(input("숫자 입력: "))

if a % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")

for i in range(1, 6):
    print(i)

for i in range(1, 11):
    if i % 2 == 0:
        print(i)

sum = 0     
for i in range(1, 11):
    sum += i
print(sum)
    
a = int(input("숫자 입력: "))

sum = 0
for i in range(1, a + 1):
    sum += i
print(sum)

a = int(input("숫자 입력: "))
dan = 0
for i in range(1, 10):
    dan = a * i
    print(f"{a} x {i} = {dan}")

a = [3, 6, 9, 12, 15]
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4]) 

a = [3, 6, 9, 12, 15]

for i in a:
    print(i)

a = [1, 2, 3, 4, 5, 6]

for i in a:
    if i % 2 == 0:
        print(i)
 
a = [1, 2, 3, 4, 5, 6]
sum = 0
for i in a:
    sum += i
print(sum)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

max_num = a[0]
for i in a:
    if i > max_num:
        max_num = i
print(max_num)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

min_num = a[0]
for i in a:
    if i < min_num:
        min_num = i
print(min_num)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

count = 0
for i in a:
    if i % 2 == 0:
        count +=1
print(count)


a = 10
b = 5

print(f"{a} + {b} = {a + b}")

x = 7
y = 3

print(f"{x} - {y} = {x - y}")

for i in range(1, 999999999999999999999999999, 10000):
    print(i)

a = int(input("숫자 입력: "))

if a % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")

b = int(input("숫자 입력: "))

if b >= 0:
    print("양수입니다.")
else:
    print("음수입니다.")

c = int(input("숫자 입력: "))

if a % 3 == 0:
    print("3의 배수입니다.")
else:
    print("3의 배수가 아닙니다.")

d = int(input("숫자 입력: "))

if d % 3 == 0 and d % 2 == 0:
    print("3의 배수이면서 짝수입니다.")
else:
    print("조건을 만족하지 않습니다.")

