escolha = input ("Digite o que deseja assistir: ")
filme_escolhido = df[df["title"] == escolha]
print(filme_escolhido[["title", "listed_in", "release_year", "duration"]])
print (100* "-", "\n")