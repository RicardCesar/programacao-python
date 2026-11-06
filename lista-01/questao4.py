'''
(Avaliacao de risco de entrega) Uma empresa de entregas quer classificar o risco de uma encomenda.
Peca ao utilizador a distancia em km, o peso em kg, se a encomenda e fragil e se a entrega e urgente.
As respostas textuais devem ser sim ou nao.
- Baixo, se a distancia for ate 10 km, o peso ate 5 kg e nao for fragil;
- Medio, se apenas uma das condicoes seguintes for verdadeira: distancia acima de 10 km, 
  peso acima de 5 kg ou produto fragil;
- Alto, se duas dessas condicoes forem verdadeiras;
- Critico, se a entrega for urgente e o risco ja seria alto;
- O programa deve mostrar a classificacao final.
'''

distancia = float(input("Informe a distância até sua casa (em km): "))
peso = float(input("Informe o peso do produto (em kg): "))
fragil = str(input("A encomenda é frágil? [S/N] ")).upper()
urgente = str(input("A entrega é urgente? [S/N] ")).upper()

dist = distancia > 10
p = peso > 5
f = fragil == 'S'

risco = dist + p + f

if risco == 0:
  print("Risco BAIXO.")
elif risco == 1:
  print("Risco MÉDIO.")
elif risco == 2:
  if urgente != 'S':
    print("Risco ALTO.")
  else:
    print("Risco CRÍTICO.")