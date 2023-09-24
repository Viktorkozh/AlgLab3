import timeit
import random
import matplotlib.pyplot as plt

a = {}
med = 0
worstTime = {}
medianTime = {}
GraphStuff = [0]
j = 0

def find(n):
    for i in range(len(a)):
        if a[i] == n:
            return i
    return -1

def fillArr(numOfEl):
    for i in range(numOfEl):
        a[i] = random.randint(0, 1000000)

for i in range(10, 10020, 10):
    GraphStuff.append(i)
    fillArr(i)
    worstTime[j] = (timeit.timeit(lambda:find(10000000), number = 10)) / 10
    j += 1

j = 0
for i in range(10, 10020, 10):
    fillArr(i)
    medianTime[j] = timeit.timeit(lambda:find(a[int(random.randint(1, i - 1))]), number = 1)
    j += 1

plt.plot(GraphStuff, worstTime.values(), linestyle='-')
plt.plot(GraphStuff, medianTime.values(), linestyle='-')
plt.xlabel('Номер числа фибоначчи')
plt.ylabel('Среднее время выполнения (секунды)')
plt.title('Зависимость времени выполнения от номера числа')
plt.xticks(GraphStuff)
plt.grid(False)
plt.show()