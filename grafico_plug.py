import matplotlib.pyplot as plt
import numpy as np
#glucose 
mium_gluc = 0.66
Ks_gluc = 0.565 
Kis_gluc = 284
Pm_sub_gluc = 95
b_gluc = 1.29
ms_gluc = 0.097
#xilose
mium_xil = 0.19
Ks_xil = 3.4
Kis_xil = 18
Pm_sub_xil = 59
b_xil = 1
ms_xil = 0.067

y1_p = []
y2_p = []

P = np.linspace(45,49.9,num=90000)
Sm_gluc = 90
Sm_xil = 7.1

teta = Sm_gluc/(Sm_gluc+Sm_xil)*mium_gluc*Sm_gluc/(Ks_gluc+Sm_gluc+Sm_gluc**2/Kis_gluc)
l = Sm_xil/(Sm_gluc+Sm_xil)*mium_xil*Sm_xil/(Ks_xil+Sm_xil+Sm_xil**2/Kis_xil)
psi_gluc = (1/Pm_sub_gluc)**b_gluc
psi_xil = (1/Pm_sub_xil)**b_xil
y2 = teta/l

for Pm in P:
    y1 = ((b_xil+1)*Pm**b_xil*psi_xil-1)/(1-(b_gluc+1)*Pm**b_gluc*psi_gluc)
    y1_p.append(y1)
    y2_p.append(y2)
    if abs(y1-y2)<=0.005:
            root = Pm
    

print('Interseção = ', round(root,2))          
plt.plot(P, y1_p, 'r')
plt.plot(P, y2_p, 'b')
plt.plot(root, y2,'o', color = 'k', label = 'P_max = ' + str(round(root,2)))
plt.legend()
plt.title('Valor máximo de produto : Reator plug flow')
plt.xlabel('P')
plt.ylabel('Expressão')
plt.show()

