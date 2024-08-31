def calcular_faturamento(dados):
    if not dados:
        return "A lista de dados está vazia."
  
    menor_faturamento = min(dados)
    maior_faturamento = max(dados)
    media_mensal = sum(dados) / len(dados)
    dias_acima_da_media = sum(1 for valor in dados if valor > media_mensal)
    
    return {
        "menor_faturamento": menor_faturamento,
        "maior_faturamento": maior_faturamento,
        "dias_acima_da_media": dias_acima_da_media
    }

def main():
    entrada = input("Digite os valores de faturamento diário separados por espaço: ")
    
    try:
        faturamento_diario = list(map(float, entrada.split()))
    except ValueError:
        print("Por favor, insira apenas números separados por espaço.")
        return
    
    resultados = calcular_faturamento(faturamento_diario)
    
    print("Menor faturamento:", resultados["menor_faturamento"])
    print("Maior faturamento:", resultados["maior_faturamento"])
    print("Número de dias acima da média mensal:", resultados["dias_acima_da_media"])

if __name__ == "__main__":
    main()
