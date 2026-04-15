a = tuple(input("단어 입력 >>> ").split())

longest = a[0]

for i in a:
    if len(i) > len(longest): #len = 길이구하는 함수
        longest = i

print(f"가장 긴 단어 : {longest}")

