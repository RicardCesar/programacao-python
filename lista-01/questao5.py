'''
(Classificacao de consumo de energia) Crie um programa que peca o consumo mensal de energia de uma
residencia em kWh e o numero de moradores. Calcule o consumo médio por morador e classifique o resultado.
- Ate 50 kWh por morador: consumo eficiente;
- Acima de 50 e ate 100: consumo moderado;
- Acima de 100 e ate 200: consumo elevado;
- Acima de 200: consumo critico;
- Se o numero de moradores for menor ou igual a zero, o programa deve mostrar uma mensagem de erro
  e nao realizar a classificacao.
'''

consumo = float(input("Infome o consumo mensal em kWh: "))
nmoradores = int(input("Quantos moradores vivem nessa residência? "))

if nmoradores <= 0:
  print("ERRO!")
else:
  media = consumo / nmoradores

  if media <= 50:
    print("Consumo eficiente.")
  elif media <= 100:
    print("Consumo moderado.")
  elif media <= 200:
    print("Consumo elevado.")
  else:
    print("Consumo crítico.")