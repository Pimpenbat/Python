import random

def heads():
    flipValue = random.randint(1, 2)
    hCons = 0
    tCons = 0
    while hCons < 4 and tCons < 4:
        if flipValue == 1:
            hCons += 1
            print("Heads")
            flipValue = random.randint(1,2)
        else:
            tCons += 1
            print("Tails")
            flipValue = random.randint(1,2)

if __name__ == "__main__":
    heads()
