a = int(input("숫자 입력 >> "))

if a % 2 == 0:
    print("짝수")

else:
    print("홀수")


a = int(input("숫자 입력 >> "))

if a % 3 == 0:
    print("3의 배수")

else:
    print("3의 배수가 아님")

a = int(input("숫자 입력 >> "))

if a % 3 == 0:
    print("3의 배수")

else:
    print("3의 배수가 아님")
    

a = int(input("숫자 입력 >> "))

if a % 3 == 0 and a % 2 == 0:
    print("3의 배수이면서 짝수입니다.")

elif a % 3 == 0:
    print("3의 배수이지만 짝수가 아닙니다.")

else:
    print("3의 배수가 아닙니다.")

    
a = int(input("숫자 입력 >> "))

if a > 0:
    print("양수 입니다.")

elif a == 0:
    print("0입니다.")

else:
    print("음수입니다.")
    

a = int(input("숫자 입력 >> "))

sum = 0
for i in range(a, a + 1):
    sum += i
    print(a)


a = int(input("숫자 입력 >> "))

for i in range(1, 10):
    print(f'{a} x {i} = {a*i}')



a = int(input("숫자 입력 >> "))

is_frime = True

if a == 1:
    is_frime = False
else:
    for i in range(2, a):
        if a % i == 0:
            is_frime = False
            break

if is_frime:
    print("소수입니다")

else:
    print("소수가 아닙니다.")


a = int(input("숫자 입력 >> "))

result = 1

for i in range(1, a + 1):
    result *= i

print(result)

a = [1, 2, 3, 4, 5, 6]

count = 0

for i in a:
    if i % 2 == 0:
        count += 1

print(count)

a = int(input("숫자 입력 >>> "))

if a % 2 == 0:
    print("짝수입니다.")

else: 
    print("홀수입니다.")


a = [1, 2, 3, 4, 5, 6]

count = 0

for i in range(1, a + 1):
    if i % 2 == 0:
        count += 1

print(count)

a = int(input("숫자 입력 >> "))

max_num = a

for i in a:
    if i > max_num:
        max_num = i
print(i)