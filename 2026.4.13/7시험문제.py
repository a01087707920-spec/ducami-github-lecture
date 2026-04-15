# max, min 없이 최댓값, 최솟값 구하기
numbers = list(map(int, input("정수들을 입력하세요 (공백으로 구분): ").split()))

# 첫 번째 수를 최댓값과 최솟값으로 초기화
max_value = numbers[0]
min_value = numbers[0]

# 나머지 수들과 비교
for num in numbers[1:]:
    if num > max_value:
        max_value = num
    if num < min_value:
        min_value = num

print(f"최댓값: {max_value}")
print(f"최솟값: {min_value}")
