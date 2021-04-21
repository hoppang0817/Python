import random

# names_String = input('내기를 할 친구들의 이름을 적습니다.콤마(,)로 분리해서 적습니다\n')
# names = names_String.split(',')  # ,기준으로 입력된 이름을 리스트에 저장해줌
# # split()안에 아무것도 적지안는다면 기본으로 띄어쓰기를 해서 구분한다

# print(names)
# print(len(names))

# a = len(names)
# b = random.randint(0, a-1)
# print(f'당첨자는 {names[b]}')


바위 = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

보 = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

가위 = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [가위, 바위, 보]  # 큰수가 작은수에게 이긴다는 루틴성립 단, 가위,보 일 경우는 따로 결정해줘야함

user_choice = int(input("가위는 0 바위는 1 보는 2 를 적어 주세요.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("컴퓨터 선택:")
print(game_images[computer_choice])


if user_choice >= 3 or user_choice < 0:
    print("잘못된 번호를 선택했어요 0 , 1, 2 중 선택하세요")
elif user_choice == 0 and computer_choice == 2:
    print('you win')
elif user_choice == 2 and computer_choice == 0:
    print('you lose')
elif user_choice == computer_choice:
    print('It\'s a draw')
elif user_choice < computer_choice:
    print('you lose')
elif user_choice > computer_choice:
    print('you win')
