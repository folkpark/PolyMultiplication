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


def dAndCVersion(polyA, polyB):
    polyC = []

    return polyC

nSquared_Outfile = open('nSquared.txt', 'w')
nSquared_Outfile.write("Hello Jack")

dAndC_Outfile = open('DC.txt', 'w')
dAndC_Outfile.write("Hello Parker")

#Get some polynomials with random coefficients
polyA = []
a_degree = 3
for i in range(a_degree):
    polyA.append(randint(0,9))

polyB = []
b_degree = 3
for j in range(b_degree):
    polyB.append(randint(0, 9))