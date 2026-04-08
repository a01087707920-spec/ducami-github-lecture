# a = 50
# b = 20
# c = a + b
# print(a, b, c)
# print('a =', a, 'b =', b, 'c =', c)

# name = "친구들"
# print(name, '반가워요!')

# a = input("First number >>> ")
# a = int(a)
# b = input("Second number >>> ")
# b = int(b)
# c = a + b
# print("두 수의 합은", c)

# print("안녕하세요!")
# name = input("이름이 뭐에요? >>> ")
# print(name, "님 반가워요")
# age = int(input("몇 살이세요? >>> "))
# print("10년 뒤에는", age, "살이 되는군요!")
# food = input("가장 좋아하는 음식이 무엇인가요? >>> ")
# print("저도", food, "아주 좋아해요.")

# price = 800
# count = 10
# total = (price * count / 0.1)
# total = float(total)
# print("천제 빵 값 : ", total)

# price = input("빵의 단가 입력 >>> ")
# price = int(price)
# count = int(input("빵의 개수 입력"))
# total = (price * count / 0.1)
# total = float(total)
# print("전체 빵 값", total)

# height = input("키 입력 >>> ")
# height = int(height)
# weight = input("몸무게 입력 >>> ")
# weight = int(weight)
# bmi = (weight / height * height * 10000)
# print("체질량 지수 : ", bmi)

pencel = 700
eraser = 500
note = 2500

pencelcount = int(input("\n연필 갯수 입력 >>> "))
erasercount = int(input("지우개 갯수 입력 >>> "))
notecount = int(input("공책 갯수 입력 >>> "))

print(f"""------------------------
연필의 판매 개수 : {pencel}
지우개의 판매 개수 : {eraser}
공책의 판매 개수 : {note}
------------------------
임준성 문방구 오늘의 매출
------------------------
1. 연필 : {pencel}개, {pencel * pencelcount}원
2. 지우개 : {eraser}개, {eraser * erasercount}원
3. 공책 : {note}개, {note * notecount}원
------------------------
오늘 총 판매 금액 : {(pencel * pencelcount) + (eraser * erasercount) + (note * notecount)}
------------------------
""")


