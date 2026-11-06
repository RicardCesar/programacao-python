'''
(Validador de codigo promocional) Crie um programa que peca um codigo promocional ao utilizador.
Um codigo e valido somente se cumprir todas as regras abaixo.
- Tem exatamente 8 caracteres;
- Comeca por PROMO;
- Os ultimos 3 caracteres sao numericos;
- O ultimo numero e par;
- Exemplo de codigo valido: PROM246.
- Caso o codigo seja invalido, o programa deve indicar a primeira regra que falhou.
'''

codigo = str(input("Insira um código promocional válido: ")).upper()

ultimos = codigo[-3:]

if len(codigo) != 8:
  print("O código não possui exatamente 8 caracteres.")
elif not codigo.startswith("PROMO"):
  print("O código não começa com PROMO")
elif not codigo[-3].isdigit():
  print("Os últimos caracteres não são numéricos.")
elif int(codigo[-1]) % 2 != 0:
  print("O último número não é par.")
else:
  print("O código é válido.")