valor_hora = float(input('digite o valor da hora trabalhada'))
qt_hora =float(input('digite a quantidade de hora trabalhada'))
salario_bruto = valor_hora * qt_hora

print('salario bruto:', valor_hora * qt_hora,':R$', salario_bruto)

if salario_bruto <= 900:
    ir = 0
    print('salario bruto até 900(inclusive)- isento')

elif salario_bruto> 900 and salario_bruto <= 1500:
    #ir = salario bruto *0,05
    ir = salario_bruto *5/100
elif salario_bruto >1500 and salario_bruto <= 2500:
    #ir = salario_bruto * 0.1
    ir =salario_bruto * 10/100