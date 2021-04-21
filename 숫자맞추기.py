import random
import art

print(art.logo)
print('당신의 이름은 ?')
name = input()

print(f'안녕하세요 {name}님 1에서 20까지 숫자 중하나를 생각합니다.')
secretNumber = random.randint(1, 20)  # 1에서 20까지 숫자중 하나 램덤으로 생성
# print(secretNumber)

for count in range(1, 7):  # 기회는 6번제공
    guess = int(input("맞춰보세요\n"))
    if(guess < secretNumber):
        print('그 숫자보다 큰수')
    elif(guess > secretNumber):
        print('그 숫자보다 작은수')
    else:
        break

if guess == secretNumber:
    print(f'잘 맞췄어요 {name}님 {count} 번만에 맞췄어요 !')
else:
    print(f'틀렸네요. 정답은 {secretNumber} 입니다.')
