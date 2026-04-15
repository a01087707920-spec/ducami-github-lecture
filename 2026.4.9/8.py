a = input("단어 입력 >>> ")

eng = 0
num = 0
space = 0
others = 0


for i in a:
    if i.isalpha(): #영문자 카운트
        eng += 1     
    elif i.isdigit(): #숫자 카운트
        num += 1    
    elif i == " ":   #스페이스 키운트
        space += 1    
    else:         #기타문자 카운트
        others += 1 

print(eng)
print(num)
print(space)
print(others)

