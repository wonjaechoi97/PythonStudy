# 양의 정수
a = 1000
print(a)

a = a+5
print(a)

a = -7
print(a)

a = 0
print(a)

# 양의 실수
a = 157.93
print(a)

# 음의 실수
a = -1837.2
print(a)

# 소수부가 0일 때 0을 생략
a = 5.
print(a)

# 정수부가 0일 때 0을 생략
a = -.7
print(a)

# 1,000,000,000의 지수 표현 방식
a = 1e9
a = int(a) # 실수 -> 정수
print(a)

# 752.5
a = 75.25e1
print(a)

# 3.954
a= 3954e-3
print(a)

# 실수형을 저장하기 우해 4바이트 혹은 8바이트의 고정된 크기의 메모리 할당하므로,
# 컴퓨터 시스템은 실수 정보를 표현한느 정확도에 한계를 가짐
# 예를 들어 10진수 체계에서는 0.3과 0.6을 더한 ㄱ밧ㅇ ㅣㅇ0.9로 정확히 떨어지나
# 2진수에서는 0.9를 정확히 표현 불가, 그래서 0.9와 최대한 가깝게 표현하지만 오차 발생

a = 0.3 + 0.6
print(a)

if a == 0.9:
    print(True)
else:
    print(False)

# 개선
a = 0.3 + 0.6
print(round(a, 4))
if round(a, 4) == 0.9:
    print(True)
else:
    print(False)

print("사칙연산************************************************")
a = 7
b = 3

#나누기
print(a/b)

# 나머지
print(a%b)

# 몫
print(a//b)


a = 5
b = 3
# 거듭 제곱
print(a ** 5)

# 제곱근
print(a ** 0.5)