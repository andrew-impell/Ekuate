# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 20:08:23 2013

@author: andrew

Simple Python program to solve certain differential equtions



4/16/13 [[Will input an option to choose different equations from a list and then 
add constants. Will need to define each equation as a procedure (e.g. eqn_1(),eqn_2()
etc...) or we would define lines 15-69 as their own function call.
From a list
(1) Ay''+ By' + Cy + D = E
(2) Ay''' + ... etc

We would ask user for input and direct to appropriate procedure
ex.

if user_answer == 2:
    eqn_2()
(All proced. are empty becaus all data is inputed within)]]

5/4/13
Implemented main() to choose different equation solvers


"""

from math import sin

print 79 * "="
print 'Differential Equation Solver'
print 79 * "="

def main():
    print """
    Choose an form of equation:
        (1) Ay' + By = C or 0
        (2) Ay'' + By' + Cy = 0
    """
    choice = int(raw_input("Enter choice: "))
    if choice == 1:
        choice1()
    if choice == 2:
        choice2()
    return 0
    
    
def choice1():
    a = float(raw_input("Enter A: ")) #Get input from user on different varibles

    b = float(raw_input("Enter B: "))

    c = float(raw_input("Enter C: "))
    
    val = float(raw_input("Enter x value to approximate: "))
    
    init = float(raw_input("Enter inital conditions (C₁): "))
    
    cons = raw_input("Constant? (Y/N): ") #Yes: there is a constant (Will querie later) No: There is no ccnstant
    
    """

    Define different procedures for equations with or without
    constants

    """
    def find_value(a,b,c,val,init): #if there is no constant...
        e = 2.718281828
        
        fin = c/2.0 
        qe = (e**((-b*val)/a))
        me = fin * qe
        
        
        print 80 *'='
        print "The value for x at y(%i) of %iy'+%iy = %i with c₁ = %i is %f" %(val,a,b,c,init,me)
        print 80 * '='
        return 0
    
    def find_value_constant(a,b,c,val,init,con_a): #if there is a constant...
        e = 2.718281828   
        fin = c/2.0 
        qe = (e**((-b*val)/a)) + (c - con_a)/b
        me = fin * qe
        
        print 80 *'='
        print "The value for x at y(%i) of %iy'+%iy + %i = %i with c₁ = %i is %f" %(val,a,b,con_a,c,init,me)
        print 80 * '='
        return 0
        
    if cons == "Y": #determine from user input if there is a constant and compute results
        
        con_a = float(raw_input("Enter constant")) #Get constant from user
        find_value_constant(a,b,c,val,init,con_a) #Compute final value
        
    else:
    
        find_value(a,b,c,val,init) #Compute final value with no constant
        
def choice2():
    
    a = float(raw_input("Enter A: ")) #Get input from user on different varibles

    b = float(raw_input("Enter B: "))

    c = float(raw_input("Enter C: "))
    
    val = float(raw_input("Enter x value to approximate: "))
    
    init = float(raw_input("Enter inital conditions (C₁): "))
    
    cons = raw_input("Constant? (Y/N): ") #Yes: there is a constant (Will querie later) No: There is no ccnstant
    
    


main()
