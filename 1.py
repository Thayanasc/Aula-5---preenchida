n1 = (input("Digite o primeiro número: "))
n2 = (input("Digite o segundo número: "))

# Verifica se os números são iguais
if n1 == n2:
    print("Os dois números são iguais.")
else:
    # Determina o maior número
    maior = n1 if n1 > n2 else n2

    if maior == int(maior):
        print("O maior número é:", int(maior))
    else:
        print("O maior número é:", maior)