# EP 2019-1: Escape Insper
#
# Alunos: 
# - Aluno A: Jonathan Mansur, jonathanm1@al.insper.edu.br
# - Aluno B: Gabriel Mauricio Kabbani, gabrielmk@al.insper.edu.br 

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
        },
        "elevador": {
                "titulo": "Elevador Schindler",
                "descricao": "Você está no elevador",
                "opcoes": {}
        },
        "escada": {
                "titulo": "Escadeiras",
                "descricao": "Você está nas escadas",
                "opcoes": {}}
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
    pontos_aluno={"hit points": 20, "pontos de ataque": 5,"pontos de defesa": 5}
    pontos_biblio={"hit points": 5, "pontos de ataque": 2,"pontos de defesa": 2}
    pontos_predador={"hit points": 3, "pontos de ataque": 7,"pontos de defesa": 7}
    objetos=["lanterna","chave de fenda", "clips"]
    game_over = False
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]
        
        print()
        print(cenario_atual["titulo"])
        trav="-"*len(cenario_atual["titulo"])
        print(trav)
        print(cenario_atual["descricao"])
        print()

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
                    print()
                    print("Caverna da tranquilidade")
                    t="-"*len("caverna da tranquilidade")
                    print(t)
                    print("Você está na biblioteca")
                    print()
                    cont+=1
                    xal=[0,0,0]
                    xbib=[0,0,0]
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
                    if cont%2==0:
                        print ('Você se deparou com a bibliotecária do mal!')
                        print('Ela pode te aremessar livros, diminuindo os itens de sua sacola')
                        print()
                        print ('Você: {0}'.format(pontos_aluno))
                        print ('Bibliotecária: {0}'.format(pontos_biblio))
                        decision=input('O que você deseja fazer? lutar ou fugir?: ')
                        if decision=='lutar':
                            if pontos_aluno['hit points']>pontos_biblio['hit points']:

                                if pontos_aluno['pontos de ataque']>pontos_biblio['pontos de defesa']:
                                    print('Parabéns!!! Você ganhou, com direito à um aumento de pontos de ataque! Pode prosseguir.')
                                    xal=[0,pontos_biblio['pontos de defesa'],0]
                                    xbib=[0,-2,-1]
                                elif pontos_aluno['pontos de ataque']<pontos_biblio['pontos de defesa']:
                                    print('OOOPSSSS, VOCÊ PERDEU')
                                    print('Você perdeu um ponto de ataque, e o último item que você pegou...')
                                    xal=[0,-1,0]
                                    if len(itens)>0:
                                        del itens[-1]
                                elif pontos_aluno['pontos de ataque']==pontos_biblio['pontos de defesa']:
                                    print('Que sorte, o combate empatou... Você não perdeu nada!')
                                pontos_aluno['hit points']-=2
                            if pontos_aluno['hit points']<pontos_biblio['hit points']:
                                if pontos_aluno['pontos de defesa']>pontos_biblio['pontos de ataque']:
                                    print('Parabéns!!! Você se defendeu! Pode prosseguir.')
                                    print('Você ganhou um ponto de defesa')
                                    xal=[0,0,1]
                                elif pontos_aluno['pontos de defesa']<pontos_biblio['pontos de ataque']:
                                    print('OOOPSSSS, VOCÊ PERDEU')
                                    print('Você perdeu um ponto de defesa, e o último item que você pegou (caso tenha)...')
                                    if len(itens)>0:
                                        del itens[-1]
                                    xal[0,0,-1]
                                elif pontos_aluno['pontos de defesa']==pontos_biblio['pontos de ataque']:
                                    print('Que sorte, o combate empatou... Você não perdeu nada!')
                                pontos_biblio['hit points']-=2
                            if pontos_aluno['hit points']==pontos_biblio['hit points']:
                                print('Que sorte... vocês empataram. Pode prosseguir.')
                            pontos_aluno["hit points"]+=xal[0]
                            pontos_aluno["pontos de ataque"]+=xal[1]
                            pontos_aluno["pontos de defesa"]+=xal[2]
                            pontos_biblio["hit points"]+=xbib[0]
                            pontos_biblio["pontos de ataque"]+=xbib[1]
                            pontos_biblio["pontos de defesa"]+=xbib[2]
                        if decision=='fugir':
                            print('Ihhhh arregão')
                            print('Você foi jogado pela bibliotecária ao saguão')
                            nome_cenario_atual="inicio"
                                    
                elif escolha=="andar professor":
                    cont+=1
                    xal=[0,0,0]
                    xpred=[0,0,0]
                    print()
                    ele_esc=input('Você pode ir de escada ou de elevador, qual você prefere?: ')
                    if ele_esc!="elevador" and ele_esc!="escada":
                        ele_esc=input('Você deve escrever elevador ou escada, para declarar a sua escolha. Qual você escolhe?: ')
                    elif ele_esc=="elevador":
                        nome_cenario_atual="elevador"
                        cenario_atual = cenarios[nome_cenario_atual]
                        opcoes = cenario_atual['opcoes']
                        print()
                        print(cenario_atual["titulo"])
                        trav="-"*len(cenario_atual["titulo"])
                        print(trav)
                        print(cenario_atual["descricao"])
                        print()
                        nome_cenario_atual="andar professor"
                        cenario_atual = cenarios[nome_cenario_atual]
                        opcoes = cenario_atual['opcoes']
                    elif ele_esc=="escada":
                        nome_cenario_atual="escada"
                        cenario_atual = cenarios[nome_cenario_atual]
                        opcoes = cenario_atual['opcoes']
                        print()
                        print(cenario_atual["titulo"])
                        trav="-"*len(cenario_atual["titulo"])
                        print(trav)
                        print(cenario_atual["descricao"])
                        print()
                        if cont%2==0:
                            print()
                            print ('Você se deparou com o predador!')
                            print('Ele pode comer as coisas que você tem, diminuindo os itens de sua sacola')
                            print()
                            print ('Você: {0}'.format(pontos_aluno))
                            print ('Predador: {0}'.format(pontos_biblio))
                            dec=input('O que você deseja fazer? lutar ou fugir?: ')
                            if dec=='lutar':
                                if pontos_aluno['hit points']>pontos_predador['hit points']:
                                    if pontos_aluno['pontos de ataque']>pontos_predador['pontos de defesa']:
                                        print('Parabéns!!! Você ganhou! Pode prosseguir.')
                                        xal=[0,pontos_predador['pontos de defesa'],0]
                                        xpred=[0,-2,-1]
                                        nome_cenario_atual="andar professor"
                                        cenario_atual = cenarios[nome_cenario_atual]
                                        opcoes = cenario_atual['opcoes']
                                    #PORQUE QUE ELE TA ENTRANDO NESSE ELIF MSM QDO ERA PRO CARA GANHAR!!!!!!!!!!!!!!!!!!!!!!!!!!
                                    elif pontos_aluno['pontos de ataque']<pontos_predador['pontos de defesa']:
                                        print('OOOPSSSS, VOCÊ PERDEU')
                                        print('Você perdeu um ponto de ataque, e o último item que você pegou...')
                                        nome_cenario_atual="inicio"
                                        cenario_atual = cenarios[nome_cenario_atual]
                                        opcoes = cenario_atual['opcoes']
                                        xal=[0,-1,0]
                                        if len(itens)>0:
                                            del itens[-1]
                                    elif pontos_aluno['pontos de ataque']==pontos_predador['pontos de defesa']:
                                        print('Que sorte, o combate empatou... Você não perdeu nada!')
                                        nome_cenario_atual="andar professor"
                                        cenario_atual = cenarios[nome_cenario_atual]
                                        opcoes = cenario_atual['opcoes']
                                    pontos_aluno['hit points']-=2
                                if pontos_aluno['hit points']<pontos_predador['hit points']:
                                    if pontos_aluno['pontos de defesa']>pontos_predador['pontos de ataque']:
                                        print('Parabéns!!! Você se defendeu! Pode prosseguir.')
                                        nome_cenario_atual="andar professor"    
                                        cenario_atual = cenarios[nome_cenario_atual]
                                        opcoes = cenario_atual['opcoes']
                                    elif pontos_aluno['pontos de defesa']<pontos_predador['pontos de ataque']:
                                        print('OOOPSSSS, VOCÊ PERDEU')
                                        print('Você perdeu um ponto de defesa, e o último item que você pegou (caso tenha)...')
                                        print("Você será redirecionado ao saguão")
                                        pontos_aluno['pontos de defesa']-=1
                                        nome_cenario_atual="inicio"
                                        cenario_atual = cenarios[nome_cenario_atual]
                                        opcoes = cenario_atual['opcoes']
                                        xal=[0,0,-1]
                                        if len(itens)>0:
                                            del itens[-1]
                                    elif pontos_aluno['pontos de defesa']==pontos_predador['pontos de ataque']:
                                        print('Que sorte, o combate empatou... Você não perdeu nada!')
                                        nome_cenario_atual="andar professor"
                                        cenario_atual = cenarios[nome_cenario_atual]
                                        opcoes = cenario_atual['opcoes']
                                    pontos_predador['hit points']-=2
                                if pontos_aluno['hit points']==pontos_predador['hit points']:
                                    print('Que sorte... vocês empataram. Pode prosseguir.')
                                    nome_cenario_atual="andar professor"
                                    cenario_atual = cenarios[nome_cenario_atual]
                                    opcoes = cenario_atual['opcoes']
                                pontos_aluno["hit points"]+=xal[0]
                                pontos_aluno["pontos de ataque"]+=xal[1]
                                pontos_aluno["pontos de defesa"]+=xal[2]
                                pontos_predador["hit points"]+=xpred[0]
                                pontos_predador["pontos de ataque"]+=xpred[1]
                                pontos_predador["pontos de defesa"]+=xpred[2]
                            if dec=='fugir':
                                print('Oooopa, olha só que marica')
                                print('Você foi jogado pelo predador ao saguão')
                                nome_cenario_atual="inicio"
                                cenario_atual = cenarios[nome_cenario_atual]
                                opcoes = cenario_atual['opcoes']
                        else:
                            nome_cenario_atual="andar professor"
                            cenario_atual = cenarios[nome_cenario_atual]
                            opcoes = cenario_atual['opcoes']
                        #nao esquecer de re-alterar para o andar professor dps.
                    if "lanterna" not in itens and nome_cenario_atual=="andar professor":
                        print()
                        print("O corredor está muito escuro, você precisa arranjar uma lanterna...")
                        print()
                        print("Você será redirecionado pelos seguranças ao saguão.")
                        nome_cenario_atual="inicio"
                elif escolha=="professor":
                    cont+=1
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
