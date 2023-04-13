def perceptron(Sensor):
    weights = [1 for i in range(15)]
    b = 7
    s = 0
    for i in range(15):
        if (Sensor[i]).isdigit() == True:
            s += int(Sensor[i]) * weights[i]
        else:
            print("ошибка значения")
            return False

    if s >= b:
        return True
    else:
        return False
