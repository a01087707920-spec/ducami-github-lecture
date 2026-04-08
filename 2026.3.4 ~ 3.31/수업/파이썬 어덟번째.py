import random

pikachu = 100
mon = 80

print("앗! 야생의 몬스터가 나타났다!\n나와라 피카츄!\n피카츄 : 삐까!\n\n피카츄!! \n1. 십만볼트! \n2. 백만볼트! \n3. 천만볼트! \n4. 치유의 물약")

while True:

    while pikachu > 0 and mon > 0:

        skill = int(input("지우 : 빨리 스킬을 써서 몬스터를 상대해야겠어! >>> "))

        if skill == 1:
            mon -= 10
            print(f"\n지우 : 좋았어 피카츄! 몬스터의 남은 HP는 {mon}이야!!")

        elif skill == 2:
            mon -= 20
            print(f"\n지우 : 좋았어 피카츄! 몬스터의 남은 HP는 {mon}이야!!")

        elif skill == 3:
            mon -= 30
            print(f"\n지우 : 좋았어 피카츄! 몬스터의 남은 HP는 {mon}이야!!!")

        elif skill == 4:
            pikachu += 10
            print(f"\n지우 : 힘내, 피카츄! (피카츄의 남은 HP는 {pikachu}이야!)")

        else:
            print("\n포켓몬 박사 : 그 기술은 아직 배우지 못했다네~")
            continue

        if mon <= 0:
            mon = 0
            print(f"몬스터 HP: {mon}")
            print("지우 : 좋았어 피카츄! 몬스터, 넌 내꺼야!!")
            break

        mons_attack = random.randint(5, 50)
        pikachu -= mons_attack
        print(f"몬스터의 공격! {mons_attack} 데미지\n피카츄 HP: {pikachu}\n")

        if pikachu <= 0:
            pikachu = 0
            print(f"피카츄 HP: {pikachu}")
            print("지우 : 피카츄..!!")
            break

    # 병원, 다시 시작
    if pikachu <= 0:
        print("\n포켓몬 센터 도착!")

        choice = input("피카츄를 치료하고 다시 시작하시겠습니까? (yes/no) >>> ")

        if choice == 'yes':
            pikachu = 100
            mon = 80
            print("\n피카츄가 완전히 회복되었습니다! 다시 출발!\n")
            continue
        else:
            print("오늘 여행은 여기서 그만해야겠어. 다음에 또 만나자!")
            break

    else:
        print("승리했습니다!")
        break