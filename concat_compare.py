import time

start = time.time()
result = ""
for i in range(1, 10001):
    result += str(i)
print(result)
print("+=Time:", time.time() - start)




start = time.time()
result = "".join(str(i) for i in range(1, 100001))  
print(result)
print("Join time:", time.time() - start)
