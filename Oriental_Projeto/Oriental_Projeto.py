'''Crie um programa que tenha uma lista de produtos com valores, e cada produto tenha seu codigo para selecionar'''

#criação da lista de produtos
print('!!!Culinaria Oriental Cardapio!!!')
print('YAKISSOBA     [1] \nCHOPP SUEY    [2] \nFRANGO XADREZ [3]')
card = int(input('Selecione o numero de acordo ao cardapio: '))

yaki = ['Yakissoba Tradicional', 'Yakissoba Especial', 'Yakissoba Vegetariano'] #Cardapio de Yakissoba

s_suey = ['Chopp Suey Tradicional', 'Chopp Suey Frango', 'Chopp Suey Camarão']# Cardapio de ChoppSuey

f_xad = ['Frango Xadrez Com Castanhas', 'Frango Xadrez Com Legumes', 'Frango Xadrez Com Champignon'] 




#Estrutura Do Cardapio De Yakissoba 
if card == 1:
    print('CARDAPIO DE YAKISSOBA: ')
    print('Yakissoba Tradicional [1] \nYakissoba Especial    [2] \nYakissoba Vegetariano [3]')
    card_y = int(input('Digite o numero do prato da sua escolha: '))     #Variavel Cardapio Yakissoba
    if card_y == 1:
        val_yt = 85 #Valor do Yakissova Tradicional R$85,00
        print('{} = {:.2f} \nConfirmar A Compra? '.format(yaki[0],val_yt))
        compra = int(input('SIM [1] \nNÃO [2] : '))
        if compra == 1:
            print('!!!OBRIGADO PELA COMPRA!!!')
            print(' 1 - Yakissoba Tradicional | R${:.2f} \n\n\nVALOR TOTAL = R${:.2f}'.format(val_yt,val_yt))
        else:
            print('VOLTE SEMPRE! ')


    elif card_y == 2:
        val_ye = 100 #Valor do Yakissoba Especial R$100,00        
        print('{} = {:.2f} \nConfirmar A Compra?'.format(yaki[1], val_ye))
        compra = int(input('SIM [1] \nNÃO [2] : '))
        if compra == 1:
            print('!!!OBRIGADO PELA COMPRA!!!')
            print(' 1 - Yakissoba Especial | R${:.2f} \n\n\nVALOR TOTAL = R${:.2f}'.format(val_ye,val_ye))
        else:
            print('VOLTE SEMPRE! ')

    elif card_y == 3:
        val_yv = 65 #Valor do Yakissoba Vegetariano R$65,00
        print('{} = {:.2f} \nConfirmar Compra? '.format(yaki[2], val_yv))
        compra = int(input('SIM [1] \nNÃO [2] : '))
        if compra == 1:
            print('!!!OBRIGADO PELA COMPRA!!!')
            print(' 1 - Yakissoba Vegetariano | R${:.2f} \n\n\nVALOR TOTAL = R${:.2f}'.format(val_yv,val_yv))
        else:
            print('VOLTE SEMPRE! ')

    

#Estrutura Do Cardapio De Chopp Suey
elif card == 2:
    print('CARDAPIO DE CHOPP SUEY: ')
    print('Chopp Suey Tracidional [1] \nChopp Suey Frango      [2] \nChopp Suey Camarão     [3]')
    card_s = int(input('Digite o numero do prato da sua escolha: '))    #Variavel Cardapio Chopp Suey 
    if card_s == 1:
        print(s_suey[0])

    elif card_s == 2:
        print(s_suey[1])

    elif card_s == 3:
        print(s_suey[2])



#Estrutura DO Cardapio De Frango Xadrez
elif card == 3:
    print('CARDAPIO DE FRANGO XADREZ: ')
    print('Frango Xadrez Com Castanhas  [1] \nFrango Xadrez Com Legumes    [2] \nFrango Xadrez Com Champignon [3]')
    card_f = int(input('Digite o numero do prato da sua escolha: '))       #variavel do cardapio de Frango Xadrez
    if card_f == 1:
        print(f_xad[0])
        
    elif card_f == 2:
        print(f_xad[1])

    elif card_f == 3:
        print(f_xad[2])


else:
    print('Voce não digitou um numero valido')

