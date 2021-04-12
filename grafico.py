import matplotlib.pyplot as plt
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

P = [40 + 0.0001*i for i in range(99000)]
S2_gluc = 50
S2_xil = 7

teta = S2_gluc/(S2_gluc+S2_xil)*mium_gluc*S2_gluc/(Ks_gluc+S2_gluc+S2_gluc**2/Kis_gluc)
l = S2_xil/(S2_gluc+S2_xil)*mium_xil*S2_xil/(Ks_xil+S2_xil+S2_xil**2/Kis_xil)
psi_gluc = (1/Pm_sub_gluc)**b_gluc
psi_xil = (1/Pm_sub_xil)**b_xil
y2 = teta/l

for P2 in P:
    y1 = ((b_xil+1)*P2**b_xil*psi_xil-1)/(1-(b_gluc+1)*P2**b_gluc*psi_gluc)
    y1_p.append(y1)
    y2_p.append(y2)
    if abs(y1-y2)<=0.0035:
            root = P2
    
          
plt.plot(P, y1_p, 'r')
plt.plot(P, y2_p, 'b')
plt.plot(root, y2,'o', color = 'k', label = 'P_max = ' + str(round(root,2)))
plt.legend()
plt.xlabel('P')
plt.ylabel('Expressão')
plt.show()

print('int = ', root)