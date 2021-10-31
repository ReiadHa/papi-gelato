
def aantal():
    print('dan krijgt u van mij een {} met {} bolletjes'.format(bak,bolletjes))
def weer():
    vraag = input('wilt u nog meer bestelen? ')
def sorry():
    print('sorry dat snap ik niet')
def horn_bak(bolletje,bak):
    print('hier is uw {}  met {} bolltjes.'.format(bolletje,bak))

def welkom():
    print('welkom bij papi gelato!')
    print('je mag alle smaken kiezne zolang het maar vanille ijs is.')
    print('')

welkom()

while True:
    bolletjes = int(input('hoeveel bolletjes wilt u? '))
    if bolletjes >=3:
        bak = input('wilt u deze {} bolletjes in A)een hoorntje of B) een bakje? '.format(bolletjes))
        if bak == 'A' or bak =='a':
            bak = 'hoorntje'
            aantal()
            horn_bak(bak,bolletjes)
            
        elif bak == 'b' or bak =='B':
            bak = 'bakje'
            aantal()
            horn_bak(bak,bolletjes)
            
        elif bak != 'A' or bak != 'a' or bak != 'b' or bak != 'B' : 
            sorry()
    vraag = input('wilty u nog meer bestelen? ')
    print(vraag)
    if vraag== 'y' or vraag== 'Y':
        pass
    elif vraag!= 'y' or vraag== 'Y':
        break

        






       







