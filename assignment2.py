def isDiv4n5():
     a=int(input("Enter the Number: "))
     if a%4==0 and a%5==0:
            print(f"{a} is divisible by 4 and 5 both")
     else:
            print(f"{a} is not divisible by 4 and 5 both")


def isRightangleTri():
     a=int(input("Enter the First Angle: "))
     b=int(input("Enter the Second Angle: "))
     c=int(input("Enter the third Angle: "))
     temo=0
     if (a+b+c)==180 and (a==90 or b==90 or c==90):
            print("Triangle is Right Angled Triangle")
     else:
            print("Triangle is not Right Angled Triangle")


def isSumEven():
     a=int(input("Enter the First Number: "))
     b=int(input("Enter the Second Number: "))

     if a+b%2==0:
            print(f"{a+b} is Even")
     else:
            print(f"{a+b} is Odd")


def isAvl():
     a=int(input("Enter a Number to Check: "))
     b=[10,20,30,40,50]

     if a in b:
            print("Available")
     else:
            print("No Output!")


def PrintEven():
     a=int(input("Enter a  Number: "))

     if a%2==0:
            for i in range(0,a):
                 print("Core2web")
     else:
            print("No Output")



def isOdd():
     a=int(input("Enter the a Number: "))

     if a%2!=0:
            print(f"{a} is Odd")



def OddSum():
     a=int(input("Enter the First Number: "))
     b=int(input("Enter the Second Number: "))

     if a%2!=0 or b%2!=0:
            print(f"Sum is {a+b}")
     else:
            print("No Output")



def isasciiEven():
     a=input("Enter a Charater: ")

     if ord(a)%2==0:
            print(f"{a}")
     else:
            print("No Output")


def asciiOdd():
     a=input("Enter the First Charater: ")
     b=input("Enter the Second Character: ")

     if ord(a)%2!=0 and ord(b)%2!=0:
            print(f"{ord(a)+ord(b)}")
     else:
            print("No Output")


def isModThree():

     a=int(input("Enter a Number: "))

     if a%8==3:
            print("3")
     else:
            print("No Output")

#isDiv4n5()
#isRightangleTri()
#isSumEven()
#isAvl()
#PrintEven()
#isOdd()
#OddSum()
#isasciiEven()
#asciiOdd()
#isModThree()
