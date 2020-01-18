class Domino:
    def __init__(self, leftDots, rightDots):
        self.leftDots = leftDots
        self.rightDots = rightDots

    def getLeftDots(self):
        return self.leftDots

    def getRightDots(self):
        return self.rightDots

    def __str__(self):
        return str(self.leftDots) + "-" + str(self.rightDots)

def DrawDominoSet():
    for i in range(7):
        for x in range(7):
            d = Domino(i, x)
            print(d)

