import time
start_time = time.time()
for a in range(1, 1001):
    for b in range(1, 1001):
        if a ** 2 + b ** 2 == (1000 - a - b) ** 2:
            print(a, b, 1000-a-b)
end_time = time.time()

print(end_time-start_time)
