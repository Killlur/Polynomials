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
                eqn += f'{abs(inlist[i]) if abs(inlist[i]) !=1 else ""}x{self.__get_super(str(self.degree - i))}{"" if inlist[i+1] == (None) else ("-" if abs([i for i in inlist[i:] if i!=0][0]) == [i for i in inlist[i:] if i!=0][0] else "+")}' if (inlist[i] != 0 and self.degree - i != 0) else (f'{inlist[i]}' if inlist[i] !=0 else "")
        return eqn
    def plotpolynomial(self):

        x = np.linspace(-1000, 1000)
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


poly1 = Polynomial([0,1,0,9,4])
print(poly1.valueofpolynomial(5),poly1.degree,poly1.nameofpolynomial())
poly1.plotpolynomial()

