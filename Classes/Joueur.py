class joueur:

    name : str
    score_devinette : int
    score_allumettes : int
    score_morpion : int
    score_puissance4 : int

    def __init__(self, name : str, score_devinette : int, score_allumettes : int, score_morpion : int, score_puissance4 : int):

        self.name = name
        self.score_devinette = score_devinette
        self.score_allumettes = score_allumettes
        self.score_morpion = score_morpion
        self.score_puissance4 = score_puissance4

    def getName(self)->str:
        return self.name

    def setName(self, name : str):
        self.name = name

    def getScoreDevinette(self)->int:
        return self.score_devinette

    def getScoreAllumettes(self)->int:
        return self.score_allumettes

    def getScoreMorpion(self)->int:
        return self.score_morpion

    def getScorePuissance4(self)->int:
        return self.score_puissance4

    def setScoreDevinette(self, score_devinette : int):
        self.score_devinette = score_devinette

    def setScoreAllumettes(self, score_allumettes : int):
        self.score_allumettes = score_allumettes

    def setScoreMorpion(self, score_morpion : int):
        self.score_morpion = score_morpion

    def setScorePuissance4(self, score_puissance4 : int):
        self.score_puissance4 = score_puissance4

    def showScoreDevinette(self):
        print(self.getName(), " : " , self.score_devinette)

    def showScoreAllumettes(self):
        print(self.getName(), " : " , self.score_allumettes)

    def showScoreMorpion(self):
        print(self.getName(), " : " , self.score_morpion)

    def showScorepuissance4(self):
        print(self.getName(), " : " , self.score_puissance4)

