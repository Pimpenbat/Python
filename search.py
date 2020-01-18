array = []

def binarySearch(value, array, p1 = 0, p2 = None):
    if array.count(value) == 0:
        return -1
    if p2 == None:
        p2 = len(array)
    p_mid = p1 + (p2 - p1) // 2
    if p2 - p1 + 1 <= 0 or p_mid == p2:
        return -1
    else:
        guess = array[p_mid]
        if guess == value:
            return p_mid
        if value < guess:
            return binarySearch(value, array, p1, p_mid)
        else:
            return binarySearch(value, array, p_mid + 1, p2)


