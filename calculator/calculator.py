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
    return choice

def main():
    print "*** CALCULATOR ***"
    choice = display_choices()
    if choice is -1:
        print "PROGRAM NOT COMPLETED"
def take_numbers():
    input1 = int(raw_input("Enter your 1st number"))
    input2 = int(raw_input("Enter your 2nd number"))
    return input1,input2
main()
