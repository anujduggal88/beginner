#
#                           FILE            :       calculator.py
#                           AUTHOR          :       ANUJ DUGGAL
#                           COLLABORATORS   :       ANIRUDH CHINTHA
#                           DESCRIPTION     :       Calculator Program
#                           DATE CREATED    :       11 SEPT, 2015
#                           DATE MODIFIED   :       11 SEPT, 2015
#                           VERSION         :       1.1
#

#
#   ------------------ ANIRUDH TO ADD FOLLOWING FUNCTIONS ----------------
#   ADDITION
#   SUBTRACTION
#   MULTIPLICATION
#   DIVISION
#   ----------------------------------------------------------------------

import math

def display_choices():
    choice = -1
    print "Pick Your Choice:"
    print "1. Adding 2 numbers."
    print "2. Subtract 2 numbers"
    print "3. Multiply 2 numbers"
    choice = int(raw_input())
    return choice

def main():
    print "*** CALCULATOR ***"
    choice = display_choices()
    if choice is -1:
        print "PROGRAM NOT COMPLETED"
    if choice is 1:
         add()
    if choice is 2:
        sub()
    if choice is 3:
        mul()
def take_numbers():
    print "Enter the 2 numbers."
    input1 = int(raw_input("Enter your 1st number "))
    input2 = int(raw_input("Enter your 2nd number "))
    return input1,input2
def add():
    inp1,inp2 = take_numbers()
    out = inp1 + inp2
    print out
def sub():
    inp1,inp2 = take_numbers()
    out = inp1 - inp2
    print out
def mul():
    inp1,inp2 = take_numbers()
    out = inp1 * inp2
    print out
main()
