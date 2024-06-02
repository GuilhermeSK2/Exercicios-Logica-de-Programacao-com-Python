# Curso Básico de Python
# Nome do Desenvolvedor: Guilherme Freitas dos Santos
# Versão 1.0
# Excercicio de Lógica de programação com a Linguagem de Programação Python

# Programa que gera um número aleatório entre 1 e 100 que o jogador deve adivinhar.

import random

numero_minimo = 1
numero_maximo = 100

numero_secreto = random.randint(numero_minimo, numero_maximo)

max_tentativas = 10

print("Bem-vindo ao jogo de adivinhação!")
print(f"O número secreto está entre {numero_minimo} e {numero_maximo}.")

for tentativa in range(1, max_tentativas + 1):
    palpite = int(input(f"Tentativa {tentativa}/{max_tentativas}. Faça seu palpite: "))

    if palpite == numero_secreto:
        print(f"Parabéns! Você acertou o número secreto {numero_secreto} em {tentativa} tentativas.")
        break
    elif palpite < numero_secreto:
        print("O número secreto é maior.")
    else:
        print("O número secreto é menor.")
else:
    print(f"Você excedeu o número máximo de tentativas. O número secreto era {numero_secreto}.")
