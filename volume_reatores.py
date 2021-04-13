#ATRIBUIÇÃO DE CONSTANTES
#glucose 
mium_gluc = 0.66
qpm_gluc = 2
Ks_gluc = 0.565 
Kp_gluc = 1.34
Kis_gluc = 284
Kip_gluc = 4890
Pm_sub_gluc = 95
Pm_prod_gluc = 103 
b_gluc = 1.29
g_gluc = 1.42
ms_gluc = 0.097
Y_PS_gluc = 0.47
Y_XS_gluc = 0.12
#xilose
mium_xil = 0.19
qpm_xil = 0.25
Ks_xil = 3.4
Kp_xil = 3.4
Kis_xil = 18
Kip_xil = 81
Pm_sub_xil = 59
Pm_prod_xil = 60
b_xil = 1
g_xil = 0.6
ms_xil = 0.067
Y_PS_xil = 0.4
Y_XS_xil = 0.16

#ATRIBUIÇÃO DE VARIÁVEIS (com base nos valores obtidos através do Excel e Python)
#glucose
P2_gluc = 50
S2_gluc = 12.67
miu_gluc = mium_gluc*S2_gluc/(Ks_gluc+S2_gluc+(S2_gluc**2/Kis_gluc))*(1-(P2_gluc/Pm_sub_gluc)**b_gluc)
#xilose
P2_xil = 29.5
S2_xil = 7.8
miu_xil = mium_xil*S2_xil/(Ks_xil+S2_xil+(S2_xil**2/Kis_xil))*(1-(P2_xil/Pm_sub_xil)**b_xil)
#mistura
P2_mist = 49.2685370741483
miu_mist = 0.2809061314810453


Vg_frac = round((P2_mist*miu_mist - P2_xil*miu_xil)/(P2_gluc*miu_gluc - P2_xil*miu_xil),10)
Vx_frac = 1-Vg_frac

Vg, Vx = Vg_frac*100000, Vx_frac*100000
Vg_perc, Vx_perc = Vg_frac*100, Vx_frac*100
print('Volume do reator com glicose: ',Vg,'(', Vg_perc,'%)')
print('Volume do reator com xilose: ',Vx,'(', Vx_perc,'%)')