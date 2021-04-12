import matplotlib.pyplot as plt

#DEFINIÇÃO DE VARIÁVEIS E CONSTANTES
G2 = 45.6
S2 = 7

#glucose
mium_gluc = 0.66
Ks_gluc = 0.565 
Kis_gluc = 284
Pm_sub_gluc = 95 
b_gluc = 1.29
#xilose
mium_xil = 0.19
Ks_xil = 3.4
Kis_xil = 18
Pm_sub_xil = 59
b_xil = 1

y = []


def P_max(P,b_gluc,b_xil,Pm_sub_gluc,Pm_sub_xil,mium_gluc,mium_xil,G2,S2,Kis_gluc,Kis_xil,Ks_gluc,Ks_xil):
    #Encontra a raiz da função (valor de P que maximiza F*P)
    root = -1
    Kg = Pm_sub_gluc**b_gluc
    Kx = Pm_sub_xil**b_xil
    kg = G2*mium_gluc*G2/(Ks_gluc+G2+G2**2/Kis_gluc)
    kx = S2*mium_xil*S2/(Ks_xil+S2+S2**2/Kis_xil)
    for i in range(len(P)):
        y.append((P[i]**b_xil*(b_xil+1)-Kx)/(Kg-P[i]**b_gluc*(b_gluc+1))-kg/kx*Kx/Kg)
        if abs(y[i])<=0.1:
            root = P[i]
    return y,root

P = [40+i*0.05 for i in range(300)]
y,root = P_max(P,b_gluc,b_xil,Pm_sub_gluc,Pm_sub_xil,mium_gluc,mium_xil,G2,S2,Kis_gluc,Kis_xil,Ks_gluc,Ks_xil)

#Print dos resultados
plt.plot(P, y)
plt.axhline(color = 'k')
print('root = ', root)
plt.axvline(x=root, color = 'r', **{'linestyle': 'dashed'})