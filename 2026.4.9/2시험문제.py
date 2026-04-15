a = list(map(int, input("숫자입력 >>> ").split()))

li1 = []
li2 = []
for i in a:
    if i % 2 == 0:
        li1.append(i)

    else:
        li2.append(i)

print(f"짝수 : {li1}")
print(f"짝수 : {li2}")

