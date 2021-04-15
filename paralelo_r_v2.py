import matplotlib.pyplot as plt
from sis_newton import newton
import numpy as np

def show_results_head():
    print('\nREATORES ABERTOS COM JUNÇÃO DE CAUDAL FINAL (com reciclagem e purga)')

def show_results(gluc_or_xil, args, plot=False):
    if (gluc_or_xil):
        abv = "gluc"
        name = "glucose"
        name_caps = "GLUCOSE"
    else:
        abv = "xil"
        name = "xilose"
        name_caps = "XILOSE"
    
    (Fw_max,Xw_max,Fs_max,Fr_max,X2_max,P_out_max,S2_max,P2_max,qp_max,miu_max,qs_max,divergente,V,F,S1,Fw_perc,Fr_perc,Fs_perc) = args


    print('\n'+name_caps)
    print('Volume do reator:',V)
    print('Parâmetros cinéticos:')
    print('qs_' +abv+' = ', qs_max)
    print('miu_'+abv+' = ',miu_max)
    print('qp_' +abv+' = ',  qp_max)
    print('Entrada: ')
    print('S1_' +abv+' = ',  S1)
    print('F_'  +abv+' = ',  F)
    print('Interior do reator:')
    print('S2_' +abv+' = ',  S2_max)
    print('X2_' +abv+' = ',  X2_max)
    print('P2_' +abv+' = ',  P2_max)
    print('Purga: ')
    print('Fw_' +abv+' = ',  Fw_max, '(',  round(Fw_perc,1), '%)')
    print('Xw_' +abv+' = ',  Xw_max)
    print('Reciclagem: ')
    print('Fr_' +abv+' = ',  Fr_max, '(',  round(Fr_perc,1), '%)')
    print('Saída: ')
    print('Fs_' +abv+' = ',  Fs_max, '(',  round(Fs_perc,1), '%)')
    print('P2*F_max_'+abv+' = ',  P_out_max)
    print('\nNão convergiram: ', divergente)
    
def show_results_final_prod(P_out_total):
    print('\nPRODUTO FINAL')
    print('P2*F_total = ',  P_out_total)
    print('Produtividade = ', P_out_total/100000,'\n')
      
def calculo_de_valores_maximos(args):
    Fw_r,Fr_r,F,V,Y_XS,ms,S2_e,S1,P2_e,qp_e,X2_e,Xw_e,mium,Kis,Ks,b,g,Kp,Kip,Pm_sub,Pm_prod,qm = args
    
    # inicialização de variáveis
    if True:
        e1_e = 50
        e2_e = 50
        divergente = 0
        c = 0
        X2_max_c = 30
        Fw_max = 'n'
        Fr_max = 'n'
        Fs_max = 'n'
        miu_max = 'n'
        qs_max = 'n'
        S2_max = 'n'
        P2_max = 'n'
        qp_max = 'n'
        X2_max = 'n'
        Xw_max = 'n'
        P_out_max = -1
    #CÁLCULO DE VALORES MÁXIMOS
    for Fw in Fw_r: # Fw varia na gama de valores definida
        for Fr in Fr_r: # Fr varia na gama de valores definida
            c += 1
            print(c)
            Fs = F-Fw
            # aux = Xw / X2
            aux = (F+Fr)/(Fw+Fr)
            miu = Fw/V*aux
            qs = miu / Y_XS + ms
            Xn, divergente = newton(S2_e,S1,P2_e,qp_e,X2_e,Xw_e,mium,Kis,Ks,b,g,Kp,Kip,Pm_sub,Pm_prod,qm,Fw,Fs,V,qs,Fr,F,miu,e1_e,e2_e,divergente)
            # atualização de variáveis S2, P2, qp, X2, Xw e P_out
            if True:
                S2 = Xn[0][0]
                P2 = Xn[1][0]
                qp = Xn[2][0]
                X2 = Xn[3][0]
                Xw = Xn[4][0]
                P_out = Fs*P2
            if P_out > P_out_max and Fr>=0 and S2>=0 and Fs>=0 and X2<X2_max_c and X2>=0:
                # atualização dos valores maximizantes
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
                c_max = c
    
    return  Fw_max,Xw_max,Fs_max,Fr_max,X2_max,P_out_max,S2_max,P2_max,qp_max,miu_max,qs_max,divergente

def main():
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
        #glucose
        V_gluc = 79307.74506
        F_gluc = 27048
        S1_gluc = 140
        Fw_gluc_r = np.linspace(0.05*F_gluc,0.3*F_gluc,num=100)  
        Fr_gluc_r = np.linspace(0.35*F_gluc,0.85*F_gluc,num=100) 
        #xilose
        V_xil = 20692.25494
        F_xil = 1052
        S1_xil = 208
        Fw_xil_r  =  np.linspace(0.05*F_xil,0.4*F_xil,num=25) 
        Fr_xil_r  = np.linspace(0.35*F_xil,0.85*F_xil,num=50)
        
        
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
    
    
    args_gluc = (Fw_gluc_r,Fr_gluc_r,F_gluc,V_gluc,Y_XS_gluc,ms_gluc,S2_gluc_e,S1_gluc,P2_gluc_e,qp_gluc_e,X2_gluc_e,Xw_gluc_e,mium_gluc,Kis_gluc,Ks_gluc,b_gluc,g_gluc,Kp_gluc,Kip_gluc,Pm_sub_gluc,Pm_prod_gluc,qpm_gluc)
    args_xil  = (Fw_xil_r,Fr_xil_r,F_xil,V_xil,Y_XS_xil,ms_xil,S2_xil_e,S1_xil,P2_xil_e,qp_xil_e,X2_xil_e,Xw_xil_e,mium_xil,Kis_xil,Ks_xil,b_xil,g_xil,Kp_xil,Kip_xil,Pm_sub_xil,Pm_prod_xil,qpm_xil)
    
    out_gluc = calculo_de_valores_maximos(args_gluc)
    out_xil  = calculo_de_valores_maximos(args_xil)

    (Fw_gluc_max,Xw_gluc_max,Fs_gluc_max,Fr_gluc_max,X2_gluc_max,P_out_gluc_max,S2_gluc_max,P2_gluc_max,qp_gluc_max,miu_gluc_max,qs_gluc_max,divergente_gluc) = out_gluc
    (Fw_xil_max,Xw_xil_max,Fs_xil_max,Fr_xil_max,X2_xil_max,P_out_xil_max,S2_xil_max,P2_xil_max,qp_xil_max,miu_xil_max, qs_xil_max,divergente_xil) = out_xil

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
    show_results_head()

    out_gluc += (V_gluc,F_gluc,S1_gluc,Fw_gluc_perc,Fr_gluc_perc,Fs_gluc_perc)
    show_results(True, out_gluc)
    
    out_xil += (V_xil,F_xil,S1_xil,Fw_xil_perc,Fr_xil_perc,Fs_xil_perc)
    show_results(False, out_xil)

    show_results_final_prod(P_out_total)

if __name__ == "__main__":    
    main()