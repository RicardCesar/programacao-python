'''
(Sequencia de Collatz com estatisticas) Crie um programa que peca um numero inteiro positivo n e gere
a sequencia de Collatz ate chegar a 1.
- Regra: se n for par, o proximo valor e n // 2; se n for impar, o proximo valor e 3 * n + 1.
- O programa deve mostrar todos os termos da sequencia, a quantidade de passos realizados e o
  maior valor atingido durante a sequencia.
- Se o utilizador inserir um valor invalido, o programa deve pedir novamente ate receber um
  inteiro positivo.
Obrigatorio: use while e condicionais dentro do ciclo.
'''

n = int(input("Digite um número: "))
passo = 0

while n <= 0:
  n = int(input("Digite um número: "))

maior = n
while True:
  print(n)

  if n > maior:
    maior = n

  if n == 1:
    break

  if n % 2 == 0:
    n = n // 2
  else:
    n = 3*n + 1
  passo += 1

print(f"Houveram {passo} iterações.\nO maior número na sequência foi {maior}.")