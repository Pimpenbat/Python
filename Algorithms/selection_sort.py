#Selection Sort
def selection_sort(l):
	for i in range (0, len(l) - 1):
		index_min = i
		for j in range (i + 1, len(l)):
			if l[j] < A[index_min]:
				index_min = j
		if index_min != i:
			l[i], l[index_min] =l[index_min], l[i]
