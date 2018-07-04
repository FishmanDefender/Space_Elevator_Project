

for m in range(0, 1440):
        if m == 0:
            u_mnext = 0
            print('Radius '+str(delta_r*m+r0)+' km: '+str(u_mnext))
        elif m == 1439:
            u_mnext = ((delta_t/delta_r)**2*(u[m]-2*u[m]+u[m-1])+(delta_t**2/(delta_r*h))*((r0/(m*delta_r+r0))**2-(r0**2*(m*delta_r+r0)/rs**3)*(u[m]-u[m])))*(y_modulus*10**3/rho)+2*u[m]-u_before[m]
            print('Radius '+str(delta_r*m+r0)+' km: '+str(u_mnext))
        else:
            u_mnext = ((delta_t/delta_r)**2*(u[m+1]-2*u[m]+u[m-1])+(delta_t**2/(delta_r*h))*((r0/(m*delta_r+r0))**2-(r0**2*(m*delta_r+r0)/rs**3))*(u[m+1]-u[m]))*(y_modulus*10**3/rho)+2*u[m]-u_before[m]
            print('Radius '+str(delta_r*m+r0)+' km: '+str(u_mnext))
            print('(('+str((delta_t/delta_r)**2)+') * ('+str(u[m+1]-2*u[m]+u[m-1])+') + ('+str((delta_t**2/(delta_r*h)))+') * (('+str((r0/(m*delta_r+r0))**2)+') - ('+str((r0**2*(m*delta_r+r0)/rs**3))+')) * ('+str(u[m+1]-u[m])+')) * ('+str(y_modulus*10**3/rho)+') + '+str(2*u[m])+' - '+str(u_before[m]))
