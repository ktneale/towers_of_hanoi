#!/usr/bin/python
#
# Based on https://www.youtube.com/watch?v=rVPuzFYlfYE
#
# Finds the correct sequence of moves to solve the 'Towers of Hanoi' problem.
#
# The problem requires shifting a stack of plates from one post (F=from) to another (T=to). 
# A spare post is available to help with the shifting (S=spare).
#
# e.g  
#
#   x       |       |                       |       x       |
#  xxx      |       |                       |      xxx      |
# xxxxx     |       |         becomes       |     xxxxx     |
# --------------------                      --------------------
#   F       T       S                       F       T       S

# Note! You are only allowed to move one plate at a time.
#
# Run using Python

def printMove( fr, to ):
    print('Move from ' + str(fr) + ' to ' + str(to))

def Towers( n, fr, to, spare ):
   if ( n==1 ):
    printMove(fr,to)
   else:
    Towers(n-1,fr,spare,to)
    Towers(1,fr,to,spare)
    Towers(n-1,spare,to,fr)

def main():
    Towers(3,'f','t','s');

main()
