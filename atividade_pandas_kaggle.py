import os

os.system ("cls")

import pandas as pd


try:

    # # Importando a Base de Dados 
    df = pd.read_csv('netflix_titles.csv', sep=',', encoding='utf-8')

    # # Conhecendo a Base de dados
    # print (df.head())
    # print (100* "-", "\n")

    # # Entendendo as colunas
    # print (df.dtypes)
    # print (100* "-", "\n")

    # # Filtrando por títulos dos filmes e seus gêneros
    # print ("Filmes Disponíveis e seus gêneros")
    # df_title = df[["title", "listed_in"]].sort_values(by="title")
    # print (df_title.head(10))
    # print (100* "-", "\n")

    # # Escolhendo o que assistir
    # escolha = input ("Digite o que deseja assistir: ")
    # filme_escolhido = df[df["title"] == escolha]
    # print(filme_escolhido[["title", "listed_in", "release_year", "duration"]])
    # # print (100* "-", "\n")

    df.to_csv('Base_modificada.cvs', index=False, sep=',', encoding='utf-8')
    df.to_excel('netflix_titles.xls', index=False, engine='openpyxl')

except Exception as e:
    print(f'Erro {e}')
    exit()