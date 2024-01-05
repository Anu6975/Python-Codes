def pattern1():
       for i in range(3):
               for j in range(3):
                      print("*",end= " ")
               print("\n")


def pattern2():
       r=1
       for i in range(4):
               for j in range(4):
                      print(r,end= " ")
                      r+=1
               print("\n")

def pattern3():
       for i in range(1,5):
               for j in range(4):
                      print(i,end= " ")
               print("\n")


def pattern4():
       for i in range(4):
               for j in range(1,5):
                      print(j,end= " ")
               print("\n")


def pattern5():
       for i in range(1,5):
               for j in range(i,4+i):
                      print(j,end= " ")
               print("\n")


def pattern6():
       for i in range(4):
               for j in range(5):
                      if(i%2==0):
                            print("#",end= " ")
                      else:
                            print("@",end=" ")
               print("\n")


def pattern7():
       r=1
       for i in range(3):
                   for j in range(3):
                          print(r,end= " ")
                          r+=2
                   print("\n")


def pattern8():
       for i in range(3):
               r=1
               for j in range(3):
                      print(r,end= " ")
                      r+=2
               print("\n")


def pattern9():
       r=1
       for i in range(3):
                   #r=2*i+1
                   for j in range(3):
                          print(r,end= " ")
                          r+=2
                   r-=4
                   print("\n")


def pattern10():
       r=1
       for i in range(4):
                   for j in range(4):
                          print(r,end= " ")
                          r+=2
                   r-=4
                   print("\n")


#pattern1()
#pattern2()
#pattern3()
#pattern4()
#pattern5()
#pattern6()
#pattern7()
#pattern8()
pattern9()
pattern10()
