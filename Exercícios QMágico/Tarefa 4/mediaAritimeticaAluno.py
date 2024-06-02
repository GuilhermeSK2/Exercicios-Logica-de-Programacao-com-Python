# Curso Básico de Python
# Nome do Desenvolvedor: Guilherme Freitas dos Santos
# Versão 1.0
# Excercicio de Lógica de programação com a Linguagem de Programação Python

# Programa que calcula a média aritmética simples e escreve uma mensagem que diz se o aluno foi ou não aprovado (considerando que nota igual ou maior que 6 o aluno é aprovado). Escreve também a média calculada.

nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))

media = (nota1 + nota2) / 2

if media >= 6:
    print("O Aluno foi aprovado com média", round(media, 2))
else:
    print("O Aluno foi reprovado com média", round(media, 2))