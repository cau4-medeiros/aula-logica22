taxa_brl_para_usd = 5.29
taxa_usd_para_brl = 1 / taxa_brl_para_usd

while True:
    #Exibe o menu de opções
    print("\n Escolha uma opção:")
    print("1. BRL para US$")
    print("2. US$ para BRL")
    print("3. Sair")

    opção = input("Digite o número de opção ")
    if opção == '1':
        valor_brl = float(input("Digite o valor em (R$):"))
        valor_usd = valor_brl / taxa_brl_para_usd 
        print(f"R$ {valor_brl:.2f} é equivalente a US$ {valor_usd:.2f}")
    elif opção == '2':
        valor_usd = float(input("Digite o valor em dólares (US$)"))
        valor_brl = valor_usd * taxa_brl_para_usd
        print(f"US$ {valor_usd:.2f} é equivalente a R$ {valor_brl:.2f}")
    elif opção == '3':
        print("Saindo...")
        break
    else:
        print("Opção inválida.. Tente novamente.") 