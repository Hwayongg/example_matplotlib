import random
import math

degree=0
i = 0
y1 = []
y2 = []
y3 = []
x = []

while degree < 180:

    x.append(degree)
    degree += 1

    y1.append(math.sin(math.radians(degree))**2)
    y2.append(math.cos(math.radians(degree))**2)
    y3.append(math.sin(math.radians(degree))**2 + math.cos(math.radians(degree))**2)

    i += 1

import matplotlib.pyplot as plt
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)

plt.show()
