def calcular_ranque(vitorias, derrotas):
    saldo_vitorias = vitorias - derrotas

    # Determinar o nível com base no número de vitórias
    if vitorias < 10:
        nivel = "Ferro"
    elif 11 <= vitorias <= 20:
        nivel = "Bronze"
    elif 21 <= vitorias <= 50:
        nivel = "Prata"
    elif 51 <= vitorias <= 80:
        nivel = "Ouro"
    elif 81 <= vitorias <= 90:
        nivel = "Diamante"
    elif 91 <= vitorias <= 100:
        nivel = "Lendário"
    else:
        nivel = "Imortal"

    return saldo_vitorias, nivel

# Exemplo de uso
def main():
    print("Calculadora de Partidas Rankeadas")
    
    # Entradas do jogador
    vitorias = int(input("Digite o número de vitórias: "))
    derrotas = int(input("Digite o número de derrotas: "))

    # Calcular resultados
    saldo, nivel = calcular_ranque(vitorias, derrotas)

    # Exibir resultado
    print(f"O Herói tem um saldo de {saldo} e está no nível {nivel}.")

if __name__ == "__main__":
    main()
