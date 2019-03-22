"""
Você deve criar uma classe carro que vai possuir
dois atributos compostos por outras duas classes:

Motor
Direção
O Motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:

Atributo de dado velocidade
Método acelerar, que deverá incremetar a velocidade de uma unidade
Método frear que deverá decrementar a velocidade em duas unidades
A Direção terá a responsabilidade de controlar a direção. Ela oferece
os seguintes atributos:

Valor de diração com valores possíveis: Norte, Sul, Leste, Oeste.
Método girar_a_direita
Método girar_a_esquerda

       N
    O     L
       S

Exemplo:
    >>> # Testando motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> # Testando Direcao
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Oeste'
"""


class Motor:
    def __init__(self, velocidade=0):
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        if self.velocidade < 2:
            self.velocidade = 0
        else:
            self.velocidade = self.velocidade - 2


class Direcao:
    def __init__(self, direcao=['Norte', 'Leste', 'Sul', 'Oeste'], valor='Norte'):
        self.direcao = direcao
        self.valor = valor


    def girar_a_direita(self):
        try:
            self.valor = self.direcao[self.direcao.index(self.valor) + 1]
        except:
            self.valor = self.direcao[0]


    def girar_a_esquerda(self):
        self.valor = self.valor = self.direcao[self.direcao.index(self.valor) - 1]

class Carro:
    def __init__(self, direcao, motor):
        self.direcao = Direcao()
        self.motor = Motor()

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        self.motor.acelerar()
        return self.motor.velocidade

    def frear(self):
        self.motor.frear()
        return self.motor.velocidade

    def calcular_direcao(self):
        return self.direcao.valor

    def girar_a_direita(self):
        self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()


if __name__ == '__main__':
    # Testando motor
    motor = Motor()
    print(motor.velocidade) # 0
    motor.acelerar()
    print(motor.velocidade) # 1
    motor.acelerar()
    print(motor.velocidade) # 2
    motor.acelerar()
    print(motor.velocidade) # 3
    print('-------')
    motor.frear()
    print(motor.velocidade) # 1
    motor.frear()
    print(motor.velocidade) # 0

    # Testando Direcao
    direcao = Direcao()
    print(direcao.valor) # Norte
    direcao.girar_a_direita()
    print(direcao.valor) # Leste
    direcao.girar_a_direita()
    print(direcao.valor) # Sul
    direcao.girar_a_direita()
    print(direcao.valor)  # Oeste
    direcao.girar_a_direita()
    print(direcao.valor)  # Norte

    print('======== esquerda')
    direcao.girar_a_esquerda()
    print(direcao.valor)  # Oeste
    direcao.girar_a_esquerda()
    print(direcao.valor)  # Sul
    direcao.girar_a_esquerda()
    print(direcao.valor)  # Leste
    direcao.girar_a_esquerda()
    print(direcao.valor)  # Norte
    direcao.girar_a_esquerda()
    print(direcao.valor)  # Oeste

    print('==== CARRO ====')
    # Testando Carro
    carro = Carro(direcao, motor)
    print(carro.calcular_velocidade()) # 0
    carro.acelerar()
    print(carro.calcular_velocidade())  # 1
    carro.acelerar()
    print(carro.calcular_velocidade())  # 1
    carro.frear()
    print(carro.calcular_velocidade())  # 0

    print(carro.calcular_direcao()) # Norte

    carro.girar_a_direita()
    print(carro.calcular_direcao()) # Leste

    carro.girar_a_esquerda()
    print(carro.calcular_direcao()) # Norte

    carro.girar_a_esquerda()
    print(carro.calcular_direcao()) # Oeste