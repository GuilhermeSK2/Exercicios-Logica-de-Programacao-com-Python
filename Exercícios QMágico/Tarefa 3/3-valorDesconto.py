# Curso Básico de Python
# Nome do Desenvolvedor: Guilherme Freitas dos Santos
# Versão 1.0
# Excercicio de Lógica de programação com a Linguagem de Programação Python

# Programa que recebe o valor de um produto a porcentagem de desconto que deve ser atribuido e retorna o valor com desconto.

print("Vamos calcular o valor de um produto com o desconto!")

valorProduto = float(input("Insira o valor do produto: "))
valorDesconto = float(input("Insira o valor de desconto: "))

desconto = valorProduto * (valorDesconto / 100)
valorFinalProduto = valorProduto - desconto
print("O valor final do produto após aplicar um desconto de",desconto,"% é:",valorFinalProduto)