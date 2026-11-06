'''
(Classificacao de senha forte) Crie um programa que peca ao utilizador uma senha e classifique-a de acordo 
com as regras abaixo.
- Invalida, se tiver menos de 8 caracteres;
- Fraca, se tiver 8 ou mais caracteres, mas for composta apenas por numeros ou apenas por letras;
- Media, se tiver letras e numeros;
- Forte, se tiver letras, numeros e pelo menos um dos seguintes simbolos: @, #, $, % ou !.
- O programa deve mostrar a classificacao final da senha.
'''

senha = str(input("Crie sua senha: "))
simbolos = {'@','#','$','%','!'}

if len(senha) < 8:
  print("Inválida.")
elif senha.isdigit() == True or senha.isalpha() == True:
  print("Senha fraca.")
elif senha.isalnum() == True:
  print("Senha média.")
elif senha.isalnum() == False:
  print("Senha forte.")