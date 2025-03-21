generos_filme = [
    ["filme de ação 1","filme de ação 2","filme de ação 3"],
    ["filme de comédia 1","filme de comédia 2","filme de comédia 3"],
    ["filme de terror 1","filme de terror 2","filme de terror 3"],
]
sinopse_filme = [
    ["sinopse de ação 1","sinopse de ação 2","sinopse de ação 3"],
    ["sinopse de comédia 1","sinopse de comédia 2","sinopse de comédia 3"],
    ["sinopse de terror","sinopse de terror 2","sinopse de terror 3"],
]
escolha_genero = input("Escolha um genero de filme para acessar a galeria. | [1] Ação | [2] Comédia | [3] Terror \n")
print("_______________")
 
""" FILMES DE AÇÃO """
if escolha_genero == "1":
    print("Filmes de Ação:")
    print(generos_filme[0])
    print("\n")
    escolha_filme = input("Deseja ver a descriçaõ de qual filme? [1] filme 1 [2] filme 2 [3] filme 3 \n")
    if escolha_filme == "1":
        print(sinopse_filme[0][0])
        breakpoint()
    if escolha_filme == "2":
        print(sinopse_filme[0][1])
        breakpoint()
    if escolha_filme == "3":
        print(sinopse_filme[0][2])
        breakpoint()
    else:
        print("escolha inválida")
 
 
""" FILMES DE COMEDIA """
if escolha_genero == "2":
    print("Filmes de Comédia:\n")
    print(generos_filme[1])
    print("\n")
    escolha_filme = input("Deseja ver a descriçaõ de qual filme? [1] filme 1 [2] filme 2 [3] filme 3 \n")
    if escolha_filme == "1":
        print(sinopse_filme[1][0])
        breakpoint()
    if escolha_filme == "2":
        print(sinopse_filme[1][1])
        breakpoint()
    if escolha_filme == "3":
        print(sinopse_filme[1][2])
        breakpoint()
    else:
        print("escolha inválida")
   
 
""" FILMES DE TERROR """
if escolha_genero == "3":
    print("Filmes de Terror:\n")
    print(generos_filme[2])
    print("\n")
    escolha_filme = input("Deseja ver a descriçaõ de qual filme? [1] filme 1 [2] filme 2 [3] filme 3 \n")
    if escolha_filme == "1":
        print(sinopse_filme[2][0])
        breakpoint()
    if escolha_filme == "2":
        print(sinopse_filme[2][1])
        breakpoint()
    if escolha_filme == "3":
        print(sinopse_filme[2][2])
        breakpoint()
    else:
        print("escolha inválida")
   
else:
    print("escolha inválida")
 