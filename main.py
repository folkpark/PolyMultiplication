'''
Author: Parker Folkman
Date: 1/26/2018
Overview: This program implements the divide and 
        conquer version of polynomial multiplication. 
'''

import math
from random import randint
from timeit import default_timer as timer


def nSquaredVersion(polyA, polyB):
    polyC = []

    return polyC


def dAndCVersion(polyA, polyB, n):
    polyC = [] #need to remove this because of recursion

    return polyC

#function to split a list in half
def split(A):
    mid = len(A)/2
    left = A[:mid]
    right = A[mid:]
    splitLists = [left,right]
    return splitLists

#Create output files
nSquared_Outfile = open('nSquared.txt', 'w')
dAndC_Outfile = open('DC.txt', 'w')

#Get some polynomials with random coefficients
degree = 3  #polynomials are of same degree
polyA = []
for i in range(degree):
    polyA.append(randint(0,9))

polyB = []
for j in range(degree):
    polyB.append(randint(0, 9))