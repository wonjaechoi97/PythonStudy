print("해시테이블 이용하므로 O(1)의 시간 복잡도를 가짐, 다른 언어에서는 해시 테이블이라고도 함")

data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)

if '사과' in data:
    print("'사과'를 키로 가지는 데이터가 존재합니다.")

key_list = data.keys()

value_list = data.values()

print(key_list)
print("리스트 형태로 출력하기 위해서 ")
print(list(key_list))
print(value_list)

for key in key_list:
    print(data[key])


print("사전은 이렇게도 초기화할 수 있다.")
data ={
'사과' : 'Apple',
'바나나' : 'Banana',
'코코넛' : 'Coconut'
}

print(data)

print("\n\n 집합이다 이제\n"
      "- 중복을 허가하지 않는다\n"
      "- 순서가 없다\n"
      "- 리스트 혹은 문자열을 이용해서 초기화 가능\n"
      "- 데이터의 조회 및 수정에 있어서 O(1)의 시간에 처리할 수 있다."
      )

list = [1, 1, 2,  2, 3, 3, 4, 4, 4, 5, 5, 5]
data = set(list)

print(data)

print("or")
data = {1, 1, 2, 2, 3, 4, 5, 5, 5}
print(data)


print("수학에서의 합집합 교집합 차집합 사용 가능!")

a = {1, 2, 3, 4, 5}
b = set([3, 4, 5, 6, 7, 8])

print(a|b)
print(a & b)
print(a - b)

print("새로운 거 추가")
a.add(9)
print(a)

print("새로운 원소 여러개 추가")
a.update([7, 8])
print(a)

print("특정 값 제거")
a.remove(3)
print(a)

print("\n이렇게 원소 추가 삭제시 상수 시간 소모")