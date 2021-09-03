jk = input('Type the word Python? ')
jk_list = list(jk)
jk_list.remove(jk_list[3])
jk_list.remove(jk_list[4])
jk_list.reverse()
jkSt = ''.join(jk_list)
print(' ', jkSt)

x = int(input('Type a one or two digit number? '))
print('x', '=', x)
y = int(input('Type a one or two digit number? '))
print('y', '=', y)
z = x + y
print('x + y', '= z =', z)
z = x - y
print('x - y', '= z =', z)
z = x / y
print('x / y', '= z =', z)
z = x * y
print('x * y', '= z =', z)

jk = input('Type a sentence using the word Python? ')
print(' ', jk)

A = 94;
B = 84;
C = 74;
D = 64;
F = 60;

grade = int(input('Type a number between 0 and 100 to see letter grade ? '))
if( grade >= 94):
    print('A')
elif (A > grade >= 90):
    print('A-')
else:
    if( 90 > grade >= 87):
        print('B+')
if (87 > grade >= B):
        print('B')
elif (B > grade >= 80):
    print('B-')
else:
    if( 80 > grade >= 77):
        print('C+')
if( 77 > grade >= C):
        print('C')
elif (C > grade >= 70):
        print('C-')
else:
    if( 70 > grade >= 67):
        print('D+')
if (67 > grade >= D):
        print('D')
elif (D > grade >= 60):
        print('D-')
else:
    if( grade < F):
        print('F')
