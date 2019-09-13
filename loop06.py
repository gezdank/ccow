M = int(input("M?"))
N = int(input("N?"))

print ( "*" * M)
for i in range(N-2):
    blankspace = " "*(M - 2)
    star = "*" 
    print(star + blankspace + star)

print ( "*" * M)
