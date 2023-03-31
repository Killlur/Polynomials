import math
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
        inlist = self.coeffilist
        if all((i == 0) for i in inlist):
            eqn='y=0'
        else:
            eqn = "y=-" if abs(inlist[0]) != inlist[0] else "y="
            for i in range(self.degree+1):
                print(inlist[i])
                eqn += f'{abs(inlist[i]) if abs(inlist[i]) !=1 else ""}x{self.__get_super(str(self.degree - i))}{"" if ((inlist[i +1]  is None) or all(f == 0 for f in inlist[i+1:])) else ("-" if abs([g for g in inlist[i+1:] if g != 0][0]) != [h for h in inlist[i+1:] if h != 0][0] else "+")}' if (inlist[i] != 0 and self.degree - i != 0) else (f'{abs(inlist[i])}' if inlist[i] != 0 else "")
                print(eqn)
        return eqn
    def plotpolynomial(self, rnge=None):

        if rnge is None:
            rnge = [-100, 100]
        x = np.linspace(rnge[0],rnge[1])
        fig, ax = plt.subplots()

        ax.plot(x, self.valueofpolynomial(x),label=self.nameofpolynomial())
        ax.plot(x,Polynomial([0]).valueofpolynomial(x))
        plt.legend()
        plt.show()

    def minima(self):
        print("no calculus yet")

    # Thank you internet
    @staticmethod
    def __get_super(x):
        normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
        super_s = "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾"
        res = x.maketrans(''.join(normal), ''.join(super_s))
        return x.translate(res)

class Projectile:
    def __init__(self,u,a,theta):
        assert u>=0,"Velocity cannot be negative,use the angle from 0 to 360 to do wacky stuff!"

        self.velocity = u
        self.gravity=abs(a)
        self.aop=math.radians(theta)

        a= round((-self.gravity)/(2*(self.velocity**2)*(math.cos(self.aop)**2)),5)
        b=round((math.tan(self.aop)),5)
        self.parabola=Polynomial([a,b,0])
        print(self.parabola.nameofpolynomial())
    def Range(self):
        return ((self.velocity**2) * math.sin(2*self.aop))/self.gravity

    def Projection(self):

        self.parabola.plotpolynomial([-50,50])




