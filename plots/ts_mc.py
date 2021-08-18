import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

def plot(xdata,ydata1,label1,ydata2,label2,ydata3,label3,xlabel,ylabel,system,skip):
    plt.plot(xdata,ydata1,color='k',label=label1,marker='x')
    plt.plot(xdata,ydata2,color='r',label=label2,marker='x')
    plt.plot(xdata,ydata3,color='b',label=label3,marker='x')
    plt.xlabel(r"%s" %(xlabel),fontsize=18)
    plt.ylabel(r"%s" %(ylabel),fontsize=18)
    plt.tick_params(axis='both',labelsize=18)
    plt.grid(b=True, which='major', axis='both', color='#808080', linestyle='--')
    plt.tight_layout()
    #plt.xticks(np.arange(0,xdata[-1]+1,skip))
    #plt.xlim((0,xdata[-1]))
    #plt.ylim((1,2500))
    plt.xscale('log')
    plt.yscale('log')
    plt.legend(loc='upper center', bbox_to_anchor=(0.45, 1.14), shadow=True, ncol=3, fontsize = 14)
    plt.savefig('%s.png' %(system))
    plt.savefig('%s.pdf' %(system))
    plt.close()



MC = np.arange(8,257,8)
avg = np.zeros((3,len(MC)),dtype=float)
for i in range(len(MC)):
    data1 = np.loadtxt("../algorithm_1/mcADI2/tscaling.MC%s.dat" %(MC[i]))
    data2 = np.loadtxt("../algorithm_2/mcADI2/tscaling.MC%s.dat" %(MC[i]))
    data3 = np.loadtxt("../algorithm_3/mcADI2/tscaling.MC%s.dat" %(MC[i]))
    avg[0,i] = np.average(data1)
    avg[1,i] = np.average(data2)
    avg[2,i] = np.average(data3)
plot(MC,avg[0],"Algorithm 1",avg[1],"Algorithm 2",avg[2],"Algorithm 3","Number of MC points per atom, $N_{MC}$","Timescaling (ns/day)","timescaling_mc.2",32)

MC = np.arange(8,153,8)
avg = np.zeros((3,len(MC)),dtype=float)
for i in range(len(MC)):
    data1 = np.loadtxt("../algorithm_1/mcADI50/tscaling.MC%s.dat" %(MC[i]))
    data2 = np.loadtxt("../algorithm_2/mcADI50/tscaling.MC%s.dat" %(MC[i]))
    data3 = np.loadtxt("../algorithm_3/mcADI50/tscaling.MC%s.dat" %(MC[i]))
    avg[0,i] = np.average(data1)
    avg[1,i] = np.average(data2)
    avg[2,i] = np.average(data3)
plot(MC,avg[0],"Algorithm 1",avg[1],"Algorithm 2",avg[2],"Algorithm 3","Number of MC points per atom, $N_{MC}$","Timescaling (ns/day)","timescaling_mc.50",16)

