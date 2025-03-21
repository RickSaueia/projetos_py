generos_filme = [
    ["filme de ação 1", "filme de ação 2", "filme de ação 3"],
    ["filme de comédia 1", "filme de comédia 2", "filme de comédia 3"],
    ["filme de terror 1", "filme de terror 2", "filme de terror 3"],
]

sinopse_filme = [
    ["sinopse de ação 1", "sinopse de ação 2", "sinopse de ação 3"],
    ["sinopse de comédia 1", "sinopse de comédia 2", "sinopse de comédia 3"],
    ["sinopse de terror 1", "sinopse de terror 2", "sinopse de terror 3"],
]

while True:
    escolha_genero = input("\nEscolha um gênero de filme para acessar a galeria:\n[1] Ação\n[2] Comédia\n[3] Terror\n[0] Sair\n")
    print("_______________")
    
    if escolha_genero == "0":
        print("Saindo do programa...")
        break

    if escolha_genero in ["1", "2", "3"]:
        indice_genero = int(escolha_genero) - 1
        print(f"Filmes de {['Ação', 'Comédia', 'Terror'][indice_genero]}:")
        for i, filme in enumerate(generos_filme[indice_genero], start=1):
            print(f"[{i}] {filme}")
            
        while True:
            escolha_filme = input("\nDeseja ver a descrição de qual filme? Digite o número ou [0] para voltar: ")
            if escolha_filme == "0":
                break
            elif escolha_filme in ["1", "2", "3"]:
                print(sinopse_filme[indice_genero][int(escolha_filme) - 1])
            else:
                print("Escolha inválida, tente novamente.")
    else:
        print("Escolha inválida, tente novamente.")