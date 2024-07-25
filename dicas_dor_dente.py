def dicas_dor_dente():
    print("Bem-vindo ao Assistente de Dicas para Dor de Dente!")
    print("Responda algumas perguntas para receber dicas personalizadas.\n")

    # Pergunta sobre a intensidade da dor
    intensidade = input("Qual é a intensidade da dor? (leve, moderada, severa): ").strip().lower()

    # Pergunta sobre a localização da dor
    localizacao = input("A dor está localizada em uma área específica ou se espalha por toda a boca? (específica, toda a boca): ").strip().lower()

    # Pergunta sobre a duração da dor
    duracao = input("Há quanto tempo você está com dor? (menos de um dia, mais de um dia, uma semana ou mais): ").strip().lower()

    print("\nAqui estão algumas dicas baseadas nas suas respostas:\n")

    # Oferece dicas com base nas respostas do usuário
    if intensidade == "leve":
        print("- Para dores leves, tente enxaguar a boca com água morna salgada.")
        print("- Use fio dental para remover qualquer alimento preso entre os dentes.")
        print("- Tome um analgésico de venda livre, como paracetamol ou ibuprofeno.")

    elif intensidade == "moderada":
        print("- Enxague a boca com uma solução de água morna e sal.")
        print("- Aplique uma compressa fria na bochecha perto da área afetada.")
        print("- Considere usar um gel anestésico oral.")

    elif intensidade == "severa":
        print("- Procure atendimento odontológico imediatamente.")
        print("- Tome analgésicos fortes, conforme recomendado por um profissional de saúde.")
        print("- Evite alimentos e bebidas quentes ou frias que possam piorar a dor.")

    if localizacao == "específica":
        print("- Evite mastigar do lado afetado.")
        print("- Use uma escova de dentes de cerdas macias para escovar a área ao redor do dente dolorido.")

    elif localizacao == "toda a boca":
        print("- Certifique-se de manter uma boa higiene oral, escovando e usando fio dental regularmente.")
        print("- Limite a ingestão de alimentos açucarados e bebidas ácidas.")

    if duracao == "menos de um dia":
        print("- Se a dor persistir, consulte um dentista para avaliar a causa subjacente.")
        
    elif duracao == "mais de um dia":
        print("- Marque uma consulta com um dentista o mais rápido possível.")
        
    elif duracao == "uma semana ou mais":
        print("- É crucial buscar ajuda profissional para evitar complicações mais graves.")

    print("\nLembre-se, estas são apenas dicas gerais. É importante consultar um dentista para um diagnóstico e tratamento adequado.")

# Executa o programa
dicas_dor_dente()
