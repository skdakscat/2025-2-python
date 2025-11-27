#32
num1 = {1,3,5,7,9}
num2 = {1,2,3,4,5}

x = set.union(num1, num2)
y = set.intersection(num1, num2)
print(x, y)

#33
num1 = {1,3,5,7,9}
num2 = {1,2,3,4,5}

x = num1 - num2
y = num1 ^ num2
print(x, y)

#34
x = {1,3,5,7,9}
x.add(100)

print(x)

#35
a = {100,200,300,400,500}
print(a)
a.intersection_update({400,500,600,700,800})
print(a)
a.difference_update({400,500,600,700,800})
print(a)
a.symmetric_difference_update({400,500,600,700,800})
print(a)

#36
a = {100,200,300,400,500}
x = a.issuperset({100,200,300,400,500})
y = a.issubset({100,200,300,400,500})

if x and y:
    print('동시')
elif x:
    print('상위')
elif y:
    print('부분')

#37
x = {1,3,5,7,9}
x.add(1000)
x.remove(9)

print(x)

#38
multiples = {x for x in range(100) if x%3==0 and x%5==0}
print(multiples)
