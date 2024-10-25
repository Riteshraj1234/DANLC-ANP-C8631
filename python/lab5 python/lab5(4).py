#1
print("first")
for i in range(1, 6):
    for j in range(i):
        print(i, end=' ')
    print()

#2
print("second")
for i in range(1, 6):
    for j in range(i):
        print(j+1, end=' ')
    print()

#3
print("third")
n = 1
for i in range(1,6):
    for j in range(i):
        print(n,end=(''))
        n+=1
    print()


#4
print("fourth")
for i in range(1, 6):
    for j in range(i,0,-1):
        print(j, end='')
    print()

#5
print("fifth")
for i in range(1, 6):
    print(' ' * (5 - i), end='')
    for j in range(1, i+1):
        print(j, end='')
    print()


#6
print("sixth")
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end='')
    print()

#7
print("seventh")
for r in range(1,6):
    for s in range(5,r,-1):
        print(end="  ")
    for c in range(1,r+1):
        print(c, end=" ")
    for c1 in range(c-1,0,-1):
        print(c1,end=" ")
    print()


#8
print("eighth")
rows = int(input("enter number of rows:"))
for r in range(1,rows+1):
    for c in range(1,r+1):
        if c == 1 or c == r or r == rows:
           print(c, end=" ")
        else:
           print(end="  ")
    print()


#9
print("nineth")
rows = int(input("enter number of rows:"))
for r in range(1,rows+1):
    for c in range(1,r+1):
        if c == 1 or c == r or r == rows:
           print(c, end=" ")
        else:
           print(end="  ")
    print()

#10
print("tenth")
for r in range(1,6):
    for s in range(5,r,-1):
        print(end="  ")
    for c in range(1,r+1):
        print(c,end=" ")
    for c1 in range(c-1,0,-1):
        print(c1,end=" ")
    print()
for r in range(4,0,-1):
    for s in range(5,r,-1):
        print(end="  ")
    for c in range(1,r+1):
        print(c,end=" ")
    for c1 in range(c-1,0,-1):
        print(c1,end=" ")
    print()


    #11
print("eleventh")
for r in range(5,0):
    for s in range(5,r,1):
        print(end="  ")
    for c in range(5,r+1):
        print(c,end=" ")
    for c1 in range(c-1,0,1):
        print(c1,end=" ")
    print()









#last
print("last question")

for r in range(65,91):
    for s in range(91,r,-1):
        print(end="  ")
    for c in range(65,r+1):
        print(chr(c), end=" ")
    for c1 in range(c-1,64,-1):
         print(chr(c1),end=" ")
    print()


