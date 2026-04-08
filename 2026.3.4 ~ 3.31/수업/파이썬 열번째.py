#주사위 경우의 수 
# for i in range(1,7):
#     for j in range(1,7):
#         print(f'({i}, {j})',end=" ")
#     print()


#타자 스피드 게임
#w에 있는 모든 단어가 다 나온 뒤 종료
#문제를 1개 씩 내서 맞출떄 맞다 문제가 넘어가는 형식
#실행예시
# [문제 1] 
# 출력 : wolf
# 입력 : wolf
#출력 : pass

import random, time

w = ['cat', 'dog', 'rabbit', 'fox', 'turtle', 'hamster', 'parrot', 'fish', 'frog', 'snake']
n = 0
start = time.time()
while w:
    for i in range(1, 7):
        print(f'[문제 {0 + i}]')
        q = random.choice(w)
        print(f'{q}')
        x = input()
        n += 1
        if x == q:
            w.remove(q)
            print('pass')
            break
end = time.time()
print(f'걸린 시간: {end - start:.2f}초, 맞은 횟수: {n}회')
