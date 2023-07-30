data = 'Hello World'
print(data)

data = "Don't you know \"Python\"?"
print(data)

a = "Hello"
b = "World"

print(a + " "+ b)

a= "String"
print(a * 3)

a = "ABCDEF"
print(a[2:4]) #인덱싱 통해 문자 바꾸는 것은 불갚

#튜플

a =  (1, 2, 3, 4, 5, 6, 7, 8, 9 ) # 원소 변경 불가
print(a)

print(a[1:3])

#dictionary 사전 자료형
# 키와 값을 쌍으로 데이터로 가지는 자료형 변경 불가능한 자료형을 키로 사용 가능 파이썬 자료형은
# 해시 테이블을 이용하므로 데이터의 조회 및 수정에서 O(1)의 시간에 처리할 수 있다.

data = dict()

data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'
print(data)

if '사과' in data:
    print("'사과'를 키로 가지는 데이터가 존재합니다.")

if 'Apple' in data.values():
    print("'Apple'을 값으로 가지는 데이터가 존재합니다.")

print(data.keys())
print(data.values())

for key in data.keys():
    print(data[key])

data = {
    '사과': 'Apple',
    '바나나': 'Banana',
    '코코넛': 'Coconut'
}

print(data)

key_list = list(data.keys())
print(key_list)

# 집합
# - 중복을 허용하지 않는다
# - 순서가 없다
# 집합은 리스트 혹은 문자열을 이용해서 초기화할 수 있다
#  - 이때 set() 이용
# - 혹은 중괄호 안에 각 원소를 콤마(,) 기준으로 구분하여 삽입함으로써 초기화할 수 있다.
# - 데이터의 조회 및 수정에 있어서 O(1)의 시간에 처리할 수 있다.



# 집합 자료형 초기화 방법1
data = set([1, 1, 2, 3, 4, 4, 5])
print(data)

# 집합 자료형 초기화 방법 2
data = {1, 1, 2, 3, 4, 4, 5}
print(data)

#기본 집합 연산 제공

a = {1, 2, 3, 4, 5}
b = set([3, 4, 5, 6, 7])

# 합집합
print(a | b)

# 교집합
print( a & b)

# 차집합
print(a - b)

# 집합 관련  함수

data = set([1, 2, 3])
print(data)

# 새로운 원소 추가
data.add(4)
print(data)

# 새로운 원소 여러 개 추가
data.update([5, 6])
print(data)

#특정한 값을 갖는 원소 삭제
data.remove(3)
print(data)
