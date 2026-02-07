M1, M2, M3 = input().split()
M1 = int(M1)
M2 = int(M2)
M3 = int(M3)
Mmax = max(M1, M2, M3)
Mmin = min(M1, M2, M3)

if 94 <= Mmin and  Mmax <= 727:
    print(Mmax)
else:
    print("Error")