class Calculadora:
    def __init__(self, n1, n2):
        self.valor_a = n1
        self.valor_b = n2

    def soma(self):
        return self.valor_a + self.valor_b

    def subtracao(self):
        return self.valor_a - self.valor_b

    def multiplicacao(self):
        return self.valor_a * self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b

calculadora = Calculadora(10, 2)
print(f'O valor A é: {calculadora.valor_a}')
print(f'O valor B é: {calculadora.valor_b}')
print(f'A soma vale: {calculadora.soma()}')
print(f'A subtração vale: {calculadora.subtracao()}')
print(f'A multiplicação vale: {calculadora.multiplicacao()}')
print(f'A divisão vale: {calculadora.divisao()}')
