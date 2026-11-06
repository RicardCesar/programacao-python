'''
(Sistema de acesso a plataforma) Crie um programa que peca a idade, se o utilizador tem autorizacao dos
responsaveis e se possui conta ativa. As respostas textuais devem ser sim ou nao.
- Menores de 13 anos nao podem aceder;
- Utilizadores entre 13 e 17 anos so podem aceder com autorizacao;
- Utilizadores com 18 anos ou mais podem aceder sem autorizacao;
- Em qualquer caso, o acesso so e permitido se a conta estiver ativa;
- O programa deve indicar se o acesso foi permitido ou negado, justificando a razao principal.
'''

idade = int(input("Digite sua idade: "))
aut = str(input("Você possui a autorização dos responsáveis? [S/N] ")).upper()
conta = str(input("Você possui conta ativa? [S/N] ")).upper()

if conta != 'S':
  print("Acesso negado.\nVocê não possui conta.")
elif idade < 13:
  print("Acesso negado.\nVocê tem menos de 13 anos.")
elif idade <= 17 and aut != 'S':
  print("Acesso negado.\nVocê não possui autorização.")
else:
  print("Seja bem-vindo!")