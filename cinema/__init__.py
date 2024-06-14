from colorama import init, Fore, Back, Style
import pyttsx3
controle = 1
lista_controle = [1]
def menu_usuario(nome_cinema):
    print(Fore.LIGHTWHITE_EX + '---------MENU------------------------------------------')
    print(Fore.LIGHTYELLOW_EX + f'Olá, seja bem-vindos ao {nome_cinema}')
    print(f'Primeira vez aqui? Faça o cadastro agora!')
    print(f'Já tem conta no {nome_cinema}? Faça o login agora!')
    print(Fore.LIGHTWHITE_EX + '-------------------------------------------------------')
    print(Fore.LIGHTCYAN_EX + '[1.]--> INSTRUÇÕES PARA NOVATOS.')#OK
    print('[2.]--> VER FILMES DISPONIVEIS.') # OK
    print('[3.]--> FAZER LOGIN.') #OK
    print('[4.]--> CRIAR CADASTRO.')# OK
    print('[5.]--> FAZER LOGIN ADM') #OK
    print('[6.]--> CONFIGURAÇÕES DO SISTEMA') # OK
    print('[7.]--> SAIR')
    falar(f"Olá, seja bem-vindos ao {nome_cinema}")
    falar(f'Para começar, Faça o cadastro agora!')
    falar(f'Caso já tenha conta no {nome_cinema} Faça o login agora!')
    falar('DIGITE A OPÇÃO DESEJADA PARA CONTINUAR:')
    falar('[1.] PARA INSTRUÇÕES PARA NOVATOS.')
    falar('[2.] PARA VER FILMES DISPONIVEIS.')
    falar('[3.] PARA FAZER LOGIN.')
    falar('[4.] PARA CRIAR CADASTRO.')
    falar('[5.] PARA FAZER LOGIN ADM')
    falar('[6.] PARA IR EM CONFIGURAÇÕES DO SISTEMA')
    falar('[7.] PARA SAIR DO PROGRAMA')
    print(Fore.LIGHTWHITE_EX + '\n------------------------------------------------------')

def instrucao():
    print(Fore.LIGHTWHITE_EX +'-----------------------------------------------------------------------------------------------------------------------------------------------@')
    print(Fore.LIGHTCYAN_EX + '\n[1]= Interessado em algum filme? faça um Cadastro apertando o numero 2, no MENU Principal.                                                     |')
    print('\n[2]= Em seguida preencha o Login com as informações criadas no Cadastro, aperte o numero 1 para efetuar o Login.                               |')
    print('\n[3]= Com isso, abrirá um MENU CLIENTE, diante disso, terá 4 opções:"Compras de Ingressos/ Mudar Senha/ Ver filmes Disponiveis/ Sair".          |')
    print('\n[4]= Na Opção "Compra de Ingressos", terá uma listagem de filmes para escolher, numeros de ingressos a serem pagos e escolha de assentos.      |')
    print('\n[5]= Na Opção "Mudar Senha", voce poderá trocar sua senha manualmente colocando seu Id Usuario e em seguida uma nova senha.                    |')
    print('\n[6]= Na Opção "Ver Filmes Disponiveis", exibirá todos os filmes do catalogo.                                                                   |')
    print('\n[7]= Na Opção "Sair", voce será deslogado do MENU CLIENTE.                                                                                     |')
    print(Fore.LIGHTWHITE_EX +'\n-----------------------------------------------------------------------------------------------------------------------------------------------@')
    falar("Estamos felizes de está conosco! Segue a seguir as instruções rapidas de utilização do nosso software.")
    falar('Caso tenha interesse em algum filme, faça um Cadastro apertando o numero 2, no MENU Principal')
    falar('Em seguida preencha o Login com as informações criadas no Cadastro, e aperte o numero 1 para efetuar o Login.')
    falar('Com isso, abrirá um MENU CLIENTE, onde você pode gerenciar sua conta e comprar os filmes')
    falar('Na Opção "Compra de Ingressos", terá uma listagem de filmes para escolher, numeros de ingressos a serem pagos e escolha de assentos.')
    falar('Na Opção "Mudar Senha", você poderá trocar sua senha manualmente colocando seu Id Usuario e em seguida uma nova senha.')
    falar('Na Opção "Ver Filmes Disponiveis", exibirá todos os filmes do catalogo.')
    falar('Esperamos que você se divirta, qualquer informação a parti, entre em contato com nosso suporte, boas compras!')
def adicionar_filme(filmes):
    import random
    IDs = random.randint(3, 50)
    nome_do_filme = input(Fore.LIGHTWHITE_EX + 'Digite o nome do filme:')
    valorIngresso = float(input('Digite o valor do ingresso:'))
    Sala_filme = input('Digite a sala que vai ocorrer esse filme:')
    Classificação = input('Digite a classificação indicativa desse filme:')
    sinopse = input('Adicione a sinopse aqui:')
    Genero = input('Digite o Genero desse filme:')
    filme = [IDs, nome_do_filme, valorIngresso, Sala_filme, Classificação, Genero, sinopse, 0, 0]
    filmes.append(filme)
    print(Fore.LIGHTWHITE_EX + '-------------------------------------- Informações digitadas ---------------------------------------')
    print(Fore.LIGHTCYAN_EX + f'ID:{IDs}, Nome do filme: {nome_do_filme}, Valor do ingresso {valorIngresso},Sala do filme: {Sala_filme}')
    print(f'Classificação:{Classificação}, Sinopse:{sinopse}, Gênero:{Genero}, Curtida: 0')
    print(Fore.LIGHTWHITE_EX + '-----------------------------------------------------------------------------------------------------')
    falar('INFORMAÇÕES DIGITADAS')
    falar(f'O ID É{IDs}, {nome_do_filme}, Valor do ingresso É {valorIngresso},Sala do filme É {Sala_filme}, A Classificação INDICARIVA É {Classificação}, A Sinopse É  :{sinopse}, O Gênero É{Genero} E O NUMERO DE Curtida É 0')
def definir_login_clienteEadm(login, opinar, contadorcriaçao, codigo_adm, loginadm):
    if (opinar == '1'):
        falar('CRIE UM ID DE USUARIO')
        idlogin1 = input(Fore.LIGHTWHITE_EX + 'Crie um ID de Usuario:')
        falar('CRIE UMA SENHA PARA O USUARIO')
        senha = input('Crie uma senha:')
        for rep in login:
            if (idlogin1 == rep):
                contadorcriaçao += 1
                while(contadorcriaçao == 1):
                    print(Fore.LIGHTRED_EX + '\nID de usuario já existe, tente cadastrar outro login\n')
                    falar('ID DE USUARIO, JÁ EXISTE, TENTE NOVAMENTE COM OUTRO LOGIN')
                    break
        if (contadorcriaçao == 0):
            idlogin = idlogin1  # SE O CADASTRO DẼ CERTO, ELE VAI PARA O PRIMEIRO MENU
            login[idlogin] = senha
            print(Fore.LIGHTGREEN_EX + '\nCriação de Login bem sucedida!\n')
            falar('CRIAÇÃO DE LOGIN BEM SUCEDIDA')
            print(Fore.LIGHTWHITE_EX + f'Seu login é {idlogin}')
            print(Fore.LIGHTWHITE_EX + f'Sua senha é {senha}')

    elif (opinar == '3'):  # SAIR DO MENU DE ESCOLHA DE LOGIN
        print(Fore.LIGHTWHITE_EX + '\n---Você Saiu---\n')
        falar('Você saiu')
    elif(opinar == '2'):  # CADASTRO ADM
        contadorcriaçaoadm = 0
        falar('DIGITE A SENHA PADRÃO CONTIDA NO MANUAL DO SOFTWARE')
        codigosecreto = input(Fore.LIGHTWHITE_EX + 'Digite a senha padrão contida no manual do software:')
        if (codigosecreto == codigo_adm):
            falar('CRIE UM NOME DE USUARIO ADMINISTRADOR')
            idloginadm1 = input('Crie um nome de Usuario ADM:')
            falar('CRIE UMA SENHA ADMINISTRADOR')
            senhaadm = input('Crie uma senha ADM:')
            for looping in loginadm:
                if (idloginadm1 == looping):
                    contadorcriaçaoadm += 1

                    while(contadorcriaçaoadm == 1):
                        print(Fore.LIGHTRED_EX + '\n ID Cliente ADM ja existe, tente cadastrar outro login')
                        falar('ID CLIENTE ADMINISTRADOR JÁ EXISTE, TENTE CADASTRAR OUTRO LOGIN')
                        contadorcriaçaoadm = -1
                        break

            if (contadorcriaçaoadm == 0):
                idloginadm = idloginadm1
                loginadm[idloginadm] = senhaadm
                print(Fore.LIGHTGREEN_EX + '\nCriação de Login ADM bem sucedida!\n')
                falar('CADASTRO DE ADMINISTRADOR FEITO COM SUCESSO')
                print(Fore.LIGHTWHITE_EX + f'Seu login é {idloginadm}')
                print(f'Sua senha é {senhaadm}')

        else:
            print(Fore.LIGHTRED_EX + '\nAcesso negado!\n')
            falar('ACESSO NEGADO, VOCÊ NÃO TEM PERMISSÃO NECESSARIA.')

def menu_cadastro():
    print(Fore.LIGHTWHITE_EX + '-------------------------------')
    print(Fore.LIGHTYELLOW_EX + 'Escolha a forma de cadastro:   |')
    print(Fore.LIGHTWHITE_EX + '-------------------------------')
    print(Fore.LIGHTYELLOW_EX + '[1.]--> Cliente                |')
    print('[2.]--> ADM                    |')
    print('[3.]--> VOLTAR                 |')
    print(Fore.LIGHTWHITE_EX + '-------------------------------')
    falar('DIGITE A OPÇÃO DE CADASTRO')
    falar('1 PARA CLIENTE')
    falar('2 PARA ADMINISTRADOR')
    falar('3 PARA VOLTAR AO MENU PRINCIPAL')


def falar(entrada):
    global controle
    global lista_controle
    variavel = lista_controle[-1]
    if variavel == 1:
        engine = pyttsx3.init()
        engine.setProperty('language', 'pt-br') #determina linguagem
        engine.setProperty("rate", 360) #determinar velocidade
        engine.say(entrada)
        engine.runAndWait()


def ativar_voz():
    global controle
    print('Olá, me chamo Hidra!')
    falar('Olá, me chamo Hidra ')
    print(Fore.LIGHTYELLOW_EX +'Para começar a usar o sistema, vamos configurar o sistema :)')
    falar('Para começar, vamos configurar o seu sistema')
    print(Fore.LIGHTYELLOW_EX +'Não se preocupe, você pode alterar as configurações depois.')
    falar("Não se preocupe, você pode alterar as configurações depois do seu cadastro")
    print(Fore.LIGHTYELLOW_EX + 'Esta voz foi projetada com cuidado para auxiliar aqueles com deficiências de leitura e visão.')
    falar('Esta voz foi projetada com cuidado para auxiliar aqueles com deficiências de leitura e visão')
    print('Você deseja que minha voz continue ativa?')
    falar("Você deseja que minha voz continue ativa?")
    print(Fore.LIGHTWHITE_EX +'---------- CONFIGURAÇÕES -------------')
    print(Fore.LIGHTCYAN_EX + '[1]--> SIM')
    print(Fore.LIGHTCYAN_EX + '[2]--> NÃO')
    print(Fore.LIGHTWHITE_EX +'--------------------------')
    falar('Digite 1 para ativar')
    falar('Digite 2 para desativar')
    decisao = input('Você deseja ativar o narrador?')
    trans = int(decisao) ##alteração aqui(caso dê bronca, o erro foi aqui)
    if trans == controle:
        controle = 1
        lista_controle.append(controle)
    else:
        controle = 0
        lista_controle.append(controle)
        print('Você desativou o narrador de voz!')


def configurar_sistema():
    global controle
    global lista_controle
    while True:
        print('Você está no menu de configurações')
        falar('Você está no menu de configurações')
        print(Fore.LIGHTWHITE_EX +'---------- CONFIGURAÇÕES -------------')
        print(Fore.LIGHTCYAN_EX + '[1]--> NARRADOR')
        print(Fore.LIGHTCYAN_EX + '[2]--> SUPORTE')
        print(Fore.LIGHTCYAN_EX + '[3]--> VOLTAR')
        print(Fore.LIGHTWHITE_EX +'--------------------------')
        falar('Digite 1 para configurar o narrador')
        falar('Digite 2 para falar com o suporte')
        falar('Digite 3 para voltar ao menu principal')
        falar("Digite a opção de sua preferencia para prosseguir..")
        confi = input('Digite a opção desejada:') #maracutaia feita aqui, caso de erro, o problema ta aqui
        auxiliar = int(confi)
        if confi == '1':
            auxiliar = int(confi)
            variavel = lista_controle[-1]
            if variavel == 1:
                print('O sistema de naração está ativo, deseja desativar?')
                print(Fore.LIGHTWHITE_EX + '---------- CONFIGURAÇÕES -------------')
                print(Fore.LIGHTCYAN_EX + '[1]--> SIM')
                print(Fore.LIGHTCYAN_EX + '[2]--> NÃO')
                print(Fore.LIGHTWHITE_EX + '--------------------------')
                falar('Digite 1 para sim')
                falar('Digite 2 para não')
                falar("Digite a opção de sua preferencia para prosseguir...")
                confi2 = int(input('Digite a opção desejada:'))
                if confi2 == 1:
                    controle = 0
                    lista_controle.append(controle)


                else:
                    controle = 1
                    lista_controle.append(controle)

            if variavel == 0:
                print('O sistema de naração está desativado, deseja ativar?')
                print(Fore.LIGHTWHITE_EX + '---------- CONFIGURAÇÕES -------------')
                print(Fore.LIGHTCYAN_EX + '[1]--> SIM')
                print(Fore.LIGHTCYAN_EX + '[2]--> NÃO')
                print(Fore.LIGHTWHITE_EX + '--------------------------')
                falar('Digite 1 para sim')
                falar('Digite 2 para não')
                falar("Digite a opção de sua preferencia para prosseguir..")
                confi2 = int(input('Digite a opção desejada:'))
                if confi2 == 1:
                    controle = 1
                    lista_controle.append(controle)
                else:
                    controle = 0
                    lista_controle.append(controle)
        if auxiliar == 2:
            print('Para entrar em contato com a gente, ligue: 0800 - 4002 -8922')
            falar('Para entrar em contato com a gente, ligue: 0800 - 4002 -8922')

        if auxiliar == 3:
            print('Você está saindo das configurações...')
            falar('Você está saindo das configurações...')
            break