words = input("단어 입력 >>> ").split()

a = ("a", "e", "i", "o", "u")

count = 0

for word in words: #단어 하나씩 꺼내기
    count = 0
    for ch in word: #문자 하나씩 검사
        if ch in a: #모음인지 확인
            count += 1 #모음이 있으면 카운트 1
    print(word, count)