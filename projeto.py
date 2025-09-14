geral = ["INICIO"]
prioridade = ["INICIO"]


def menu():
    print(f"\nMenu principal:")
    print(f"1 - Para adicionar cliente:")
    print(f"2 - para atender o cliente:")
    print(f"3 - para ver as filas:")
    print(f"4 - relatorio das listas")
    print(f"5 - para sair do menu:")
    volta = int(input(f"DIGITE AQUI: "))
    if volta == 1:
        adicionar()
    elif volta == 2:
       atender()
    elif volta == 3:
        verlistas()
    elif volta == 4:
        relatorio()
    elif volta == 5:
        print(f"obrigado por usar o nosso sistema!")



def adicionar():
    print("\naqui para adicionar cliente:")
    nome = str(input("ESCREVA O SEU NOME AQUI: "))
    idade = int(input("DIGITE A SUA IDADE AQUI: "))
    gestantes = bool(input("VOÇê É GESTANTE( SE NÃO FOR DEIXE EM BRANCO): "))
    pcd = bool(input("TEM ALGUMA DEFICIENICA( SE NÃO TIVER DEIXE EM BRANCO )\n"))
    
    if (60 <= idade) or (gestantes == True) or (pcd == True):
        prioridade.append(nome)
        numero = prioridade.index(nome)
        print(F"Essa é a sua posição na fila de PRIORIDADE: {numero}\n{prioridade} ")
        resp = int(input("Quer voltar para o menu:\n1 - para voltar\n2 - para sair\nDIGITE AQUI: "))
        if resp == 1:
            menu()
        else :    
            print("obrigado por usar o nosso sistema!")

    else :
        geral.append(nome)
        numero = geral.index(nome)
        print(f"Essa é a sua posição na fila GERAL: {numero}\n{geral}")
        resp = int(input("Quer voltar para o menu:\n1 - para voltar\n2 - para sair\nDIGITE AQUI: "))
        if resp == 1:
            menu()
        else :    
            print("obrigado por usar o nosso sistema!")



def atender():
    print("\nde atendiento ao cliente:")
    print("1 - para atender a fila geral:")
    print("2 - para atender a fila de prioridade:")
    print("3 - para voltar ao menu:")
    volta = int(input("AQUI: "))
    if volta == 1:
            ret = int(input("qual o numero dessa pessoa: "))
            geral.pop(ret)
            print(f"essa é a nova fila {geral}")
            resp = int(input("Quer voltar para o menu:\n1 - para voltar\n2 - para sair\nDIGITE AQUI: "))
            if resp == 1:
                menu()
            else :    
                print("obrigado por usar o nosso sistema!")

    elif volta == 2:
        ret = int(input("qual o numero dessa pessoa: "))
        prioridade.pop(ret)
        print(f"essa é a nova fila {prioridade}")
        resp = int(input("Quer voltar para o menu:\n1 - para voltar\n2 - para sair\nDIGITE AQUI: "))
        if resp == 1:
            menu()
        else :    
            print("obrigado por usar o nosso sistema!")

    elif volta == 3:
        menu()


def verlistas():
    print("\nEssa opção serve so para ver as listas: ")
    print(f"essa é a fila geral {geral}: ")
    print(f"essa é a fila de prioridade {prioridade}: ")
    resp = int(input("Quer voltar para o menu:\n1 - para voltar\n2 - para sair\nDIGITE AQUI: "))
    if resp == 1:
            menu()
    else :    
            print("obrigado por usar o nosso sistema!")


def relatorio():
    print(f"\nqual relatorio deve ser imprimido:")
    print(f"1 - para a fila geral:")
    print(f"2 - para a fila de prioridade:")
    print(f"3 - para voltar ao menu:")
    volt = int(input("AQUI: "))
    if volt == 1:
        relatgeral()
    elif volt == 2:
        relatprioridade()
    elif volt == 3:
        menu()
        

def relatgeral():

    lista_antiga = ["INICIO"]

    geral

    set_antiga = set(lista_antiga)
    set_nova = set(geral)

    itens_removidos = set_antiga - set_nova

    itens_adicionados = set_nova - set_antiga

    porcentagem_saida = (len(itens_removidos) / len(lista_antiga)) * 100
    porcentagem_entrada = (len(itens_adicionados) / len(lista_antiga)) * 100


    print("Relatorio da fila geral:")
    print(f"- Total original: {len(lista_antiga)} itens")
    print(f"- Itens removidos: {len(itens_removidos)} ({porcentagem_saida:.2f}%) → {list(itens_removidos)}")
    print(f"- Itens adicionados: {len(itens_adicionados)} ({porcentagem_entrada:.2f}%) → {list(itens_adicionados)}\n")
    resp = int(input("Quer voltar para o menu:\n1 - para voltar\n2 - para sair\nDIGITE AQUI: "))
    if resp == 1:
        menu()
    else :    
        print("obrigado por usar o nosso sistema!")






def relatprioridade():
    lista_antiga = ["INICIO"]

    prioridade

    set_antiga = set(lista_antiga)
    set_nova = set(prioridade)

    itens_removidos = set_antiga - set_nova

    itens_adicionados = set_nova - set_antiga

    porcentagem_saida = (len(itens_removidos) / len(lista_antiga)) * 100
    porcentagem_entrada = (len(itens_adicionados) / len(lista_antiga)) * 100

    print("Relatorio da fila de prioridade:")
    print(f"- Total original: {len(lista_antiga)} itens")
    print(f"- Itens removidos: {len(itens_removidos)} ({porcentagem_saida:.2f}%) → {list(itens_removidos)}")
    print(f"- Itens adicionados: {len(itens_adicionados)} ({porcentagem_entrada:.2f}%) → {list(itens_adicionados)}\n")
    resp = int(input("Quer voltar para o menu:\n1 - para voltar\n2 - para sair\nDIGITE AQUI: "))
    if resp == 1:
        menu()
    else :    
        print("obrigado por usar o nosso sistema!")





menu()
