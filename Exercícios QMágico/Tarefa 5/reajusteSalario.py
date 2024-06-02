# Curso Básico de Python
# Nome do Desenvolvedor: Guilherme Freitas dos Santos
# Versão 1.0
# Excercicio de Lógica de programação com a Linguagem de Programação Python

# Programa para calcular o novo salário após reajuste.

salario_atual = float(input("Digite o salário mensal atual do funcionário: "))

percentual_reajuste = float(input("Digite o percentual de reajuste: "))

novo_salario = salario_atual + (salario_atual * percentual_reajuste / 100)

print("O novo salário do funcionário é: R$", round(novo_salario,2))