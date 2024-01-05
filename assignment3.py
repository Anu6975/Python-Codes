def printFirst10():
        print("\n********Printing First 10 Digits*********\n")
        for i in range(1,11):
               print(i,end=" ")

def print100():
        print("\n\n********Printing First 100 Digits*********\n")

        for i in range(1,101):
               print(i,end=" ")

def print3Digit():

        print("\n\n********Printing First 3 Digit numbers*********\n")
        for i in range(100,110): 
               print(i,end=" ")

def printEven():
        print("\n\n********Printing Even Number*********\n")
        for i in range(1,101):
               if i%2==0:
                    print(i, end=" ")

def printOdd():
        print("\n\n********Printing Odd*********\n")
        for i in range(1,50):
               if i%2!=0:
                    print(i, end=" ")

def printReverse():
        print("\n\n********Printing in Reverse Order*********\n")
        for i in range(100,1,-1):
               print(i, end=" ")


def table12():
        print("\n\n********Printing table of 12*********\n")
        for i in range(12,121,12):
                 print(i, end=" ")


def ReverseTable12():
        print("\n\n********Printing table of 12 in Reverse*********\n")
        for i in range(120,11,-12):
                 print(i, end=" ")


def printSum():
        print("\n\n********Printing Sum of First 10 Numbers*********\n")
        sum=0
        for i in range(1,11):
                 sum=sum+i
        print(sum)

def printProduct():
        print("\n\n********Printing Product of First 10 Numbers*********\n")
        p=1
        for i in range(1,11):
                 p=p*i
        print(p)


#printFirst10()
#print100()
#print3Digit()
#printEven()
#printOdd()
#printReverse()
#table12()
#ReverseTable12()
#printSum()
#printProduct()
