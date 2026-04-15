num = int(input("정수 입력 >>> "))

sum = 0

for i in range(1, num + 1):
    if i % 3 == 0:
        sum += i
    else:
        None

print(sum)
