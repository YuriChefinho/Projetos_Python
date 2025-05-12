'''Crie um programa que tenha uma lista de produtos com valores, e cada produto tenha seu codigo para selecionar'''

#criação da lista de produtos
print('!!!Culinaria Oriental Cardapio!!!')
print('YAKISSOBA     [1] \nCHOPP SUEY    [2] \nFRANGO XADREZ [3]')
cardápio = int(input('Selecione o numero de acordo ao cardapio: '))

yakissoba = ['Yakissoba Tradicional', 'Yakissoba Especial', 'Yakissoba Vegetariano'] #Cardapio de Yakissoba

choppSuey = ['Chopp Suey Tradicional', 'Chopp Suey Frango', 'Chopp Suey Camarão']# Cardapio de ChoppSuey

frangoXadrez = ['Frango Xadrez Com Castanhas', 'Frango Xadrez Com Legumes', 'Frango Xadrez Com Champignon'] 




#Estrutura Do Cardapio De Yakissoba 

if cardápio == 1:
    print('CARDAPIO DE YAKISSOBA: ')
    print('Yakissoba Tradicional [1] \nYakissoba Especial    [2] \nYakissoba Vegetariano [3]')
    cardápio_yakissoba = int(input('Digite o numero do prato da sua escolha: '))     #Variavel Cardapio Yakissoba

    if cardápio_yakissoba == 1:
        valor_yaki_tradicional = 85 #Valor do Yakissova Tradicional R$85,00
        print('{} = {:.2f} \nConfirmar A Compra? '.format(yakissoba[0],valor_yaki_tradicional))
        compra = int(input('SIM [1] \nNÃO [2] : '))
        if compra == 1:
            print('!!!OBRIGADO PELA COMPRA!!!')
            print(' 1 - Yakissoba Tradicional | R${:.2f} \n\n\nVALOR TOTAL = R${:.2f}'.format(valor_yaki_tradicional,valor_yaki_tradicional))
        else:
            print('VOLTE SEMPRE! ')


    elif cardápio_yakissoba == 2:
        valor_yaki_especial = 100 #Valor do Yakissoba Especial R$100,00        
        print('{} = {:.2f} \nConfirmar A Compra?'.format(yakissoba[1], valor_yaki_especial))
        compra = int(input('SIM [1] \nNÃO [2] : '))
        if compra == 1:
            print('!!!OBRIGADO PELA COMPRA!!!')
            print(' 1 - Yakissoba Especial | R${:.2f} \n\n\nVALOR TOTAL = R${:.2f}'.format(valor_yaki_especial,valor_yaki_especial))
        else:
            print('VOLTE SEMPRE! ')

    elif cardápio_yakissoba == 3:
        valor_yaki_vegetariano = 65 #Valor do Yakissoba Vegetariano R$65,00
        print('{} = {:.2f} \nConfirmar Compra? '.format(yakissoba[2], valor_yaki_vegetariano))
        compra = int(input('SIM [1] \nNÃO [2] : '))
        if compra == 1:
            print('!!!OBRIGADO PELA COMPRA!!!')
            print(' 1 - Yakissoba Vegetariano | R${:.2f} \n\n\nVALOR TOTAL = R${:.2f}'.format(valor_yaki_vegetariano,valor_yaki_vegetariano))
        else:
            print('VOLTE SEMPRE! ')

    

#Estrutura Do Cardapio De Chopp Suey

elif cardápio == 2:
    print('CARDAPIO DE CHOPP SUEY: ')
    print('Chopp Suey Tracidional [1] \nChopp Suey Frango      [2] \nChopp Suey Camarão     [3]')
    cardápio_choppSuey = int(input('Digite o numero do prato da sua escolha: '))    #Variavel Cardapio Chopp Suey 
    if cardápio_choppSuey == 1:
        print(choppSuey[0])

    elif cardápio_choppSuey == 2:
        print(choppSuey[1])

    elif cardápio_choppSuey == 3:
        print(choppSuey[2])



#Estrutura DO Cardapio De Frango Xadrez
elif cardápio == 3:
    print('CARDAPIO DE FRANGO XADREZ: ')
    print('Frango Xadrez Com Castanhas  [1] \nFrango Xadrez Com Legumes    [2] \nFrango Xadrez Com Champignon [3]')
    cardápio_frangoXadrez = int(input('Digite o numero do prato da sua escolha: '))       #variavel do cardapio de Frango Xadrez
    if cardápio_frangoXadrez == 1:
        print(frangoXadrez[0])
        
    elif cardápio_frangoXadrez == 2:
        print(frangoXadrez[1])

    elif cardápio_frangoXadrez == 3:
        print(frangoXadrez[2])


else:
    print('Voce não digitou um numero valido')

