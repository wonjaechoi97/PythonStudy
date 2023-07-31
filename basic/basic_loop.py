print("for문 써야 빠르니깐 for 쓰자")

i = 1
result = 0

while i <= 9:
    result += i
    i += 1

print(result)

print("1 ~ 9 홀수만 더하기")

i = 1
result = 0

while i <= 9:
    if i % 2 == 1:
        result += i
    i += 1

print(result)

print("for 등장")

array = [9, 8, 7, 6, 5]

for x in array:
    print(x, end=" ")
print()
for i in range(1, 10):  # 1~9
    print(i, end=" ")

print("continue 등장")

result = 0

for i in range(1, 10):
    if i % 2 == 0:
        continue
    result += i

print(result)

print("------------------ break 등장 ------------")

i = 1

while True:
    print("현재의 값 : ", i)
    if i == 10:
        break

    i += 1

print("------------------ 합격 여부 판단 ------------")

scores = [98, 85, 27, 95, 64, 72, 56, 42]
cheating_student_list = {2, 4}

for i in range(len(scores)):
    if i + 1 in cheating_student_list:
        continue
    if scores[i] >= 80:
        print(f"{i + 1}번 학생은 합격입니다.")


print("------------------ 중첩된 반복문 ------------")

for i in range(2,10):
    for j in range(1, 10):
        print(i, " X ", j," = ", i*j)
    print()