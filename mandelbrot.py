#!/usr/bin/python3

import mand_functions as mand

# Set dimensions of lattice
n=250
m=250

# Enter a complex number for Julia set generation
c = -0.74434 - 0.10772j

# Generate the Mandelbrot and Julia sets from given n, m & c
mand.mandelbrot(n,m)
mand.julia(n,m,c)
