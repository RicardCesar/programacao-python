'''
(Simulador de autenticacao com senha e confirmacao) Crie um programa que peca ao utilizador para criar
uma senha valida.
- A senha deve cumprir todas as regras: ter pelo menos 8 caracteres, conter pelo menos um digito e
  conter pelo menos uma letra.
- Enquanto a senha nao for valida, o programa deve indicar apenas a primeira regra que falhou e pedir
  uma nova senha.
- Quando a senha for valida, o programa deve pedir confirmacao. Se a confirmacao for diferente da
  senha, deve pedir novamente apenas a confirmacao ate coincidir.
Obrigatorio: use pelo menos dois ciclos while. Nao use listas.
'''

senha = str(input("Digite sua senha: "))

while True:
  if len(senha) < 8:
    print("Sua senha tem menos de 8 caracteres.")
    senha = str(input("Digite outra senha: "))
    continue

  temdigito = False
  temcaractere = False
  for i in senha:
    if i.isdigit():
      temdigito = True
    if i.isalpha():
      temcaractere = True

  if not temdigito:
    print("Sua senha não possui nenhum digito.")
    senha = str(input("Digite outra senha: "))
    continue
  if not temcaractere:
    print("Sua senha não possui nenhum caractere.")
    senha = str(input("Digite outra senha: "))
    continue
  break

confirmacao = str(input("Confirme a senha: "))
while confirmacao != senha:
    confirmacao = str(input("Senha incorreta.\nConfirme a senha: "))
print("Autenticação concluída.")