import timeit
import random
import matplotlib.pyplot as plt
import numpy as np


a = {}
worst_time = {}
median_time = {}
graph_stuff = [i for i in range(10, 10010, 10)]


def find(n):
    for i in range(len(a)):
        if a[i] == n:
            return i
    return -1


def fill_arr(numOfEl):
    a.clear()
    for i in range(numOfEl):
        a[i] = random.randint(0, 1000000)


for i in range(10, 10010, 10):
    fill_arr(i)
    worst_time[i] = (timeit.timeit(lambda: find(10000000), number=100)) / 100

for i in range(10, 10010, 10):
    fill_arr(i)
    t = int(random.randint(1, i - 1))
    median_time[i] = timeit.timeit(lambda: find(a[t]), number=100) / 100

A = np.vstack([graph_stuff, np.ones(len(graph_stuff))]).T
y = np.array(list(worst_time.values()))[:, np.newaxis]
alpha = np.dot(
    (np.dot(np.linalg.inv(np.dot(A.T, A)), A.T)), np.array(list(worst_time.values()))
)  

plt.figure(1).set_figwidth(8)
plt.xlabel("Количество элементов в массиве")
plt.ylabel("Среднее время выполнения (секунды)")
plt.title("Зависимость времени поиска элемента от размера массива\n(Худший случай)")
plt.scatter(graph_stuff, worst_time.values(), s=5)
plt.grid(False)
plt.plot(graph_stuff, alpha[0] * np.array(list(graph_stuff)) + alpha[1], "r")

formatted_alpha = [format(a, ".10f") for a in alpha]
print(
    "Коэффициенты прямой худшего случая: a =",
    formatted_alpha[0],
    "b =",
    formatted_alpha[1],
)
print("Worst time correlation", np.corrcoef(graph_stuff, list(worst_time.values()))[0, 1])

A = np.vstack([graph_stuff, np.ones(len(graph_stuff))]).T
y = np.array(list(median_time.values()))[:, np.newaxis]
alpha = np.dot(
    (np.dot(np.linalg.inv(np.dot(A.T, A)), A.T)), np.array(list(median_time.values()))
)

plt.figure(2).set_figwidth(8)
plt.xlabel("Количество элементов в массиве")
plt.ylabel("Среднее время выполнения (секунды)")
plt.title("Зависимость времени поиска элемента от размера массива\n(Средний случай)")
plt.scatter(graph_stuff, median_time.values(), s=5)
plt.grid(False)
plt.plot(graph_stuff, alpha[0] * np.array(list(graph_stuff)) + alpha[1], "r")

formatted_alpha = [format(a, ".10f") for a in alpha]
print(
    "Коэффициенты прямой среднего случая: a =",
    formatted_alpha[0],
    "b =",
    formatted_alpha[1],
)
print(
    "Median time correlation", 
    np.corrcoef(graph_stuff, list(median_time.values()))[0, 1]
)

plt.show()
