#DEFINIÇÃO DE CONSTANTES
if True:
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

#VALORES OBTIDOS PELO PROGRAMA simultaneo_rec.py
# GLUCOSE
V_gluc = 79307.74506
# Parâmetros cinéticos:
qs_gluc =  0.5744391030292313
miu_gluc =  0.05729269236350776
qp_gluc =  1.050005639479172
# Entrada:
S1_gluc =  140
F_gluc =  27048
# Interior do reator:
S2_gluc =  89.94269377671188
X2_gluc =  29.719605163396942
P2_gluc =  91.49849111583129
# Purga:
Fw_gluc =  1489.0060606060606
Xw_gluc =  90.6904179492694
# Reciclagem:
Fr_gluc =  10969.466666666665 
# Saída:
Fs_gluc =  25558.99393939394 
P2_F_max_gluc =  2338609.379893222

# Não convergiram:  35

# XILOSE
V_xil = 20692.25494
# Parâmetros cinéticos:
qs_xil =  0.16050013949732708
miu_xil =  0.014960022319572332
qp_xil =  0.04233141545213093
# Entrada:
S1_xil =  208
F_xil =  1052
# Interior do reator:
S2_xil =  114.69987356643867
X2_xil =  29.553895772592256
P2_xil =  24.613534427886407
# Purga:
Fw_xil =  113.96666666666667
Xw_xil =  80.2743787630018
# Reciclagem:
Fr_xil =  432.6081632653061 
# Saída:
Fs_xil =  938.0333333333333 
P2_F_max_xil =  23088.315744505046


f1_gluc = miu_gluc-mium_gluc*S2_gluc/(Ks_gluc+S2_gluc+(S2_gluc**2/Kis_gluc))*(1-(P2_gluc/Pm_sub_gluc)**b_gluc)
f2_gluc = qp_gluc-qpm_gluc*S2_gluc/(Kp_gluc+S2_gluc+(S2_gluc**2/Kip_gluc))*(1-(P2_gluc/Pm_prod_gluc)**g_gluc)
f3_gluc = F_gluc*S1_gluc-qs_gluc*X2_gluc*V_gluc-Fs_gluc*S2_gluc-Fw_gluc*S2_gluc
f4_gluc = qp_gluc*X2_gluc*V_gluc-Fw_gluc*P2_gluc-Fs_gluc*P2_gluc
f5_gluc = (F_gluc+Fr_gluc)*X2_gluc-(Fw_gluc+Fr_gluc)*Xw_gluc
f6_gluc = -Fs_gluc+F_gluc-Fw_gluc
aux_gluc = (F_gluc+Fr_gluc)/(Fw_gluc+Fr_gluc)
f7_gluc = -miu_gluc+Fw_gluc/V_gluc*aux_gluc
f8_gluc = -qs_gluc + miu_gluc / Y_XS_gluc + ms_gluc

f1_xil = miu_xil-mium_xil*S2_xil/(Ks_xil+S2_xil+(S2_xil**2/Kis_xil))*(1-(P2_xil/Pm_sub_xil)**b_xil)
f2_xil = qp_xil-qpm_xil*S2_xil/(Kp_xil+S2_xil+(S2_xil**2/Kip_xil))*(1-(P2_xil/Pm_prod_xil)**g_xil)
f3_xil = F_xil*S1_xil-qs_xil*X2_xil*V_xil-Fs_xil*S2_xil-Fw_xil*S2_xil
f4_xil = qp_xil*X2_xil*V_xil-Fw_xil*P2_xil-Fs_xil*P2_xil
f5_xil = (F_xil+Fr_xil)*X2_xil-(Fw_xil+Fr_xil)*Xw_xil
f6_xil = -Fs_xil+F_xil-Fw_xil
aux_xil = (F_xil+Fr_xil)/(Fw_xil+Fr_xil)
f7_xil = -miu_xil+Fw_xil/V_xil*aux_xil
f8_xil = -qs_xil + miu_xil / Y_XS_xil + ms_xil

print('\nSe o método estiver correto, todas as funções devem tomar valores em módulo inferiores a 10')
print('\nGLUCOSE: ')
print('f1: ',f1_gluc)
print('f2: ',f2_gluc)
print('f3: ',f3_gluc)
print('f4: ',f4_gluc)
print('f5: ',f5_gluc)
print('f6: ',f6_gluc)
print('f7: ',f7_gluc)
print('f8: ',f8_gluc)
print('\nXILOSE: ')
print('f1: ',f1_xil)
print('f2: ',f2_xil)
print('f3: ',f3_xil)
print('f4: ',f4_xil)
print('f5: ',f5_xil)
print('f6: ',f6_xil)
print('f7: ',f7_xil)
print('f8: ',f8_xil)