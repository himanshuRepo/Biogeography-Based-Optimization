# -*- coding: utf-8 -*-
"""
Python code of Biogeography-Based Optimization (BBO)
Coded by: Raju Pal (emailid: raju3131.pal@gmail.com) and Himanshu Mittal (emailid: himanshu.mittal224@gmail.com)
The code template used is similar to code given at link: https://github.com/himanshuRepo/CKGSA-in-Python 
 and matlab version of the BBO at link: http://embeddedlab.csuohio.edu/BBO/software/

Reference: D. Simon, Biogeography-Based Optimization, IEEE Transactions on Evolutionary Computation, in print (2008).
@author: Dan Simon (http://embeddedlab.csuohio.edu/BBO/software/)

-- ClearDups File: Function for removing the duplicates in the Population

Code compatible:
 -- Python: 2.* or 3.*
"""

import numpy
import random

def ClearDups(Population, PopSize, dim, MaxParValue, MinParValue):

    for i in range(PopSize):
        Chrom1 = numpy.sort(Population[i,:]);
        for j in range(i+1,PopSize):
            Chrom2 = numpy.sort(Population[j,:]);
            if Chrom1 is Chrom2:
                parnum = numpy.ceil(dim * random.random());
                Population[j,parnum] = MinParValue + (MaxParValue - MinParValue) * random.random();
    return Population
                
