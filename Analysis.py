import numpy as np
import matplotlib.pyplot as plt

RF = np.arange(0.5, 4.6, 0.2)
P85 = np.array(
    [0.1508,
    0.2507,
    0.3499,
    0.449,
    0.548,
    0.6467,
    0.7458,
    0.8443,
    0.9436,
    1.0426,
    1.1416,
    1.2402,
    1.3395,
    1.4388,
    1.5366,
    1.6345,
    1.7325,
    1.8315,
    1.9288,
    2.0354,
    2.1332])
P87 = np.array(
    [0.0692,
    0.1357,
    0.2024,
    0.269,
    0.3351,
    0.4009,
    0.467,
    0.5332,
    0.599,
    0.6652,
    0.7312,
    0.7972,
    0.8632,
    0.9284,
    0.9945,
    1.060,
    1.1262,
    1.1924,
    1.2583,
    1.3242,
    1.3893])
N85 = np.array(
    [-0.339,
    -0.4382,
    -0.5372,
    -0.6364,
    -0.7354,
    -0.8342,
    -0.9331,
    -1.0318,
    -1.1305,
    -1.2291,
    -1.3282,
    -1.4269,
    -1.5243,
    -1.6224,
    -1.7206,
    -1.8185,
    -1.9165,
    -2.0145,
    -2.1119,
    -2.2097,
    -2.307])
N87 = np.array(
    [-0.255,
    -0.3217,
    -0.388,
    -0.454,
    -0.521,
    -0.586,
    -0.653,
    -0.719,
    -0.785,
    -0.851,
    -0.917,
    -0.983,
    -1.049,
    -1.115,
    -1.181,
    -1.246,
    -1.313,
    -1.379,
    -1.445,
    -1.510,
    -1.576])


graphs = [P85, P87, N85, N87]
names = ["Rb85", "Rb87"]

def LeastSquares(X, Y):
    # X = np.reshape(X, (Y.size, 1))
    A = np.ones((Y.size, 2))
    A[::, 1] = X
    return np.linalg.lstsq(A, Y)[0]

def LeastSquaresError(a,b,X,Y):
    RF1 = a*X+b
    diff = RF1-Y
    sumsquares = np.sum(np.square(diff))
    errsq = sumsquares/(Y.size-2)
    print errsq, Y.size
    errB = errsq**0.5/((Y.size)**0.5)
    xmean = np.mean(X)
    xprime = X - xmean
    xprimesquared = np.square(xprime)
    print X
    print xprimesquared
    errA = (errsq)**0.5/(np.sum(xprimesquared))**0.5
    errB = (errB**2 + errA**2*xmean**2)**0.5
    return errA, errB

def errGraphs():
    plt.figure(1)
    # subplotnum = 220
    index = 0
    for g in graphs:
        # subplotnum +=1
        # ax = plt.subplot(subplotnum)
        # ax.set_title(names[index])
        # ax.set_xlabel('Current (A)')
        # plt.set_ylabel('Resonance Frequency (MHz)')
        b,a = LeastSquares(g, RF)
        Y = a*g+b
        plt.plot(g, Y, label=names[index] + " Trendline " + "(y = "+ str(round(a,3))+"x + "+str(round(b,3)) + ")")
        errA, errB = LeastSquaresError(a,b,g,RF)
        # plt.scatter(g, RF, label=names[index] + " (Error: a' = +/- " + str(errA) + " b = +/-" + str(errB) + ")") #points
        plt.scatter(g, RF, label=names[index] + " (Error: a = +/- " + '{:0.3e}'.format(errA) + " b = +/-" +'{:0.3e}'.format(errB) + ")") #points
        index+=1
    # plt.title("test")
    plt.xlabel('Current (A)')
    plt.ylabel('Resonance Frequency (MHz)')
    plt.legend(bbox_to_anchor=(0., 1.17, 1., .102), loc=2)
    plt.grid(color='k', linestyle='-', linewidth=0.5)
    plt.show()


# print "P85"
# b,a = LeastSquares(P87, RF)
# errA, errB = LeastSquaresError(a,b,P85,RF)
# print "P85 A,B", a,b
# print "P85 ERRA, ERRB", errA, errB
RF = np.append(RF, -RF)
graphs = [np.append(P85, N85), np.append(P87,N87)]
errGraphs()

