import numpy
import math
# This is a sample Python script.

# By D. Whyman Last Update 28/02/2024


def angleCritCalc(poles, zeros):
    print("Hi")

def thing():
    overshoot = 0.05
    stepSSE = 0.01
    rampSSE = 0.02
    settleTime = 2
    settlePercent = 0.02
    lnOvershoot = numpy.square(numpy.log(overshoot))
    pi2 = numpy.square(numpy.pi)

    zeta = numpy.sqrt(lnOvershoot/(pi2 + lnOvershoot))
    noTimeConst = -numpy.log(settlePercent)
    omegaN = noTimeConst/(zeta*settleTime)
    thetaMax = numpy.arccos(zeta)

    print(zeta,", ",omegaN)

    zetaTarget = 0.75
    omegaNTarget = 4.4
    clPole = [-zetaTarget*omegaNTarget-0.0, omegaNTarget*numpy.sqrt(1-numpy.square(zetaTarget))]
    print(clPole)

    plantPoles = [0, -1, -5]

    ##Angle Crit

    theta1 = numpy.arctan(clPole[1]/clPole[0]) + numpy.pi
    thetaleft = numpy.pi - theta1
    thetaLead = thetaleft/2
    ##print(theta1, thetaleft, thetaLead)

    pLead = clPole[0] - clPole[1]/numpy.tan(thetaLead)
    print(pLead)

    ##Gain Calculation

    modPLead = numpy.sqrt(numpy.square(clPole[1]) + numpy.square(pLead-clPole[0]))
    modP0 = numpy.sqrt(numpy.square(clPole[0]) + numpy.square(clPole[1]))

    K = numpy.square(modPLead)*modP0
    KC = K/2
    print(KC)

    ##Lag Calculation with ramp sse

    lagRatio = (5*numpy.square(pLead))/(2*KC*1*5*0.01984) ## Less than 0.02 to make the gain found in the compensator approx 126 so sse < 0.02
    print(lagRatio)
    zLag = 0.05

    pLag = zLag/lagRatio
    print(pLag)

    C = KC*(zLag*1*5)/(pLag*pLead**2)
    print(C)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    thing()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
