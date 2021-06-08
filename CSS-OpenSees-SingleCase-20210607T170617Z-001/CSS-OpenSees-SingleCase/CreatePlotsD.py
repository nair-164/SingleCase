import numpy as np
import matplotlib.pyplot as plt

def createPlotsD():
    # Read Data
    # ---------
    strain = np.loadtxt('CycstrainD.out')
    stress = np.loadtxt('CycstressD.out')

    #Remove time column
    strain = np.delete(strain, 0, 1)
    stress = np.delete(stress, 0, 1)

    p0  = (stress[0,0]+stress[0,1]) / 2.0
    p   = (stress[:,0]+stress[:,1]) / 2.0
    ru  = 1 - p / p0  # ru evaluated using change in effective mean stress p
    ru2 = 1-stress[:,1]/stress[0,1]  # ru evaluated using chanve in vertical effective stress
 

    #Plot Results
    # -----------
    fig1 = plt.figure(num=1, figsize=(12, 12))
    plt.clf()
    
    axs = []
    axs.append(fig1.add_subplot(221))
    axs.append(fig1.add_subplot(222))
    axs.append(fig1.add_subplot(224))
    
    axs[0].clear()
    axs[0].plot(strain[:,2]*100, stress[:,2], color='black', linestyle='solid', linewidth=1.25)
    axs[0].set_xlabel(r'$\gamma$(%)', fontsize=14)
    axs[0].set_ylabel(r'$\tau$(kPa)', fontsize=14)
    axs[0].grid(True)
    # --------------------
    axs[1].clear()
    axs[1].plot(-stress[:,1], stress[:,2], color='black', linestyle='solid', linewidth=1.25)
    axs[1].set_ylabel(r'$\tau$(kPa)', fontsize=14)
    axs[1].set_xlabel(r'$\sigma_v$ (kPa)', fontsize=14)
    axs[1].grid(True)
    # --------------------
    axs[2].clear()
    axs[2].plot(strain[:,2]*100, ru2, color='green', linestyle='dashed',  linewidth= 1.00, label=r'$1-\sigma_v / \sigma_{v0}$' )
    #axs[2].plot(strain[:,2]*100, 1-stress[:,1]/stress[0,1], color='green', linestyle='dashed',  linewidth= 1.00, label=r'$1-\sigma_v / \sigma_{v0}$' )
    axs[2].plot(strain[:,2]*100, ru, color='blue', linestyle='solid',  linewidth= 1.00, label=r'$1-p / p_{0}$' )
    axs[2].set_ylabel(r'Ru', fontsize=14)
    axs[2].set_xlabel(r'$\gamma$(%)', fontsize=14)
    axs[2].grid(True)
    axs[2].set_xlim(-3, 3)
    axs[2].legend()

    plt.savefig(r'PM4Sand_wikiD.png')
    plt.show()
    

    #plt.figure(figsize=(12, 12))
    #plt.clf()
    #plt.subplot(2, 2, 1)
    #plt.plot(strain[:,2]*100, stress[:,2], color='black', linestyle='solid', linewidth=1.25)
    #plt.grid()
    #plt.xlabel(r'$\gamma$(%)', fontsize=14)
    #plt.ylabel(r'$\tau$(kPa)', fontsize=14)
#
    #plt.subplot(2, 2, 2)
    #plt.plot(-stress[:,1], stress[:,2], color='black', linestyle='solid', linewidth=1.25)
    #plt.grid()
    #plt.xlabel(r'$\sigma_v$ (kPa)', fontsize=14)
    #plt.ylabel(r'$\tau$(kPa)', fontsize=14)
#
    #plt.subplot(2, 2, 4) 
    #plt.plot(strain[:,2]*100, 1-stress[:,1]/stress[0,1], color='green', linestyle='dashed',  linewidth= 1.00, label=r'$1-\sigma_v / \sigma_{v0}$' )
    #plt.plot(strain[:,2]*100, ru, color='blue', linestyle='solid',  linewidth= 1.00, label=r'$1-p / p_{0}$' )
    #plt.xlim(-3, 3)
    #plt.grid()
    #plt.xlabel(r'$\gamma$(%)', fontsize=14)
    #plt.ylabel(r'Ru', fontsize=14)
    #plt.legend()

    #plt.savefig(r'PM4Sand_wikiD.png')

    #plt.show()

if __name__ == "__main__":
    createPlotsD()
