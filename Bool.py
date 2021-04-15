# bool 타입 (True , False)
my_bool = (True)
print(my_bool)

# 비교연산지
print(2 > 1)
print(2 < 1)

x = 1
y = 2
print(x < y)
print(x > y)
print(x == y)
print(x != y)

print('\n')
print(bool(True))
print(bool(False))
print(bool(1))
print(bool(0))
print(bool('True'))
print(bool('안녕'))

# 논리 연산자 and or not
print("\n")
print(True and True)  # 둘다 참이여야 참
print(True and False)
print(True or False)  # 둘중 하나라도 참이면 참
print(False or False)
print(True or True)

print(not False)
print(not True)


print("\n")
x, y, z = 1, 2, 3
print(z > x and y > z)
print(z > x or y > z)
print(not z > x)
