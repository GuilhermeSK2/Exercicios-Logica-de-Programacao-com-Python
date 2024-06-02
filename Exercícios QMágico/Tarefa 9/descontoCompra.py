# Curso Básico de Python
# Nome do Desenvolvedor: Guilherme Freitas dos Santos
# Versão 1.0
# Excercicio de Lógica de programação com a Linguagem de Programação Python

# Programa que lê o valor de uma compra e a categoria do cliente, aplicando os descontos correspondentes.

valor = float(input("Digite o valor da compra: "))
categoria = int(input("Digite a categoria do cliente (1 para comum, 2 para associado, 3 para VIP): "))

if categoria == 1:
    desconto = 0
elif categoria == 2:
    desconto = 0.10
elif categoria == 3:
    desconto = 0.20
else:
    desconto = 0
    print("Categoria inválida. Sem desconto aplicado.")

valor_final = valor * (1 - desconto)
print("O valor final da compra é: R$", round(valor_final, 2))
