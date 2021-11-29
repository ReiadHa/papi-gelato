def welkom():
    print('Welkom bij Papi Gelato!')
    print('je mag alle smaken kiezen zolang dat het vanile, aardbei, chocolade en munt is')


def sorry():
    print('sorry dat begrijp ik niet! ')

def factuur():
        print('----------["Papi Gelato"]----------')
        print('Bolletjes     ',aantalbollen, 'x', 5.50, ' =',  aantalbollen * 5.50 )
        print('Horrentje     ',1, 'x', horn,'=',       1 * horn )
        print('Bakje         ',0, 'x', bakjes, '=',       0.75 * bakjes)
        print('                         ------')
        print('Totaal                  = ',(aantalbollen*1.10)+(bakjes*0.75)+(horn*1.25))
        
def loop():
    bestellingen = int(input('hoeveel beestellingen wilt u maken ?'))
    for i in range(bestellingen):
        bolletjes()

def vraag():
    vraag = input('wilt u nog meer bestellen? ')
    if vraag == 'y' or vraag == 'yes' or vraag == 'Y':
        return loop()
    elif vraag == 'n' or vraag == 'no' or vraag == 'N':
        print('bedankt voor je bestelling! ')
        print('tot ziens')
    elif vraag != vraag != 'y' or vraag != 'yes' or vraag != 'Y' or vraag != 'n' or vraag != 'no' or vraag != 'N':
        sorry()
        loop()
aantalbollen = 0
horn = 0
bakjes = 0

def bolletjes():
    global aantalbollen
    global horn
    global bakjes
    welkom()
    aantal = str(input('hoeveel bolletjes wilt u? '))
    aantalbollen += int(aantal)
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
            keuze = input('wilt u deze {} bolletjes in A) een Bakje of b) een Hoorntje? '.format(aantal))
            bak = 'bak'
            hoornjte = 'hoorntje'
            if keuze == 'a' or keuze == 'A':
                print('dan krijgt u van mij {} bolletjes in een {}'.format(aantal, bak))
                print('hier is uw {} in een {}'.format(aantal, bak))
                bakjes += 1
            
            elif keuze == 'b' or keuze == 'B':
                print('dan krijgt u van mij {} bolletjes in een {}'.format(aantal, hoornjte))
                print('hier is uw {} bolletjes in een {}'.format(aantal, hoornjte))
                horn += 1   
            else:
                sorry()
                smaken()

        if 4 <= aantal <= 8:
            print('dan krijgt u van mij een bakje met {} bolletjes'.format(aantal))
        elif aantal >= 9:
            print('sorry, zulke grote bakken hebben we niet')
    elif not aantal.isdigit():
        sorry()
        bolletjes()

loop()
factuur()
vraag()
