a = int(input("학생수입력 >>> "))

students = {}

pass_list = {}
fail_list = {}

for i in range(1, a + 1):
    name, score = input(f"{i}번째 학생 이름, 점수 >>> ").split()
    score = int(score)

    students[name] = score  

for name, score in students.items():
    if score >= 80:
        pass_list[name] = score
    else:
        fail_list[name] = score

for name, score in pass_list.items():
    print(f"{name} : 합격")

for name, score in fail_list.items():
    print(f"{name} : 불합격")

