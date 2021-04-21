def add(a, b):
    result = a+b

    print(f"{a} + {b} = {result}")


add(10, 5)


def add(a, b):
    return a+b


print(add(10, 5))

rainbow = ['빨강', '주황', '노랑', '초록', '파랑', '남색', '보라']
first_color = rainbow[0]
last_color = rainbow[-1]
print(f"무지개의 첫번째 색은 {first_color}이다.")
print(f"무지개의 마지막 색은 {last_color}이다.")


list1 = [1, 2, 3]
list1.append(4)
print(list1)

list = [1, 2, 3]
list = list+[4]
print(list)

numbers = [1, 2, 3, 4, 5]
n = 5
if n in numbers:
    print(f"{n}가 리스트에 있다")

list2 = [1, 2, 3]
list2.remove(2)
print(list2)


days_in_month = {
    '1월': 31,
    '2월': 28,
    '3월': 31
}
days_in_month['2월'] = 29

print(days_in_month)


dict1 = {}
dict1['이름'] = '홍길동'
dict1['번호'] = 1010
dict1['취미'] = ['낮잠', '숨시기', '커피']
print(dict1)
