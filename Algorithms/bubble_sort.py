import numpy as np

#Bubble Sort
def bubble_sort(l):
    for i in range(0, len(l) - 1):
        end = True
        for j in range(0, len(l) - 1 - i):
            if l[j] > l[j + 1]:
                l[j], l[j+1] = l[j+1], l[j]
                end = False
        if end:
            break

if __name__ == "__main__":
    modulo = input("Highest value: ")
    length = input("Length of sequence: ")
    l = np.random.randint(modulo, size = length)

    print("Random sequence:")
    print(l)

    bubble_sort(l)
    print("Sorted sequence:")
    print(l)
