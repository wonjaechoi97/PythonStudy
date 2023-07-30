# print("input()은 한 줄의 문자열을 입력 받는 함수")
# print("map()은 리스트의 모든 원소에 각각 특정한 함수를 적요할 때 사용")
#
#
# result = list(map(str, input().split()))
# print(result)
#
# n = int(input()) # 몇개 데이터 들어오나?
# data = list(map(int, input().split()))
#
# data.sort(reverse=True)
# print(data)
#
# # print(listmap(int, input().split()))
#
# a, b, c = map(int, input().split())
# print(a, b, c)


print("입력이 많을 때는 아래와 같이 사용한다. 표준 라이브러리 sys, rstrip은 엔터 문자 제외시켜준다.")
import sys
print("엔터 포함")

data = sys.stdin.readline().rstrip() # rstrip 오른쪽 공백 제거, lstrip 왼쪽 공백 제거
print(data)

print("print는 기본적으로 줄바꾸지만 end= 조건을 변경해서 변경가능")
a = 1
b = 2
print(a, b)
print(7, end=" ")
print(8, end="어쩌구")

answer = 7
print("정답은 " + str(7)+ "입니다.")

print("fstring")
answer = 7

print(f"정답은 {answer}입니다.")