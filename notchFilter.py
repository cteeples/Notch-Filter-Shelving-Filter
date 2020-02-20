# -*- coding: utf-8 -*-
"""
Christian Teeples
"""

import numpy as np
import matplotlib.pyplot as plt
import csv

def applyNotch(fs, dataFile) :
    n = 0
    m = n - 2
    l = n - 1
    f = 17
    normF = f / fs
    w = normF *2*np.pi
    y = []
    csvFile = importCSV(dataFile)
    while n < len(csvFile) + 100:
        x = csvFile
        N = len(x)
        xVal = 0
        yValMinusOne = 0
        xValMinusOne = 0
        yValMinusTwo = 0
        xValMinusTwo = 0
        if ((n < 0) or ((N - 1) < n)):
            xVal = 0
        else:
            xVal = x[n]
        if ((l < 0) or ((N - 1) < l)):
            xValMinusOne = 0
        else:
            xValMinusOne = x[l]
        if (l < 0):
            yValMinusOne = 0
        else:
            yValMinusOne = y[l]
        if ((m < 0) or ((N - 1) < m)):
            xValMinusTwo = 0
        else:
            xValMinusTwo = x[m]
        if (m < 0):
            yValMinusTwo = 0
        else:
            yValMinusTwo = y[m]
            
        y.append(1.8744*yValMinusOne*np.cos(w) - 0.8783*yValMinusTwo + xVal - 2*xValMinusOne*np.cos(w) + xValMinusTwo)
        n = n + 1
        m = m + 1
        l = l + 1
    graph(x, "Original", -25, 625, None, None)
    graph(y, "Filtered", None, None, -2.25, 2.25)
    graphCOS(10, 33, "Combined Freqz", -25, 625)
    
def graphCOS(f1, f2, Title, xStart, xEnd):
    plt.subplot(3, 1, 1)
    if(xStart != None and xEnd != None):
        x = np.arange(xStart, xEnd, 1)
        y1 = np.cos(2*np.pi*f1/xEnd*x)
        y2 = np.cos(2*np.pi*f2/xEnd*x)
        y = y1 + y2
        plt.xlim([xStart, xEnd])
        plt.plot(x, y)
    else:
        x = np.arange(0, 2000, 1)
        y1 = np.cos(2*np.pi*f1/2000*x)
        y2 = np.cos(2*np.pi*f2/2000*x)
        y = y1 + y2
        plt.plot(x, y)
    plt.title(Title)
    plt.tight_layout()
    plt.show()
    
def graph(x, Title, xStart, xEnd, yStart, yEnd):
    plt.subplot(3, 1, 1)
    plt.title(Title)
    if (xStart != None and xEnd != None):
        plt.plot(x)
        plt.xlim([xStart, xEnd])
    if (yStart != None and yEnd != None):
        plt.plot(x)
        plt.ylim([yStart, yEnd])
    else:
        plt.plot(x)
    plt.tight_layout()
    plt.show()
    
def importCSV(name):
    t = []
    file = open(name, 'r')
    values = csv.reader(file)
    for row in values:
        for item in row:
            t.append(float(item))
    return t
############################################################
###########################  main  #########################
if __name__ == "__main__":
    fs = 500
    dataFileName = "notchData.csv"

    # write this function
    applyNotch(fs, dataFileName)
