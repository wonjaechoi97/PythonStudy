import time

array = [3, 5, 1, 2, 4]
sum = 0
start_time = time.time()
for x in range(100000):
    sum += x
end_time = time.time()
print(sum)
print("이 경우 O(N)임")
print
print("소요 시간 : ", end_time - start_time)
print("----------------------------------------")
start_time = time.time()
for i in range(100000):
    for j in range(100000):
        temp = i*j
        # print(temp)
end_time = time.time()
print("이 경우 O(N^2)임")
print("소요 시간 : ", end_time - start_time)