import math

x = 1
z = 0

for i in range(1,1000):
    z = z + x**x
    x += 1

# print(z)
y = str(z)


print(y[-11: -1])