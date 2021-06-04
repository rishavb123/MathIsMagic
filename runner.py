from func import calculate, output
import sys

if len(sys.argv) > 1:
    z = float(sys.argv[1])
    s = float(sys.argv[2]) if len(sys.argv) > 2 else 0
else:
    z = float(input("How many instants and sorceries will you cast? "))
    s = float(input("How many other spells will you cast? "))

x, y, l, x_round, y_round, l_round = calculate(z, s)

output(z, s, x, y, l, x_round, y_round, l_round)