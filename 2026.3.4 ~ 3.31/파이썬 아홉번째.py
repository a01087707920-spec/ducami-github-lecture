# import random

# user = input("숫자 2개 입력(숫자 사이 공백) >>> ")
# user = list(map(int, user.split(' ')))

# com = [random.randint(1, 6), random.randint(1, 6)]

# print(f"com = {com}  user = {user}")

# count = 0
# for i in user:
#     if i in com:
#         count += 1
#         com.remove(i)

# if count == 2:
#     print("1등")
# elif count == 1:
#     print("2등")
# else:
#     print("꽝")

#----------------------------------------------
# #세 개의 숫자가 주어질 때 오름차순으로 나열했을때 두번째로 큰 수를 출력하시오
# num = input("숫자 3개 입력(숫자 사이 공백) >>> ")
# num = list(map(int, num.split(' ')))
# sorted_num = sorted(num)
# print(sorted_num[1])    
#----------------------------------------------

su = int(input("정수 입력 >>> "))

print(f"10진수 {su} 2진수 {bin(su)} 8진수 {oct(su)} 16진수 {hex(su)}")

ch = input("문자 입력 >>> ")
ch_b = ch.encode('utf-8')
print(f"문자 {ch} 2진수 {bin(ch_b[0])} 8진수 {oct(ch_b[0])} 16진수 {hex(ch_b[0])}")