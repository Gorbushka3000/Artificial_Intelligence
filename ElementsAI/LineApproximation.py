import random

k = random.uniform(-5, 5)
c = random.uniform(-5, 5)
rate = 0.0001
print('Начальная прямая: Y = ', k, '*X+', c)
data = {
    22: 150,
    23: 155,
    24: 160,
    25: 162,
    26: 171,
    27: 174,
    28: 180,
    29: 183,
    30: 189,
    31: 192
}


def proceed(x):
    return x * k + c


for i in range(100000):
    x = random.choice(list(data.keys()))
    true_result = data[x]
    out = proceed(x)
    delta = true_result - out
    k += delta * rate * x
    c += delta * rate

print('Готовая прямая: Y = ', k, '* X +', c)
