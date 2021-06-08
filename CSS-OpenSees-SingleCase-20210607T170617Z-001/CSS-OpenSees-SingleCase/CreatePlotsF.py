import numpy as np
import matplotlib.pyplot as plt

def createPlotsF():
    # Read Data
    # ---------
    strain = np.loadtxt('CycstrainF.out')
    stress = np.loadtxt('CycstressF.out')
    pwp = np.loadtxt('CycpressF.out')

    #Remove time column
    strain = np.delete(strain, 0, 1)
    stress = np.delete(stress, 0, 1)
    pwp = np.delete(pwp, 0, 1)

    ru =  -pwp[:,0] / stress[0,1]      # ru = pwp / sigV(0)
    ru1 = -pwp[:,0]/(0.75*stress[0,1]) # ru = pwp / p(0), p(0) = 1/2*(sigV+sigH), sigH = 0.5 sigV
    ru2 = 1-stress[:,1]/stress[0,1]    # ru = (sigV - sigV(0)) / sigV(0)

    #Plot Results
    # -----------
    plt.figure(figsize=(12, 12))
    plt.clf()
    plt.subplot(2, 2, 1)
    plt.plot(strain[:,2]*100, stress[:,2], color='black', linestyle='solid', linewidth=1.25)
    plt.grid()
    plt.xlabel(r'$\gamma$(%)', fontsize=14)
    plt.ylabel(r'$\tau$(kPa)', fontsize=14)

    plt.subplot(2, 2, 2)
    plt.plot(-stress[:,1], stress[:,2], color='black', linestyle='solid', linewidth=1.25)
    plt.grid()
    plt.xlabel(r'$\sigma_v$ (kPa)', fontsize=14)
    plt.ylabel(r'$\tau$(kPa)', fontsize=14)

    plt.subplot(2, 2, 3)
    plt.plot(strain[:,2]*100, pwp[:,0], color='black', linestyle='solid', linewidth=1.25, label='pwp from pressure node')
    plt.legend()
    plt.xlim(-3, 3)
    plt.ylim(0, 101.3)
    plt.grid()
    plt.xlabel(r'$\gamma$(%)', fontsize=14)
    plt.ylabel(r'pwp(kPa)', fontsize=14)

    plt.subplot(2, 2, 4)
    plt.plot(strain[:,2]*100, ru, color='red', linestyle='solid', linewidth=1.25, label=r'pwp/$\sigma_{v0}$')
    plt.plot(strain[:,2]*100, ru1, color='blue', linestyle='dashed',  linewidth= 1.25, label=r'pwp / $p_0$')
    plt.plot(strain[:,2]*100, ru2, color='green', linestyle='dashed',  linewidth= 1.00, label=r'$1-\sigma_v / \sigma_{v0}$' )

    plt.xlim(-3, 3)
    plt.grid()
    plt.xlabel(r'$\gamma$(%)', fontsize=14)
    plt.ylabel(r'Ru', fontsize=14)
    plt.legend()

    #plt.savefig('PM4Sand_wikiF.eps')
    plt.savefig(r'PM4Sand_wikiF.png')

    plt.show()

if __name__ == "__main__":
    createPlotsF()
