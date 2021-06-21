import matplotlib.pyplot as plt
import random

x = [i for i in range(10)]

y = [2**i for i in x]
y2 = [20*i for i in x]
y3 = [random.randint(0, 1024) for i in x]

plt.plot(x, y, label="2^x")
plt.plot(x, y2, label="20*x")
plt.plot(x, y3, label="randint(0, 1024)")
plt.xlabel("x axis")
plt.ylabel("y axis")

plt.title("Zwei interessante Graphen")
plt.legend()
plt.show()