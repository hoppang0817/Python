# 랜덤모듈 먼저 import해줘야함
import random
# 외부에 생성한 내 모듈가져오기
import my_module  # as my <- my_module의 별칭을 정해주는거

# random.randint(시작,마지막)
# 시작과 마지막 값 사이 숫자가 랜덤으로 나옴
random_side = random.randint(0, 1)
print(random_side)

if random_side == 1:
    print("앞면")
else:
    print("뒤면")

# 들고와서 사용가능
print(my_module.pi)
