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
                "biblioteca": "Ir para a biblioteca",
                "sala mágica": "Tentar entrar na sala mágica",
                "sala transporte": "Tentar entrar na sala capaz de moldar dimensões e transportar matéria"
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
                "opcoes": {}},
        "sala mágica": {
                "titulo": "Salinha da magia",
                "descricao": "Voce está em um ambiente mágico, que libera super poderes de luta",
                "opcoes": {"inicio": "Voar para o saguão"} 
                },
        "sala transporte": {
                "titulo": "Transportador mágico",
                "descricao": "Voce está em um transportador inovador desenvolvido pelos alunos do Insper. Ele tem a capacidade de te levar para algumas salas secretas do Insper.",
                "opcoes": {"sala dos animais":"Tentar entrar na sala animal", "sala do mago": "tentar entrar na sala em que reside o grande mago do Insper", "sala secreta": "tentar entrar na sala desconhecida"}
                },
        "sala secreta": {
                "titulo": "Uma das três salas secretas Insper",
                "cor": "laranja",
                "descricao": "Quem dirá o que pode estar presente nesta sala...",
                "opcoes":{"inicio": "voltar ao saguão"}
                },
        "sala do mago": {
                "titulo": "Uma das três salas secretas Insper",
                "cor":"marrom",
                "descricao": "Quem dirá o que pode estar presente nesta sala...",
                "opcoes":{"inicio": "voltar ao saguão"}
                },
        "sala dos animais": {
                "titulo": "Uma das três salas secretas Insper",
                "cor":"amarelo",
                "descricao": "Quem dirá o que pode estar presente nesta sala...",
                "opcoes":{"inicio": "voltar ao saguão"}
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
    pontos_aluno={"hit points": 20, "pontos de ataque": 5,"pontos de defesa": 5}
    pontos_biblio={"hit points": 5, "pontos de ataque": 2,"pontos de defesa": 2}
    pontos_predador={"hit points": 8, "pontos de ataque": 3,"pontos de defesa": 3}
    objetos=["lanterna","chave de fenda", "clips"]
    game_over = False
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]
        
        print()
        print()
        print(cenario_atual["titulo"])
        trav="-"*len(cenario_atual["titulo"])
        print(trav)
        print(cenario_atual["descricao"])
        print()
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
            if cont==7:
                print()
                print("EASTER EGG: A cor da sala do mago é MARROM")
                print()
            elif cont==12:
                print()
                print ("EASTER EGG: A cor da sala dos animais é AMARELO")
                print()
            elif cont==17:
                print()
                print("EASTER EGG: A cor da sala secreta é LARANJA")
                print()
            for choice in opcoes:
                print("{0}: {1}".format(choice,opcoes[choice]))
                print()
            print()
            escolha = input("O que você quer fazer?: ")

            if escolha in opcoes:
                nome_cenario_atual = escolha
                opcoes = cenario_atual['opcoes']
                cenario_atual = cenarios[nome_cenario_atual]
                
                
                
                if escolha=="sala mágica":
                    cont+=1
                    if "clips" and "chave de fenda" in itens and cont%2!=0:
                        print()
                        print(cenario_atual["titulo"])
                        trav="-"*len(cenario_atual["titulo"])
                        print(trav)
                        print(cenario_atual["descricao"])
                        print()
                        print()
                        print("Bem vindo à sala mágica")
                        print("Você pode escolher receber hit points, pontos de ataque, ou pontos de defesa.")
                        d=input("Qual você quer? ")
                        if d=="hit points":
                            pontos_aluno["hit points"]+=5
                        elif d=="pontos de ataque":
                            pontos_aluno["pontos de ataque"]+=2
                        elif d=="pontos de defesa":
                            pontos_aluno["pontos de defesa"]+=2
                        elif d!="hit points" and d!="pontos de ataque" and d!="pontos de defesa":
                            print("A sala ficou brava que você não escreveu sua escolha da maneira correta e decidiu não te dar nada. Próxima vez escreva tudo de maneira simples, sem letra maiúscula, como está escrito na pergunta da sala!")
                    else:
                        print("A sala está fechada... tente de novo mais tarde. Não se esqueça de pegar a chave de fenda e o clips para abrir a sala!")
                
                
                
                elif escolha == "sala transporte":
                    cont+=1
                    nome_cenario_atual="sala transporte"
                    cenario_atual = cenarios[nome_cenario_atual]
                    opcoes = cenario_atual['opcoes']
                    if cont%2!=0:
                        print("Opsss.. sala fechada, desculpa... você será levado ao saguão.")
                        nome_cenario_atual="inicio"
                    print()
                    print("Bem vindo à estação")
                    print()
                    if cont%2==0:
                        print("Que sorte, a sala está funcionando!")
                        print()
                        for choice in opcoes:
                            print("{0}: {1}".format(choice,opcoes[choice]))
                            print()
                        lugar=input("Para qual lugar você deseja ser transportado?")
                        print()
                        print("Você será redirecionado ao lugar desejado, somente caso saiba adivinhar a cor da porta de entrada ao local que você deseja ir!")
                        color=input("Qual cor você adivinha?: ")
                        if color==cenarios[lugar]["cor"]:
                            print("Correto! Você será transportado.")
                            nome_cenario_atual=lugar
                            escolha=lugar
                        else:
                            print("Cor errada... você será transportado ao saguão")
                            nome_cenario_atual="inicio"
                                
                                
                                
                if escolha=="sala secreta":
                    print()
                    print("Bem-vindo à sala secreta")
                    print("Aqui é o único lugar em que você receberá uma carta que contém informações reveladoras sobre quebras de ética do professor. Com essa carta na sua sacola, e somente assim, você conseguirá adiar a entrega do seu EP.")
                    itens.append("Carta")
                    print()
                    print("Agora que você tem a carta, será redirecionado ao saguão")
                    nome_cenario_atual="inicio"
                    
                    
                
                if escolha=="sala dos animais": 
                    print()
                    print("Bem-vindo à sala dos animais")
                    print("Aqui reside um tigre e um leao, que podem talvez te ajudar.")
                    ani=input("Qual deles você quer que te ajude? escreva leao ou tigre para decidir: ")
                    if ani=="leao":
                        print("O nobre leão te dá dicas sobre como fazer o seu EP em 15 minutos!")
                        print("Assim, acaba de ser adicionado à sua sacola um EP prontinho para ser entregue!!!")
                        print("Agora você será direcionado ao saguão")
                        itens.append("EP")
                    elif ani=="tigre":
                        print("O feroz tigre ficou bravo que você quer burlar a data do EP, e comeu todos os itens de sua sacola...")
                        print("Você será direcionado ao saguão")
                    nome_cenario_atual="inicio"
                    
                
                
                if escolha=="sala do mago": 
                    print()
                    print("Bem-vindo à sala do grande mago do Insper.")
                    print()
                    numero_mago=2
                    num=int(input("Escolha um número entre 0 e 2, caso ele esteja certo, você receberá a ajuda do mago: "))
                    if numero_mago==num:
                        print("Parabéns, você acertou o número.")
                        print("O mago fez uma poção para você beber.")
                        deci=input("Você deseja bebê-la? sim ou nao?: ")
                        if deci=="sim":
                            print("Sábia escolha, o mago adicionou um EP à sua sacola, pode ir à sala do professor entregá-lo")
                            itens.append("EP")
                        if deci=="nao":
                            print("Que escolha ruim... você gastou tempo a toa.")
                    else:
                        print("Número errado...")
                    print()
                    print("Você será redirecionado ao saguão")
                    nome_cenario_atual="inicio"
                                    #COLOCAR UM JEITO DELE GANHART NO PROFESSOR
                                    
                                    
                                    
                elif escolha == "biblioteca":
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
                                    print('Parabéns!!! Você ganhou, com direito à um aumento de pontos de defesa! Pode prosseguir.')
                                    xal=[0,0,pontos_biblio['pontos de defesa']-1]
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
                            elif pontos_aluno['hit points']<pontos_biblio['hit points']:
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
                            elif pontos_aluno['hit points']==pontos_biblio['hit points']:
                                print('Que sorte... vocês empataram. Pode prosseguir.')
                            pontos_aluno["hit points"]+=xal[0]
                            pontos_aluno["pontos de ataque"]+=xal[1]
                            pontos_aluno["pontos de defesa"]+=xal[2]
                            pontos_biblio["hit points"]+=xbib[0]
                            pontos_biblio["pontos de ataque"]+=xbib[1]
                            pontos_biblio["pontos de defesa"]+=xbib[2]
                        elif decision=='fugir':
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
                        if cont%2==0:
                            print ("Você encontrou o anjo do elevador, ele te dará 3 hitpoints, dois pontos de ataque, e um de defesa!!!!!!")
                            pontos_aluno["hit points"]+=3
                            pontos_aluno["pontos de ataque"]+=2
                            pontos_aluno["pontos de defesa"]+=1
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
                            print ('Predador: {0}'.format(pontos_predador))
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
                                elif pontos_aluno['hit points']<pontos_predador['hit points']:
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
                                elif pontos_aluno['hit points']==pontos_predador['hit points']:
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
                            elif dec=='fugir':
                                print('Oooopa, olha só que marica')
                                print('Você foi jogado pelo predador ao saguão')
                                nome_cenario_atual="inicio"
                                cenario_atual = cenarios[nome_cenario_atual]
                                opcoes = cenario_atual['opcoes']
                        else:
                            nome_cenario_atual="andar professor"
                            cenario_atual = cenarios[nome_cenario_atual]
                            opcoes = cenario_atual['opcoes']
                    if "lanterna" not in itens and nome_cenario_atual=="andar professor":
                        print()
                        print("O corredor está muito escuro, você precisa arranjar uma lanterna...")
                        print()
                        print("Você será redirecionado pelos seguranças ao saguão.")
                        nome_cenario_atual="inicio"
                
                
                
                elif escolha=="professor": #consertar opcoes mwomwo
                    cont+=1
                    print()
                    if "chave de fenda" and "clips" in itens:
                        print("Parabéns, você tem as ferramentas necessárias! Agora utilize seu clips e sua chave de fenda para conseguir destrancar a sala do professor.") 
                        if "EP" and "Carta" not in itens:
                            print("Você tem certeza que você quer entrar agora? Ele está bem bravo e você está de mãos abanando.")
                            decisa=input("O que você quer fazer? fugir ou entrar?: ")
                            if decisa=="fugir":
                                print("Você será redirecionado ao saguão.")
                                nome_cenario_atual="inicio"
                        if "EP" in itens:
                            print("Professor-- Olá!!! Você veio entregar seu EP? Pode deixar ele na minha mesa. Boa tarde.")
                            game_over=True
                        if "Carta" in itens:
                            print("Professor--Você está maluco??? Daonde você tem essa carta?")
                            print("Ok, vou lhe conceder uma extensão, mas isso quer dizer que você será pra sempre o meu aluno mais odiado")
                            decis=input("Você quer aceitar a extensão? sim ou nao?: ")
                            if decis=="sim":
                                print("Professor-- essas crianças de hoje em dia não dá. Vá embora e faça seu trabalho")
                                game_over=True
                            if decis=="nao":
                                print("Professor-- Você pode não ter um EP, mas tem meu respeito. Relaxa, é só 20% da nota!")
                                game_over=True
                    else:
                        print("Você precisa de um clips e de uma chave de fenda para destrancar a sala do professor.")
                        print() 
                        print("Você será levado de volta ao saguão pelos seguranças.")
                        nome_cenario_atual="inicio"
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True
    print()
    print("Você está na parte de fora do Insper. Vá para casa!")
    print()
    print("Busca pelo EP=finalizada")


# Programa principal.
if __name__ == "__main__":
    main()
