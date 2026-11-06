'''
(Simulador de prioridade em atendimento) Crie um programa que peca a idade, se a pessoa esta gravida,
se possui deficiencia e se esta com atendimento agendado. As respostas textuais devem ser sim ou nao.
- Prioridade maxima, se a pessoa tiver 80 anos ou mais;
- Prioridade alta, se for idosa, gravida ou possuir deficiencia;
- Prioridade media, se tiver atendimento agendado;
- Atendimento comum, nos demais casos;
- Considere idosa a pessoa com 65 anos ou mais.
'''

idade = int(input("Digite sua idade: "))
gravida = str(input("Você está grávida? [S/N] ")).upper()
defic = str(input("Você possui alguma deficiência? [S/N] ")).upper()
atend = str(input("Você está com atendimento agendado? [S/N] ")).upper()

if idade >= 80:
  print("Prioridade máxima.")
elif idade >= 65 or gravida == 'S' or defic == 'S':
  print("Prioridade alta.")
elif atend != 'S':
  print("Prioridade média.")
else:
  print("Atendimento comum.")