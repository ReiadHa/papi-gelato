def sorry():
    print('sorry dat begrijp ik niet! ')
def bolletjes():
    aantal = str(input('hoeveel bolletjes wilt u? '))
    if aantal.isdigit():
        aantal = int(aantal)
        if aantal <= 3:
            keuze = input('wilt u deze {} bolletjes in A) een hoorntje of b) een bakje? '.format(aantal))
            bak = 'bak'
            hoornjte = 'hoorntje'
            if keuze == 'a' or keuze == 'A':
                print('dan krijgt u van mij {} bolletjes in een {}'.format(aantal,bak))
                print('hier is uw {} in een {}'.format(aantal, hoornjte))
            if keuze == 'b' or keuze == 'B':
                print('dan krijgt u van mij {} bolletjes in een {}'.format(aantal,hoornjte))
                print('hier is uw {} in een {}'.format(aantal, bak))
            elif keuze != keuze !='a' or keuze !='A' or keuze !='b' or keuze !='B':
                sorry()
                bolletjes()
                
        elif aantal >= 4 and aantal <= 8:
            print('dan krijgt u van mij een bakje met {} bolletjes'.format(aantal))
        elif aantal >= 9:
            print('sorry, zulke grote bakken hebben we niet')
    else:
        sorry()
    vraag = input('wilt u nog meer bestellen? ')
    if vraag == 'y' or vraag =='yes' or vraag =='Y':
        return bolletjes()
    elif vraag == 'n' or vraag == 'no' or vraag == 'N':
        print('bedankt voor je bestelling! ')
        print('tot ziens')
    elif vraag != vraag != 'y' or vraag !='yes' or vraag !='Y' or vraag != 'n' or vraag != 'no' or vraag != 'N':
        sorry()
        bolletjes()




bolletjes()