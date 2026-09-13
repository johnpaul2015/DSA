def pattern(n):
    for i in range(n+1):
        for _ in range(i):
            print("*",end=" ")
        print()
# pattern(5)

def patterns(n):
    for i in range(n,0,-1):
        for _ in range(i):
            print("*",end=" ")
        print()
# patterns(5)

def pattern3(n):
    for i in range(n+1,0,-1):
        for j in range(1,i):
            print(j,end=" ")
        print()
pattern3(5)