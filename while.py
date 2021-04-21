count = 0
while count < 3:
    print(f'횟수 : {count}')
    count = count+1

print('종료')

name = ''
while name != '펭수':
    name = input('펭수를 입력하시오 :')  # 펭수가 입력될때까지 무한반복함
print('Thank you!')

hit = 0
while hit < 10:
    hit = hit+1
    print(f'나무를 {hit}번 찍었습니다')
    if hit == 10:
        print('나무 넘어갑니다')


# continue  break
count = 0
while count < 10:
    count += 1
    print(count)
    if count < 4:
        continue
    if count == 8:
        break
