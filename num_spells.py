from root_finding import bisection_method
from func import calculate
import sys

if len(sys.argv):
    total_life = int(sys.argv[1])
else:
    total_life = int(input("How much life do you want to gain"))

g = lambda z: calculate(z, 0)[5] - total_life

spells = bisection_method(g, 0, 10)

print(f"{str(spells):<.10} instant/sorcery spells are required to gain {total_life}")