import numpy as np

def calculate(z, s):
    c = z ** 2 + z * (2 * s + 1) + (s **2 + s - 1)

    x = (1/3) * (np.sqrt(4 + 3 * c) - 2)
    x_round = np.round(x)

    y = z - x
    y_round = z - x_round

    def f(x, y):
        return x**2/2 + x/2 + y*s*x + y*x**2 + s*x**2 + y**2*x/2 + s**2*x/2 + 5*y*x/2 + 5*s*x/2 + y**2 + s**2 + 2*y*s + y + s

    l = f(x, y)
    l_round = f(x_round, y_round)

    return x, y, l, x_round, y_round, l_round

def output(z, s, x, y, l, x_round, y_round, l_round):

    template = "{:8.8} {:10.10} {}"

    print("{:8.8} {:10.10} {}".format("Name", "Value", "Rounded Value"))
    print(template.format("z", str(z), int(z)))
    print(template.format("s", str(s), int(s)))
    print(template.format("x", str(x), int(x_round)))
    print(template.format("y", str(y), int(y_round)))
    print(template.format("l", str(l), int(l_round)))