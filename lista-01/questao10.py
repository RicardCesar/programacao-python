'''
(Analise de aprovacao em concurso) Crie um programa que peca a nota da prova objetiva, a nota da prova 
pratica, a nota da entrevista e se o candidato entregou a documentacao. As respostas textuais devem
ser sim ou nao.
- Qualquer nota abaixo de 50 elimina o candidato;
- A media final deve ser calculada por: objetiva * 0.4 + pratica * 0.4 + entrevista * 0.2;
- O candidato e aprovado se a media final for maior ou igual a 70 e a documentacao tiver sido entregue;
- Se a media for maior ou igual a 70, mas a documentacao nao tiver sido entregue, o candidato fica pendente;
- Se a media for menor que 70, fica reprovado;
- O programa deve mostrar a media final e a situacao do candidato.
'''

#questão 10
notaobj = float(input("Digite sua nota da prova obejtiva: "))
notaprat = float(input("Digite sua nota da prova prática: "))
notaent = float(input("Digite sua nota da entrevista: "))
doc = str(input("O candidato entregou as documentações necessárias? [S/N]")).upper().strip()

media = (notaobj * 4 + notaprat * 4 + notaent * 2) / 10

if notaobj < 50 or notaprat < 50 or notaent < 50:
  print(f"CANDIDATO ELIMINADO (nota em uma das provas abaixo de 50).\nMédia = {media:.1f}")
elif media < 70:
  print(f"CANDIDATO REPROVADO.\nMédia = {media:.1f}")
elif doc != 'S':
  print(f"CANDIDATO PENDENTE.\nMédia = {media:.1f}")
else:
  print(f"CANDIDATO APROVADO.\nMédia = {media:.1f}")