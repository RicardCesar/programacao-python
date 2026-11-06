'''
(Caixa automatico com menu persistente) Crie um programa que simule um caixa automatico com
saldo inicial de 100 euros.
- Enquanto o utilizador nao escolher a opcao de sair, o programa deve apresentar um menu com as opcoes:
  1 - Consultar saldo; 2 - Depositar; 3 - Levantar; 4 - Sair.
- Depositos e levantamentos devem aceitar apenas valores positivos. Um levantamento so pode ser 
  realizado se houver saldo suficiente.
- O programa deve contar quantas operacoes validas de deposito e levantamento foram realizadas.
- Ao sair, mostre o saldo final e o numero total de operacoes validas.
'''

saldo = 100
op = 0
totalop = 0
while op != 4:
  print("1 - Consultar saldo\n2 - Depositar\n3 - Levantar\n4 - Sair")
  op = int(input("Qual operação deseja realizar? "))
  if op == 1:
    print(f"Seu saldo é de {saldo} euros.\n")
  elif op == 2:
    deposito = float(input("Informe o valor a ser depositado na conta: "))
    if deposito > 0:
      saldo += deposito
    else:
      print("Valor inválido.")
      continue
  elif op == 3:
    saque = float(input("Informe o valor do saque desejado: "))
    if saque > 0:
      saldo -= saque
    else:
      print("Valor inválido.")
      continue
  elif op > 4 or op < 1:
    print("Operação inexistente.\n")
  totalop += 1
else:
  print(f"Seu saldo é de {saldo} euros.\nForam realizadas {totalop} operações.")