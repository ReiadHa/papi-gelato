def welkom():
    print('Welkom bij Papi Gelato!')
    print('je mag alle smaken kiezen zolang dat het vanile, aardbei, chocolade en munt is')


def sorry():
    print('sorry dat begrijp ik niet! ')


def vraag():
    vraag = input('wilt u nog meer bestellen? ')
    if vraag == 'y' or vraag == 'yes' or vraag == 'Y':
        return bolletjes()
    elif vraag == 'n' or vraag == 'no' or vraag == 'N':
        print('bedankt voor je bestelling! ')
        print('tot ziens')
    elif vraag != vraag != 'y' or vraag != 'yes' or vraag != 'Y' or vraag != 'n' or vraag != 'no' or vraag != 'N':
        sorry()
        bolletjes()


def bolletjes():
    welkom()
    aantal = str(input('hoeveel bolletjes wilt u? '))
    def smaken():
        nummer = 0
        for x in range(int(aantal)):
            nummer+=1
            smaak = input('wat voor smaak wilt u voor bolletje nummer {}: A) Chocolade B) Aardbei C) vanile D) Munt. type(A or B or c or D): '.format(nummer))
            if smaak == 'a' or smaak == 'A':
                smaak = 'chocolade'
            elif smaak == 'b' or smaak == 'B':
                smaak = 'aardbei'
            elif smaak == 'c' or smaak == 'C':
                smaak = 'vanile'
            elif smaak == 'd' or smaak == 'D':
                smaak = 'munt'
            else:
                sorry()
                smaken()
    smaken()

          
    if aantal.isdigit():
        aantal = int(aantal)
        if aantal <= 3:
            keuze = input('wilt u deze {} bolletjes in A) een hoorntje of b) een bakje? '.format(aantal))
            bak = 'bak'
            hoornjte = 'hoorntje'
            if keuze == 'a' or keuze == 'A':
                print('dan krijgt u van mij {} bolletjes in een {}'.format(aantal, bak))
                print('hier is uw {} in een {}'.format(aantal, hoornjte))
            if keuze == 'b' or keuze == 'B':
                print('dan krijgt u van mij {} bolletjes in een {}'.format(aantal, hoornjte))
                print('hier is uw {} bolletjes in een {}'.format(aantal, bak))
            elif keuze != keuze != 'a' or keuze != 'A' or keuze != 'b' or keuze != 'B':
                sorry()
                smaken()
        if 4 <= aantal <= 8:
            print('dan krijgt u van mij een bakje met {} bolletjes'.format(aantal))
        elif aantal >= 9:
            print('sorry, zulke grote bakken hebben we niet')
    elif not aantal.isdigit():
        sorry()
        bolletjes()


bolletjes()
vraag()
