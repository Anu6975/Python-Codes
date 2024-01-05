def printN():
      a=int(input("\n\nEnter Starting Range: "))
      b=int(input("Enter Ending Range: "))
      print("***********Printing n Numbers********\n")
      for i in range(a,b+1):
            print(i,end=" ")

def printEven():
      a=int(input("\n\nEnter Starting Range: "))
      b=int(input("Enter Ending Range: "))
      print("***********Printing Even Numbers with Given Range***********\n")
      for i in range(a,b+1):
            if(i%2==0):
                  print(i,end=" ")
def printSum():
      a=int(input("\n\nEnter Starting Range: "))
      b=int(input("Enter Ending Range: "))
      print("***********Printing Sum of n Numbers********\n")
      sum=0
      for i in range(a,b+1):
           sum=sum+i
      print(sum,end=" ")

def printChar():
      print("\n\nEnter the Range of Ascii Value of Characters: ")
      a=int(input("Enter Starting Range: "))
      b=int(input("Enter Ending Range: "))
      print("***********Printing Characters of Ascii Values***********\n")
      if a>=65<b<=90 or a>=97<b<=122:
            for i in range(a,b+1):
                   print(f"The Character of Ascii Value {i} is {chr(i)}")
      else:
            print("Invalid Range!!")


def Divby7():
      print("\n\n***********Printing Numbers Dividible by 7 and not 3**********\n")
      for i in range(1,100):
            if i%7==0 and i%3!=0:
                  print(i,end=" ")

def printAscii():
      print("\n\nEnter the Character Range: ")
      a=input("Enter Starting Range: ")
      b=input("Enter Ending Range: ")
      print("\n***********Printing Ascii of Given Range**********\n")
      for i in range(ord(a),ord(b)+1):
            print(f"ASCII Value of {chr(i)} is {i}")

def printPositive():
      a=int(input("\n\nEnter Starting Range: "))
      b=int(input("Enter Ending Range: "))
      print("\n***********Printing only Positive Numbers**********\n")
      if(a<0):
          a=1
      for i in range(a,b+1):
            print(i,end=" ")

def divby3n5():
      a=int(input("\n\nEnter Starting Range: "))
      b=int(input("Enter Ending Range: "))
      print("\n***********Printing 3 n 5 Divisible********\n") 
      for i in range(a,b+1):
            if i%3==0 and i%5==0:
                   print(i,end=" ")

def countNegative():
      a=int(input("\n\nEnter Starting Range: "))
      b=int(input("Enter Ending Range: "))
      print("\n\n***********Counting Negative Numbers of Given Range*********\n")
      count=0
      for i in range(a,b+1):
            if i<0:
                  count+=1
      print("Count of Negative Numbers is: ",count)


def productOddCount():
      a=int(input("\n\nEnter Starting Range: "))
      b=int(input("Enter Ending Range: "))
      print("\n***********Printing product of count of Odd Numbers********\n")
      count=0
      for i in range(a,b+1):
            if(i%2!=0):
                 count+=1
      c=count**count
      print(c)


#printN()
#printEven()
#printSum()
#printChar()
#Divby7()
#printAscii()
#printPositive()
divby3n5()
countNegative()
productOddCount()
