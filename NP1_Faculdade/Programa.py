generos_filme = [
    ["Missão: Impossível", "Velozes e Furiosos", "John Wick"],
    ["Se Beber, Não Case!", "As Branquelas", "Gente Grande"],
    ["Invocação do Mal", "O Exorcista", "IT: A Coisa"],
]

sinopse_filme = [
    [
        "Um agente secreto enfrenta missões impossíveis repletas de ação e espionagem.",
        "Corridas clandestinas, perseguições intensas e assaltos eletrizantes ao redor do mundo.",
        "Um ex-assassino busca vingança contra aqueles que destruíram sua vida."
    ],
    [
        "Após uma despedida de solteiro em Las Vegas, amigos acordam sem lembrar de nada.",
        "Dois agentes disfarçados se passam por socialites para resolver um caso.",
        "Um grupo de amigos revive momentos da infância com muito humor e confusão."
    ],
    [
        "Investigadores paranormais enfrentam uma entidade demoníaca em uma casa assombrada.",
        "Uma menina possuída aterroriza sua família, levando a um exorcismo assustador.",
        "Um palhaço demoníaco aterroriza crianças em uma pequena cidade."
    ]
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