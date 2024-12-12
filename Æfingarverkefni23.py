
class myDawg:
    #Constructor
    def __init__(self,nafn,aldur,tegund):
        self.nafn = nafn
        self.aldur = aldur
        self.tegund = tegund
    
    def gelt(self):
        print("Voff Grr pAhpAhpAh")
    def __str__(self):
        return f"Nafn: {self.nafn}, Aldur: {self.aldur}, Tegund: {self.tegund}"
    

def main():
    Fokus = myDawg("Fókus",3,"Bordercollie")
    print(Fokus)
    Fokus.gelt()


class nemandi:
    def __init__(self):
        self.einkunn = 10

    def upGrade(self):
        self.einkunn += 10
        
    def lowgrade(self):
        self.einkunn -= 10
        
    def __str__(self):
        return f"Einkunn: {self.einkunn}"
    
def main2():
    Haffi = nemandi()
    Vally = nemandi()

    Haffi.lowgrade()
    Vally.upGrade()
    print(Vally)
    print(Haffi)

class squareMare:
    def __init__(self,l,b):
        self.lengd = l
        self.breidd = b
    
    def ummal(self):
        return (self.lengd + self.breidd) * 2
    
    def flatarmal(self):
        return self.lengd * self.breidd
 
    def __str__(self):
        return f"Flatarmál: {self.flatarmal()}, Ummál: {self.ummal()}" 

def main3():
    kassi = squareMare(10,10)
    print(kassi)



    # print(f"Ummál: {kassi.ummal()}")
    # print(f"Flatarmál: {kassi.flatarmal()}")
