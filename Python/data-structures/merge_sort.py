def merge1(S, L, R):
    k = 0

    while len(L) > 0 and len(R) > 0:
        if L[0] <= R[0]:
            S[k] = L.pop(0)
        else:
            S[k] = R.pop(0)
        k += 1

    while len(L) != 0:
        S[k] = L.pop(0)
        k += 1

    while len(R) != 0:
        S[k] = R.pop(0)
        k += 1


def mergesort1(S):
    n = len(S)

    if n > 1:
        print("Splitting:", S)

        mid = n // 2
        L, R = S[:mid], S[mid:]

        mergesort1(L)
        mergesort1(R)

        merge1(S, L, R)

        print("Merging :", S)


def main():
    S = [38, 27, 43, 3, 9, 82, 10]

    print("Original List:", S)
    mergesort1(S)
    print("Sorted List:", S)


if __name__ == "__main__":
    main()