words = input("문자열 입력 >>> ").split()

a = ("a", "e", "i", "o", "u")

count = 0

for words in words:
    for ch in words:
        if ch.lower() in a:
            count += 1

print(f'모음 개수 : {count}')
