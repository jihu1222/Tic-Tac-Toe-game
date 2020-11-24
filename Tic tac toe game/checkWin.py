#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 09:42:27 2020
@author: Dr. Z - modified from https://stackoverflow.com/questions/39922967/python-determine-tic-tac-toe-winner
"""
import numpy as np

'''Requires list of empty lists, with the same shape as the board. For example,
a 3x3 board should have a list like this:
    [[ [1],[],[] ],
     [ [],[],[] ],
     [ [],[],[] ] ]
    
This is best done by using a for loop to create the list. See boardList.py for 
code.'''

def checkRows(scoreBoard):
    '''Looks along a row to see if everything in the row is the same value.
    If the entire row is the same, it returns the value found across the whole row.
    If the entire row is NOT the same, it returns 0.'''
    for row in scoreBoard:
        if len(set(row)) == 1:
            return row[0]
    return 0 # you may want to change this value! (this is the "no-3-in-a-row" "value)

def checkDiagonals(scoreBoard):
    '''Looks along diagonals for the same values thorughout.
    If the entire diagonal is the same (length doesn't matter), this function
    returns the value found on the diagaonal.
    If the entire diagonal is NOT the same, this function returns 0.'''
    if len(set([scoreBoard[i][i] for i in range(len(scoreBoard))])) == 1:
        return scoreBoard[0][0]
    if len(set([scoreBoard[i][len(scoreBoard)-i-1] for i in range(len(scoreBoard))])) == 1:
        return scoreBoard[0][len(scoreBoard)-1]
    return 0 # you may want to change this value! (this is the "no-3-in-a-row" "value)

def checkWin(scoreBoard):
    '''Checks the for the win conditions by looking through the rows and a 
    diagonal in one direction, then rotating the list and looking for rows 
    again (effectively columns and diagonal in the opposite direction).'''
    #transposition to check rows, then columns
    for newBoard in [scoreBoard, np.transpose(scoreBoard)]:
        result = checkRows(newBoard)
        if result:
            return result
    return checkDiagonals(scoreBoard)


# Uncomment everything below to test this code.
# Add values into this list of lists to see the different outcomes
# a = [['', '', ''], # 'X','X','X'
#      ['', '', ''],
#      ['', '', '']]


# # You'll write something like this for your end game scenario
# if checkWin(a)=='X':
#     print('X won!')
# elif checkWin(a)=='O':
#     print('O won!')
# elif checkWin(a)=='':
#     print(checkWin(a))
#     print('Empty!')
# elif checkWin(a)==0: 
#     print('Stalemate!')