#39
x = int(input('양수를 입력하세요. : '))
def odd():
    for i in range(1, x+1):
        if i % 2 != 0:
            print(i, end=' ')

odd()

#40
x = int(input('랜덤한 숫자를 입력하세요. : '))
def random():
    if x % 3 == 0:
        print(x)

random()

#41
x = list(map(int, input('숫자를 4개 입력하세요. : ').split(',')))
def cal():
  print('최댓값: ',max(x))
  print('최솟값: ',min(x))

cal()

#42
x = int(input('양수를 입력하세요.: '))
def odd():
    for i in range(1, x+1):
        if i % 2 != 0:
            print(i, end=' ')

#43
x = int(input('0이상의 정수를 입력하세요.: '))
def n():
    result = 1
    for i in range(1, x+1):
        result *= i
    return result
    print(result)

n()

#44
i,j = list(map(int, input('2 이상 9 이하의 정수를 2개 입력하세요. : ').split(',')))
def if_total(i, j):
    result = 0
    for x in range (1, i+1):
        for y in range (1, j+1):
            if x * y >= 30:
              result = x * y
    return result
    print(result)

if_total(i, j)


