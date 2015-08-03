###############################################
# Name      : SABOOR AHMED SIDDIQIE
# Class     : CMPS 5363 Cryptography
# Date      : 3 Aug 2015
# Program 3 : Elliptical Curve Encryption
###############################################


#importing numpy and matplotlib for generating curve
import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction


def compatible(x1,y1,x2,y2,x3,y3,a,b):
    #calculating and checking compatibility and return 1 if compatible else 0
    cy1=y1*y1
    cx1=x1*x1*x1
    cx1=cx1+a*x1+b
    cy2=y2*y2
    cx2=x2*x2*x2
    cx2=cx2+a*x2+b
    cy3=y3*y3
    cx3=x3*x3*x3
    cx3=cx3+a*x3+b
    print("the cx3 and cy3 points are :",cx3,cy3)
    if(cy1==cx1 and cx2==cy2 and cy3==cx3):
        return 1
    else:
        return 0


#definition for drawing curve
def drawcurve(da,db,dx1,dy1,dx2,dy2,dx3,dy3,dslope,a,b):
    #Values defining our curve
    a = da
    b = db
    x1 = dx1
    y1 = dy1
    x2 = dx2
    y2 = dy2
    x3=dx3
    y3=dy3

    #The slope of the line   
    m=dslope

    #finding the greater value for calculating our rectange width and height        
    big=0
    listcompare=[dx1,dx2,dx3,dy1,dy2,dy3]
    for i in range(len(listcompare)):
        if(listcompare[i]<0):
            st=str(listcompare[i])
            st=st[1:]
            listcompare[i]=Fraction(st)
            if(big<listcompare[i]):
                big=listcompare[i];
        else:
            if(big<listcompare[i]):
                big=listcompare[i];
    
    
    #Determines width and height of plot
    w = big+10
    h = big+10
    
    # Annotate the plot with your name using width (w) and height (h) as your reference points.
    an1 = plt.annotate("Saboor Ahmed Siddiqie", xy=(-w+2 , h-2), xycoords="data",
                  va="center", ha="center",
                  bbox=dict(boxstyle="round", fc="w"))

    # This creates a mesh grid with values determined by width and height (w,h)
    # of the plot with increments of .0001 (1000j = .0001 or 5j = .05)
    y, x = np.ogrid[-h:h:1000j, -w:w:1000j]
    

    
    # Plot the curve (using matplotlib's countour function)
    # This drawing function applies a "function" described in the
    # 3rd parameter:  pow(y, 2) - ( pow(x, 3) - x + 1 ) to all the
    # values in x and y.
    # The .ravel method turns the x and y grids into single dimensional arrays
    
    #print("the x value is :",x)
    #plt.contour(x.ravel(), y.ravel(), pow(y, 2) - ( pow(x, 3) -x  + 1), [0])
    
    plt.contour(x.ravel(), y.ravel(), pow(y, 2) - ( pow(x, 3)+a*x+b), [0])
    
    
    # Plot the points ('ro' = red, 'bo' = blue, 'yo'=yellow and so on)
    plt.plot(x1, y1,'ro')

    # Annotate point 1
    plt.annotate('x1,y1', xy=(x1, y1), xytext=(x1+1,y1+1),
            arrowprops=dict(arrowstyle="->",
            connectionstyle="arc3"),
            )

    plt.plot(x2, y2,'ro')

    # Annotate point 2
    plt.annotate('x2,y2', xy=(x2, y2), xytext=(x2+1,y2+1),
            arrowprops=dict(arrowstyle="->",
            connectionstyle="arc3"),
            )

    # Use a contour plot to draw the line (in pink) connecting our point.
    plt.contour(x.ravel(), y.ravel(), (y-y1)-m*(x-x1), [0],colors=('pink'))

    # I hard coded the third point, YOU will use good ol mathematics to find
    # the third point
    plt.plot(x3,y3,'yo')
    #print("x3 and y3",x3,y3)

    # Annotate point 3
    plt.annotate('x3,y3', xy=(x3,y3), xytext=(x3+1,y3+1),
            arrowprops=dict(arrowstyle="->",
            connectionstyle="arc3"),
            )
    plt.plot(x3, y3,'ro')
    # Show a grid background on our plot
    plt.grid()

    # Show the plot
    plt.show()