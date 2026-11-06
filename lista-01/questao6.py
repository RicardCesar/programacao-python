'''
(Verificacao de matricula academica) Crie um programa que peca o numero de creditos concluidos,
a media atual, se as propinas estao regularizadas e se existem pendencias documentais.
As respostas textuais devem ser sim ou nao.
- O aluno esta apto para renovar a matricula se tiver pelo menos 30 creditos concluidos;
- A media deve ser igual ou superior a 9.5;
- As propinas devem estar regularizadas;
- Nao pode haver pendencia documental;
- Caso a matricula nao possa ser renovada, o programa deve mostrar apenas a primeira razao encontrada.
'''

credit = int(input("Informe o número de créditos concluídos: "))
media = float(input("Informe sua média: "))
propin = str(input("As propinas estão regularizadas? [S/N] ")).upper().strip()
doc = str(input("Existem pendências documentais? [S/N] ")).upper().strip()
if credit < 30:
  print("Você não possui créditos suficientes.")
elif media < 9.5:
  print("Você não atingiu a média necessária.")
elif propin != 'S':
  print("As propinas não foram regularizadas.")
elif doc != 'N':
  print("Você possui pendências documentais.")
else:
  print("Você está apto a renovar a matrícula.")