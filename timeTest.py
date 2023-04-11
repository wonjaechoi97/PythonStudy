import time

print(1)
p = 0

start_time = time.time()
for i in range(100000):
    p = i
    
end_time = time.time()

print("time:", end_time - start_time)