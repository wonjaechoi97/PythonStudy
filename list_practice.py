a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)

print(a[3])

n = 10
a = [0] * n
print(a)

# 인덱스 값 입력하여 리스트 특정한 원소에 접근하는 것을 인덱싱
# 양의 정수 음의 정수 모두 사용
# 음의 정수 넣으면 뒤에서부터
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a[7])

print(a[-1])

print(a[-3])

a[3] = 7
print(a)

# 슬라이싱 : 연속적인 위치를 갖는 원소들을 가져와야할 때 사용
# 대괄호 안 ":" 사용해서 시작 인덱스 끝 인덱스 설정 가능 "끝 인덱스는 실제 인덱스보다 +1"

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a[3])

print(a[1:4]) # 인덱스 1 2 3

#리스트 컴프리헨션
print("리스트 컴피리헨션")

array = [i for i in range(10)]# 0 ~ 9

print(array)

a2 = [ i*10 for i in range(50)]
print(a2)

array = [i for i in range(20) if i % 2 ==1]
print(array)

array = [i*i for i in range(1, 10)]
print(array)


# 격자 만들때 사용할 것
n = 4
m = 3

array = [[0] * m for _ in range(n)]
print(array)

array[1][1] = 5
print(array)

array = [[0] * m] * n
print(array)

# 반복을 위한 변수의 값을 무시하고자 할 때 _ 언더바 사용


array[1][1]=5
print(array)

sum = 0
for i in range(1, 11):
    sum = sum + i

print(sum)

for _ in range(10):
    print("hello")

# 리스트 관련 기타 메서드
print("리스트 관련 기타 메서드 ***********************************")
a = [1, 4, 3]
print("기본 리스트" , a)

# 리스트에 원소 삽입
a.append(2)
print("삽입: ", a)

# 오름차순 정렬
a.sort()
print("오름차순 정렬: ", a)

#내림차순 정렬
a.sort(reverse=True)
print("내림차순 정렬: ",a)

# 리스트 원소 뒤집기
a.reverse()
print("원소 뒤집기 : ", a)

# 특정 인덱스에 데이터 추가
a.insert(2, 3)
print("인덱스 2에 3추가", a)

# 특정 값인 데이터 개수 세기
print("값이 3인 데이터 개수: ", a.count(3))

# 특정 값 데이터 삭제
a.remove(1)
print("값이 1인 데이터 삭제 : ", a)

# 특정 값을 가지는 원소 모두 제거하기
a = [1, 2, 3, 4, 5, 5, 5, 5]
remove_set = {3, 5}# 집합 자료형 추후 다시 학습
result = [i for i in a if i not in remove_set]
print(result)