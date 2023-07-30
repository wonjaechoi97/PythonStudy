# 배열 사용할 때 리스트 사용 자바의 ArrayList

list = []
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)

# 네번째 원소 출력
print(a[3])

n = 10
a = [0]*n
print(a)

a = [4, 5, 1, 12, 5, 89]

print(a)

# 인덱싱
a[4] = 27
print(a)

print(a[-1]) # 마지막 자리
print(a[0]) # 첫자리

# 슬라이싱
b = a[0:5] # 시작 인덱스 : 마지막 인덱스 +1
print(b)

# 리스트 컴프리헨션
print("리스트 컴프리헨션")
array = [i*2 for i in range(10)]
print(array)

print("\n 0 ~ 19중 홀수만")
array = [i for i in range(20) if i % 2 == 1]
print(array)

array = [i*i for i in range(10)]
print(array)

n = 4
m = 3
array = [[0]* m for _ in range(n) ]
print(array)
array[1][1] = 5
print(array)

print("잘 못된 초기화")
array = [[0]*m]*n
print(array)
array[1][1] = 5
print(array)


print("리스트 관련 메서드")
a = [1, 8, 4, 3, 27, 2, 90]
print("기본 리스트 : ", a)

a.append(7)
print("삽입", a)

a.sort()
print("오름차순 정렬:", a)

a.sort(reverse = True)
print("내림차순", a)

a.reverse()
print("원소 뒤집기:", a)

a.insert(2, 65) # 2번 인덱스에 65넣기
print("인덱스 2에 65 추가", a)

print("값이 3인 데이터 개수:", a.count(8))

a.remove(1)
print("값이 1인 데이터 삭제 : ", a)


print("특정 값을 가지는 원소 모두 제거")

a = [1, 2, 3, 4, 5, 6, 10, 27]
remove_set = {3, 27}

result = [i for i in a if i not in remove_set]
print(result)