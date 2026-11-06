'''
(Validador de PIN com bloqueio) Crie um programa que simule o acesso a uma conta protegida por PIN.
O PIN correto deve ser definido no proprio programa, por exemplo "4826".
- O utilizador tem no maximo 3 tentativas para inserir o PIN correto.
- A cada tentativa incorreta, o programa deve informar quantas tentativas restam.
- Se o PIN for inserido corretamente, o programa deve terminar imediatamente o ciclo e mostrar "Acesso permitido".
- Se as 3 tentativas forem usadas sem sucesso, o programa deve mostrar "Conta bloqueada".
Obrigatorio: use while, break e while...else.
'''

contador = 3
pin = "4826"

while (contador >= 1):
  senha = str(input("Digite a senha: "))
  if senha == pin:
    print("Acesso permitido!")
    break
  elif senha!= pin:
    contador -= 1
    print(f"Acesso negado!\nVocê possui {contador} tentativas.")
else:
  print("Conta bloqueada.")