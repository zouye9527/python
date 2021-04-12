import math
h = 500
g = 9.8
t = math.sqrt(2 * h / g)
hx = g * (t - 1) * (t - 1) / 2
hh = h - hx
print("小球最后1秒下落的位移是：", hh, "米")
