'''
(Analisador de sequencia com sentinela) Crie um programa que leia numeros inteiros introduzidos pelo
utilizador ate que seja digitado 0.
- Sem usar listas, o programa deve calcular e mostrar: quantidade de numeros lidos, quantidade de
  positivos, quantidade de negativos, soma dos numeros pares, maior numero introduzido e menor
  numero introduzido.
- O valor 0 serve apenas para terminar a leitura e nao deve entrar nos calculos.
- Se o primeiro valor digitado for 0, o programa deve informar que nenhum numero foi analisado.
Obrigatorio: use while e condicionais aninhadas quando necessario.
'''

qtdnum = 0
qtdpos = 0
qtdneg = 0
somapar = 0

n = int(input("Digite um número: "))

if n == 0:
  print("Nenhum número foi analisado.")
else:
  maior = n
  menor = n
  while n != 0:
    qtdnum += 1

    if n > maior:
      maior = n
    if n < menor:
      menor = n

    if n > 0:
      qtdpos += 1
    elif n < 0:
      qtdneg += 1

    if n % 2 == 0:
      somapar += n

    n = int(input("Digite outro número: "))

  print(f"Fim da leitura.\nQuantidade de números lidos: {qtdnum}\nQuantidade de positivos: {qtdpos}\nQuantidade de negativos: {qtdneg}\nSoma dos pares: {somapar}\nMaior número: {maior}\nMenor número: {menor}\n")
