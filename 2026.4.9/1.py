a = int(input("학생수입력. >>> "))

sum = 0
score = []

for i in range(1, 1 + a):
    jum = int(input(f"{i}번째 학생의 점수 입력 >>> "))

    sum += jum
    score.append(jum)
    

print(f"총점 : {sum}")
print(f"평균 : {sum / i}")
print(f"최고 : {max(score)}")
print(f"최저 : {min(score)}")





