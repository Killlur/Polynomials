import matplotlib.pyplot as plt
import numpy as np

def polynomial(inlist=[]):
    var = inlist.pop(0)
    r = len(inlist)
    eqn = 0
    weqn=""
    for i in range(len(inlist)-1):
        eqn += inlist[i]*var**(r-i)
        weqn += str(inlist[i])+"$\mathregular{x^{2}}$"
    print(weqn)
    return eqn

def plotpolynomial(inlist1=[]):
    a = inlist1.pop(0)
    pollist=[i for i in inlist1]
    print(a,pollist)

    x = np.linspace(-a,a)
    fig,ax = plt.subplots()
    ax.plot(x,polynomial([x] + pollist),label=)
    # ax.set(ylim=(-abs(polynomial([a] + pollist)),abs(polynomial([a] + pollist))))
    plt.show()



plotpolynomial([100,3,0,0])