# 리스트 메소드는 리스트.함수(매개변수)
# [].index('값'):값에 해당하는 인덱스 번호를 리턴한다.없는 경우 에러
a = ['개', '고양이', '박쥐', '곰']
print(a.index("고양이"))
# print(a.index('소'))


# append() 리스트의 끝에 추가해준다
a.append("소")
print(a)

# pop() 리스트 끝에 아이테 제거하면서 리턴
a.pop()
print(a)

# insert(a,b) 특정 위치(a)에 아이템(b) 입력
a.insert(1, '염소')
print(a)


# remove() 리스트에 특정 요소를 삭제
# 값이 여러개라면 그중 가장 앞에있는 하나만 지워진다
a.remove('염소')
print(a)

# sort() 정렬 숫자를 순서대로 정렬한다
b = [5, 9, 7, 3]
b.sort()
print(b)
b.sort(reverse=True)  # 역순으로 정렬해줌
print(b)

# 기본 매개변수 print(end='\n')
for i in range(101):
    # print(i)  # 기본적으로 한줄을 띄우며서 출력해줌
    print(i, end=" ")  # end 에 공백으로 넣어주면 줄을 띄우지 않고 공백을 넣어 출력해줌
