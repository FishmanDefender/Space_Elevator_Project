import numpy as np
import matplotlib.pyplot as plt


class cable:

    def __init__(self,r0,rt,rs,sigma,rho,g,As=1):
        '''
        This class contains methods that calculate specific properties of the cable.
        '''

        h = 10**6*sigma/(rho*g)

        self.params = (r0,rt,rs,sigma,rho,g,As,h)

    def taper_ratio(self):
        '''
        This module returns the taper ratio of a space tether.
        '''
        Ar = np.exp((self.params[0]**2/self.params[7])
                    * (1/self.params[0]+(self.params[0]**2/(2*self.params[2]**3))
                    - 1/self.params[2]-(self.params[2]**2/(2*self.params[2]**3)))
                    )

        taper_ratio = Ar/self.params[6]

        return taper_ratio


    def taper_plot(self):

        x_data = np.arange(6000, 150000, 1)
        y_data = np.exp(((self.params[0]**2)/self.params[7])
                        * (1/self.params[0]+(self.params[0]**2/(2*self.params[2]**3))
                        - 1/x_data-(x_data**2/(2*self.params[2]**3)))
                        )

        print(y_data)

        ax = plt.axes(xlim=(6000,150000), ylim=(0,2))
        ax.set_xlabel('Radial Distance (km)')
        ax.set_ylabel('Cross-Sectional Area Ratio')
        ax.set_title('Taper Ratio for CNT Cable')
        ax.plot(x_data, y_data)

        plt.show()


cnt_cable = cable(6000, 150000, 42300, 7.9*10**-3, 39, 9.81, 1)

tr = cnt_cable.taper_ratio()

print(tr)

cnt_cable.taper_plot()
