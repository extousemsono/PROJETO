import matplotlib.pyplot as plt
from colorama import init, Fore, Back, Style
from win10toast import ToastNotifier
import cinema
def logar_menuadm(loginadm, usuarioadm, senhaadm):
    if usuarioadm in loginadm:
        for x in loginadm:
            if(senhaadm == loginadm[x]):
                return True
    return False

def menu_adm():
    print(Fore.LIGHTWHITE_EX + '---------------------- MENU -----------------------')
    print(Fore.LIGHTYELLOW_EX + 'Seja bem vindo ao Menu do Administrador.')
    print(f'O que deseja fazer hoje?')
    print('[1.]--> ADICIONAR FILME.')  # OK
    print('[2.]--> EDITAR FILME.')  # OK
    print('[3.]--> VER FATURAMENTO DO CINEMA.')
    print('[4.]--> LISTA USUARIOS ADM. ')  # OK
    print('[5.]--> MUDAR NOME DO CINEMA. ')  # OK
    print('[6.]--> MUDAR SENHA SOFTWARE.')
    print('[7.]--> REMOVER FILME.')
    print('[8.]--> BUSCAR FILMES')
    print('[9.]--> ESTATISTICAS')
    print('[10.]--> HISTORICO DE INGRESSOS')
    print('[11.]--> BUSCAR INGRESSOS EM HISTORICO')
    print('[12.]--> GERAR HISTORICO.TXT ')
    print('[13.]--> CONFIGURAÇÕES DO SISTEMA')
    print('[0.]--> SAIR')
    cinema.falar('Seja bem vindo ao menu de administrador')
    cinema.falar('O quê deseja fazer hoje?')
    cinema.falar('Digite 1 para adicionar filme')
    cinema.falar('Digite 2 para editar filme cadastrado')
    cinema.falar('Digite 3 para ver faturamento do cinema')
    cinema.falar('Digite 4 para listar usuarios administradores')
    cinema.falar('Digite 5 para mudar nome do cinema')
    cinema.falar('Digite 6 para mudar senha padrão do software ')
    cinema.falar('Digite 7 para remover filme do catalago')
    cinema.falar('Digite 8 para buscar filmes cadastrados ')
    cinema.falar('Digite 9 para visualizar as estatiticas')
    cinema.falar('Digite 10 para ver historico dos ingressos')
    cinema.falar('digite 11 para buscar ingressos em historico')
    cinema.falar('digite 13 para acessar as configurações do sistema')
    cinema.falar('Digite 12 para gerar historico txt.')
    cinema.falar('Digite 0 para sair do menu de administrador')
    print(Fore.LIGHTWHITE_EX + '-------------------------------------\n')
def editar_filme(filmes):
    print(Fore.LIGHTWHITE_EX + '---------------------- MENU -----------------------')
    n = 0
    for i in filmes:  # posição e variavel
        print(Fore.LIGHTCYAN_EX + f'Fileira N*:{n}\n')
        print(f'[1.]-->Nome do Filme:{i[1]}')
        print(f'[2.]-->Valor do Ingresso:{i[2]}')
        print(f'[3.]--> Sala do Filme:{i[3]}')
        print(f'[4.]--> Classificaçao:{i[4]}')
        print(f'[5.]--> Genero:{i[5]}')
        print(f'[6.]--> Sinopse:{i[6]}')
        print(Fore.LIGHTWHITE_EX + '-------------------------------------\n')
        n += 1
    cinema.falar('informe a opção que você gostaria de mudar')
    ordem = int(input('Informe a Opção que voce gostaria de mudar\n'))
    cinema.falar('Informe a fileira do filme')
    fileira = int(input('Informe a Fileira do Filme\n'))
    if (ordem == 1):
        cinema.falar('informe a mudança')
        mudança = input('Informe a Mudança:\n')
        for i in range(len(filmes)):
            if i == fileira:
                filmes[i][ordem] = mudança
        print(Fore.LIGHTGREEN_EX + '\nAlteração Concluida!\n')
        cinema.falar('Alteração concluida')
    elif (ordem == 2):
        cinema.falar('informe a mudança')
        mudança = int(input(Fore.LIGHTWHITE_EX + 'Informe a Mudança:\n'))
        for i in range(len(filmes)):
            if i == fileira:
                filmes[i][ordem] = mudança
                print(filmes)
        print(Fore.LIGHTGREEN_EX + '\nAlteração Concluida!\n')
        cinema.falar('Alteração concluida')

    elif (ordem == 3):
        cinema.falar('informe a mudança')
        mudança = input(Fore.LIGHTWHITE_EX + 'Informe a Mudança:\n')
        for i in range(len(filmes)):
            if i == fileira:
                filmes[i][ordem] = mudança
        print(Fore.LIGHTGREEN_EX + '\nAlteração Concluida!\n')
        cinema.falar('alteração concluida')

    elif (ordem == 4):
        cinema.falar('informe a mudança')
        mudança = input(Fore.LIGHTWHITE_EX + 'Informe a Mudança:\n')
        for i in range(len(filmes)):
            if i == fileira:
                filmes[i][ordem] = mudança
        print(Fore.LIGHTGREEN_EX + '\nAlteração Concluida!\n')
        cinema.falar('alteração concluida')

    elif (ordem == 5):
        cinema.falar('informe a mudança')
        mudança = input(Fore.LIGHTWHITE_EX + 'Informe a Mudança:\n')
        for i in range(len(filmes)):
            if i == fileira:
                filmes[i][ordem] = mudança
        print(Fore.LIGHTGREEN_EX + '\nAlteração Concluida!\n')
        cinema.falar('Alteração concluida')

    elif (ordem == 6):
        cinema.falar('informe a mudança')
        mudança = input(Fore.LIGHTWHITE_EX + 'Informe a Mudança:\n')
        for i in range(len(filmes)):
            if i == fileira:
                filmes[i][ordem] = mudança
        print(Fore.LIGHTGREEN_EX + '\nAlteração Concluida!\n')
        cinema.falar('Alteração concluida')

def remover_filme(filmes):
    print(Fore.LIGHTWHITE_EX + '\n---------------- CATALAGO -------------------')
    cinema.falar('Você está vendo o catalago')
    for i in filmes:
        print(Fore.LIGHTWHITE_EX + '------------------- LISTA ------------------')
        print(Fore.LIGHTCYAN_EX + f'ID do filme: [{i[0]}] ')
        print(f'Nome do filme: {i[1]}')
        print(f'Numero da Sala: {i[3]}')
        print(f'Valor do Ingresso: {i[2]}')
        print(Fore.LIGHTWHITE_EX + '----------------------------------------------')
    cinema.falar('Digite o id do filme em que deseja remover')
    id_para_remover = int(input(Fore.LIGHTWHITE_EX + 'Digite o id do filme em que deseja remover:'))
    for filme in filmes:
        if (filme[0] == id_para_remover):
            filmes.remove(filme)
            for i in filmes:
                print(Fore.LIGHTGREEN_EX + f'O id: {filme[0]} foi removido!')
                cinema.falar(f'O id: {filme[0]} foi removido! Segue lista atualizada:')
                print(Fore.LIGHTWHITE_EX + '---- LISTA -----')
                print(Fore.LIGHTCYAN_EX + f'ID do filme: [{i[0]}] ')
                print(f'Nome do filme: {i[1]}')
                print(f'Numero da Sala: {i[3]}')
                print(f'Valor do Ingresso: {i[2]}')
                print(Fore.LIGHTWHITE_EX + '-------------------------------')


def procurar_filme(filmes):
    print(Fore.LIGHTWHITE_EX + '-------------------------------')
    cinema.falar('Digite o nome do filme em que deseja buscar')
    busca = input('Procure por um filme:\n')
    print('-------------------------------')
    for xxx in filmes:
        if xxx[1] in busca:
            print(Fore.LIGHTGREEN_EX + f'\nFilme encontrado:\n{xxx[1]}\n')
            cinema.falar('Filme encontrado')
            print(Fore.LIGHTWHITE_EX + f'Sinopse: {xxx[6]}')
            break
        else:
            print(Fore.LIGHTRED_EX + "Filme não foi encontrado.")
            cinema.falar('Filme não encontrado')

def alterar_senhapadrao(codigo_adm):
    global equalizador
    cinema.falar("Digite a senha antiga do sistema")
    senha_antiga = input(Fore.LIGHTWHITE_EX + 'Digite a antiga senha do sistema:')
    cinema.falar('Digite a nova senha do sistema')
    senha_nova = input('Digite a nova senha do sistema:')
    if (senha_antiga == codigo_adm):
        print('---------------------------------------------------')
        print(Fore.LIGHTWHITE_EX + f'A senha do sistema agora é {senha_nova}')
        print(Fore.LIGHTGREEN_EX + 'Você vai ser deslongado para motivos de segurança. ')
        cinema.falar('Alteração feita, você será deslogado por motivos de segurança')
        print(Fore.LIGHTWHITE_EX +'---------------------------------------------------')
        equalizador = -1
    else:
        print(Fore.LIGHTRED_EX + 'Senha Incorreta')
        cinema.falar('senha incorreta')

def trocar_nome_cinema():
        global nome_cinema  # Declarando que vamos usar a variável global
        cinema.falar('Informe o novo nome do sistema')
        novo_nome = input('Informe o novo nome: ')
        nome_cinema = novo_nome
def faturamento(faturamentt):
    contadorzin = 0
    for x in faturamentt:
        contadorzin += 1
        if contadorzin == 1:
            print(Fore.LIGHTWHITE_EX +'\n------------------------------------------')
            print(Fore.LIGHTCYAN_EX + f'O faturamento de hoje foi de {faturamentt[-1]} Reais')
            print(Fore.LIGHTWHITE_EX +'------------------------------------------\n')
            cinema.falar(f'O faturamento de hoje foi de {faturamentt[-1]} Reais')
            break


def listar_usuarios(loginadm):
    for chaves in loginadm:
        cinema.falar('Segue lista de logins e senhas dos usuarios cadastrados:')
        print(Fore.LIGHTWHITE_EX + '\n--------------------------------------------')
        print(Fore.LIGHTCYAN_EX + f'Login: {chaves}, Senha: {loginadm[chaves]}')
        print(Fore.LIGHTWHITE_EX + '--------------------------------------------\n')


def estatisticas(filmes):
    eixo_x = []
    eixo_y = []
    for x in filmes:
        eixo_x.append(x[1])
        eixo_y.append(x[8])
    plt.bar(eixo_x, eixo_y)
    plt.title('Estatistica Cinema')
    plt.xlabel('Filmes')
    plt.ylabel('Ingressos Comprados')
    plt.show()

def historico_adm(historico):
    print(Fore.LIGHTWHITE_EX + '\n---------------- HISTORICO -------------------')
    cinema.falar('Segue historico de compras:')
    for x in historico:
        print(Fore.LIGHTCYAN_EX + f'Nome do Filme:{x[3]}')
        print(f'Sala:{x[0]}')
        print(f'Custo do(s) Ingresso(s):R${x[4]}')
        print(f'Fileira:{x[1]} // Numero do Assento:[{x[2]}]')
        print(Fore.LIGHTWHITE_EX + '---------------------------------------------\n')

def historico_especificar(historico):
    print(Fore.LIGHTWHITE_EX + '\n---------------- HISTORICO -------------------')
    cinema.falar('Informe o nome do filme')
    buscar = input(Fore.LIGHTWHITE_EX + 'Informe o nome do filme').lower()
    for x in historico:
        if x[3] in buscar:
            cinema.falar('Filme encontrado, segue informações a baixo:')
            print(Fore.LIGHTCYAN_EX + f'Nome do Filme:{x[3]}')
            print(f'Sala:{x[0]}')
            print(f'Custo do(s) Ingresso(s):R${x[4]}')
            print(f'Fileira:{x[1]} // Numero do Assento:[{x[2]}]')
            print(Fore.LIGHTWHITE_EX + '---------------------------------------------\n')

def historico_TXT_adm(historico):
    txt = open('ingressos_adm.txt', 'w')
    txt.write('---------------- HISTORICO.TXT -------------------\n')
    for x in historico:
        txt.write(f'Nome do Filme:{x[3]}\n')
        txt.write(f'Sala:{x[0]}\n')
        txt.write(f'Custo do(s) Ingresso(s):R${x[4]}\n')
        txt.write(f'Fileira:{x[1]} // Numero do Assento:[{x[2]}]\n')
        txt.write('---------------------------------------------\n')
    txt.close()