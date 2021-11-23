# Import
import sys
import time

# Functions
def printy(text, delay=0.05): 
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Code
selection=int(input("[1] Calculator [2] Counting"))

if selection==1:
  
 printy("You can calculate 4 types of method")
 time.sleep(1)
 printy("Please type the number of the method you want")
 time.sleep(1)
 x = int(input("[1] Addition [2] Subtraction [3] Multiplication   [4] Division :"))

#Addition
 if x == 1:
  printy("Ok, so you want the Additon method")
  time.sleep(1)
  printy("Look carefully the format is like this")
  time.sleep(1)
  printy("“ a+b=c　“")
  time.sleep(1)
  a = int(input("What you want <a> to be? :"))
  b = int(input("What you want <b> to be? :"))
  printy("Calculating....")
  time.sleep(2)
  print("Aha! The answer is", a + b)

#Subtraction
 elif x == 2:
  printy("Ok, so you want the Subtraction method")
  time.sleep(1)
  printy("Look carefully the format is like this")
  time.sleep(1)
  printy("“ a-b=c　“")
  time.sleep(1)
  a = int(input("What you want <a> to be? :"))
  b = int(input("What you want <b> to be? :"))
  printy("Calculating....")
  time.sleep(2)
  print("Aha! The answer is", a - b)
  
#Multiplication
 elif x == 3:
  printy("Ok, so you want the Multiplication method")
  time.sleep(1)
  printy("Look carefully the format is like this")
  time.sleep(1)
  printy("“ a×b=c　“")
  time.sleep(1)
  a = int(input("What you want <a> to be? :"))
  b = int(input("What you want <b> to be? :"))
  printy("Calculating....")
  time.sleep(2)
  print("Aha! The answer is", a * b)

#Division
 elif x == 4:
  printy("Ok, so you want the Division method")
  time.sleep(1)
  printy("Look carefully the format is like this")
  time.sleep(1)
  printy("“ a÷b=c　“")
  time.sleep(1)
  a = int(input("What you want <a> to be? :"))
  b = int(input("What you want <b> to be? :"))
  printy("Calculating....")
  time.sleep(2)
  try:
    ans = a/b
    print("Aha! The answer is", a / b)
  except:
      printy("An error has been detected, pleasetry again")


#Error
 else:
  printy("Hey! This is not a valid number!")
  printy("Please try again")

if selection==2:
 for i in range(999999999999999):
   print(i)
   time.sleep(1)  


