# this is for plotting the PL from the Horiba in the nanofab.
# Exporting spectra as a text file gives a pretty 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Arial']
rcParams['font.weight'] = 'bold'
rcParams['axes.labelweight'] = 'bold'
rcParams['savefig.dpi'] = 300


def main():
    dataloc = r"enter file"
    data_load = pd.read_csv(dataloc, header=None, sep='\s')

    fontsize = 40
    mpl.rcParams.update({'font.size': fontsize, 'figure.autolayout': True})
    fig, ax = plt.subplots(figsize=(14,10), tight_layout=True)
    plt.rc('font', size=12)
    ax.plot(data_load[0], data_load[1], color='black', linewidth=7)
    ax.set_xlabel("Wavelength (nm)")
    ax.set_ylabel('Intensity (counts)')
    ax.xaxis.labelpad = 5
    ax.yaxis.labelpad = 5
    ax.tick_params(axis = 'both', direction='in', which='both', length=18, width=3)
    
    
    for axis in ['top','bottom','left','right']:
        ax.spines[axis].set_linewidth(3)

    plt.show()


if __name__ == "__main__":
    main()
