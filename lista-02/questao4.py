'''
(Classificacao de numero perfeito, abundante ou deficiente) Crie um programa que peca um numero inteiro
positivo maior que 1.
- O programa deve calcular a soma dos divisores proprios do numero, ou seja, todos os divisores positivos
  menores que o proprio numero.
- Depois, classifique o numero como: perfeito, se a soma dos divisores proprios for igual ao numero;
  abundante, se a soma for maior que o numero; deficiente, se a soma for menor que o numero.
Exemplo: 6 e perfeito, pois 1 + 2 + 3 = 6.
Obrigatorio: use while para testar os possiveis divisores.
'''

n = int(input("Digite um número inteiro maior que um: "))

while n <= 1:
  n = int(input("Digite outro número: "))

divisor = n - 1
somadiv = 0

while divisor > 0:
  if n % divisor == 0:
    somadiv += divisor
  divisor -= 1

if somadiv > n:
  print(f"O número {n} é abundante, visto que {somadiv} > {n}.")
elif somadiv == n:
  print(f"O número {n} é perfeito, visto que {somadiv} = {n}.")
else:
  print(f"O número {n} é deficiente, visto que {somadiv} < {n}.")