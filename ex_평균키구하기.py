import random

student_heights = input("학생들의 키를 입력하세요\n").split()

# range(0, len(student_heights)) 마지막은 포함하지 않고 그앞 숫자까지
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

# len을 사용하지 않고 for문으로 학생수 구하는법
# number_of_strudent =0
# for strudent in student_heights:
#   number_of_strudent+=1

print(f"학생 수 = {len(student_heights)}")

total_height = 0
# student_heights배열안에 있는 숫자들을 height로 하나하나 꺼내서 넣어줌
for height in student_heights:
    total_height += height
print(f"전체 키의 합 = {total_height}")

a = total_height/len(student_heights)
print(f'평균 키 = {a}')


# 높은점수 구하기
student_scores = input("학생들의 성적을 입력 : \n").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

print(student_scores)

highest_score = 0
for scores in student_scores:
    if scores > highest_score:
        highest_score = scores

print(f"가장 높은 점수는 : {highest_score}")


# 비밀번호 생성기
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("파이썬 비밀번호 생성기!")
nb_letters = int(input("몇개의 영문자? "))
nb_symbols = int(input("몇개의 특수문자? "))
nb_numbers = int(input("몇개의 숫자? "))


# 패스워드를 저장할 리스트를 생성
password_list = []

# 영문자 개수만큼 반복문
# random.choice 를사용하면 아무 원소나 하나를 출력해줌
# 반복만하기 위한 for문이기때문에
#  range(1, nb_letters + 1)입력하게 되면 1~입력숫자 +1 만큼 반복함(ex) 입력값 =3 이면 1~3까지 총 3번 반복)
# range(0, nb_letters)로 사용해도됨 (ex) 입력값 =3 이면 0~2까지 총 3번 반복)
for i in range(1, nb_letters + 1):
    password_list.append(random.choice(letters))
    # 비밀번호 리스트에 문자열리스트에서 랜덤으로 하나 추가

for i in range(1, nb_numbers + 1):
    password_list.append(random.choice(numbers))


for i in range(1, nb_symbols + 1):
    password_list.append(random.choice(symbols))

print(password_list)
# 셔플하면 리스트의 순서를 랜덤으로 재설정
random.shuffle(password_list)
# print(password_list)

password = ""
for char in password_list:
    password += char

print(f"생성된 패스워드 : {password}")
