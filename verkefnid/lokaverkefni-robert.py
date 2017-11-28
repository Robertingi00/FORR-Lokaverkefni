'''
Lokaverkefni
'''
import random
class Nagdyr:
    def __init__(self, tegund, stadsetning, afl):
        self.teg = tegund
        self.stad = stadsetning
        self.afl = afl
    def upp(self):
        return self.teg , str(self.stad) , str(self.afl) 
    
class border:
    def endir(self):
        print("WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW")
        print("><><><><><><><><> Niður staða <><><><><><><><><")
 
    def byrjun(self):
        print("WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW")
        print("><><><><><><><><><> leikur " + str(teljari) + " <><><><><><><><><><")
 
    def fotur(self):
        print("WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW")

def kast(tegund):
    if tegund.teg == "Mús":
        kast = random.randint(1,6)
    return kast
    

 
game = 0
border = border()
teljari = 1
rottur = list() 

mus = Nagdyr("Mús",1,random.randrange(2,7,2))
rotta = Nagdyr("Rotta",random.randrange(2,100,),random.randrange(2,7,2))
rotta2 = Nagdyr("Rotta_2",random.randrange(2,100,),random.randrange(2,7,2))
rotta3 = Nagdyr("Rotta_3",random.randrange(2,100,),random.randrange(2,7,2))
hamstur = Nagdyr("Hamstur",random.randrange(2,100,),random.randrange(2,7,2))

print(mus.stad)
print(rotta.stad)
print(rotta2.stad)
print(rotta3.stad)
print(hamstur.stad)
rottur.append(rotta)
rottur.append(rotta2)
rottur.append(rotta3)


while game != "buinn":
    mus.stad +=kast(mus)
    print(mus.stad)
    for x in rottur:
        if mus.stad == x.stad:
            if mus.afl > x.afl:
                x.stad -=mus.afl
                print("mus vann rottu1")
            else:
                mus.stad -=x.afl
                print("mus tapaði fyrir "+ x.teg+ " og fer " + str(x.afl)+" reiti aftur á bak og er á reit "+ str(mus.stad))

    if mus.stad == hamstur.stad:
        mus.stad += hamstur.afl
        print("Hamstur kastar mús um "+ str(hamstur.afl) +" reiti, mus er á reiti "+ str(mus.stad))

    if mus.stad >= 100:
        game = "buinn"
        print("Músin vann")

    
