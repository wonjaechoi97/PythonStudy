print("프로그램의 흐름을 제어")
x = 15
if x >= 10:
    print("x >= 10")

if x >= 0:
    print("x >= 0")

if x >= 30:
    print("x >= 30")

print("들여쓰기 주의")

score = 85

if score >= 70:
    print("성적이 70점 이상입니다.")
    if score >= 90:
        print('우수한 성적입니다.')

else:
    print('성적이 70 미만입니다.\n'
          '분발하시죠?')

print("프로그램 종료")


a = -20

if a>= 0:
    print("a >= 0")
elif a >= -10:
    print("0 > a >= -10")
else:
    print("a < -10")


score = 50
grade =""

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(grade)

x = False

if not x:
    print("x : False")
else:
    print("x : True")


a = 15

if a <= 20 and a >=10:
    print(" 10 <= a <= 20")

list = [1, 3, 4, 8, 9, 112]

if 112 not in list:
    print("112가 리스트에 없다")
else:
    print("안에 있다")

print("---------------------------------------------")
print("pass 가능")
a=50
if a >= 30:
    pass # 아예 아무것도 없으면 오류
else:
    print("30보다 작음")

print("코드가 한줄인 경우 간단하게 표현 가능")

score = 85

if score >= 80 : result = "Success"
else: result =  "Fail"

print(result)

score = 85

result = "Success" if score >= 80 else "Fail"
print(result)


print("대수학 형태의 부등식 사용가능")
x = 5
if 10 < x < 20:
    print("10 < x < 20")
else:
    print("예외")