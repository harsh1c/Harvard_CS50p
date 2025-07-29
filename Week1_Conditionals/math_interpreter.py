question = input("Type your input as - a b c \nwhere, 'a' is 1st number , 'b' is the operator , 'c' is the 2nd number \n")

x,y,z = question.split()

if y== '+':
    ans = int(x) + int(z)
    print(float(ans))
elif y== '-':
    ans = int(x) - int(z)
    print(float(ans))
elif y== '*':
    ans = int(x) * int(z)
    print(float(ans))
elif y == '/' :

    ans = int(x) / int(z)
    print(float(ans))