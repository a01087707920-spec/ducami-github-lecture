pw = input("비밀번호를 입력하세요. >>> ")


if len(pw) >= 8 and any(ch.isalpha() for ch in pw) and any(ch.isdigit() for ch in pw):
    print("사용가능한 비밀번호")
else:
    print("사용불가한 비밀번호")



