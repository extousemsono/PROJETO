import audioop
from colorama import init, Fore, Back, Style
from winotify import Notification, audio
import cinema
def logar_menucliente(login, idlogin, senha):
    if idlogin in login:
        for x in login:
            if(senha == login[x]):
                return True
    return False

def menu_cliente(idlogin, nome_cinema):
    print(Fore.LIGHTWHITE_EX + '---------------- MENU -----------------')
    print(Fore.LIGHTYELLOW_EX + f'Olá, seja bem-vindos ao {nome_cinema}')
    print(f'O quê deseja fazer hoje {idlogin}?')
    print(Fore.LIGHTWHITE_EX + f'----------------------------------')
    print(Fore.LIGHTYELLOW_EX + '[1.]--> COMPRAR INGRESSOS.')
    print('[2.]--> MUDAR SENHA.')
    print('[3.]--> HISTORICO.')
    print('[4.]--> VER FILMES DISPONIVEIS. ')
    print('[5.]--> GERAR HISTORICO.TXT.')
    print('[6.]--> CONFIGURAÇÕES DO SISTEMA')
    print('[7.]--> SAIR DO LOGIN.')
    cinema.falar(f'Olá, seja bem-vindos ao {nome_cinema}')
    cinema.falar(f'O quê deseja fazer hoje {idlogin}?')
    cinema.falar('Digite a opção desejada para continuar')
    cinema.falar('Digite 1 para comprar ingressos')
    cinema.falar('Digite 2 para sua mudar a senha')
    cinema.falar('Digite 3 para ver historico de compras')
    cinema.falar('Digite 4 para ver filmes disponiveis')
    cinema.falar('Digite 5 para gerar historico.txt')
    cinema.falar('Digite 6 IR EM CONFIGURAÇÕES DO SISTEMA')
    cinema.falar('Digite 7 para sai do login')
    print(Fore.LIGHTWHITE_EX + '\n------------------------')
def mudanca_senhacliente(login, idcliente, novasenha):
    for x in login:
        if idcliente in x:
            login[idcliente] = novasenha
            return True
    return False

def ver_historico(historico):
    print(Fore.LIGHTWHITE_EX + '\n---------------- HISTORICO -------------------')
    for x in historico:
        print(Fore.LIGHTCYAN_EX + f'Nome do Filme:{x[3]}')
        print(f'Sala:{x[0]}')
        print(f'Custo do(s) Ingresso(s):R${x[4]}')
        print(f'Fileira:{x[1]} // Numero do Assento:[{x[2]}]')
        cinema.falar( f'Nome do Filme:{x[3]}')
        cinema.falar(f'Sala:{x[0]}')
        cinema.falar(f'Custo do(s) Ingresso(s):R${x[4]}')
        cinema.falar(f'Fileira:{x[1]} // Numero do Assento:[{x[2]}]')

        print(Fore.LIGHTWHITE_EX + '---------------------------------------------\n')

def listar_filmesCliente(filmes):
    print(Fore.LIGHTWHITE_EX + '------------------ FILMES DISPONIVEIS -------------------------------')
    for x in filmes:
        print(Fore.LIGHTCYAN_EX + f'Nome do Filme: {x[1]}')
        print(f'Sala: {x[3]}')
        print(f'Genero:{x[5]}')
        print(f'>Não Recomendado para Menores de:{x[4]} anos <\n')
        cinema.falar(f'Nome do Filme: {x[1]}')
        cinema.falar(f'Genero:{x[5]}')
        cinema.falar(f'Esse filme não Recomendado para Menores de:{x[4]} anos')
    print(Fore.LIGHTWHITE_EX + '---------------------------------------------------------------------')

def mudaca_senhacliente2(login, idcliente, novasenha):
    print(Fore.LIGHTWHITE_EX + '-----------------------------------------------')
    print('Você vai mudar a senha, Por favor, informe o id')
    cinema.falar('Você vai mudar a senha, por favor, informe seu ID')
    print(Fore.LIGHTWHITE_EX + '-----------------------------------------------')
    cinema.falar('Informe o ID cliente para a alteração de senha')
    idcliente = input('Informe o Id Cliente para a alteraçao de senha:')
    cinema.falar('Informe sua senha nova')
    novasenha = input('Informe sua senha nova:')
    return mudanca_senhacliente(login, idcliente, novasenha)


def menucurtida(filmes):
    for filme in filmes:
        print(Fore.LIGHTWHITE_EX + '---------------------')
        print(Fore.LIGHTCYAN_EX + f'Filme: {filme[1]} ')
        print(f'ID Filme: {filme[0]}')
        print(Fore.LIGHTWHITE_EX + f'--------------')
        print(f'----------Sinopse -------')
        print(Fore.LIGHTCYAN_EX + f'{filme[6]}')
        print(f'- Numero de curtidas: {filme[7]}')
        print(Fore.LIGHTWHITE_EX + '------------------------------')



def contadordecurtida(filmes, id_feedback):
    menucurtida(filmes)
    feedback = input('Você deseja curtir algum filme? (s/n): ')
    cinema.falar('Você deseja curtir algum filme?')
    if feedback == 'sim':
        cinema.falar('Digite o ID do filme no qual quer curtir')
        id_feedback = int(input('Digite o ID do filme no qual quer curtir: '))
    for f in filmes:
        if id_feedback == f[0]:
            f[7] += 1
            print('\n---------------------')
            print(f'Você curtiu o filme!')
            print('---------------------')
            cinema.falar('Você curtiu o filme!')
    else:
        print('\n----- Você foi redirecionado para o menu principal ----\n')
        cinema.falar('Você está sendo redirecionado para o menu principal')
def compra_de_ingressos(ticket, ticketValor, aux, resultado, filmes, historico, breaker, faturamentt):
    visualizar = 0
    assentos = {'A': ['[00]', '[01]', '[02]', '[03]', '[04]'],
                'B': ['[00]', '[01]', '[02]', '[03]', '[04]'],
                'C': ['[00]', '[01]', '[02]', '[03]', '[04]']}
    contar = 0
    apontar = 0
    for x in range(0, ticketValor):
        if breaker == True:
            break
        contar = contar + 1
        print(contar)
        print(Fore.LIGHTWHITE_EX + f'------------- SALA ------------------')
        print(Fore.LIGHTCYAN_EX + f'A =', assentos['A'])
        print(f'B =', assentos['B'])
        print(f'C =', assentos['C'])
        print(Fore.LIGHTWHITE_EX + f'-------------------------------------')
        print('-------------- TELA ------------------')
        if ticketValor >= 1:
            cinema.falar('Selecione a fileira no qual deseja escolher')
            camada = input('Selecione a fileira desejada:').upper()
            cinema.falar('Selecione o numero do assento')
            cadeira = int(input('Selecione o número do assento: '))
            for xl in assentos:
                if breaker == True:
                    break
                if (assentos[camada][cadeira] == '[XX]'):
                    print(Fore.LIGHTRED_EX + '\n----- Compra de Ingressos Interrompida, o Local ja foi escolhido! -----\n')
                    cinema.falar('Compra do ingresso interrupida, o local já foi escolhido')
                    for remov in range(0, contar):
                        aux -= resultado
                        apontar = 1
                        breaker = True
            if cadeira <= 4:
                if camada == 'A' or 'B' or 'C':
                    if apontar == 0:
                        for i in range(0, 1):
                            assentos[camada][cadeira] = '[XX]'
                            print(Fore.LIGHTWHITE_EX + f'------------- SALA ------------------')
                            print(Fore.LIGHTCYAN_EX + f'A =', assentos['A'])
                            print(f'B =', assentos['B'])
                            print(f'C =', assentos['C'])
                            print(Fore.LIGHTWHITE_EX + f'-------------------------------------')
                            print('-------------- TELA ------------------')
                            print(Fore.LIGHTGREEN_EX + 'Seu assento foi marcado com sucesso. ')
                            cinema.falar('Seu assento foi marcado com sucesso')
                        for j in filmes:
                            if j[0] == ticket:
                                if apontar == 0:
                                    resultado = j[2]
                                    aux += resultado
                                    faturamentt.append(aux)
                                    print(Fore.LIGHTWHITE_EX + '-------------------------------------------------------------------')
                                    print(Fore.LIGHTGREEN_EX + 'Compra Aprovada!')
                                    print(Fore.LIGHTCYAN_EX + f'Você comprou o ingresso :{j[1]}, Total Por Ingresso: R${resultado}')
                                    print(f'Sala:{j[3]}, Assento: {camada} + {cadeira}')
                                    print(Fore.LIGHTWHITE_EX + '-------------------------------------------------------------------')
                                    cinema.falar('Sua compra foi aprovada!')
                                    global notificacao
                                    global duration
                                    notificacao = Notification(app_id="Mensagem do sistema", title="Compra aprovada com sucesso!", msg = f'Você comprou o ingresso para o filme: {j[1]}')
                                    notificacao.set_audio(audio.LoopingAlarm, loop=False)
                                    duration = "short"
                                    notificacao.show()
                                    historico.append([j[3], camada, cadeira, j[1], resultado])
                                    visualizar += 1
                                    j[8] = (j[8] + visualizar) - contar + 1

                if (apontar == 1):
                    print(Fore.LIGHTWHITE_EX + '\n(--Dinheiro Reembolsado--)\n')
                    cinema.falar('Seu dinheiro foi reembolsado')
                    aux += resultado
                    for x in filmes:
                        if ticket == x[0]:
                            x[8] -= visualizar

def listar_TXT(historico):
    txt = open('ingressos.txt', 'w')
    txt.write('---------------- HISTORICO.TXT -------------------\n')
    for x in historico:
        txt.write(f'Nome do Filme:{x[3]}\n')
        txt.write(f'Sala:{x[0]}\n')
        txt.write(f'Custo do(s) Ingresso(s):R${x[4]}\n')
        txt.write(f'Fileira:{x[1]} // Numero do Assento:[{x[2]}]\n')
        txt.write('---------------------------------------------\n')
    txt.close()