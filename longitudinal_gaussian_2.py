import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def init_u(delta_r, rt, r0):
    '''
    This method calculates u_vec at time-step 0 with gaussian distribution centered at rt and of magnitude 10 cm.
    '''
    u0 = 0.00001  # kilometers --> 1 cm amplitude
    u_minus = []
    loc_u = []  # Defining an empty list for use in the loops

    for m in range(0, 1440):

        if m == 0:
            u_n = 0
            u_nminus = 0
        else:
            u_n = u0*np.exp((-((m*delta_r+r0) - (rt))**2)/(200000*delta_r))
            u_nminus = u0*np.exp((-((m*delta_r+r0) - (rt+delta_r*10**-2))**2)/(200000*delta_r))

        loc_u.append(u_n)
        u_minus.append(u_nminus)

    return (u_minus, loc_u)


def get_u(u_vec, r0, rt, delta_r, delta_t, rho, sigma, g, y_modulus, h, rs, n):
    '''
    This method returns the u vector for a single time step.
    '''

    u_next = []

    u = u_vec[-1]
    u_before = u_vec[-2]

    for m in range(0, 1440):
        if m == 0:
            u_mnext = 0
        elif m == 1439:
            u_mnext = 0.00001*np.exp(-((m*delta_r+r0) - (rt-n*delta_r*10**-2))**2/(200000*delta_r))

        elif m == 1438:
            u_mnext = ((delta_t/delta_r)**2*(u[m+1]-2*u[m]+u[m-1])+(delta_t**2/(delta_r*h))*((r0/(m*delta_r+r0))**2-(r0**2*(m*delta_r+r0)/rs**3))*(u[m+1]-u[m]))*(y_modulus*10**-3/rho)+2*u[m]-u_before[m]
        else:
            u_mnext = ((delta_t/delta_r)**2*(u[m+1]-2*u[m]+u[m-1])+(delta_t**2/(delta_r*h))*((r0/(m*delta_r+r0))**2-(r0**2*(m*delta_r+r0)/rs**3))*(u[m+1]-u[m]))*(y_modulus*10**-3/rho)+2*u[m]-u_before[m]

        u_next.append(u_mnext)

    return u_next


def simulate_gaussian(r0, rt, rs, sigma, rho, g, y_modulus, delta_t, delta_r):
    '''
    Method to simulate a gaussian pulse in a tapered space cable.
    '''

    # r0 = planet radius (km)
    # rt = max height of cable from planet center (km)
    # rs = geosychronous orbit (km)
    # sigma = maximum stress (GPa)
    # rho = mass density (kg/m^3)
    # g = gravitational acceleration at planet surface (m/s^2)
    # y_modulus = Young's Modulus for the material (GPa)
    # delta_t = the time-step size (s)
    # delta_r = the radius step size (km)

    u_vec = []  # This will be the array that contains the u vector at each time step

    h = 10**6*sigma/(rho*g)
    print('h = '+str(np.round(h, decimals=0))[:-2]+' km')

    for x in init_u(delta_r, rt, r0):
        u_vec.append(x)

    # Setting Up the Plot
    fig = plt.figure()
    ax = plt.axes(xlim=(6000, 150000), ylim=(-1, 1))
    line, = ax.plot([], [], lw=2)

    # initialization function: plot the background of each frame
    def init():
        line.set_data([], [])
        return line,

    # animation function.  This is called sequentially
    def animate(i):
        x = np.linspace(6000, 150000, 1440)
        y = get_u(u_vec, r0, rt, delta_r, delta_t, rho, sigma, g, y_modulus, h, rs, i)
        u_vec.append(get_u(u_vec, r0, rt, delta_r, delta_t, rho, sigma, g, y_modulus, h, rs, i))

        if i % 450 == 0:
            print('... '+str(i/45)+'%')

        line.set_data(x, y)
        return line,

    # call the animator.  blit=True means only re-draw the parts that have changed.
    anim = animation.FuncAnimation(fig, animate, 4500, init_func=init, interval=240, blit=True)

    print('... Done')

    plt.show()

    return u_vec



    # for n in range(2, 4500):
    #     u_vec.append(get_u(u_vec, r0, rt, delta_r, delta_t, rho, sigma, g, y_modulus, h, rs, n))
    #     if n % 450 == 0:
    #         print('... '+str(count*10)+'%')
    #         count += 1
    #
    # print('... Done')
    #
    # with open('u_vec_2.txt', 'w') as u_vec_file:
    #     for elem in u_vec:
    #         u_vec_file.write('%s\n' % elem)
    #
    # return u_vec


u_vec = simulate_gaussian(6000, 150000, 42300, 300, 1300, 9.81, 950, 2400, 100)

# Source: https://jakevdp.github.io/blog/2012/08/18/matplotlib-animation-tutorial/






# writer = animation.writers['ffmpeg'](fps=30)
# anim.save('Longituninal_Gaussian.avi', writer=writer, fps=30, extra_args=['-vcodec', 'libx264'])
