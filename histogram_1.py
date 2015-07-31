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
        data.append(open('./angmom/' + f, 'r').read().split());

print str(len(data)) + ' non empty files found.';

Ldota = []
Ldotb = []
Ldotc = []
Ldotn = [Ldota, Ldotb, Ldotc]
for d in data:
    for n in range(0, 3):   
        if not math.isnan(float(d[9+n])):
            angle= abs(180/math.pi*math.acos(float(d[9+n])))
            if angle > 90:
                angle = 180 - angle
            Ldotn[n].append(angle)

nbins = 20;
defbins = np.linspace(0, 90, nbins);
plt.hist(Ldota, bins=defbins, normed=True, color='black', histtype='step', label='Major-axis');
plt.hist(Ldotb, bins=defbins, normed=True, color='red', histtype='step', label='Intermediate-axis');
plt.hist(Ldotc, bins=defbins, normed=True, color='green', histtype='step', label='Minor-axis');
plt.ylabel('N/N$_{top}$');
plt.xlabel('Alignment [degrees]');
plt.legend(loc='upper left');
plt.show();
