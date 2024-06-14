
while True:
    # Dupla: José Victor Cirilo Guedes e Júlia Etiene
    from cinema import *
    import cinema
    import cliente
    import adm
    import matplotlib.pyplot as plt
    from win10toast import ToastNotifier

    login = {'1': '1'}
    contadorlogin = 0
    loginadm = {'1': '1'}
    contadorloginadm = 0
    filmes = [[1, 'homem aranha', 60, '1', '12', 'Aventura', 'Após ser atingido por uma teia radioativa, Miles Morales, um jovem negro do Brooklyn, se torna o Homem-Aranha, inspirado no legado do já falecido Peter Parker\n', 0, 0], [2, 'Star Wars', 50, '2', '12', 'sci-fi',  'A princesa Leia é mantida refém pelas forças imperiais comandadas por Darth Vader. Luke Skywalker e o capitão Han Solo precisam libertá-la e restaurar a liberdade e a justiça na galáxia.', 0, 0]]
    contadorcriaçaoadm = 0
    faturamento = 0
    nome_cinema = 'Cine Mania'
    codigo_adm = '405061'
    historico = []
    valordoid = []
    aux = 0
    repeti = 0
    resultado = 0
    faturamentt = [0]
    id_feedback = 999999999
    lista_controle = [1]
    cinema.ativar_voz()
    while True:
        cinema.menu_usuario(nome_cinema)
        escolha = input(Fore.LIGHTWHITE_EX + 'Digite opção desejada:')
        quebrar = False
        tirar = False
        slash = False
        if (escolha == '1'):
            cinema.instrucao()
        elif (escolha == '2'):  # listar filmes e curtir
            cliente.contadordecurtida(filmes, id_feedback)
        while escolha == '3':  # USUARIO JÁ CADASTRADO
            if quebrar == True:
                break
            cinema.falar('Digite seu ID')
            idlogin = input(Fore.LIGHTWHITE_EX + 'Digite seu ID:')
            cinema.falar('Digite sua senha')
            senha = input('Digite sua senha:')
            if cliente.logar_menucliente(login, idlogin, senha):
                print('\nLogin Efetuado!\n')
                cinema.falar('Login efetuado')
                while True:
                    cliente.menu_cliente(idlogin, nome_cinema)
                    breaker = False
                    cinema.falar('Digite a opção desejada')
                    escolha2 = input(Fore.LIGHTWHITE_EX + 'Digite opção desejada:')  # COMPRAR INGRESSOS
                    if escolha2 == '1':
                        print(Fore.LIGHTWHITE_EX + '\n---------------- CATALAGO -------------------')
                        cinema.falar('Segue filmes disponiveis em nosso catalago')
                        for i in filmes:
                            print(Fore.LIGHTCYAN_EX + f'ID do filme: [{i[0]}] ')
                            print(f'Nome do filme: {i[1]}')
                            print(f'Numero da Sala: {i[3]}')
                            print(f'Valor do Ingresso: {i[2]}')
                            print(Fore.LIGHTWHITE_EX + '-------------------------------')
                            idn = i[0]
                            valordoid.append(idn)
                        print('-----------------------------------------\n')
                        cinema.falar('Digite o ID do filme')
                        ticket = int(input(Fore.LIGHTWHITE_EX + 'Digite o ID do filme:'))
                        cinema.falar('Digite a quantidade de ingressos desejado')
                        ticketValor = int(input(Fore.LIGHTWHITE_EX + 'Digite a quantidade de ingressos:'))
                        if ticketValor <= 4:
                            cliente.compra_de_ingressos(ticket, ticketValor, aux, resultado, filmes, historico, breaker,faturamentt)
                        else:
                            print('\nVoce digitou um numero muito alto, Tente novamente!\n')
                    elif escolha2 == '2':
                        idcliente = ''
                        novasenha = ''
                        if cliente.mudaca_senhacliente2(login, idcliente, novasenha):
                            print(Fore.LIGHTGREEN_EX + '\nSenha alterada\n')
                            cinema.falar('Senha alterada')
                        else:
                            print(Fore.LIGHTRED_EX + '\vTente novamente\n')
                            cinema.falar('Tente novamente')
                    elif (escolha2 == '3'):
                        cliente.ver_historico(historico)
                    elif (escolha2 == '4'):
                        cliente.listar_filmesCliente(filmes)
                    elif (escolha2 == '6'):
                        cinema.configurar_sistema()
                    elif (escolha2 == '7'):
                        print(Fore.LIGHTWHITE_EX + '\nVocê foi Deslogado...\n')
                        cinema.falar('Você foi deslogado')
                        quebrar = True
                        break
                    elif (escolha2 == '5'):
                        cliente.listar_TXT(historico)
            else:
                print(Fore.LIGHTWHITE_EX + '\n-------------------------------------------------------------------')
                print(Fore.LIGHTRED_EX + '\n|  Seu Login não existe, ou senha ou ID do Usuario estão errados  |\n')
                print(Fore.LIGHTWHITE_EX + '-------------------------------------------------------------------')
                cinema.falar('Seu login não existe, senha ou ID do usuario estão incorretos')
                break

        while (escolha == '4'):  # FAZER CADASTRO
            contadorcriaçao = 1
            contadorcriaçao -= 1
            cinema.menu_cadastro()
            slash = False
            cinema.falar('Digite a opção desejada')
            op = input(Fore.LIGHTWHITE_EX + '\nDigite opção desejada:\n')
            if (op == '1'):
                cinema.definir_login_clienteEadm(login, '1', contadorcriaçao, codigo_adm, loginadm)
                break
            elif (op == '3'):  # SAIR DO MENU DE ESCOLHA DE LOGIN
                cinema.definir_login_clienteEadm(login, '3', contadorcriaçao, codigo_adm, loginadm)
                break
            elif (op == '2'):  # CADASTRO ADM
                cinema.definir_login_clienteEadm(login, '2', contadorcriaçao, codigo_adm, loginadm)
                break
        while escolha == '5':
            if slash == True:
                break
            cinema.falar('Informe seu usuario administrador')
            usuarioadm = input(Fore.LIGHTWHITE_EX + 'Informe seu Usuario ADM')
            cinema.falar('Informe sua senha administrador')
            senhaadm = input(Fore.LIGHTWHITE_EX + 'Informe sua Senha ADM')
            if adm.logar_menuadm(loginadm, usuarioadm, senhaadm):
                print(Fore.LIGHTGREEN_EX + '\nLogin Efetuado!\n')
                cinema.falar('Login efetuado com sucesso')
                while (True):
                    if (slash == True):
                        break
                    adm.menu_adm()
                    cinema.falar('Digite a opção desejada')
                    opcao = input(Fore.LIGHTWHITE_EX + 'Digite a opção desejada:')
                    if (opcao == '1'):  # ADICIONAR NA LISTA FILMES OUTRA LISTA COM MAIS FILMES E EDITAR CASO FOR PRECISO
                        cinema.adicionar_filme(filmes)
                    elif (opcao == '2'):  # EDITAR FILME
                        adm.editar_filme(filmes)
                    elif (opcao == '3'):  # FATURAMENTO
                        adm.faturamento(faturamentt)
                    elif (opcao == '4'):  # LISTAR USUARIOS
                        adm.listar_usuarios(loginadm)
                    elif (opcao == '5'):
                        cinema.falar('Informe o novo nome')
                        nome_cinema = input('Informe o novo nome:')
                        print(Fore.LIGHTGREEN_EX + '\nAlteracao Concluida!\n')
                        cinema.falar('alteração concluida')
                    elif (opcao == '6'):  # ALTERAR SENHA PADRAO
                        cinema.falar('Informe a nova senha do sistema')
                        codigo_adm = input(Fore.LIGHTWHITE_EX + 'Informe a Nova senha do sistema:')
                        print(Fore.LIGHTGREEN_EX + '\nAlteracao Concluida! Voce será deslogado por motivos de segurança...\n')
                        cinema.falar('Alteração concluida, você sera deslogado por motivos de segurança')
                        slash = True
                    elif (opcao == '7'):  # LISTAR FILMES E REMOVER POR ID
                        adm.remover_filme(filmes)
                    elif (opcao == '8'):  # PROCURAR FILMES
                        adm.procurar_filme(filmes)
                    elif (opcao == '9'):
                        adm.estatisticas(filmes)
                    elif (opcao == '10'):
                        adm.historico_adm(historico)
                    elif (opcao == '11'):
                        adm.historico_especificar(historico)
                    elif (opcao == '12'):
                        adm.historico_TXT_adm(historico)
                    elif (opcao == '13'):  # configuração do sistema para n precisar ir no menu principal para desativar a voz da mulher
                        cinema.configurar_sistema()
                    elif (opcao == '0'):  # SAIR
                        print(Fore.LIGHTWHITE_EX + '\n Voce foi Deslogado...\n')
                        cinema.falar('Você foi deslogado')
                        slash = True
            else:
                print(Fore.LIGHTWHITE_EX + '\n-------------------------------------------------------------------')
                print(Fore.LIGHTRED_EX + '\n|  Seu Login não existe, ou senha ou ID do Usuario estão errados  |\n')
                print(Fore.LIGHTWHITE_EX + '-------------------------------------------------------------------')
                cinema.falar('Seu login não existe, senha ou ID de usuario estão incorretos')
                break

        if (escolha == '6'):
            cinema.configurar_sistema()

        if (escolha == '7'):  # SAIR DO PROGRAMA
            print(Fore.LIGHTWHITE_EX + 'Até mais ;)')
            cinema.falar('Vejo você em breve...')
            break