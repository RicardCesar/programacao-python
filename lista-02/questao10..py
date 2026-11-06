'''
(Validacao de votacao com auditoria simples) Crie um programa que simule uma votacao entre tres 
candidatos: A, B e C. O programa deve continuar a pedir votos enquanto o utilizador nao digitar FIM.
- Votos validos sao apenas A, B ou C. Qualquer outro valor diferente de FIM deve ser contado como voto
  invalido e o ciclo deve continuar.
- Ao final, mostre: total de votos validos, total de votos invalidos, votos de cada candidato e o vencedor.
- Se houver empate no maior numero de votos, mostre "Empate" em vez de indicar um vencedor.
Obrigatorio: use while, continue para tratar votos invalidos e condicionais para determinar o resultado.
'''

a = 0
b = 0
c = 0
votovalido = 0
invalido = 0
voto = " "
while voto != "fim":
  print("Candidato A\nCandidato B\nCandidato C")
  voto = str(input("Informe seu voto: ")).strip().lower()
  if voto == 'fim':
    break
  elif voto != "a" and voto != "b" and voto != "c":
    votos_invalidos += 1
    print("Voto inválido!")
    continue

  elif voto == 'a':
    a += 1
    votovalido += 1
  elif voto == 'b':
    b += 1
    votovalido += 1
  elif voto == 'c':
    c += 1
    votovalido += 1

print(f"Votos válidos: {votovalido}\nVotos inválidos: {invalido}\nCandidato A: {a} votos\nCandidato B: {b} votos\nCandidato C: {c} votos")
if a > b and a > c:
  print("Candidato A venceu a eleição.")
elif b > a and b > c:
  print("Candidato B venceu a eleição.")
elif c > a and c > b:
  print("Candidato C venceu a eleição.")
else:
  print("EMPATE.")