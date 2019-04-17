# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Gabriel Mauricio Kabbani, gabrielmk@al.insper.edu.br
# - aluno B: Jonathan Mansur, jonathanm1@al.insper.edu.br

def carregar_cenarios():
    cenarios = {
        "inicio": {
            "titulo": "Saguao do perigo",
            "descricao": "Voce esta no saguao de entrada do insper",
            "opcoes": {
                "andar professor": "Tomar o elevador para o andar do professor",
                "biblioteca": "Ir para a biblioteca"
            }
        },
        "andar professor": {
            "titulo": "Andar do desespero",
            "descricao": "Voce chegou ao andar da sala do seu professor",
            "opcoes": {
                "inicio": "Tomar o elevador para o saguao de entrada",
                "professor": "Falar com o professor"
            }
        },
        "professor": {
            "titulo": "O monstro do Python",
            "descricao": "Voce foi pedir para o professor adiar o EP. "
                         "O professor revelou que é um monstro disfarçado "
                         "e devorou sua alma.",
            "opcoes": {}
        },
        "biblioteca": {
            "titulo": "Caverna da tranquilidade",
            "descricao": "Voce esta na biblioteca",
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada"
            }
        }
    }
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual


def main():
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    print()
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte...)")
    print()

    cenarios, nome_cenario_atual = carregar_cenarios()
    cont=0
    itens=[]
    objetos=["lanterna","chave de fenda", "clips"]
    game_over = False
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]

        # Aluno A: substitua este comentário pelo código para imprimir 
        # o cenário atual.

        opcoes = cenario_atual['opcoes']
        if len(opcoes) == 0:
            print()
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:
            print()
            print("Escolha sua opção:")
            print()
            for choice in opcoes:
                print("{0}: {1}".format(choice,opcoes[choice]))
                print()
            print()
            escolha = input("O que você quer fazer?: ")

            if escolha in opcoes:
                nome_cenario_atual = escolha
                if escolha == "biblioteca":
                    print("Você se deparou com um estoque infinito de três tipos de objetos.")
                    print()
                    print("Os objetos são: {0}".format(objetos))
                    print()
                    decisao=input("Você deseja pegar algum dos objetos? Caso afirmativo, digite sim: ")
                    while decisao=="sim":
                        print()
                        item=input("Qual?")
                        itens.append(item)
                        print("Item adicionado à sua sacola")
                        decisao=input("Você deseja pegar mais algum dos objetos? Caso afirmativo, digite sim: ")
                if escolha=="andar professor":
                    print()
                    if "lanterna" not in itens:
                        print()
                        print("O corredor está muito escuro, você precisa arranjar uma lanterna...")
                        print()
                        print("Você será redirecionado pelos seguranças ao saguão.")
                        nome_cenario_atual="inicio"
                if escolha=="professor":
                    print()
                    if "chave de fenda" and "clips" in itens:
                        print("Parabéns, você tem as ferramentas necessárias! Agora utilize seu clips e sua chave de fenda para conseguir destrancar a sala do professor.") 
                    else:
                        print("Você precisa de um clips e de uma chave de fenda para destrancar a sala do professor.")
                        print() 
                        print("Você será levado de volta ao saguão pelos seguranças.")
                        nome_cenario_atual="inicio"
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True

    print("Você morreu!")


# Programa principal.
if __name__ == "__main__":
    main()
