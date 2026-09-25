excelente = 0
ruim = 0
bom= 0

for i in range(50):
    print("Entrevistado", i + 1)

    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))

    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    opiniao = int(input("Digite sua opinião: "))

    if opiniao == 1:
        excelente = excelente + 1
    elif opiniao == 3:
        ruim = ruim + 1
    elif opiniao == 2:
        bom = bom + 1

print("Quantidade de respostas EXCELENTE:", excelente)
print("Quantidade de respostas RUIM:", ruim)
print("Quantidade de respostas BOM:", bom)
