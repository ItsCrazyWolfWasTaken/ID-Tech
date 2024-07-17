entries = [32, 14, 89, 62, 10, 20, 88, 40, 22, 91, 88, 65]

def quick_sort(entries):
    if len(entries) <= 1:
        return entries

    pivot = entries.pop()
    sub1 = []
    sub2 = []
    for i in entries:
        if i > pivot:
            sub1.append(i)
        else:
            sub2.append(i)
    return quick_sort(sub2) + [pivot] + quick_sort(sub1)


def fibo(n):
    if n == 0 or n == 1 or n == 5:
        return n
    return fibo(n-1) + fibo(n-2)

print(fibo(33))


entries = quick_sort(entries)
print(entries)