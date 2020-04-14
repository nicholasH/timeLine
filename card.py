class Card:
    def __init__(self, id, name, year, bc, info):
        self.id = id
        self.name = name
        self.year = year
        self.bc_ac = 1
        if bc is not None:
            if bc.strip() == "bc":
                self.bc_ac = -1

        self.info = info

    def __gt__(self, other):
        isGT =  False

        if(self.bc_ac > other.bc_ac):
            isGT = True
        elif(self.bc_ac == other.bc_ac):
            if(self.bc_ac == -1):
                if(self.year < other.year):
                    isGT = True
            elif(self.bc_ac == 1):
                if(self.year > other.year):
                    isGT = True

        return isGT

    def __lt__(self, other):
        isLT = False

        if (self.bc_ac < other.bc_ac):
            isLT = True
        elif (self.bc_ac == other.bc_ac):
            if (self.bc_ac == -1):
                if (self.year > other.year):
                    isLT = True
            elif (self.bc_ac == 1):
                if (self.year < other.year):
                    isLT = True

        return isLT

    def __eq__(self, other):
        if(self.bc_ac == other.bc_ac):
            if(self.year == other.year):
                return True
        return False

    def __str__(self):
        if self.bc_ac == -1:
            return  str(self.year) + " BC"
        else:
            return str(self.year) + " AC"