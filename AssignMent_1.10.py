a = 799
b = 0

if a >= 500:
    c = int(a / 500)
    print('500: ', c)
    b += c
    a = a % 500
if a >= 100:
    c = int(a / 100)
    print('100: ', c)
    b += c
    a = a % 100
if a >= 50:
    c = int(a / 50)
    print('50: ', c)
    b += c
    a = a % 50
if a >= 20:
    c = int(a / 20)
    print('20: ', c)
    b += c
    a = a % 20
if a >= 10:
    c = int(a / 10)
    print('10: ', c)
    b += c
    a = a % 10
if a >= 5:
    c = int(a / 5)
    print('5: ', c)
    b += c
    a = a % 5
if a >= 2:
    c = int(a / 2)
    print('2: ', c)
    b += c
    a = a % 2
if a >= 1:
    c = int(a / 1)
    print('1: ', c)
    b += c
    a = a % 1
    
print('Total Note Count:',b)