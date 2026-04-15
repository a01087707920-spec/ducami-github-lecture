num = map(int, input("숫자 입력 >>> ").split())

even_sum = 0
odd_sum = 0

for i in num:
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

print(f"짝수 합 : {even_sum}")
print(f"홀수 합 : {odd_sum}")