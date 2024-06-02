# Curso Básico de Python
# Nome do Desenvolvedor: Guilherme Freitas dos Santos
# Versão 1.0
# Excercicio de Lógica de programação com a Linguagem de Programação Python

# Programa que simula o lançamento de um dado e conta a frequência de cada número obtido.

import random

def simular_lancamento_dados(n_lancamentos):
    frequencia_numeros = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for _ in range(n_lancamentos):
        resultado_lancamento = random.randint(1, 6)
        frequencia_numeros[resultado_lancamento] += 1
    return frequencia_numeros

n_lancamentos = int(input("Digite o número de lançamentos a serem simulados: "))
frequencia_numeros = simular_lancamento_dados(n_lancamentos)

print("Frequência de cada número:")
for numero, frequencia in frequencia_numeros.items():
    print(f"Número {numero}: {frequencia} vezes")