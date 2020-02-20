import random

def quick_sort3(A, l, r):
    if l >= r:
        return
    random.seed(1)
    k = random.randint(l, r)
    A[k], A[l] = A[l], A[k]

    left, right = partition3(A, l, r)
    quick_sort3(A, l, left - 1)
    quick_sort3(A, right + 1, r)

def partition3(A, l ,r):
    pivot, left, right = A[l], l, r
    i = left

    while i <= right:
        if A[i] < pivot:
            A[left], A[i] = A[i], A[left]
            left += 1
        elif A[i] > pivot:
            A[i], A[right] = A[right], A[i]
            right -= 1
            i -= 1
        i += 1

    return left, right

if __name__ == "__main__":
    random.seed(1)
    A = [random.randint(0,10) for x in range(10)]
    print(A)
    for i in range(20000):
        quick_sort3(A, 0, len(A) - 1)
    print(A)
