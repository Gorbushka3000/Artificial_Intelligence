import random
from perceptron import perceptron

number0 = list('111101101101111')
number1 = list('001001001001001')
number2 = list('111001111100111')
number3 = list('111001111001111')
number4 = list('101101111001001')
number5 = list('111100111001111')
number6 = list('111100111101111')
number7 = list('111001001001001')
number8 = list('111101111101111')
number9 = list('111101111001111')

nums = [number0, number1, number2, number3, number4, number5, number6, number7, number8, number9]

tema = 5
n_sensor = 15
weights = [0 for i in range(n_sensor)]
quantityLes = 100



class Teaching:
    def decrease(self, number):
        for i in range(n_sensor):
            if int(number[i]) == 1:
                weights[i] -= 1

    def increase(self, number):
        for i in range(n_sensor):
            if int(number[i]) == 1:
                weights[i] += 1.

    def teach(self):
        for i in range(quantityLes):
            j = random.randint(0, 9)
            r = perceptron(nums[j], weights)

            if j != tema:
                if r:
                    self.decrease(nums[j])
            else:
                if not r:
                    self.increase(nums[tema])
            print(j)
            print(weights)


Teacher = Teaching()
Teacher.teach()
