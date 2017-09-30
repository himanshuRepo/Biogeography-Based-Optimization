# -*- coding: utf-8 -*-
"""
Python code of Biogeography-Based Optimization (BBO)
Coded by: Raju Pal (emailid: raju3131.pal@gmail.com) and Himanshu Mittal (emailid: himanshu.mittal224@gmail.com)
The code template used is similar to code given at link: https://github.com/himanshuRepo/CKGSA-in-Python 
 and matlab version of the BBO at link: http://embeddedlab.csuohio.edu/BBO/software/

Reference: D. Simon, Biogeography-Based Optimization, IEEE Transactions on Evolutionary Computation, in print (2008).
@author: Dan Simon (http://embeddedlab.csuohio.edu/BBO/software/)

-- BBO File: Performing the Biogeography-Based Optimization(BBO) Algorithm 

Code compatible:
 -- Python: 2.* or 3.*
"""

from __future__ import division
import random
import numpy
import math
from solution import solution
import time
import ClearDups


        
def BBO(objf,lb,ub,dim,PopSize,iters):
    # Defining the solution variable for saving output variables
    s=solution()
    
    # Initializing the parameters with default values
    fit = numpy.zeros(PopSize)
    EliteSolution=numpy.zeros((Keep,dim))
    EliteCost=numpy.zeros(Keep)
    Island=numpy.zeros((PopSize,dim))
    mu=numpy.zeros(PopSize)
    lambda1=numpy.zeros(PopSize)
    MinCost=numpy.zeros(iters)
    Bestpos=numpy.zeros(dim)

    # Initializing BBO parameters
    pmutate = 0.01; # initial mutation probability
    Keep = 2; # elitism parameter: how many of the best habitats to keep from one generation to the next

    # Initializing Population
    pos=numpy.random.uniform(0,1,(PopSize,dim)) *(ub-lb)+lb

    #Calculate objective function for each particle
    for i in range(PopSize):
        # Performing the bound checking
        pos[i,:]=numpy.clip(pos[i,:], lb, ub)
        fitness=objf(pos[i,:])
        fit[i]=fitness

    # Calculating the mu and lambda
    for i in range(PopSize):
        mu[i] = (PopSize + 1 - (i)) / (PopSize + 1)
        lambda1[i] = 1 - mu[i]

    print("BBO is optimizing  \""+objf.__name__+"\"")    
    
    timerStart=time.time() 
    s.startTime=time.strftime("%Y-%m-%d-%H-%M-%S")

    # Defining the loop
    for l in range(iters):
        # Defining the Elite Solutions
        for j in range(Keep):
            EliteSolution[j,:]=pos[j,:]
            EliteCost[j]=fit[j]

        # Performing Migration operator 
        for k in range(PopSize):
            for j in range(dim):
                if random.random() < lambda1[k]:
                    # Performing Roulette Wheel
                    RandomNum = random.random() * sum(mu);
                    Select = mu[1];
                    SelectIndex = 0;
                    while (RandomNum > Select) and (SelectIndex < (PopSize-1)):
                        SelectIndex = SelectIndex + 1;
                        Select = Select + mu[SelectIndex];
                
                    Island[k,j] = pos[SelectIndex,j]
                else:
                    Island[k,j] = pos[k,j]

        # Performing Mutation
        for k in range(PopSize):
            for parnum in range(dim):
                if pmutate > random.random():
                    Island[k,parnum] = lb + (ub-lb) * random.random();

        # Performing the bound checking
        for i in range(PopSize):
            Island[i,:]=numpy.clip(Island[i,:], lb, ub)

        # Replace the habitats with their new versions.
        for k in range(PopSize):
            pos[k,:] = Island[k,:]

        #Calculate objective function for each individual
        for i in range(PopSize):
            fitness=objf(pos[i,:])
            fit[i]=fitness

        # Sort the fitness
        fitness_sorted=numpy.sort(fit)

        # Sort the population on fitness
        I=numpy.argsort(fit)
        pos=pos[I,:]

        # Replacing the individual of population with EliteSolution
        for k in range(Keep):
            pos[(PopSize-1)-k,:] = EliteSolution[k,:];
            fit[(PopSize-1)] = EliteCost[k];
        
        # Removing the duplicate individuals
        pos=ClearDups.ClearDups(pos, PopSize, dim, ub, lb)

        #Calculate objective function for each individual
        for i in range(PopSize):
            fitness=objf(pos[i,:])
            fit[i]=fitness

        # Sort the fitness
        fitness_sorted=numpy.sort(fit)

        # Sort the population on fitness
        I=numpy.argsort(fit)  
        pos=pos[I,:]

        # Saving the best individual
        MinCost[l] = fit[1]
        Bestpos=pos[1,:]
        gBestScore=fit[1]

        # Displaying the best fitness of each iteration
        if (l%1==0):
               print(['At iteration '+ str(l+1)+ ' the best fitness is '+ str(gBestScore)]);

    timerEnd=time.time()  
    s.endTime=time.strftime("%Y-%m-%d-%H-%M-%S")
    s.executionTime=timerEnd-timerStart
    s.convergence=MinCost
    s.optimizer="BBO"
    s.objfname=objf.__name__

    return s
         
    
