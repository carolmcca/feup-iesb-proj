import matplotlib.pyplot as plt
import numpy as np
#ATRIBUIÇÃO DE CONSTANTES
if True: 
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
   
#INICIALIZAÇÃO DE VARIÁVEIS
if True:
    global miu_gluc_max,MIU_gluc_max,F_max,P_out_max,Pout_max,qp_gluc_max,\
                    QP_gluc_max,X2_max,X_max,P2_max,S2_gluc_max,miu_gluc,F,P_out,\
                    qp_gluc,X2,P2,S2_gluc

    #Gráficos
    QP_gluc = []
    QP_gluc_max = []
    MIU_gluc = []
    MIU_gluc_max = []
    Pout = []
    Pout_max = []
    x2 = []
    x = []
    X = []
    X_max = []
    c = 0
    
    # ciclo
    P_out_max = 0 
    

    V = 70385 # definição do volume
    P = np.linspace(20,94,num=600) # a concentração de produto não pode passar os 95 g/L  
    S_gluc = np.linspace(12,60,num=500)
    
def update_max_values():
    #atualização dos valores máximos
                global miu_gluc_max,MIU_gluc_max,F_max,P_out_max,Pout_max,\
                    qp_gluc_max,QP_gluc_max,X2_max,X_max,P2_max,S2_gluc_max
                #atualização dos parâmetros cinéticos
                miu_gluc_max = miu_gluc
                MIU_gluc_max.append(miu_gluc_max)
                qp_gluc_max = qp_gluc
                QP_gluc_max.append(qp_gluc_max)
                #atualização do caudal de saída de produto
                F_max = F
                P_out_max = P_out
                Pout_max.append(P_out_max)
                #atualização das [] no reator
                S2_gluc_max = S2_gluc
                X2_max = X2
                X_max.append(X2_max)
                P2_max = P2
                
                
def show_results(plot=False):
    if plot:
        plt.figure()  
        plt.title('Caudal mássico de saída de produto: glucose')          
        plt.plot(x2, Pout, 'r', label='P2*F')
        plt.plot(x, Pout_max, 'b', label='P2*F_max') 
        plt.legend(loc='best')
        plt.figure()
        plt.title('qp da glucose')  
        plt.plot(x2,QP_gluc, 'r', label='qp')
        plt.plot(x,QP_gluc_max, 'b', label='qp_max')
        plt.legend(loc='best')
        plt.figure()
        plt.title('miu da glucose') 
        plt.plot(x2,MIU_gluc,'r', label='miu')
        plt.plot(x,MIU_gluc_max,'b', label='miu_max')
        plt.legend(loc='best')
        plt.figure()
        plt.title('X : glucose')
        plt.plot(x2,X,'r', label='X2')
        plt.plot(x,X_max,'b', label='X2_max')
        plt.legend(loc='best')
        plt.show()
    print('\nQUIMIOSTATO GLUCOSE')
    print('Valores fixos:')
    print('V = ', V)
    print('Parâmetros cinéticos:')
    print('miu_gluc = ', miu_gluc_max)
    print('qs = ', qs_gluc_max)
    print('qp = ', qp_gluc_max)
    print('Concentrações de entrada:')
    print('S1 = ', S1_gluc_max)
    print('Concentrações de saída == interior do quimiotato')
    print('X = ', X2_max)
    print('S2 = ', S2_gluc_max)
    print('P2 = ', P2_max)
    print('Fluxos:')
    print('F = ', F_max)
    print('P2*F_max = ', P_out_max)
    print('Produtividade: ',P_out_max/100000,'\n')                

#CÁLCULO DE VALORES MÁXIMOS
for P2 in P: #P2 varia na gama de valores definida
    for S2_gluc in S_gluc: #S2 varia na gama de valores definida
            c += 1
            #cálculo do miu
            miu_gluc = mium_gluc*S2_gluc/(Ks_gluc+S2_gluc+(S2_gluc**2/Kis_gluc))*(1-(P2/Pm_sub_gluc)**b_gluc)
            #cálculo do caudal de saída de produto
            F = miu_gluc*V
            P_out = P2*F #caudal mássico de saída do produto
            #cálculo do qp
            qp_gluc = qpm_gluc*S2_gluc/(Kp_gluc+S2_gluc+(S2_gluc**2/Kip_gluc))*(1-(P2/Pm_prod_gluc)**g_gluc)
            #cálculo de X
            X2 = F*P2/(qp_gluc*V)
            
            if P_out > P_out_max: #quando a saída de produto é superior à máxima já encontrada
                #atualização dos valores maximizantes
                update_max_values()
                #atualização de lista para grágicos
                x.append(c)
                
            if c%10 == 0: #atualização dos pontos para representação gráfica
                x2.append(c)
                Pout.append(P_out)
                QP_gluc.append(qp_gluc)
                MIU_gluc.append(miu_gluc)
                X.append(X2)

#cálculo do qs
qs_gluc_max = miu_gluc_max/Y_XS_gluc + ms_gluc
#cálculo de [substrato] de entrada
S1_gluc_max = S2_gluc_max + X2_max*qs_gluc_max*V/F_max

#DISPLAY DE RESULTADOS
show_results()