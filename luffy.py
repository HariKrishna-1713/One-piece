class Strawhats():
    def __init__(self):
        self.zoro = ""
        self.nami = ""
        self.sanji = ""
        self.ussop = ""
        self.Luffy = ""
        
class Nicknames(Strawhats):
    def show(self):
        self.Luffy = "King_of_Pirates"
        self.zoro = "King_of_Hell"
        self.sanji = "Blackleg"
        self.ussop = "Sogeking"
        self.nami = "Catburglur"
        
        print("Luffy :", self.Luffy)
        print("Zoro  :", self.zoro)
        print("Sanji :", self.sanji)
        print("Usopp :", self.ussop)
        print("Nami  :", self.nami)
        
    @staticmethod
    def __init__():
        print("Orewa Monkey D Luffy")
        print()
        
h = Nicknames()
h.show()