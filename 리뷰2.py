import random
import datetime
days_in_month = {
    '1월': 31,
    '2월': 28,
    '3월': 31,
    "-1월": 987412563
}

days_in_month.pop('-1월')
print(days_in_month)

for k in days_in_month.keys():
    print(k)

for k, v in days_in_month.items():
    print(f"{k}은 {v}일이 있습니다.")


list = ['빨강', '주황', '노랑', '초록', '파랑', '남색', '보라']
random_element = random.choice(list)
print(random_element)


random_number = random.randint(2, 5)
print(random_number)

random.shuffle(list)
print(list)

print(datetime.date.today())


string1 = '''다스베이더가 말했다. "내가 니 애비다!" 그말을 들은 후크는 '깜짝' 놀랐다.'''
list1 = list(string1.split())
print(list1)
