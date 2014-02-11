#! /usr/bin/env python
import numpy as np
import numpy.random as npr
import pylab as P
from matplotlib import pyplot as plt

DoSave = True

def GaussSamp(Dist,B,N):
    # Dist - The distribution from which we sample
    # B - Size of the bins we use
    # N - Number of samples
    
    Dist = np.array(Dist)
    Dist.astype(float)
    
    Samp = np.ndarray(N) # Sample N times
    l = len(Dist) # Highest integer index drawn from
    Bin = np.ndarray(B)
    for I in range(N):
        for J in range(B):
            IndRand = npr.random_integers(0,l-1) # Pick a random index
            Bin[J] = Dist[IndRand]
            
        Samp[I] = sum(Bin)/B # Average it
        
    return Samp
    
# Pick a (hopefully) random distribution off the top of my head
MyDist = [1,1,1,1,2,2,2,3,4,4,4,4,4,6,6,10,10,10,10,10,10,10,10,10,10]
# Four 1's, three 2's, one 3, five 4's, two 6;s, ten 10's.
B = 100
N = 1000
GaussDist = GaussSamp(MyDist,B,N)

## Plot MyDist, and save it as a PDF

MDAxes = list(set(MyDist)) # Unique elements for plotting
MDPlot = [MyDist.count(I) for I in MDAxes]

MyIm = plt.figure(0)
MyIm
plt.bar(MDAxes,MDPlot,align='center')
plt.xticks(range(max(MDAxes)+1))
plt.xlabel('Integers in the Distribution')
plt.ylabel('Frequency of Appearance')
plt.title('A Very Non-Gaussian Distribution $N(n)$ From $1$ to $10$')
if DoSave:
    plt.savefig('MyDist_Plot.pdf')

## Plot the Gaussian Distribution

GIm = plt.figure(1)
GIm
(n,bins,patches) = P.hist(GaussDist,20,histtype='bar',color='red')
P.xlabel('Bin of mean values for samples of $N(n)$')
P.ylabel('Frequency of bin')
P.title('Distribution of $%s$ means of $%s$ element samples of $N(n)$'%(N,B))
if DoSave:
    P.savefig('GaussDist_Plot.pdf')
    
def AllanVar(Dist,B,N):
    # Dist - The distribution in question
    # B - This is the MAXIMUM bin size (1 to B)
    # N - Number of samples per bin
    
    Dist = np.array(Dist)
    Dist.astype(float)
    
    StDev = np.ndarray(B) # Vector of standard deviations
    for I in range(0,B+1):
        SampAv = GaussSamp(Dist,I+1,N) # Sample averages
        StDev[I-1] = np.std(SampAv)
        
    return StDev
    
AllanDist = AllanVar(MyDist,B,N)
print AllanDist

# Plot the Allan Variance

Alm = plt.figure(2)
Alm
SampAx = range(1,B+1)
plt.plot(SampAx,AllanDist)
plt.xlabel('Bin Size')
plt.ylabel('Standard Deviation')
plt.title('Standard Deviations of Means $%s$ Samples of $N(n)$ vs. Bin Size'%(N))
if DoSave:
    plt.savefig('StDev_Plot.pdf')
    
plt.show()
    
    
