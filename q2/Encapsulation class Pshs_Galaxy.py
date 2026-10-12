class Pshs_Galaxy:
    def __init__(self):
        self.__letter = "Z"
    @property 
    def letter(self):
     return self.__letter
    @letter.setter
    def letter(self, value):
      self.__letter = value


class Nationality(Pshs_Galaxy):
    def __init__(self):
        self.__letter = "Z"
        self.__nationality = "Filipino"
    @property
    def nationality (self):
     return self.__nationality
    @nationality.setter
    def nationality(self, value):
     self.__nationality = value

    @property
    def name(self):
     return self.__letter
    @name.setter
    def name(self, value):
     self.__letter = value 

  
class Alien(Pshs_Galaxy):
    def __init__(self):
        self.__letter = "Z"
        self.__creature = "Mythical"

    @property
    def creature(self):
     return self.__creature
    @creature.setter
    def creature(self, value):
     self.__creature = value

    @property
    def name(self):
     return self.__letter
    @name.setter
    def name(self, value):
     self.__letter = value



class Filipino(Nationality):
    def __init__(self):
        self.__currency = "Peso"

    @property
    def currency(self):
        return self.__currency

class Indonesian(Nationality):
    def __init__(self):
        self.__currency = "Rupiah"

    @property
    def currency(self):
        return self.__currency

class Spaniard(Nationality):
    def __init__(self):
        self.__currency = "Euro"

    @property
    def currency(self):
        return self.__currency

class Marvel(Alien):
    def __init__(self):
        self.character = "Spider-Man"

class Avengers(Alien):
    def __init__(self):
        self.character = "Iron Man"

print ("--!! Pshs_Galaxy class --!!")
print ("Attribute:" + Pshs_Galaxy().letter)

print ("--- Nationality class ---")
print ("Nationality:" + Nationality().nationality)

print ("--- Nationality: Filipino class ---")
print ("Currency:" + Filipino().currency)

print ("--- Nationality: Indonesian class ---")
print ("Currency:" + Indonesian().currency)

print ("--- Nationality: Spaniard class ---")
print ("Currency:" + Spaniard().currency)

print ("---!!! Alien class !!!---")
print ("Creature:" + Alien().creature)

print ("--- Alien: Marvel class ---")
print ("Character:" + Marvel().character)

print ("--- Alien: Avengers class ---")
print ("Character:" + Avengers().character)
