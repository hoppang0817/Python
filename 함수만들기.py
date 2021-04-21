# 함수 만들기
def hello():
    print('하이')
    print('안녕')
    print('니하오')


# 만든 함수 불러오기
hello()
hello()


def hello2(name):
    print("하이"+name)


hello2("길동")


def add10(n):
    return n+10


print(add10(1))
print(add10(2))


def is_odd(n):
    if n % 2 == 0:
        return "짝수"
    else:
        return "홀수"


print(is_odd(1))
print(is_odd(2))

# 매개변수 앞에 *이있으면 여러개의 매개변수를 의미함


def avgNums(*n):
    return sum(n)/len(n)


print(avgNums(1, 2, 3))
