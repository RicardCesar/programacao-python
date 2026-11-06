'''
(Verificador de compatibilidade para bolsa de estudo) Crie um programa que peca o rendimento mensal familiar,
o numero de pessoas no agregado familiar, a media academica e se o estudante ja recebe outra bolsa.
- O estudante e elegivel se o rendimento por pessoa for inferior ou igual a 600;
- A media academica deve ser igual ou superior a 14;
- O estudante nao pode receber outra bolsa;
- Classifique como Elegivel com prioridade se o rendimento por pessoa for ate 400 e a media for igual ou
  superior a 16;
- Classifique como Elegivel se cumprir as regras gerais;
- Classifique como Nao elegivel caso contrario;
- Se o numero de pessoas no agregado for menor que 1, o programa deve apresentar erro.
'''

renda = float(input("Qual é a renda familiar mensal: "))
npessoas = int(input("Quantas pessoas compõem sua família? "))
media = float(input("Informe sua média acadêmica: "))
bolsa = str(input("Você já recebe alguma bolsa? ")).upper().strip()

if npessoas < 1:
  print("ERRO")
else:
  rpp = renda / npessoas

  if rpp > 600 or media < 14 or bolsa == 'S':
    print("Não elegível.")
  elif rpp <= 400 and media >= 16:
    print("Elegível com prioridade!")
  else:
    print("Elegível.")