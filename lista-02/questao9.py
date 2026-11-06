'''
(Padrao numerico em piramide invertida e alinhada) Crie um programa que peca um numero natural
N entre 3 e 9.
O programa deve imprimir uma piramide invertida alinhada a direita, usando ciclos while aninhados.
Exemplo para N = 5:
    1 2 3 4 5
      1 2 3 4
        1 2 3
          1 2
            1
Se N estiver fora do intervalo, o programa deve pedir novamente ate receber um valor valido.
Obrigatorio: use while aninhado para controlar linhas, espacos e numeros.
'''

n = int(input("Digite um número: "))

while True:
  if n < 3 or n > 9:
    n = int(input("Digite um número maior que 3 e menor que 9: "))
  else:
    break

qtdlinha = 1
while qtdlinha <= n:
  espaco = 1
  while espaco < qtdlinha:
    print("  ", end="")
    espaco += 1

  cont = 1
  max = n - qtdlinha + 1
  while cont <= max:
    print(f"{cont} ", end="")
    cont += 1

  print("")
  qtdlinha += 1