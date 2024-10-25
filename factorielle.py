def Factorielle(N):
    if N == 0:
        return 1
    else:
        return N*Factorielle(N-1)
    
print(Factorielle(3))
