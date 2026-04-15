word = input("문자열 입력 >>> ")
word_clean = word.replace(" ", "").lower() # 문자열 공백, 대문자를 소문자로 맞추기

if word_clean == word_clean[::-1]: #문자열 뒤집기 원래 문자열이랑 같으면 회문
    print("회문입니다")
else:
    print("회문이 아닙니다")
    