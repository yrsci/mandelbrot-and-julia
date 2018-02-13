#!/usr/bin/env python3
import numpy as np

def binary_lattice(n,m):
    """
    Generates a 2D lattice of arbritrary size populated with 
    0's and 1's. Taken from notes.
    """
    
    A = np.random.random_sample(n*m).reshape(n,m)
    B = np.rint(A)

    return B


def pbm(lattice,filename):
    """
    Writes a portable bitmap image file from a given binary 
    n x m lattice. File is saved with user-given filename to same 
    directory.
    """

    dimensions = ""
    for i in lattice.shape:
        dimensions += str(i) + " "
    dimensions += "\n"

    # If necessary, converts given binary lattice to 0s and 1s req'd for .pbm format.
    body = ""
    for i in lattice:
        for j in i:
            if j <= 0:
                j = 0
            body += str(int(j))+" "
        body += "\n"

    # Writing the .pbm file:

    new_img = open(filename, "w")

    new_img.write("P1\n")
    new_img.write("# This image file was automatically generated from a Numpy lattice using Functions.pbm .\n")
    new_img.write(dimensions)    
    new_img.write(body)
    
    new_img.close()



def mandelbrot(n,m):
    
    """
    Takes an n x m lattice and generates a .pbm image of the Mandelbrot set.
    """
    
    lattice = binary_lattice(n,m)
        
    # run through lattice & test whether points are in set
    for p in range(0,n):
        for q in range(0,m):

    # standard settings for centered, zoomed-out Mandelbrot set
            a =  4 * (p / (float(n)) - 0.5)
            b =  4 * (q / (float(m)) - 0.5)  
    
    #        a =  (p / (3*float(n)) - 1.3)
    #        b =  (q / (3*float(m)) + 0.1)                
            
            c = a + 1j*b
            
    #       initialise complex variable before iteration
            z = 0 + 0j
            
            for num in range(100):
                if np.absolute(z) < 100:
                    z = z**2 + c
                    lattice[p][q] = 0
                else:
                    lattice[p][q] = 1

    # save image files of the mandelbrot lattice
    pbm(lattice,"mandelbrot.pbm")


def julia(n,m,c):
    
    """
    Takes an n x m lattice and generates a .pbm image of the Mandelbrot set.
    """
    
    lattice = binary_lattice(n,m)
        
    # run through lattice & test whether points are in set
    for p in range(0,n):
        for q in range(0,m):

    # standard settings for centered, zoomed-out Mandelbrot set
            a =  4 * (p / (float(n)) - 0.5)
            b =  4 * (q / (float(m)) - 0.5)  
    
    #        a =  (p / (3*float(n)) - 1.3)
    #        b =  (q / (3*float(m)) + 0.1)                
            
            z = a + 1j*b
            
    #       initialise complex variable before iteration
#            z = 0 + 0j
            
            for num in range(100):
                if np.absolute(z) < 100:
                    z = z**2 + c
                    lattice[p][q] = 0
                else:
                    lattice[p][q] = 1

    # save image files of the mandelbrot lattice
    pbm(lattice,"julia.pbm")
