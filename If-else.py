if True:
    print('if문 실행1')
    print('if문 실행2')
    print('if문 실행3')

print('if문아님')

name = 'Alice'
if name == 'Alice':
    print('Hi,Alice')
print('종료')


print('\n')

# if else

# name = '밥'
# if name == '앨리스':
#     print('당신이 앨리스군요')
# else:
#     print('누구인가')

# if elif else
name = '밥'
if name == '앨리스':
    print('당신이 앨리스군요')
elif name == '밥':
    print('당신이 밥이군요')
elif name == '펭수':
    print('당신이 펭수이군요')
else:
    print('누구인가')


number = int(input('숫자를 입력 : \n'))
if number % 2 == 0:
    print("짝수 입니다")
else:
    print("홀수 입니다")


height = int(input('키를 cm로 입력해 주세요 : \n'))

if height > 120:
    print('청룡열차를 탈수 있습니다')
    age = int(input('나이를 입력해 주세요 : \n'))
    if age < 12:
        print('요금은 5000원 입니다')
    elif age >= 12 and age <= 18:
        print('요금은 7000원 입니다')
    else:
        print('요금은 12000원 입니다')
else:
    print('죄송하지만 탈수 없습니다')
