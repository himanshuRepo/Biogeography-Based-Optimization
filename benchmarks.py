# -*- coding: utf-8 -*-
"""

Python code of Biogeography-Based Optimization (BBO)
Coded by: Raju Pal (emailid: raju3131.pal@gmail.com) and Himanshu Mittal (emailid: himanshu.mittal224@gmail.com)
The code template used is similar to code given at link: https://github.com/7ossam81/EvoloPy

Reference: D. Simon, Biogeography-Based Optimization, IEEE Transactions on Evolutionary Computation, in print (2008).
@author: Dan Simon (http://embeddedlab.csuohio.edu/BBO/software/)

-- Benchmark Function File: Defining the benchmark function along its range lower bound, upper bound and dimensions

Code compatible:
 -- Python: 2.* or 3.*
"""

import numpy
import math

# define the function blocks
    
def F1(x):
    s=numpy.sum(x**2);
    return s

def getFunctionDetails(a):
    
    # [name, lb, ub, dim]
    param = {  0: ["F1",-100,100,30],
            }
    return param.get(a, "nothing")



