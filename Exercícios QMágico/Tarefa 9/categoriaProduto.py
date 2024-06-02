# Curso Básico de Python
# Nome do Desenvolvedor: Guilherme Freitas dos Santos
# Versão 1.0
# Excercicio de Lógica de programação com a Linguagem de Programação Python

# Programa que lê o código de um produto e informa a sua categoria.

codigo = int(input("Digite o código do produto: "))
if 1 <= codigo <= 10:
    print("Alimento não-perecível.")
elif 11 <= codigo <= 20:
    print("Alimento perecível.")
elif 21 <= codigo <= 30:
    print("Vestuário.")
elif 31 <= codigo <= 40:
    print("Eletrônicos.")
else:
    print("Código inválido.")
