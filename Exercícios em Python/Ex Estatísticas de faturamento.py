def calcular_estatisticas_faturamento(faturamento_diario):
    n = len(faturamento_diario)
    media_mensal = sum(faturamento_diario) / n
    menor_valor = min(faturamento_diario)
    maior_valor = max(faturamento_diario)
    dias_acima_media = sum(1 for faturamento in faturamento_diario if faturamento > media_mensal)
    return (menor_valor, maior_valor, dias_acima_media)

faturamento_diario = [1000, 2000, 1500, 1800, 1200, 900, 1700, 1100, 2100, 1900, 1600, 1400, 2000, 2500, 2200, 1800, 1700, 1500, 1900, 2100, 2000, 1700, 2200, 2400, 2300, 1800, 2100, 1900, 2200, 2000, 2300]
(menor_valor, maior_valor, dias_acima_media) = calcular_estatisticas_faturamento(faturamento_diario)
print("Menor valor de faturamento:", menor_valor)
print("Maior valor de faturamento:", maior_valor)
print("Número de dias com faturamento acima da média:", dias_acima_media)
