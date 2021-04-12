import matplotlib.pyplot as plt
from sis_newton import newton


#ATRIBUIÇÃO DE CONSTANTES
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
    
#INICIALIZAÇÃO DE VARIÁVEIS
if True:
    global  miu_gluc,miu_xil,qp_gluc,X2_gluc,X2_xil,qp_xil,P2_gluc, P2_xil,\
        S2_xil,S2_gluc,x2,x,V,S1_gluc,S1_xil

    V = 100000 #definição do volume
    
    #glucose
    F_gluc = 34119
    S1_gluc = 139
    Fw_gluc_r = [0.1*F_gluc + i*50 for i in range(int(F_gluc*0.1/50))]  
    Fr_gluc_r = [0.35*F_gluc + i*250 for i in range(int(F_gluc*0.50/250))] 
    #xilose
    F_xil = 6353
    S1_xil = 140 
    Fw_xil_r  = [0.08*F_xil + i*25 for i in range(int(F_xil*0.12/25))]  
    Fr_xil_r  = [0.35*F_xil + i*100 for i in range(int(F_xil*0.50/100))]
    
    
    #ESTIMATIVAS NEWTON
    #glucose
    S2_gluc_e = 12.7
    P2_gluc_e = 50
    qp_gluc_e = 1.05
    X2_gluc_e = 14.7
    Xw_gluc_e = 2.5*X2_gluc_e
    #xilose
    S2_xil_e = 7.9
    P2_xil_e = 20
    qp_xil_e = 0.0015
    X2_xil_e = 23
    Xw_xil_e = 2.5*X2_xil_e
    
    

    
def results():   
        print('REATORES ABERTOS EM PARALELO (com reciclagem e purga)')
        print('Valores fixos:')
        print('V = ', V)
        
        print('\nGLUCOSE')
        print('Parâmetros cinéticos:')
        print('qs_gluc = ', qs_gluc_max)
        print('miu_gluc = ',miu_gluc_max)
        print('qp_gluc = ', qp_gluc_max)
        print('Entrada: ')
        print('S1_gluc = ', S1_gluc)
        print('F_gluc = ', F_gluc)
        print('Interior do reator:')
        print('S2_gluc = ', S2_gluc_max)
        print('X2_gluc = ', X2_gluc_max)
        print('P2_gluc = ', P2_gluc_max)
        print('Purga: ')
        print('Fw_gluc = ', Fw_gluc_max)
        print('Xw_gluc = ', Xw_gluc_max)
        print('Reciclagem: ')
        print('Fr_gluc = ', Fr_gluc_max)
        print('Saída: ')
        print('Fs_gluc = ', Fs_gluc_max)
        print('P2*F_max_gluc = ', P_out_gluc_max)
        
        print('\nNão convergiram: ',divergente_gluc)
        
        print('\nXILOSE')
        print('Parametros cinéticos: ')
        print('qs_xil = ', qs_xil_max)
        print('miu_xil = ',miu_xil_max)
        print('qp_xil = ', qp_xil_max)
        print('Entrada: ')
        print('S1_xil = ', S1_xil)
        print('F_xil = ', F_xil)
        print('Interior do reator:')
        print('S2_xil = ', S2_xil_max)
        print('X2_xil = ', X2_xil_max)
        print('P2_xil = ', P2_xil_max)
        print('Purga: ')
        print('Fw_xil = ', Fw_xil_max)
        print('Xw_xil = ', Xw_xil_max)
        print('Reciclagem: ')
        print('Fr_xil = ', Fr_xil_max)
        print('Saída: ')        
        print('Fs_xil = ', Fs_xil_max)
        print('P2*F_max_xil = ', P_out_xil_max)
        print('\nNão convergiram: ',divergente_xil)
        print('PRODUTO FINAL')
        print('P2*F_total = ', P_out_total)

def upgrade_max_values(Fw,Fr,Fs,miu,qs,S2,P2,qp,X2,Xw,P_out,X2):
        Fw_max = Fw
        Fr_max = Fr
        Fs_max = Fs
        miu_max = miu
        qs_max = qs
        S2_max = S2
        P2_max = P2
        qp_max = qp
        X2_max = X2
        Xw_max = Xw
        P_out_max = P_out
        X2_min = X2
        
def calculo_de_valores_maximos(Fw_r,Fr_r,F,V,Y_XS,ms,S2_e,S1,P2_e,qp_e,X2_e,Xw_e,mium,Kis,
                               Ks,b,g,Kp,Kip,Pm_sub,Pm_prod,qm):
    #inicialização de variáveis
    e1_e = 50
    e2_e = 50
    P_out_max = -1
    X2_min = 300
    divergente = 0
    c = 0
    #CÁLCULO DE VALORES MÁXIMOS
    for Fw in Fw_r: #Fw varia na gama de valores definida
        for Fr in Fr_r: #Fr varia na gama de valores definida
            c+=1
            #cálculo de Fs
            Fs = F-Fw
            # aux = Xw / X2
            aux = (F+Fr)/(Fw+Fr)
            #cálculo de parâmetros cinéticos
            miu = Fw/V*aux
            qs = miu / Y_XS + ms
            #cálculo de Xn através do método de Newton de resolução de sistemas
            Xn, divergente = newton(S2_e,S1,P2_e,qp_e,X2_e,Xw_e,mium,Kis,Ks,b,g,Kp,
                                    Kip,Pm_sub,Pm_prod,qm,Fw,Fs,V,qs,Fr,F,miu,e1_e,e2_e,divergente)
            
            #atualização dos valores de S2, P2 e X2
            S2 = Xn[0][0]
            P2 = Xn[1][0]
            X2 = Xn[3][0]
            P_out = F*P2
            if P_out > P_out_max and Fr>=0 and S2>=0 and Fs>=0 and X2<=X2_min and X2>0:
                #atualização dos valores maximizantes
                upgrade_max_values(Fw,Fr,Fs,miu,qs,S2,P2,Xn[2][0],X2,Xn[4][0],P_out,X2)
                
    
    return Fw_max,Xw_max,Fs_max,Fr_max,X2_max,P_out_max,P_out_p,P_out_max_p,S2_max,\
           P2_max,qp_max,miu_max,qs_max,Fr_p,X2_p,Xw_p,miu_p,qp_p,qs_p,S2_p,divergente

            
Fw_gluc_max,Xw_gluc_max,Fs_gluc_max,Fr_gluc_max,X2_gluc_max,P_out_gluc_max,\
                            P_out_gluc_p,P_out_gluc_max_p,S2_gluc_max,P2_gluc_max,qp_gluc_max,\
                            miu_gluc_max, qs_gluc_max,Fr_gluc_p,X2_gluc_p,Xw_gluc_p,\
                            miu_gluc_p,qp_gluc_p,qs_gluc_p,S2_gluc_p,divergente_gluc= \
                            calculo_de_valores_maximos(
                            Fw_gluc_r,Fr_gluc_r,F_gluc,V,Y_XS_gluc,ms_gluc,S2_gluc_e,
                            S1_gluc,P2_gluc_e,qp_gluc_e,X2_gluc_e,Xw_gluc_e,mium_gluc,Kis_gluc,Ks_gluc,
                            b_gluc,g_gluc,Kp_gluc,Kip_gluc,Pm_sub_gluc,Pm_prod_gluc,qpm_gluc)
                            
Fw_xil_max,Xw_xil_max,Fs_xil_max,Fr_xil_max,X2_xil_max,P_out_xil_max,\
                            P_out_xil_p,P_out_xil_max_p,S2_xil_max,P2_xil_max,qp_xil_max,\
                            miu_xil_max, qs_xil_max,Fr_xil_p,X2_xil_p,Xw_xil_p,\
                            miu_xil_p,qp_xil_p,qs_xil_p,S2_xil_p,divergente_xil= \
                            calculo_de_valores_maximos(
                            Fw_xil_r,Fr_xil_r,F_xil,V,Y_XS_xil,ms_xil,S2_xil_e,
                            S1_xil,P2_xil_e,qp_xil_e,X2_xil_e,Xw_xil_e,mium_xil,Kis_xil,Ks_xil,
                            b_xil,g_xil,Kp_xil,Kip_xil,Pm_sub_xil,Pm_prod_xil,qpm_xil)


#cálculo do caudal mássico de produto total 
P_out_total = P_out_xil_max + P_out_gluc_max

#definição de variáveis para gráficos
x_gluc = list(range(len(P_out_gluc_p)))
x_gluc_max = list(range(len(P_out_gluc_max_p)))
x_Fw_gluc = [i*len(Fr_gluc_r) for i in range(len(Fw_gluc_r))]

x_xil = list(range(len(P_out_xil_p)))
x_xil_max = list(range(len(P_out_xil_max_p)))
x_Fw_xil = [i*len(Fr_xil_r) for i in range(len(Fw_xil_r))]

#DISPLAY DE RESULTADOS
results()
