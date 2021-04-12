import matplotlib.pyplot as plt
from sis_newton import newton
import numpy as np

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
    Fw_gluc_r = np.linspace(0.1*F_gluc,0.2*F_gluc,num=25)  
    Fr_gluc_r = np.linspace(0.35*F_gluc,0.85*F_gluc,num=10) 
    #xilose
    F_xil = 6353
    S1_xil = 140 
    Fw_xil_r  =  np.linspace(0.08*F_xil,0.2*F_xil,num=25) 
    Fr_xil_r  = np.linspace(0.35*F_xil,0.85*F_xil,num=10)
    
    
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
        # fig, axs = plt.subplots(3)
        # fig.suptitle('Caudal mássico de saída: glicose')
        # axs[0].plot(x_gluc, P_out_gluc_p, 'r', label='Pout')
        # axs[0].plot(x_gluc_max, P_out_gluc_max_p, 'b', label='Pout_max') 
        # axs[1].plot(x_gluc, Fr_gluc_p, color = 'r', label='Fr')
        # for i in range(len(x_Fw_gluc)):
        #     axs[1].axvline(x=x_Fw_gluc[i], color = 'b', **{'linestyle': 'dashed'})
        # axs[2].plot(x_gluc, X2_gluc_p, color='r', label='X2')
        # axs[2].plot(x_gluc, Xw_gluc_p, color='b', label='Xw')
        # axs[0].legend(loc='best')
        # axs[1].legend(loc='best')
        # axs[2].legend(loc='best')
        # fig, axs = plt.subplots(3)
        # axs[0].plot(x_gluc, miu_gluc_p, color='r', label='miu')
        # axs[0].plot(x_gluc, qp_gluc_p, color='b', label='qp')
        # axs[0].plot(x_gluc, qs_gluc_p, color='k', label='qs')
        # axs[1].plot(x_gluc, Fr_gluc_p, color = 'r', label='Fr')
        # for i in range(len(x_Fw_gluc)):
        #     axs[1].axvline(x=x_Fw_gluc[i], color = 'b', **{'linestyle': 'dashed'})
        # axs[2].plot(x_gluc, S2_gluc_p, color='r',label='S2')
        # axs[0].legend(loc='best')
        # axs[1].legend(loc='best')
        # axs[2].legend(loc='best')
        # plt.figure()
        # plt.title('Caudal mássico de saída: xilose')          
        # plt.plot(x_xil, P_out_xil_p, 'r', label='Pout_xil')
        # plt.plot(x_xil_max, P_out_xil_max_p, 'b', label='Pout_xil_max') 
        # plt.legend(loc='best')
        print('REATORES ABERTOS EM PARALELO (com reciclagem e purga)')
        print('Valores fixos:')
        print('V = ', V)
        
        print('\nGLUCOSE')
        print('Parâmetros cinéticos:')
        print('qs_gluc = ', round(qs_gluc_max,3))
        print('miu_gluc = ',round(miu_gluc_max,3))
        print('qp_gluc = ',  round(qp_gluc_max,3))
        print('Entrada: ')
        print('S1_gluc = ',  round(S1_gluc))
        print('F_gluc = ',  round(F_gluc))
        print('Interior do reator:')
        print('S2_gluc = ',  round(S2_gluc_max,3))
        print('X2_gluc = ',  round(X2_gluc_max,3))
        print('P2_gluc = ',  round(P2_gluc_max,3))
        print('Purga: ')
        print('Fw_gluc = ',  round(Fw_gluc_max,3), '(',  round(Fw_gluc_perc,3), '%)')
        print('Xw_gluc = ',  round(Xw_gluc_max,3))
        print('Reciclagem: ')
        print('Fr_gluc = ',  round(Fr_gluc_max,3), '(',  round(Fr_gluc_perc,3), '%)')
        print('Saída: ')
        print('Fs_gluc = ',  round(Fs_gluc_max,3), '(',  round(Fs_gluc_perc,3), '%)')
        print('P2*F_max_gluc = ',  round(P_out_gluc_max,3))
        
        print('\nNão convergiram: ', divergente_gluc)
        
        print('\nXILOSE')
        print('Parametros cinéticos: ')
        print('qs_xil = ',  round(qs_xil_max,3))
        print('miu_xil = ',  round(miu_xil_max,3))
        print('qp_xil = ',  round(qp_xil_max,3))
        print('Entrada: ')
        print('S1_xil = ',  round(S1_xil))
        print('F_xil = ',  round(F_xil))
        print('Interior do reator:')
        print('S2_xil = ',  round(S2_xil_max,3))
        print('X2_xil = ',  round(X2_xil_max,3))
        print('P2_xil = ',  round(P2_xil_max,3))
        print('Purga: ')
        print('Fw_xil = ',  round(Fw_xil_max,3), '(',  round(Fw_xil_perc,3), '%)')
        print('Xw_xil = ',  round(Xw_xil_max,3))
        print('Reciclagem: ')
        print('Fr_xil = ',  round(Fr_xil_max,3), '(',  round(Fr_xil_perc,3), '%)')
        print('Saída: ')        
        print('Fs_xil = ',  round(Fs_xil_max,3), '(',  round(Fs_xil_perc,3), '%)')
        print('P2*F_max_xil = ',  round(P_out_xil_max,3))
        print('\nNão convergiram: ',divergente_xil)
        print('\nPRODUTO FINAL')
        print('P2*F_total = ',  round(P_out_total,3))
        
def calculo_de_valores_maximos(Fw_r,Fr_r,F,V,Y_XS,ms,S2_e,S1,P2_e,qp_e,X2_e,Xw_e,mium,Kis,
                               Ks,b,g,Kp,Kip,Pm_sub,Pm_prod,qm):
    #inicialização de variáveis
    e1_e = 50
    e2_e = 50
    P_out_max = -1
    X2_min = 300
    divergente = 0
    c = 0
    X2_max_c = 40
    Fw_max = Fw_r[0]
    Fr_max = Fr_r[0]
    Fs_max = F-Fw_r[0]
    miu_max = Fw_r[0]/V*((F+Fr_r[0])/(Fw_r[0]+Fr_r[0]))
    qs_max = miu_max / Y_XS + ms
    S2_max = S2_e
    P2_max = P2_e
    qp_max = qp_e
    X2_max = X2_e
    Xw_max = Xw_e
    P_out_max = F*P2_e
    #CÁLCULO DE VALORES MÁXIMOS
    for Fw in Fw_r: #Fw varia na gama de valores definida
        print('####################################################################################')
        for Fr in Fr_r: #Fr varia na gama de valores definida
            c+=1
            Fs = F-Fw
            # aux = Xw / X2
            aux = (F+Fr)/(Fw+Fr)
            miu = Fw/V*aux
            qs = miu / Y_XS + ms
            Xn, divergente = newton(S2_e,S1,P2_e,qp_e,X2_e,Xw_e,mium,Kis,Ks,b,g,Kp,Kip,Pm_sub,Pm_prod,
                        qm,Fw,Fs,V,qs,Fr,F,miu,e1_e,e2_e,divergente)
            S2 = Xn[0][0]
            P2 = Xn[1][0]
            qp = Xn[2][0]
            X2 = Xn[3][0]
            Xw = Xn[4][0]
            P_out = F*P2
            if P_out > P_out_max and Fr>=0 and S2>=0 and Fs>=0 and X2<X2_max_c and X2>0:
                #atualização dos valores maximizantes
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
                X2_max = X2
    
    return Fw_max,Xw_max,Fs_max,Fr_max,X2_max,P_out_max,S2_max,\
           P2_max,qp_max,miu_max,qs_max,divergente

            
Fw_gluc_max,Xw_gluc_max,Fs_gluc_max,Fr_gluc_max,X2_gluc_max,P_out_gluc_max,\
                            S2_gluc_max,P2_gluc_max,qp_gluc_max,\
                            miu_gluc_max, qs_gluc_max,divergente_gluc= \
                            calculo_de_valores_maximos(
                            Fw_gluc_r,Fr_gluc_r,F_gluc,V,Y_XS_gluc,ms_gluc,S2_gluc_e,
                            S1_gluc,P2_gluc_e,qp_gluc_e,X2_gluc_e,Xw_gluc_e,mium_gluc,Kis_gluc,Ks_gluc,
                            b_gluc,g_gluc,Kp_gluc,Kip_gluc,Pm_sub_gluc,Pm_prod_gluc,qpm_gluc)
                            
Fw_xil_max,Xw_xil_max,Fs_xil_max,Fr_xil_max,X2_xil_max,P_out_xil_max,\
                            S2_xil_max,P2_xil_max,qp_xil_max,\
                            miu_xil_max, qs_xil_max,divergente_xil= \
                            calculo_de_valores_maximos(
                            Fw_xil_r,Fr_xil_r,F_xil,V,Y_XS_xil,ms_xil,S2_xil_e,
                            S1_xil,P2_xil_e,qp_xil_e,X2_xil_e,Xw_xil_e,mium_xil,Kis_xil,Ks_xil,
                            b_xil,g_xil,Kp_xil,Kip_xil,Pm_sub_xil,Pm_prod_xil,qpm_xil)


#cálculo das percentagens dos fluxos
Fw_gluc_perc = Fw_gluc_max/F_gluc*100
Fr_gluc_perc = Fr_gluc_max/F_gluc*100
Fs_gluc_perc = Fs_gluc_max/F_gluc*100
Fw_xil_perc = Fw_xil_max/F_xil*100
Fr_xil_perc = Fr_xil_max/F_xil*100
Fs_xil_perc = Fs_xil_max/F_xil*100
#cálculo do caudal mássico de produto total 
P_out_total = P_out_xil_max + P_out_gluc_max

#DISPLAY DE RESULTADOS
results()
