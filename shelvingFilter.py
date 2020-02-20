# -*- coding: utf-8 -*-
"""
Christian Teeples
"""

import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

###############################################################################
def applyShelvingFilter(inName, outName, g, fc) :
    data, samplerate = readWaveFile(inName)
    x = data
    mew = 10 ** (g/20)
    thetaC = 2*np.pi*fc/samplerate
    gamma = (1 - (4/(1 + mew))*np.tan(thetaC / 2)) / (1 + (4/(1 + mew))*np.tan(thetaC / 2))
    alpha = (1 - gamma) / 2
    u = [0]
    y = []
    n = 0
    m = n - 1
    N = len(data)
    while n < N:
        xVal = 0
        xValMinusOne = 0
        uVal = 0
        uValMinusOne = 0
        if ((n < 0) or ((N - 1) < n)):
            xVal = 0
            uVal = 0
        else:
            xVal = x[n]
            uVal = u[n]
        if ((m < 0) or ((N - 1) < m)):
            xValMinusOne = 0  
            uValMinusOne = 0
        else:
            xValMinusOne = x[m]
            uValMinusOne = u[m]
            
        u.append(alpha * (xVal + xValMinusOne) + gamma * uValMinusOne)
        y.append(xVal + (mew - 1) * uVal)
        n = n + 1
        m = m + 1
    originalFFT = np.fft.fft(x)
    filteredFFT= np.fft.fft(y)
    bothLists = []
    bothLists.extend(originalFFT)
    bothLists.extend(filteredFFT)
    maximum = abs(max(bothLists)) + 100
    graph(abs(originalFFT), "Original", 0, N/4, 0, maximum, 1, 2, 1)
    graph(abs(filteredFFT), "Filtered FFT", 0, N/4, 0, maximum, 1, 2, 2)
    sf.write(outName, y, samplerate)
    
###############################################################################        
def graph(x, Title, xStart, xEnd, yStart, yEnd, first, second, third):
    plt.subplot(first, second, third)
    plt.title(Title)
    if (xStart != None and xEnd != None):
        plt.xlim([xStart, xEnd])
    if (yStart != None and yEnd != None):
        plt.ylim([yStart, yEnd])
    plt.plot(x)
    plt.tight_layout()
    plt.show()
###############################################################################    
def readWaveFile(fileName):
    data, samplerate = sf.read(fileName)
    return data, samplerate
##########################  main  #############################################
if __name__ == "__main__" :
    inName = "P_9_1.wav"
    gain = -4  # can be positive or negative
                # WARNING: small positive values can greatly amplify the sounds
    cutoff = 300
    outName = "shelvingOutput.wav"

    applyShelvingFilter(inName, outName, gain, cutoff)
    