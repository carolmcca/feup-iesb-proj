import matplotlib.pyplot as plt
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
    global MIU_mist_max,P_out_max,Pout_max,QP_gluc_max,QP_xil_max,QP_mist_max,\
           X_max,miu_gluc,miu_xil,miu_mist,F,P_out,qp_gluc,qp_xil,qp_mist,X2,\
           P2,S2_xil,S2_gluc,x2,x,Pout,QP_gluc,QP_xil,QP_mist,MIU_mist,X,V
    
    #GRÁFICOS
    #glucose
    QP_gluc = []
    QP_gluc_max = []
    #xilose
    QP_xil = []
    QP_xil_max = []
    #globais
    QP_mist = []
    QP_mist_max = []
    MIU_mist = []
    MIU_mist_max = []
    x = []
    x2 = []
    X = []
    X_max = []
    Pout = []
    Pout_max = []
    c = 0
    
    #CICLO
    P_out_max = 0 
    
    V = 100000 #definição do volume
    P = np.linspace(45, 55, num=500) #a concentração de produto não pode passar os 60 g/L
    S_xil = np.linspace(7, 10, num=50)   
    S_gluc = np.linspace(12, 60, num=300)
    
def update_max_values():
                global miu_gluc_max,miu_xil_max,miu_mist_max,MIU_mist_max,\
                    F_max,P_out_max,Pout_max,qp_gluc_max,QP_gluc_max,qp_xil_max,\
                    QP_xil_max,qp_mist_max,QP_mist_max,X2_max,X_max,P2_max,\
                    S2_xil_max,S2_gluc_max
                #atualização dos parâmetros cinéticos
                miu_gluc_max = miu_gluc
                miu_xil_max = miu_xil
                miu_mist_max = miu_mist
                MIU_mist_max.append(miu_mist_max)
                qp_gluc_max = qp_gluc
                QP_gluc_max.append(qp_gluc_max)
                qp_xil_max = qp_xil
                QP_xil_max.append(qp_xil_max)
                qp_mist_max = qp_mist
                QP_mist_max.append(qp_mist_max)
                #atualização do caudal de saída de produto
                F_max = F
                P_out_max = P_out
                Pout_max.append(P_out_max)
                #atualização das [] no reator
                S2_xil_max = S2_xil
                S2_gluc_max = S2_gluc
                X2_max = X2
                X_max.append(X2_max)
                P2_max = P2
                   
def results(plot=True):
    if plot:
        plt.figure()  
        plt.title('Caudal mássico de saída de produto: mistura')          
        plt.plot(x2, Pout, 'r', label='P2*F')
        plt.plot(x, Pout_max, 'b', label='P2*F_max') 
        plt.legend(loc='best')
        plt.figure()
        plt.title('qp da glucose na mistura')  
        plt.plot(x2,QP_gluc, 'r', label='qp_gluc')
        plt.plot(x,QP_gluc_max, 'b', label='qp_gluc_max')
        plt.legend(loc='best')
        plt.figure()
        plt.title('qp da xilose na mistura')  
        plt.plot(x2,QP_xil, 'r', label='qp_xil')
        plt.plot(x,QP_xil_max, 'b', label='qp_xil_max')
        plt.legend(loc='best')
        plt.figure()
        plt.title('qp da mistura')  
        plt.plot(x2,QP_mist, 'r', label='qp_mist')
        plt.plot(x,QP_mist_max, 'b', label='qp_mist_max')
        plt.legend(loc='best')
        plt.figure()
        plt.title('miu da mistura') 
        plt.plot(x2,MIU_mist,'r', label='miu_mist')
        plt.plot(x,MIU_mist_max,'b', label='miu_mist_max')
        plt.legend(loc='best')
        plt.figure()
        plt.title('[células]: mistura')
        plt.plot(x2,X,'r', label='X')
        plt.plot(x,X_max,'b', label='X_max')
        plt.legend(loc='best')
        plt.show()
    print('\nQUIMIOSTATO MISTURA')
    print('Valores fixos:')
    print('V = ', V)
    print('Parâmetros cinéticos:')
    print('miu_gluc = ', miu_gluc_max)
    print('miu_xil = ', miu_xil_max)
    print('miu_mist = ', miu_mist_max)
    print('qs_gluc = ', qs_gluc_max)
    print('qs_xil = ', qs_xil_max)
    print('qp_gluc = ', qp_gluc_max)
    print('qp_xil = ', qp_xil_max)
    print('qp_mist = ', qp_mist_max)
    print('Concentrações de entrada:')
    print('S1_gluc = ', S1_gluc_max)
    print('S1_xil = ', S1_xil_max)
    print('Concentrações de saída == interior do quimiotato')
    print('X = ', X2_max)
    print('S2_gluc = ', S2_gluc_max)
    print('S2_xil= ', S2_xil_max)
    print('P2 = ', P2_max)
    print('Fluxos:')
    print('F = ', F_max)
    print('Pout_max = ', P_out_max)
    print('Produtividade: ',P_out_max/100000,'\n')                



#CÁLCULO DE VALORES MÁXIMOS
for P2 in P: #P varia na gama de valores definida
    for S2_xil in S_xil: #S2_xil varia na gama de valores definida
        for S2_gluc in S_gluc: #S2_gluc varia na gama de valores definida
            #cálculo dos mius
            miu_gluc = mium_gluc*S2_gluc/(Ks_gluc+S2_gluc+(S2_gluc**2/Kis_gluc))*(1-(P2/Pm_sub_gluc)**b_gluc)
            miu_xil = mium_xil*S2_xil/(Ks_xil+S2_xil+(S2_xil**2/Kis_xil))*(1-(P2/Pm_sub_xil)**b_xil)
            miu_mist = miu_gluc*S2_gluc/(S2_gluc+S2_xil)+miu_xil*S2_xil/(S2_xil+S2_gluc)
            #cálculo do caudal de saída de produto
            F = miu_mist*V
            P_out = P2*F #caudal mássico de saída do produto
            c += 1
            #cálculo dos qps
            qp_gluc = qpm_gluc*S2_gluc/(Kp_gluc+S2_gluc+(S2_gluc**2/Kip_gluc))*(1-(P2/Pm_prod_gluc)**g_gluc)
            qp_xil = qpm_xil*S2_xil/(Kp_xil+S2_xil+(S2_xil**2/Kip_xil))*(1-(P2/Pm_prod_xil)**g_xil)
            qp_mist = qp_xil + qp_gluc
            #cálculo de X
            X2 = F*P2/(qp_mist*V)
            
            if P_out > P_out_max: #quando a saída de produto é superior à máxima já encontrada
                #atualização dos valores maximizantes
                update_max_values()
                #atualização de lista para grágicos
                x.append(c)
                
            if c%10 == 0: #atualização dos pontos para representação gráfica
                x2.append(c)
                Pout.append(P_out)
                QP_gluc.append(qp_gluc)
                QP_xil.append(qp_xil)
                QP_mist.append(qp_mist)
                MIU_mist.append(miu_mist)
                X.append(X2)

#cálculo dos qs
qs_gluc_max = miu_gluc_max/Y_XS_gluc + ms_gluc
qs_xil_max = miu_xil_max/Y_XS_xil + ms_xil
#cálculo de [substrato] de entrada
S1_xil_max = S2_xil_max + X2_max*qs_xil_max*V/F_max
S1_gluc_max = S2_gluc_max + X2_max*qs_gluc_max*V/F_max

#DISPLAY DE RESULTADOS
results()