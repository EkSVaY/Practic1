import math
r_blind = float(input())
signal_r = float(input())
print(abs((math.pi * 2 * signal_r ** 2)/2 - (math.pi * 2 * r_blind ** 2)/2))
