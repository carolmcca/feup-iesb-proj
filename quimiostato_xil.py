import matplotlib.pyplot as plt
import numpy as np
#ATRIBUIÇÃO DE CONSTANTES
if True: 
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
    global miu_xil_max,MIU_xil_max,F_max,P_out_max,Pout_max,qp_xil_max,\
                    QP_xil_max,X2_max,X_max,P2_max,S2_xil_max,miu_xil,F,P_out,\
                    qp_xil,X2,P2,S2_xil
    
    #gráficos
    MIU_xil = []
    MIU_xil_max = []
    QP_xil = []
    QP_xil_max = []
    Pout = []
    Pout_max = []
    x = []
    x2 = []
    X = []
    X_max = []
    
    #ciclo
    P_out_max = 0 
    c = 0
    
    V = 100000 #definição do volume
    P = np.linspace(20,59,num=400) # O produto não pode passar os 60  
    S_xil = np.linspace(7,10,num=100)
    
def update_max_values():
                global miu_xil_max,MIU_xil_max,qp_xil_max,QP_xil_max,F_max,\
                    P_out_max,Pout_max,S2_xil_max,X2_max,X_max,P2_max
                #atualização dos parâmetros cinéticos
                miu_xil_max = miu_xil
                MIU_xil_max.append(miu_xil_max)
                qp_xil_max = qp_xil
                QP_xil_max.append(qp_xil_max)
                #atualização do caudal de saída de produto
                F_max = F
                P_out_max = P_out
                Pout_max.append(P_out_max)
                #atualização das [] no reator
                S2_xil_max = S2_xil
                X2_max = X2
                X_max.append(X2_max)
                P2_max = P2
                
                
def show_results(plot=False):
    if plot:
        plt.figure()  
        plt.title('Caudal mássico de saída de produto: xilose')          
        plt.plot(x2, Pout, 'r', label='P2*F')
        plt.plot(x, Pout_max, 'b', label='P2*F_max') 
        plt.legend(loc='best')
        plt.figure()
        plt.title('qp da xilose')  
        plt.plot(x2,QP_xil, 'r', label='qp')
        plt.plot(x,QP_xil_max, 'b', label='qp_max')
        plt.legend(loc='best')
        plt.figure()
        plt.title('miu da xilose') 
        plt.plot(x2,MIU_xil,'r', label='miu')
        plt.plot(x,MIU_xil_max,'b', label='miu_max')
        plt.legend(loc='best')
        plt.figure()
        plt.title('X : xilose')
        plt.plot(x2,X,'r', label='X')
        plt.plot(x,X_max,'b', label='X_max')
        plt.legend(loc='best')
        plt.show()
    print('\nQUIMIOSTATO XILOSE')
    print('Valores fixos:')
    print('V = ', V)
    print('Parâmetros cinéticos:')
    print('miu_xil = ', miu_xil_max)
    print('qs_xil = ', qs_xil_max)
    print('qp_xil = ', qp_xil)
    print('Concentrações de entrada:')
    print('S1 = ', S1_xil_max)
    print('Concentrações de saída == interior do quimiotato')
    print('X = ', X2_max)
    print('S2 = ', S2_xil_max)
    print('P2 = ', P2_max)
    print('Fluxos:')
    print('F = ', F_max)
    print('P2*F_max = ', P_out_max,'\n')                

#CÁLCULO DE VALORES MÁXIMOS
for P2 in P:
    for S2_xil in S_xil:
            #cálculo do miu
            miu_xil = mium_xil*S2_xil/(Ks_xil+S2_xil+(S2_xil**2/Kis_xil))*(1-(P2/Pm_sub_xil)**b_xil)
            #cálculo do caudal de saída de produto
            F = miu_xil*V
            P_out = P2*F #caudal mássico de saída do produto
            c += 1
            #cálculo do qp
            qp_xil = qpm_xil*S2_xil/(Kp_xil+S2_xil+(S2_xil**2/Kip_xil))*(1-(P2/Pm_prod_xil)**g_xil)
            #cálculo de X
            X2 = F*P2/(qp_xil*V)
            
            if P_out > P_out_max: #quando a saída de produto é superior à máxima já encontrada
                #atualização dos valores maximizantes
                update_max_values()
                #atualização de lista para grágicos
                x.append(c)
                
            if c%10 == 0: #atualização dos pontos para representação gráfica
                x2.append(c)
                Pout.append(P_out)
                QP_xil.append(qp_xil)
                MIU_xil.append(miu_xil)
                X.append(X2)

#cálculo dos qs
qs_xil_max = miu_xil_max/Y_XS_xil + ms_xil
#cálculo de [substrato] de entrada
S1_xil_max = S2_xil_max + X2_max*qs_xil_max*V/F_max

#DISPLAY DE RESULTADOS
show_results()