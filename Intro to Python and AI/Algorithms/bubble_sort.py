entries = [32, 14, 89, 62, 10, 20, 88, 40, 22,  91, 88, 65]

def swap(values, i, j):
    temp = values[i]
    values[i] = values[j]
    values[j] = temp
def bubble_sort(values):
    for i in range(len(values)-1):
        for j in range(0, len(values)-1):
            if values[j]>values[i]:
                swap(values, i, j)
bubble_sort(entries)
print(entries)
