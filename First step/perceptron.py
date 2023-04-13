def perceptron(Sensor):
    weights = [1 for i in range(15)]
    b=7
    s=0
    for i in range(15):
        s += int(Sensor[i]) * weights[i]

    if s >= b:
        return True
    else:
        return False

num1 = list('001001001001001')
num2 = list('111001111100111')


print(perceptron(num1))
print(perceptron(num2))