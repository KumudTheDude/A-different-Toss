import os
import random

j = 0
while j< 10:
    print(" ")
    print(" ")
    print(" ")
    print("                                                âï¸xXxâï¸  ð²   A Different Toss  ð²    âï¸xXxâï¸" )
    print('')
    num = int(input("Enter number here : "))
    a = list(range(0,num))   
    b = random.choice(a) 
    print(" ")
    print("A random number will be selected from the below list:  ðð¼")
    print(" ")
    print(a)
    print(" ")
    print("                                                                                                                                Scroll up for entire list")
    print(" ")
    print("                                        â¨ The Randomly Selected Number is:  ",b," â¨")
    print(" ")
    print(" ")
    if b <num/2:
        print("  ")
        print("                                 ", "Half of", num, " is " ,num/2, "    and    ", b," < ",num/2) 
        print(" ")
        otherinfo = ((num/2  - b)/(num/2))*100
        x = (((num/2 +1)*100)/b)
        probability = (1/num)*100
        print("ð Other Info: ")
        print("Person who selected   MORE  :")
        print("       Lost by (Units) :", (num/2  - b))
        print("       Lost by (%)     :",round(otherinfo,2),"%" )
        print("       - -")
        print("       Increase ",b," by ",round(x-100,2),"% to Win" )
        print("       Probability of this number getting selected: ",round(probability,6), "%")
        print(" ")
        print("                                                 _____________ ")
        print(" ")
        print("                              Result      **ð**|  LESS ð» WINS  |**ð** ")  
        print("                                                 _____________")
    else:
         print("  ")
         print("                       ", b ," is More than half of", num, " which is " ,num/2, "   and   ", b," > ",num/2, " ")
         print(" ")
         print(" ")
         print(" ")
         otherinfo = ((b  - num/2)/(num/2))*100
         x = ((num/2 -1)*100)/b
         probability = (1/num)*100
         print("ð Other Info: ")
         print("Person who selected   LESS :")
         print("       Lost by (Units) :", (b- num/2))
         print("       Lost by (%)     :",round(otherinfo,2),"%" )
         print("       - -")
         print("       Decrease ",b," by ",round(-(100-x),2),"% to Win" )
         print("       Probability of this number getting selected: ",round(probability,6), "%")
         print(" ")
         print("                                               _____________ ")
         print(" ")
         print("                           Result      **ð**|  MORE ð WINS  |**ð** ")  
         print("                                               _____________") 
         print(" ")
