decrescente = True
anterior = int(input("Digite o primeiro número da sequencia!"))

valor = 1

while valor != 0 and decrescente:
    valor = int(input("Degite o próximo número da sequência: "))
    if valor > anterior:
        decrescente = False
        anterior = valor
    
    if decrescente:
        print("A sequência está em ordem decrescente!")
    else:
        print("A sequência não esta em ordem decrescente!")