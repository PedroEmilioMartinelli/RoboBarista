print("Ola, seja bem vindo a minha cafeteria")

nome = ""

while len(nome) ==0:
    nome  = input("Qual o seu nome?\n")


menu = "Cafe, Espresso, capuchino, Late, Chocotino "

if nome == "Ben" or  nome == "Patricia" or nome == "Loki":
    nome_mau = input("Você é mau??\n")
    while len(nome_mau) ==0:
        nome_mau  = input("Você é mau??\n ")
    boas_acoes =int(input("Quantas atitudes boas voce fez hoje?\n"))
    if nome_mau == "Sim" and boas_acoes < 4:
        print(nome + " ,você não é bem vindo aqui. SAIA AGORA")
        exit()
    else:
        print("Ho, temos uma coisa rara aqui, seja bem vindo(a) " + nome)

pedido = input(nome + ", oque voce gostaria de beber?\n" + menu  + ":\n")


if pedido == "Cafe":
    price = 4
elif pedido == "Espresso":
    price = 6
elif pedido == "Late":
    extra = input("QUER CHANTILI EXTRA?\n")
    if extra == "Sim":
        price = 12
    else:
        price = 10
elif pedido == "Chocotino":
    price = 9
else:
    print("não temos isso, desculpa, tente  outra coisa")
    exit()

quantidade = input("quantos voce vai querer?\n")

preço = price * int(quantidade)

print("O seu " + pedido + " ficara pronto em breve")

print("Aqui esta " + nome + ", O seu " + pedido +  " fica: R$" + str(preço))
