import matplotlib.pyplot as plt
import numpy as np

from func import calculate

g = np.vectorize(lambda z: calculate(z, 0)[5])

x = np.linspace(0, 10)
y = g(x)

plt.plot(x, y)
plt.xlabel("Number of instants and sorceries cast")
plt.ylabel("Amount of life Gained")
plt.savefig("graph.png")
plt.show()