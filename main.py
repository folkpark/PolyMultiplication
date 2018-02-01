'''
Author: Parker Folkman
Date: 1/26/2018
Overview: This program implements the divide and 
        conquer version of polynomial multiplication and compares
        the running time to the known O(n^2) version. 
Code also available online at:
https://github.com/folkpark/PolyMultiplication
'''

import math
import operator
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


def recPolyMult(polyA, polyB, n):
    if n==1:
        return polyA[0]*polyB[0]
    else:
        d = int(math.ceil(n/2) )   # Ceiling of n/2
        aSplit = split(polyA) # split A into two sublists
        A_1 = aSplit[0]       # Assign A_1 to the left sublist
        A_2 = aSplit[1]       # Assign A_2 to the right sublist
        bSplit = split(polyB) # split B into two sublists
        B_1 = bSplit[0]       # Assign B_1 to the left sublist
        B_2 = bSplit[1]       # Assign B_2 to the right sublist

        R = recPolyMult(A_2, B_2, d)
        S = recPolyMult(A_1 + A_2, B_1 + B_2, d)
        T = recPolyMult(A_1, B_1, d)


        for i in range(0,(n-1)):
            if isinstance(T, int):
                recProdList[i] = T
            else:
                recProdList[i] = T[i]
            if isinstance(S,int) and isinstance(R,int) and isinstance(T,int):
                recProdList[i+d] = S - R - T

            if isinstance(R,int):
                recProdList[i+(2*d)] = R
            else:
                recProdList[i + (2 * d)] = R[i]

        return recProdList

#function to split a list in half
def split(A):
    mid = int(len(A)/2)
    left = A[:mid]
    right = A[mid:]
    splitLists = [left,right]
    return splitLists

#Create output files
nSquared_Outfile = open('nSquared.txt', 'w')
dAndC_Outfile = open('DC.txt', 'w')

#Get some polynomials with random coefficients
degree = 4  #polynomials are of same degree
polyA = []
for i in range(degree):
    polyA.append(randint(0,9))
polyB = []
for j in range(degree):
    polyB.append(randint(0, 9))

# this code prints the polynomials to the screen
# in order to test that the functions work
print("First polynomial: "+str(polyA).strip('[]'))
print("Second polynomial: "+str(polyB).strip('[]'))
product = nSquaredVersion(polyA,polyB)
print("Product polynomial: "+str(product).strip('[]'))

recProdList = []
for q in range(0, (len(polyA) + len(polyB) - 1)):
    recProdList.append(0)

final = recPolyMult(polyA, polyB, degree)
print("Rec polynomial: "+str(final).strip('[]'))

print("Program Terminating")



