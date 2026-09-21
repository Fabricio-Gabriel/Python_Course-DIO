'''Não existem constantes no Python, mas por convenção, variáveis que não devem ser alteradas são escritas em letras maiúsculas.'''


nome = "Guilherme"
idade = 28

print(nome, idade)

limite_saque_diario = 1000.00

BRAZILIAN_STATES = ["SP", "RJ", "MG", "ES"]

for estado in BRAZILIAN_STATES:
    if estado == "SP":
        print("Poluição do ar é alta")
        break
    else:
        print("Poluição do ar é baixa")

