a = int(input("학생수입력 >>> "))

max_score = 0
max_name = ""

for i in range(1, a + 1):
    name, score = input(f"{i}번째 학생 이름, 점수 >>> ").split()
    score = int(score)

    if score > max_score:
        max_score = score
        max_name = name

print(f"{max_name} : {max_score}")