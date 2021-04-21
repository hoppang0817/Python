# key : value 쌍으로 저장 {}를 사용함
d0 = {}
d0[1] = "a"
d0["b"] = 2
d0["c"] = "d"
print(d0)

# 인덱스번호가 아닌 키값으로 찾아야함
myCat = {'사이즈': '소형', '색': '연한갈색', '특기': '잠자기'}
myCat2 = {'특기': '잠자기', '사이즈': '소형', '색': '연한갈색'}
print(f"내 고양이 색깔은 {myCat['색']} 이다.")

# 딕셔너리 타입은 순서가 없다
print([1, 2, 3] == [3, 2, 1])  # 리스트는 순서가 틀리면 다른 리스트이다
print(myCat == myCat2)


# 키 값이 있는지없는지 확인(in,not in)
if'색' in myCat:
    print(myCat['색'])

# key 값 value값, 둘다 출력
print(list(myCat.keys()))  # key값만 출력
print(list(myCat.values()))  # value값만 출력
print(list(myCat.items()))  # 둘다 출력

# for반복문으 딕셔너리에 사용
for k in myCat.keys():
    print(k)
for v in myCat.values():
    print(v)
for k, v in myCat.items():
    print(k, v)


# get(키)메소드
print(myCat.get('이름'))  # 키 값이 없는 경우 none값으로 출력됨
print(myCat.get('색'))
