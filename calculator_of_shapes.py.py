class circle:
    __color = "blue"

    def mohite_circle(self, x):
        x = 2 * x
        pi = 3.1415926535
        A = (x * pi)
        print("P of circlr is:",A)
        A = "\n" + str(A)
        s(A)

    def masahate_cicle(self, x):
        x = x ** 2
        pi = 3.1415926535
        A = (pi * x)
        print("S of cicle is:",A)
        A = "\n" + str(A)
        s(A)

class moraba:
    __color = "blue"

    def mohit_moraba(self, x):
        A = (4 * x)
        print("P of square is:",A)
        A = "\n" + str(A)
        s(A)

    def masahat_moraba(self, x):
        A = (x ** 2)
        print("S of square is:",A)
        A = "\n" + str(A)
        s(A)

class mostatil:
    __color = "blue"

    def mohit_mostatil(self, x, y):
        A = ((2 * x )+ (2 * y))
        print("P of mos is:",A)
        A = "\n" + str(A)
        s(A)

    def masahat_mostatil():
        A = (x * y)
        print("S of mos is:",A)
        A = ("\n" + str(A))
        s(A)

class mosalas:
    __color = "blue"

    def masahat_mosalas(self, x, y):
        A = ((x * y) / 2)
        print("S of mosalas:",A)
        A = ("\n" + str(A))
        s(A)

    def mohit_mosalas(self,x,y,z):
        A = (x + y + z)
        print("P of mosalas:", A)
        A = "\n" + str(A)
        s(A)

def s(A):
    file = open("PSV.txt", "a")
    file.write(A)
    file.close()

def r():
    file = open("PSV.txt", "r")
    count = file.read()
    print(count)
    file.close()

#جدا کننده قسمت پایینی از بالایی_____________________________________________________________________________
print("If you will want see history.in front of all qustion enter '$history'")
a = input("1 Square_2 Rectangle_3 Circle_4 triangle:")
if a == "1":
    b = input("1 Environment_2 Area:")
    if b == "1":
        x = int(input("Enter the size of the square side:"))
        moraba.mohit_moraba(2 , x)
    elif b == "2":
        x = int(input("Enter the size of the square side"))
        moraba.masahat_moraba(2 , x)
    else:
        r()
elif a == "2":
    c = input("1 Environment_2 Area:")
    if c == "1":
        x = int(input("Enter the size of the shape length:"))
        y = int(input("Enter the width of the shape:"))
        mostatil.mohit_mostatil(2, x , y)
    elif c == "2":
        x = int(input("Enter the size of the shape length"))
        y = int(input("Enter the width of the shape:"))
        mostatil.masahat_mostatil(2, x, y)
    else:
        r()
elif a == "3":
    d = input("1 Environment_2 Area:")
    if d == "1":
        x = int(input("Insert the radius of the circle:"))
        circle.mohite_circle(2, x)
    elif d == "2":
        x = int(input("Insert the radius of the circle:"))
        circle.masahate_cicle(2, x)
    else:
        r()
elif a == "4":
    e = input("1 Environment_2 Area:")
    if e == "1":
        z = int(input("enter the first side:"))
        x = int(input("enter the seccond side:"))
        y = int(input("enter the third side:"))
        mosalas.mohit_mosalas(2,x,y,z)
    elif e == "2":
        x = int(input("Enter Circle rule:"))
        y = int(input("Enter Circle height:"))
        mosalas.masahat_mosalas(2,x, y)
else:
    r()
