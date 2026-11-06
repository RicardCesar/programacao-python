'''
(Maximo divisor comum pelo algoritmo de Euclides) Crie um programa que peca dois numeros inteiros positivos.
- Valide as entradas: se algum numero for menor ou igual a zero, o programa deve voltar a pedir os dois valores.
- Depois, calcule o maximo divisor comum usando o algoritmo de Euclides, baseado em sucessivas substituicoes
  pelo resto da divisao.
- O programa deve mostrar o MDC e tambem quantas iteracoes foram necessarias ate chegar ao resultado.
Obrigatorio: use while e o operador %.
'''

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

while a <= 0 or b <= 0:
  a = int(input("Digite o primeiro número: "))
  b = int(input("Digite o segundo número: "))

num1, num2 = a, b
iteracoes = 0

while b != 0:
  resto = a % b
  a = b
  b = resto
  iteracoes += 1
print(f"O MDC entre {num1} e {num2} é {a}.\nOcorreram {iteracoes} iterações até chegar ao resultado.")