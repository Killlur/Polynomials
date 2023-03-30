import matplotlib.pyplot as plt
import numpy as np

class Polynomial:
    def __init__(self,coefflist : list):
        self.degree= len(coefflist)-1
        self.coeffilist=coefflist
    def degreofpolynomial(self):
        return self.degree

    def valueofpolynomial(self,x):
        inlist = self.coeffilist
        eqn = 0
        for i in range(self.degree+1):
            eqn += inlist[i] * (x ** (self.degree - i))
        return eqn
    def nameofpolynomial(self):
        print("x\u00b2 + y\u00b2 = 2")
        pass

    def plotpolynomial(self):


        x = np.linspace(-100, 100)
        fig, ax = plt.subplots()
        ax.plot(x, self.valueofpolynomial(x))
        # ax.set(ylim=(-abs(polynomial([a] + pollist)),abs(polynomial([a] + pollist))))
        plt.show()


def polynomial(inlist=[]):
    x = inlist.pop(0)
    r = len(inlist)
    eqn = 0
    weqn=""
    for i in range(len(inlist)-1):
        eqn += inlist[i]*x**(r-i)
        weqn += str(inlist[i])+"$\mathregular{x^{2}}$"
    print(weqn)
    return eqn

def plotpolynomial(inlist1=[]):
    a = inlist1.pop(0)
    pollist=[i for i in inlist1]
    print(a,pollist)

    x = np.linspace(-a,a)
    fig,ax = plt.subplots()
    ax.plot(x,polynomial([x] + pollist))
    # ax.set(ylim=(-abs(polynomial([a] + pollist)),abs(polynomial([a] + pollist))))
    plt.show()


quadratic = Polynomial([2,0,4])
print(quadratic.valueofpolynomial(5),quadratic.degree,quadratic.nameofpolynomial())
quadratic.plotpolynomial()