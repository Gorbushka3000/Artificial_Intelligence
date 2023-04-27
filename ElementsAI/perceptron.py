def perceptron(Sensor, weights):
    b = 7
    s = 0
    for i in range(15):
        try:
            x = float(Sensor[i]) or int(Sensor[i])
            s += int(Sensor[i]) * weights[i]
        except ValueError:
            print("ошибка значения")
            return False

    if s >= b:
        return True
    else:
        return False
