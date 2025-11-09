#25
x = {'alpha':30, 'bravo':40, 'charlie':50, 'delta':60, 'echo':70, 'foxtrot':80, 'golf':90}
del x['alpha']
print(x)

#26
park = {'korean':94, 'english':91, 'mathematics':89, 'science':83}
print(park['english'], park['science'])

#27
kim = {'korean':94, 'english':91, 'mathematics':89, 'science':83}
kim.update({'korean':100, 'english':100, 'mathematics':100, 'science':100})
print(kim)

#28
lee = {'korean':94, 'english':91, 'mathematics':89, 'science':83}
print('english' in lee)
del lee['english']
print(lee)

#29
lim = {'korean':94, 'english':91, 'mathematics':89, 'science':83}
print(lim.items())

#30 90 이상만 출력
choi = {'korean':94, 'english':91, 'mathematics':89, 'science':83}

for i in choi:
    if choi[i] >= 90:
        print(i)

#31 4과목 평균 출력
yoo = {'korean':94, 'english':91, 'mathematics':89, 'science':83}

x = 0
for i in yoo:
    x += yoo[i]
    
y = x / len(yoo)
    print(y)
