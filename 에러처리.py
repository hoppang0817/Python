# def div10(num):
#     return 10/num

# 에러 원인을 알때
# def div10(num):
#     try:
#         return 10/num
#     except ZeroDivisionError:
#         print("에러: 0으로 나눌수없습니다")

# 에러원인을 모를때
def div10(num):
    try:
        return 10/num
    except:
        print("에러")


print(div10(2))  # 정상적으로 리턴
print(div10(0))  # 에러 발생
print(div10(5))
