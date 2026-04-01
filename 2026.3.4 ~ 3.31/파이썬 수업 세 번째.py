a = input("a 합격(T/F): ").upper()
b = input("b 합격(T/F): ").upper()
c = input("c 합격(T/F): ").upper()
d = input("d 합격(T/F): ").upper()

a = (a == "T")
b = (b == "T")
c = (c == "T")
d = (d == "T")

Pass = True

if b and not a:
    Pass = False

if not c and not b:
    Pass = False

if not (a or d):
    Pass = False

if d != b:
    Pass = False


if Pass:
    print("조건 만족")
else:
    print("조건 불만족")

# a = input()
# b = input()
# c = input()
# d = input()

# if b == 'False' and a == b:
#     print("조건 불만족")
    
# elif b == 'False' and a == b:
#     print("조건 불만족")

# elif b == 'False' and a == b:
#     print("조건 불만족")

# elif b == 'False' and a == b:
#     print("조건 불만족")

# a = input("a(T/F): ").upper()
# b = input("b(T/F): ").upper()
# c = input("c(T/F): ").upper()
# d = input("d(T/F): ").upper()

# a = a == "T"
# b = b == "T"
# c = c == "T"
# d = d == "T"

# if (not b or a) and (c or b) and (a != d) and (d == b):
#     print("조건 만족")
# else:
#     print("조건 불만족")

# # 각각 입력 받기
# a = input("a: ").lower()
# b = input("b: ").lower()
# c = input("c: ").lower()
# d = input("d: ").lower()

# # 입력이 T F F T면 만족
# if a == "t" and b == "f" and c == "f" and d == "t":
#     print("조건 만족")
# else:
#     print("조건 불만족")

clean = input('세탁할 물건을 선택하십시오. >>> ')

if clean == "안경 닦이":
    print("세탁을 안 합니다.")

elif clean == "신분":
    print("다시 태어나세요.")

elif clean == "티셔츠" and "바지" and "양말":
    print("세탁기에 넣고 돌리세요.")

elif clean == "교복":
    print("드라이 세탁 하세요")

else:
    print("엄마한테 물어보세요.")