
A = set(map(int, input("A 집합 >>> ").split()))
B = set(map(int, input("B 집합 >>> ").split()))


union = A | B #합집합 : A와 B의 모든 요소를 합침 중복은 자동 제거

intersection = A & B #교집합 : 두 집합에 공통으로 있는 값만

difference = A - B # 차집합 (A - B) : A에는 있고 B에는 없는 값

print("합집합:", union)
print("교집합:", intersection)
print("차집합(A-B):", difference)
