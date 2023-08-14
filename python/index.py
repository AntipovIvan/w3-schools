import numpy
from scipy import stats

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]


# Среднее арифметическое
mean = numpy.mean(speed)
print(mean)


# В центре списка
median = numpy.median(speed)
print(median)


# Повторы
mode = stats.mode(speed)
print(mode)


# Отклонение
deviation = numpy.std(speed)
print(deviation)


# Процент
percentile = numpy.percentile(speed, 13)
print(percentile)


# 250 случайных чисел от 0.0 до 5.0
bigdata = numpy.random.uniform(0.0, 5.0, 250)
print(bigdata)


import matplotlib.pyplot as plt

# hysto = numpy.random.uniform(0.0, 5.0, 100000)
# plt.hist(hysto, 100)
# plt.show()


# normal = numpy.random.normal(5.0, 1.0, 100000)
# plt.hist(normal, 100)
# plt.show()


carAge = numpy.random.normal(5.0, 1.0, 100000)
carSpeed = numpy.random.normal(10.0, 2.0, 100000)

plt.scatter(carAge, carSpeed)
plt.show()
