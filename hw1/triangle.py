# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 19:54:28 2021

@author: weige
"""
import unittest

def classifyTriangle(a,b,c):
    try:
        a = float(a)
    except:
        print("Input A is not a number")
        return "Error"
    try:
        b = float(b)
    except:
        print("Input B is not a number")
        return "Error"
    try:
        c = float(c)
    except:
        print("Input C is not a number")
        return "Error"
    if a > 0 and b > 0 and c > 0:
        if a + b > c and a + c > b and b + c > a:
            if a == b == c:
                return "Equilateral"
            elif a == b or a == c or b == c:
                return "Isoceles"
            elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
                return "Right"
            else:
                return "Scalene"
    return "Not a Triangle"    

def runClassifyTriangle(a,b,c):
    print('classifyTriangle(',a, ',', b, ',', c, ') = ',classifyTriangle(a,b,c),sep="")
    
class TestTriangles(unittest.TestCase):
    def testSet1(self):
        self.assertEqual(classifyTriangle(3,4,-1),"Not a Triangle","Testing negative input")
        self.assertEqual(classifyTriangle(3,4,'five'),"Error","Testing string input")
        self.assertEqual(classifyTriangle(1,4,2),"Not a Triangle","Testing invalid triplet")
        
    def testSet2(self):
        self.assertEqual(classifyTriangle(0.3,0.5,0.4),"Right","Testing Right triangle and float input")
        self.assertEqual(classifyTriangle(3,3,3),"Equilateral","Testing Equilateral")
        self.assertEqual(classifyTriangle(3,3.0001,3.0002),"Scalene","Testing Scalene")
        self.assertEqual(classifyTriangle(1,2,2),"Isoceles","Testing Isoceles")
        
if __name__  == '__main__':
    unittest.main(exit=False)