def classificar_heroi():
    while True:
        nome = input("Digite o nome do herói (ou 'sair' para encerrar): ").strip()
        if nome.lower() == "sair":
            print("Encerrando o programa. Até a próxima!")
            break

        xp_input = input(f"Digite a quantidade de XP para o herói {nome}: ").strip()
        
        try:
            xp = int(xp_input) # Converte o XP para inteiro
            if xp < 0:
                print("XP inválido. O valor deve ser maior ou igual a 0.")
                continue

            # Classificação com base no XP

            if xp <= 1000:
                nivel = "Ferro"
            elif 1001 <= xp <= 2000:
                nivel = "Bronze"
            elif 2001 <= xp <= 5000:
                nivel = "Prata"
            elif 5001 <= xp <= 7000:
                nivel = "Ouro"
            elif 7001 <= xp <= 8000:
                nivel = "Platina"
            elif 8001 <= xp <= 9000:
                nivel = "Ascendente"
            elif 9001 <= xp <= 10000:
                nivel = "Imortal"
            else:
                nivel = "Radiante"

            # Mensagem de saída
            print(f"O Herói de nome **{nome}** está no nível de **{nivel}**\n")
        
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro para o XP.")

# Executar o programa
classificar_heroi()