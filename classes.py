from functions import lines, append_in_data, body_of_menu, lines_in_archive

archive = 'banco_de_dados.txt'
class Action:
    def __init__(self, option):
        if option == '1':
            lines()
            nome = str(input('Digite o nome do comprador: '))
            produto = str(input('Digite qual produto você vendeu: '))
            valor = input('Digite o preço da venda: ')

            try:
                float(valor)
            except:
                print('ERRO 3: O VALOR DA VENDA ESTÁ INCORRETO.')

                valor2 = ''
                while not valor2.isdigit():
                    valor = input('Digite o preço da venda: ')
                    valor2 = valor.replace('.', '0')
                float(valor)
            finally:
                lines()
                confirmation = str(input(f'Você realmente deseja adicionar:\nCliente: {nome.title()}\nProduto: {produto}\nValor: {valor}\n[S/N]'))
                lines()
                if confirmation in 'Ss':
                    append_in_data(archive, f'{nome.title()}/{produto}/{valor}')
                    print(f'OK, foi adicionado.')
                else:
                    print(f'OK, não foi adicionado.')
            lines()

        if option == '2':
            list_of_option2 = body_of_menu(35, 'Pesquisar por cliente', 'Ver todas as vendas')
            option2 = 0
            while option2 not in list_of_option2:
                option2 = str(input('Digite uma opção: '))

            if option2 == '1':
                search = str(input('Digite o nome do cliente: ')).title()
                cont = 0
                a = open(archive)
                for c in range(0, lines_in_archive(archive)):
                    line = a.readline().replace('\n', '').split('/')

                    if line[0] == search:
                        lines()
                        print(f'Compra do cliente {line[0]} encontrada!\nCompra: {line[1]}\nPreço: {line[2]}')
                        lines()
                a.close()

            if option2 == '2':
                a = open(archive)
                for c in range(0, lines_in_archive(archive)):
                    line = a.readline().replace('\n', '').split('/')
                    lines()
                    print(f'Cliente: {line[0]}\nCompra: {line[1]}\nPreço: {line[2]}')
                    lines()
                a.close()

        if option == '3':
            total = 0
            a = open(archive)
            for c in range(0, lines_in_archive(archive)):
                line = a.readline().replace('\n', '').split('/')
                total += float(line[2])
            a.close()
            print(f'O valor total de dívidas é: {total}')

        if option == '4':
            list_of_clients = []
            lines()
            a = open(archive)
            for c in range(0, lines_in_archive(archive)):
                line = a.readline().replace('\n', '').split('/')
                if line[0] not in list_of_clients:
                    print(f'Cliente: {line[0]}')
                    list_of_clients.append(line[0])
                    lines()
            a.close()

            remove = str(input('Qual cliente você deseja excluir a dívida?')).title()
            debt = 0
            list_with_outhers_clients = []
            a = open(archive)
            for c in range(0, lines_in_archive(archive)):
                line = a.readline().replace('\n', '').split('/')
                if line[0] == remove:
                    debt += float(line[2])
                else:
                    list_with_outhers_clients.append(line)

            if debt != 0:
                print(f'A dívida atual do cliente {remove} é: {debt}')
            else:
                print(f'Cliente {remove} não encontrado.')
            a.close()
            confirmation_remove_debt = str(input(f'Você realmente deseja excluir a dívida de {remove} no valor de {debt} reias? [S/N]'))
            if confirmation_remove_debt in 'Ss':
                a = open(archive, 'w')
                for c in range(0, len(list_with_outhers_clients)):
                    a.write(f'{list_with_outhers_clients[c][0]}/{list_with_outhers_clients[c][1]}/{list_with_outhers_clients[c][2]}\n')
                a.close()
                print(f'Foi exluído a dívida de {remove}.')
            else:
                print(f'Não foi excluído a dívida de {remove}.')
