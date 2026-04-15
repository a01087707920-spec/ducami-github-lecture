s = input("문자열 입력 >>> ")

result = []

for ch in s:
    if s.count(ch) > 1 and ch not in result:
        result.append(ch)

print(result)
