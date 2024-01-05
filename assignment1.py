print("Hello, Its my 2nd Program ")


def isMax():
     print("Enter two numbers: ")
     a=int(input())
     b=int(input())
     if(a>b):
         print(a, "is Maximum than ",b)
     else:
         print(b, "is Maximum than ",a)



def isNegative():
     print("Enter a Number: ")
     a=int(input())

     if(a<0):
         print(a, "is Negative Number")
     else:
         print(a, "is Positive Number")


def isEvenOdd():
     print("Enter a number: ")
     a=int(input())

     if(a%2==0):
         print(a, "is an Even Number")
     else:
         print(a, "is Odd Number")


def isdiv5():
     print("Enter a number: ")
     a=int(input())

     if(a%5==0):
         print(a, "is Divisible of 5")
     else:
         print(a, "is not Divisible of 5")


def day():
     print("Enter a number between 0 and 6: ")
     a=int(input())

     if a in range(0,7):
         if a==0:
             print("Monday")
         elif a==1:
             print("Tuesday")
         elif a==2:
             print("Wednesday")
         elif a==3:
             print("Thursday")
         elif a==4:
             print("Friday")
         elif a==5:
             print("Saturday")
         elif a==6:
             print("Sunday")
     else:
             print("Entered Number is not Between 0 and 6")



def isAlphabet():

     print("Enter data: ")
     a=input()

     if 'a'<=a<='z' or 'A' <= a<= 'Z':
        print(a, "is an Alphabet") 
     else:
        print(a," is not an Alphabet")


def isGreater10():
     print("Enter a Number: ")
     a=int(input())

     if(a<10):
        print(a, " is not Greater than 10")
     elif(a>10):
        print(a," is Greater than 10")
     elif(a==10):
        print(a, " is Equals to 10")

def isVowel():
     print("Enter a Character: ")
     a=input()
     a=a.lower()
     if a=='a'or a=='e' or a=='o' or a=='u' or a=='i':
        print(a,"is Vowel")
     else:
        print(a, "is Consonant")


def isLeap():
     a=int(input("Enter a year: "))
     if (a%4==0 and a%100!=0) or a%400==0 :
        print(a, "is a Leap Year")
     else:
        print(a,"is not Leap Year")

def month():
    a=int(input("Enter Month Number: "))
    dict={
           1: "January is a 31-day month",
           2: "February is a 28-day month",
           3: "March is a 31-day month",
           4: "April is a 30-day month",
           5: "May is a 31-day month",
           6: "June is a 30-day month",
           7: "July is a 31-day month",
           8: "August is a 31-day month",
           9: "September is a 30-day month",
           10: "October is a 31-day month",
           11: "November is a 30-day month",
           12: "December is a 31-day month"
            }
    n=dict.get(a,".. ") 
    if a not in range(1,13):
          print("Enter Valind Month Number!!")
    else:
          print(f"{n}") 

#isMax()
#isNegative()
#isEvenOdd()
#isdiv5()
#day()
#isAlphabet()
month()
#isGreater10()
#isVowel()
#isLeap()
