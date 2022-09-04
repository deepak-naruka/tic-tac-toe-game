
a=True
b=True
add = True
l1= ["1","2","3"]
l2= ["4","5","6"]
l3= ["7","8","9"]
c1 =["--","--","--","--",'--']

import random
numlst = []

while len(numlst) < 10:
    rnd = random.randint(0, 9)
    if rnd in numlst:
        continue
    numlst += [rnd]


def printing():
    for i in l1:
        print(" ",i,'' ,end=' ',sep='|')
    print()
    for e in c1:
        print(e,'',end='',sep='__')
    print()
    for i in l2:
        print(" ",i,'', end=' ',sep='|')
    print()
    for e in c1:
        print(e,'',end='',sep='__')
    print()
    for i in l3:
        print(' ',i,'', end=' ',sep='|')
    print()





print("welcome to the tic tac toe game ")
print('its a multiplayer game ')
printing()
while add:

    while b:
        x1 = int(input("x player enter the position  -->  "))
        if x1 == 1 and l1[0] != 'x' and l1[0] != 'o':
            l1[0] = 'x'
            break
        elif x1 == 2 and l1[1] != 'x' and l1[1] != 'o':
            l1[1] = 'x'
            break
        elif x1 == 3 and l1[2] != 'x' and l1[2] != 'o':
            l1[2] = 'x'
            break
        elif x1 == 4 and l2[0] != 'x' and l2[0] != 'o':
            l2[0] = 'x'
            break
        elif x1 == 5 and l2[1] != 'x' and l2[1] != 'o':
            l2[1] = 'x'
            break
        elif x1 == 6 and l2[2] != 'x' and l2[2] != 'o':
            l2[2] = 'x'
            break
        elif x1 == 7 and l3[0] != 'x' and l3[0] != 'o':
            l3[0] = 'x'
            break
        elif x1 == 8 and l3[1] != 'x' and l3[1] != 'o':
            l3[1] = 'x'
            break
        elif x1 == 9 and l3[2] != 'x' and l3[2] != 'o':
            l3[2] = 'x'
            break
        else:
            print('position',x1,' occupied again give the value of x')
    printing()
    if l1[0]==l2[0]==l3[0]=='x' or l1[1]==l2[1]==l3[1]=='x' or l1[2]==l2[2]==l3[2]=='x' or l1[0]==l1[1]==l1[2]=='x' or l2[0]==l2[1]==l2[2]=='x' or l3[0]==l3[1]==l3[2]=='x' or l1[0]==l2[1]==l3[2]=='x' or l1[2]==l2[1]==l3[0]=='x':
        print("x player won the game")
        break
    if (l1[0]=='x' or l1[0]=='o')  and (l2[0]=='x' or l2[0]=='o') and (l3[0] =='x' or l3[0] == 'o') and (l1[1]=='x' or l1[1]=='o')  and (l2[1]=='x' or l2[1]=='o') and (l3[1] =='x' or l3[1] == 'o') and (l1[2]=='x' or l1[2]=='o')  and (l2[2]=='x' or l2[2]=='o') and (l3[2] =='x' or l3[2] == 'o'):
        print('its a tie better luck next time')
        break
    while a:
        o1 = int(input('o player enter the position  -->  '))
        if o1 == 1 and l1[0] != 'x' and l1[0] != 'o':
            l1[0] = 'o'
            break
        elif o1 == 2 and l1[1] != 'x' and l1[1] != 'o':
            l1[1] = 'o'
            break
        elif o1 == 3 and l1[2] != 'x' and l1[2] != 'o':
            l1[2] = 'o'
            break
        elif o1 == 4 and l2[0] != 'x' and l2[0] != 'o':
            l2[0] = 'o'
            break
        elif o1 == 5 and l2[1] != 'x' and l2[1] != 'o':
            l2[1] = 'o'
            break
        elif o1 == 6 and l2[2] != 'x' and l2[2] != 'o':
            l2[2] = 'o'
            break
        elif o1 == 7 and l3[0] != 'x' and l3[0] != 'o':
            l3[0] = 'o'
            break
        elif o1 == 8 and l3[1] != 'x' and l3[1] != 'o':
            l3[1] = 'o'
            break
        elif o1 == 9 and l3[2] != 'x' and l3[2] != 'o':
            l3[2] = 'o'
            break
        else:
            print('position occupied again give the value of o')
    printing()
    if l1[0]==l2[0]==l3[0]=='o' or l1[1]==l2[1]==l3[1]=='o' or l1[2]==l2[2]==l3[2]=='o' or l1[0]==l1[1]==l1[2]=='o' or l2[0]==l2[1]==l2[2]=='o' or l3[0]==l3[1]==l3[2]=='o' or l1[0]==l2[1]==l3[2]=='o' or l1[2]==l2[1]==l3[0]=='o':
        print("o player won the game ")
        break