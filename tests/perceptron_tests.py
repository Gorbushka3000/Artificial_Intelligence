from unittest import TestCase, main
from ElementsAI.perceptron import perceptron


class PreceptronTest(TestCase):

    def test_preceptron(self):
        self.assertEquals(perceptron(num1), False)
        self.assertEquals(perceptron(num2), True)
        self.assertEquals(perceptron(num3), False)
        self.assertEquals(perceptron(num4), False)


num1 = list('001001001001001')
num2 = list('111001111100111')
num3 = list('asexjdvnkndjkjk')
num4 = list('11sddfr00101sd6')

if __name__ == '__main__':
    main()
