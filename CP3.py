import os

carteiras = 8

fileiras = 5

reservas = carteiras * fileiras

alunos = []

lugares = []

reserva = 0

sair = False

while sair == False:
    os.system('cls')
    print('Sala de aula')
    print('Carteiras: ', carteiras)
    print('Fileiras: ', fileiras)
    print('Reservas: ', reservas)
    print()
    print('Alunos:')
    for i in range(len(alunos)):
        print(alunos[i], ' - ', lugares[i])
    print()
    print('1 - Reservar')
    print('2 - Sair')
    opcao = int(input('Opção: '))
    if opcao == 1:
        if reserva < reservas:
            nome = input('Nome: ')
            fileira = int(input('Fileira: '))
            carteira = int(input('Carteira: '))
            if fileira <= fileiras and carteira <= carteiras:
                alunos.append(nome)
                lugares.append(str(fileira) + ' - ' + str(carteira))
                reserva = reserva + 1
            else:
                print('Carteira inexistente!')
        else:
            print('Reservas esgotadas!')
    else:
        sair = True