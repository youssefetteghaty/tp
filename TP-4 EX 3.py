def permute():
    global A, B
    A, B = B, A
A = 5
B = 10
print("Avant permutation : A =", A, "B =", B)
permute()
print("Après permutation : A =", A, "B =", B)