

def pattern1(n):
    for i in range(0,n):
        for j in range(0,n):
            print("*",end="")
        print("")

def pattern2(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("*",end="")
        print("")

def pattern3(n):
    for i in range(0,n):
        for j in range(0,n-i):
            print("*",end="")
        print("")

def pattern4(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end="")
        print("")

def pattern5(n):
    for i in range(1,2*n):
        cols = i
        if(i>n):
            cols = 2*n -i; 
        for j in range(0,cols) :
            print("*",end="")
        print("")

def pattern6(n):
    for i in range(0,n):
        for j in range(0,n):
            if(j<n-i-1):
                print(" ", end="")
            else:
                print("*",end="")
        print("")

def pattern7(n):
    for i in range(0,n):
        for j in range(0,n):
            if(j<i):
                print(" ", end="")
            else:
                print("*",end="")
        print("")

def pattern8(n):
    for i in range(0,n):
        for j in range(0,2*n-1):
            if(j<n-i-1 or j>= 2*n-(n-i)):
                print(" ", end="")
            else:
                print("*", end="")
        print("")

def pattern9(n):
    for i in range(0,n):
        for j in range(0,2*n-1):
            if(j<i or j>= 2*n -i-1):
                print(" ", end="")
            else:
                print("*", end="")
        print("")

def pattern10(n):
    for i in range(0,n):
        for j in range(0,2*n-1):
            if(j<n-i-1 or j>= 2*n-(n-i)):
                print(" ", end="")
            else:
                if(i%2==0):
                    if(j%2 ==0):
                        print("*", end="")
                    else:
                        print(" ", end="")
                else:
                    if(j%2!=0):
                        print("*", end="")
                    else:
                        print(" ", end="")
        print("")


# pattern1(5)
# pattern2(5)
# pattern3(5)
# pattern4(5)
# pattern5(5)
# pattern6(5)
# pattern7(5)
# pattern8(5)
# pattern9(5)
pattern10(5)