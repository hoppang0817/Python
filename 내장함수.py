# 터미널 클리어 cls명령어
# dir 객체가 자체적으로 가진 변수나 함수를 보여준다
# print(dir(__builtins__))  # 내장함수들을 보여준다

# 문자열관련 내장함수를 보여줌
# print(dir("1"))

# 문자열을 배열에 담아줌
print(list("python"))

# 최대값을 출력해줌(문자열도해줌)
print(max([90, 10, 20, 70, 80]))

# 최소값을 출려해줌(문자열도 해줌)
print(min([90, 10, 20, 70, 80]))

print(list(range(5)))
print(list(range(5, 10)))
# 세번째는 증감값 따라서 0부터 99까지숫자중 짝수출력
print(list(range(0, 100, 2)))
# 반대로 100부터0까지 출력
print(list(range(100, 0, -1)))

# 반올림
print(round(4.4))

# ,다음은 자릿수
s = 3.01456
print(round(s, 2))

# sum()리스트의 모든수 합
print(sum([1, 2, 3]))

# type()입력값의 자료형을 알려줌
