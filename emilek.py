import random

class Emil:
    "Emil, cute son of Teru and Lubiador"
    def __init__(self):
        word = 'uaaaa'
    def say(self, word):
        walrus = random.sample(word,len(word))
        #print(walrus)
        #walrus = <bound method Random.sample of <random.Random object at 0x1010b6818>>
        babble = ''.join(random.sample(word,len(word)))
        print(babble)
        #return babble

    #emil zatím umí jen pár otázek    
    def ask(self, oselector):
        if (oselector == 1):
            otaznik = "Moze vegan chovat ptaka v kleci?"
        if (oselector == 2):
            otaznik = "Kolik stoji touha?"
        else:
            otaznik = "Tak todle cislo si strc za klobouk"
        if ((oselector == 1) | (oselector == 2)):
            print('?')
        else:
            print('!!!')
        print(otaznik)
        
        return otaznik    	    

Emil = Emil()
#nevim jestli je to jen KLACEK (tak se jmenuje muj pocitac) 
#ale v me konfiguraci pajthn nedava diakritiku v random.sample
#tak jsem to zkratila 
#v tve jo?
#je moc pozde, podivamsenatozitra
Emil.say('Jak se mate')
Emil.ask('mroz')
