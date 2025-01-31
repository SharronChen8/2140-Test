# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 12:16:58 2025

@author: sharr
"""
    
# Question 1
def right_tri():
    for i in range (6):
        print ("*" *i) # Increase the symbol by the range of i

#==============================================================================
# Question 2
def invert_right():
    for i in range (6,0,-1): # The range starts at 6 with an index of 5 and reduces by 1
        print ("#" * i) # Increase the symbol by the range of i
        
#==============================================================================
# Question 3
def pyramid():
    for i in range (5):
        print (" " * (5-i-1), end="") # Creates the spaces that aligns the pyramid, decreasing by i
        print ("$" * (2*i+1)) # Prints the $ in odd numbers 

#==============================================================================
# Question 4
def invert_pyr():
    for i in range (5):
        print (" " * i, end="") # Creates spaces by the value of i, using end to start a new line in the console
        print ("@" * (9-2*i)) # Reduce the initial 9 symbols in the top row by 2 and i

#==============================================================================
# Question 5
def diamond():
    for i in range (5):
        print (" " * (5-i-1), end="")  # Creates spaces by the value of i, using end to start new lines 
        print ("&" * (2*i+1)) # Increases the symbol by the range of i and 2+1
    for i in range (4): # Because the previous line already sets the max symbols in the row, you only need 4 additional rows
        print (" ", end="") # Creates spaces by the value of i
        print (" " * i, end="") # Creates space so that the 4 rows have space
        print ("&" * (7-2*i)) # Reduce from 7 symbols to the last value in the rnage of i

#==============================================================================
# Question 6
def square():
    for i in range (5):
        print ("%" * (6)) # This will set the symbol range to 6 producing 5 index

#==============================================================================
# Question 7
def right_90 ():
        for i in range (6):
            print (" " * (5-i), end="")  # Reduce i by 5 because you're increasing by increments of 1
            print ("+ " * (i)) # This will print the symbols according to i
            
#==============================================================================
def main():
    print ("Executing question 1.")
    right_tri()
    print ("Executing question 2.")
    invert_right()
    print ("Executing question 3.")
    pyramid()
    print ("Executing question 4.")
    invert_pyr()
    print ("Executing question 5.")
    diamond()
    print ("Executing question 6.")
    square()
    print ("Executing question 7." )
    right_90()
#==============================================================================
main()