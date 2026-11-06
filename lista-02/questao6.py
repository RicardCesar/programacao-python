'''
(Conversor de decimal para binario sem bin()) Crie um programa que peca um numero inteiro nao 
negativo e apresente sua representacao em binario.
- Nao utilize a funcao bin() nem estruturas de dados como listas.
- A conversao deve ser feita por divisoes sucessivas por 2, acumulando os restos na ordem correta.
- O programa deve tratar corretamente o caso em que o numero digitado e 0.
Obrigatorio: use while para realizar as divisoes sucessivas.
'''

n = int(input("Digite um número: "))

while n < 0:
  n = int(input("Digite um número inteiro não negativo: "))

aux = n
binario = ''
while True:
  if aux % 2 == 0:
    binario = '0' + binario
  else:
    binario = '1' + binario
  aux = aux // 2

  if aux == 0:
    break
print(f"{n} em binário é {binario}.")