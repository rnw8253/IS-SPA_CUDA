import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

def plot(xdata,ydata1,yerr1,label1,ydata2,yerr2,label2,ydata3,yerr3,label3,xlabel,ylabel,system):
    #plt.errorbar(xdata,ydata1,yerr=yerr1,color='k',label=label1,marker='x')
    #plt.errorbar(xdata,ydata2,yerr=yerr2,color='r',label=label2,marker='x')
    #plt.errorbar(xdata,ydata3,yerr=yerr3,color='b',label=label3,marker='x')
    plt.plot(xdata,ydata1,color='k',label=label1,marker='x')
    plt.plot(xdata,ydata2,color='r',label=label2,marker='x')
    plt.plot(xdata,ydata3,color='b',label=label3,marker='x')
    plt.xlabel(r"%s" %(xlabel),fontsize=18)
    plt.ylabel(r"%s" %(ylabel),fontsize=18)
    plt.tick_params(axis='both',labelsize=18)
    plt.grid(b=True, which='major', axis='both', color='#808080', linestyle='--')
    #plt.xticks(np.arange(0,1201,200))
    plt.tight_layout()
    #plt.xlim((10,1200))
    #plt.ylim((10,1550))
    plt.xscale('log')
    plt.yscale('log')
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.14), shadow=True, ncol=3, fontsize = 14)
    plt.savefig('%s.png' %(system))
    plt.savefig('%s.pdf' %(system))
    plt.close()



nMols = np.array((2,10,25,50))
nAtoms = np.zeros(np.shape(nMols),dtype=float)
for i in range(len(nMols)):
    nAtoms[i] = nMols[i]*22

avg = np.zeros((3,len(nMols)),dtype=float)
std = np.zeros((3,len(nMols)),dtype=float)
for i in range(len(nMols)):
    data1 = np.loadtxt("../algorithm_1/ADI%s/tscaling.ADI%s.dat" %(nMols[i],nMols[i]))
    data2 = np.loadtxt("../algorithm_2/ADI%s/tscaling.ADI%s.dat" %(nMols[i],nMols[i]))
    data3 = np.loadtxt("../algorithm_3/ADI%s/tscaling.ADI%s.dat" %(nMols[i],nMols[i]))
    avg[0,i] = np.average(data1)
    avg[1,i] = np.average(data2)
    avg[2,i] = np.average(data3)
    std[0,i] = np.std(data1)
    std[1,i] = np.std(data2)
    std[2,i] = np.std(data3)

print(avg)
plot(nAtoms,avg[0],std[0],"Algorithm 1",avg[1],std[1],"Algorithm 2",avg[2],std[2],"Algorithm 3","Number of Atoms, N","Timescaling (ns/day)","timescaling_atoms")
