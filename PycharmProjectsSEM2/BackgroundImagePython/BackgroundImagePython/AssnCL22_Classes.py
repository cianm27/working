class Address:

    def __init__(self, city,  country):
        # private variables
        self.__city = city
        self.__country = country

    def readCity(self):
        return self.__city

    def readCountry(self):
        return self.__country

    def updateCity(self, city):
        self.__city = city

#---------------------------------------------

class Athlete:

    def __init__(self, name, age, city, country):
        # private variables
        self.__name = name
        self.__age = age
             # aggregation
        self.__address = Address(city, country)
        self.__wins = 0
        self.__fit = True


    def readFit(self):
        return self.__fit

    def markFit(self):
        self.__fit = True

    def markUnfit(self):
        self.__fit = False

    def readName(self):
        return self.__name

    def readAge(self):
        return self.__age

    def stepAge(self):
        self.__age += 1

    def stepWins(self, wins):
        if (self.__fit==True):
            self.__wins = wins

    def readWins(self):
        return self.__wins

    def readCity(self):
        return self.__address.readCity()

    def readCountry(self):
        return self.__address.readCountry()

    # Polymorphic Methods

    def readType(self):
        return ''

    def readDescriptionPart1(self):
        return ''

    def readDescriptionPart2(self):
        return ''

    def readDescriptionPart3(self):
        return ''



    #--------------------------------------------

class Swimmer(Athlete):

    def __init__(self, name, age, city, country,
                 style, goggles, diver):
        super().__init__(name, age, city, country)
        self.__style = style
        self.__goggles = goggles
        self.__diver = diver

    def readType(self):
        return 'Swimmer'

    def readDescriptionPart1(self):
        return 'Swim Style: : ' + str(self.__style)

    def readDescriptionPart2(self):
        return 'Goggles : ' + str(self.__goggles)

    def readDescriptionPart3(self):
        return str(self.__diver)


    #--------------------------------------------

class Cyclist(Athlete):

    def __init__(self, name, age, city, country,
                 domain, bike, team):
        super().__init__(name, age, city, country)
        self.__domain = domain
        self.__bike = bike
        self.__team = team

    def readType(self):
        return 'Cyclist'

    def readDescriptionPart1(self):
        return 'Domain : ' + str(self.__domain)

    def readDescriptionPart2(self):
        return 'Bike : ' + str(self.__bike)

    def readDescriptionPart3(self):
        return 'Team : ' + str(self.__team)


    #--------------------------------------------

class Runner(Athlete):

    def __init__(self, name, age, city, country,
                 distance, trainers, outdoor):
        super().__init__(name, age, city, country)
        self.__distance = distance
        self.__trainers = trainers
        self.__outdoor = outdoor

    def readType(self):
        return 'Runner'

    def readDescriptionPart1(self):
        return 'Distance : ' + str(self.__distance)

    def readDescriptionPart2(self):
        return 'Trainers : ' + str(self.__trainers)

    def readDescriptionPart3(self):
        return 'Outdoor/Indoor: ' + str(self.__outdoor)
