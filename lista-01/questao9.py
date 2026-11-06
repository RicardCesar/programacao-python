'''
(Classificacao de temperatura corporal) Crie um programa que peca a temperatura corporal de uma pessoa e se
ela apresenta sintomas. A resposta textual deve ser sim ou nao. Primeiro, classifique a temperatura; depois,
apresente uma recomendacao.
- Abaixo de 35: hipotermia;
- De 35 ate 37.4: temperatura normal;
- De 37.5 ate 38: estado febril;
- Acima de 38: febre;
- Se houver sintomas e a temperatura for maior ou igual a 37.5, mostrar: recomenda-se procurar orientacao medica;
- Se nao houver sintomas e a temperatura for normal, mostrar: sem sinais de alerta;
- Nos demais casos, mostrar: acompanhar evolucao.
'''

temp = float(input("Informe sua temperatura corporal: "))
sintomas = str(input("Você apresenta sintomas? [S/N] ")).upper()

if temp < 35:
  classificacao = "Hipotermia"
elif temp < 37.4:
  classificacao = "Temperatura normal."
elif temp < 38:
  classificacao = "Estado Febril."
else:
  classificacao = "Febre."

if sintomas == 'S' and temp >= 37.5:
  recomend = "Recomenda-se procurar orientação médica."
elif sintomas != 'S' and temp >= 35:
  recomend = "Sem sinais de alerta."
else:
  recomend = "Acompanhar evolução."

print(f"{classificacao} {recomend}")