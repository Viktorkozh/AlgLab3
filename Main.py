import timeit
import random
import matplotlib.pyplot as plt
import numpy as np

a = {}
worstTime = {}
medianTime = {}
GraphStuff = [i for i in range(10, 20020, 10)]

def find(n):
    for i in range(len(a)):
        if a[i] == n:
            return i
    return -1

def fillArr(numOfEl):
    a.clear()
    for i in range(numOfEl):
        a[i] = random.randint(0, 1000000)

def least_squares(X, Y):
    # Calculate the necessary sums
    n = len(X)
    sum_x = sum(X)
    sum_y = sum(Y)
    sum_x_squared = sum(x ** 2 for x in X)
    sum_xy = sum(x * y for x, y in zip(X, Y))
    
    # Calculate the coefficients (slope and intercept) for the linear equation
    slope = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x ** 2)
    intercept = (sum_y - slope * sum_x) / n
    
    return slope, intercept

for i in range(10, 20020, 10):
    fillArr(i)
    worstTime[i] = (timeit.timeit(lambda:find(10000000), number = 10)) / 10

for i in range(10, 20020, 10):
    fillArr(i)
    medianTime[i] = timeit.timeit(lambda:find(a[int(random.randint(1, i - 1))]), number = 1)

# Convert the dictionary values to lists for regression analysis
graph_stuff_list = list(GraphStuff)
worst_time_list = list(worstTime.values())
median_time_list = list(medianTime.values())

# Perform linear regression
worst_slope, worst_intercept = least_squares(graph_stuff_list, worst_time_list)
median_slope, median_intercept = least_squares(graph_stuff_list, median_time_list)

plt.figure(1)
plt.xlabel('Количество элементов в массиве')
plt.ylabel('Среднее время выполнения (секунды)')
plt.title('Зависимость времени поиска элемента от размера массива\n(Худший случай)')
plt.scatter(GraphStuff, worstTime.values(), s=5)
plt.plot(graph_stuff_list, [worst_slope * x + worst_intercept for x in graph_stuff_list], label="Worst Case Regression", color='red')
plt.grid(False)

plt.figure(2)
plt.xlabel('Количество элементов в массиве')
plt.ylabel('Среднее время выполнения (секунды)')
plt.title('Зависимость времени поиска элемента от размера массива\n(Средний случай)')
plt.scatter(GraphStuff, medianTime.values(), s=5)
plt.grid(False)
plt.plot(graph_stuff_list, [median_slope * x + median_intercept for x in graph_stuff_list], label="Median Case Regression", color='red')

plt.show()