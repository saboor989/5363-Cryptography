###############################################
# Name      : SABOOR AHMED SIDDIQIE
# Class     : CMPS 5363 Cryptography
# Date      : 3 Aug 2015
# Program 3 : Elliptical Curve Encryption
###############################################


#importing Fraction , decimal library
#importing drawCurve program to draw curve
from fractions import Fraction
from decimal import Decimal
import argparse
import sys
import drawCurve as dc


# Command to run the program
#$ python main.py -x1 1 -y1 1 -x2 2 -y2 -3 -a 1 -b -1


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-x1", "--x1", dest="x1", help="x1 for slope")
    parser.add_argument("-y1", "--y1", dest="y1", help="y1 for slope")
    parser.add_argument("-x2", "--x2", dest="x2", help="x2 for slope")
    parser.add_argument("-y2", "--y2", dest="y2",help="y2 for slope")
    parser.add_argument("-a", "--a", dest="a", help="Part 'a' of elliptical curve: y^2 = x^3 + ax + b")
    parser.add_argument("-b", "--b", dest="b", help="Part 'b' of elliptical curve: y^2 = x^3 + ax + b")
    
    args = parser.parse_args()
    #print("the args is :",args.x1)
    
    a=int(args.a)
    b=int(args.b)
    
    y1=Fraction(args.y1)
    y2=Fraction(args.y2)
    x1=Fraction(args.x1)
    x2=Fraction(args.x2)
    slope=0
    slopey=y2-y1
    slopex=x2-x1
    slope=slopey/slopex
    print("the slope:",slope)

  
    #The x3 calculation
    x3=slope*slope-x1-x2
    #x3=Fraction(x3).limit_denominator(1000)
    #print("the x3 is :",x3)
    
    #The y3 calculation
    x123=x3-x1
    y3=slope*x123+y1
    #y3=Fraction(y3).limit_denominator(1000)
    #print("the y3 is :",y3)
    
    #checking the compatiblility of points and if compatible then generating curve
    ret=dc.compatible(x1,y1,x2,y2,x3,y3,a,b)
    if(ret==1):
        print("The points are compatible")
        dc.drawcurve(a,b,x1,y1,x2,y2,x3,y3,slope,a,b)
    else:
        print("The points are not compatible")
    

    

if __name__ == '__main__':
    main()
