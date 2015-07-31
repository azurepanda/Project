import math
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams["savefig.dpi"] = 100
import numpy as np
import os
from os import path

data = [];
for f in os.listdir('./angmom/'): 
    if path.getsize('./angmom/' + f) > 0:
        for line in open('./angmom/' + f, 'r').read().split('\n'):
            data.append(line.split())

print str(len(data)) + ' galaxies found.'

Lgx = [];
Lgy = [];
Lgz = [];
a = [];
b = [];
c = [];
Ldotn = [Lgx, Lgy, Lgz, a, b, c];
for d in data:
    valid = True;
    if len(d) >= 12:
        for n in range(0, 6): 
            if math.isnan(float(d[3+n])):
                valid = False;
        if valid:
            for n in range(0, 6):
                Ldotn[n].append(float(d[3+n]));

#Ldota[] = Lgx[0]*evecs[0][0]+Lgy[1]*evecs[0][1]+Lgz[2]*evecs[0][2];
#Ldotb[] = Lgx[0]*evecs[1][0]+Lgy[1]*evecs[1][1]+Lgz[2]*evecs[1][2];
#Ldotc[] = Lgx[0]*evecs[2][0]+Lgy[1]*evecs[2][1]+Lgz[2]*evecs[2][2];


#nbins = 20;
#defbins = np.linspace(0, 90, nbins);
#plt.hist(Ldota, bins=defbins, normed=True, color='black', histtype='step', label='Major-axis');
#plt.hist(Ldotb, bins=defbins, normed=True, color='red', histtype='step', label='Intermediate-axis');
#plt.hist(Ldotc, bins=defbins, normed=True, color='green', histtype='step', label='Minor-axis');
#plt.ylabel('N/N$_{top}$');
#plt.xlabel('Alignment [degrees]');
#plt.legend(loc='upper left');
#plt.show();
