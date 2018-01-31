'''
Author: Parker Folkman
Date: 1/26/2018
Overview: This program implements the divide and 
        conquer version of polynomial multiplication. 
'''

import math
from random import randint
from timeit import default_timer as timer


#tested successfully against WolframAlpha.com
def nSquaredVersion(polyA, polyB):
    #create a blank list and initialize it to zero
    product = []
    for q in range(0,(len(polyA)+len(polyB)-1)):
        product.append(0)

    #multiply each term by every term in the other polynomial
    for i in range(0,len(polyA)):
        for j in range(0,len(polyB)):
            product[i+j] = product[i+j] + (polyA[i]*polyB[j])
    return product


def dAndCVersion(polyA, polyB, n):
    product = [] #need to remove this because of recursion

    return product

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

#this code prints the polynomials to the screen
# in order to test that the functions work
print("First polynomial: "+str(polyA).strip('[]'))
print("Second polynomial: "+str(polyB).strip('[]'))
product = nSquaredVersion(polyA,polyB)
print("Product polynomial: "+str(product).strip('[]'))



