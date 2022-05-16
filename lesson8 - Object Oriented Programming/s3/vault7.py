class Vault:
    def __init__(self, galleons = 0, sickles = 0, knuts = 0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
        
    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"
    
    def __add__(self, other):                                                                               
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)
        
        
potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)

malfoy = Vault(3000,9500,50)
print(malfoy)

total = potter + weasley + malfoy                                                                ######  Using the overrides of each name provided, we're gonna add the contents of the vaults
print(total)