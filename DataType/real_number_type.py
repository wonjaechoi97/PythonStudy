r = .7

print(r)

a = 123.12
print(a)


a = -214.75
print(a)

# 굳이?
a = 5.
print(a)

a = -.7
print(a)

a = 1e9
print(a)

a = 3594e-3
print(a)

# 정수형으로 활용하고자 할 때
a = int(1e9)
print(a)

a = 10/3

print(a)

a = 0.3 + 0.6
if a == 0.9:
    print(True)
else:
    print(False)
print(a)

#실수는 정확히 저장하지 못해서 오차 발생 그래서  round 함수로 반올림하여 사용
a = 123.456
print(round(a, 2)) # 세째 자리에서 반올림123.46

a = 0.3+0.6
if round(a,2) == 0.9:
    print(True)
else:
    print(False)


a = 7
b = 3

print(a / b)

print(a % b)

print(a // b)


