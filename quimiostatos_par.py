import matplotlib.pyplot as plt
import numpy as np
   
def update_max_values(miu,MIU_max,qp,QP_max,F,P_out,Pout_max,S2,X2,X_max,P2):
    #ATUALIZAÇÃO DOS VALORES MÁXIMOS
    #atualização dos parâmetros cinéticos
    miu_max = miu
    MIU_max.append(miu_max)
    qp_max = qp
    QP_max.append(qp_max)
    #atualização do caudal de saída de produto
    F_max = F
    P_out_max = P_out
    Pout_max.append(P_out_max)
    #atualização das [] no reator
    S2_max = S2
    X2_max = X2
    X_max.append(X2_max)
    P2_max = P2
    return miu_max,MIU_max,F_max,P_out_max,Pout_max,qp_max,QP_max,X2_max,X_max,P2_max,S2_max            
                
def show_results(gluc_or_xil, args, plot=True):
    if (gluc_or_xil):
        abv = "gluc"
        name = "glucose"
        name_caps = "GLUCOSE"
    else:
        abv = "xil"
        name = "xilose"
        name_caps = "XILOSE"

    (miu_max,MIU_max,F_max,P_out_max,Pout_max,qp_max,QP_max,X2_max,X_max,P2_max,x,x_max,Pout,QP,MIU,X,S2_max,qs_max,S1_max,V) = args

    if plot:
        plt.figure()
        plt.title('Caudal mássico de saída de produto: ' +name)          
        plt.plot(x, Pout, 'r', label='P2*F')
        plt.plot(x_max, Pout_max, 'b', label='P2*F_max') 
        plt.legend(loc='best')
        plt.figure()
        plt.title('qp da '+name)  
        plt.plot(x,QP, 'r', label='qp')
        plt.plot(x_max,QP_max, 'b', label='qp_max')
        plt.legend(loc='best')
        plt.figure()
        plt.title('miu da '+name) 
        plt.plot(x,MIU,'r', label='miu')
        plt.plot(x_max,MIU_max,'b', label='miu_max')
        plt.legend(loc='best')
        plt.figure()
        plt.title('X : '+name)
        plt.plot(x,X,'r', label='X2')
        plt.plot(x_max,X_max,'b', label='X2_max')
        plt.legend(loc='best')
        plt.show()
    print('\nQUIMIOSTATO '+name_caps)
    print('Valores fixos:')
    print('V = ', V)
    print('Parâmetros cinéticos:')
    print('miu = ', miu_max)
    print('qs = ', qs_max)
    print('qp = ', qp_max)
    print('Concentrações de entrada:')
    print('S1 = ', S1_max)
    print('Concentrações de saída == interior do quimiotato')
    print('X = ', X2_max)
    print('S2 = ', S2_max)
    print('P2 = ', P2_max)
    print('Fluxos:')
    print('F = ', F_max)
    print('P2*F_max = ', P_out_max)
    print('Produtividade: ',P_out_max/100000,'\n')                

def calculate_max_values(args):
    #CÁLCULO DE VALORES MÁXIMOS
    (P,S,mium,Ks,Kis,Pm_sub,b,V,qpm,Kp,Kip,Pm_prod,g) = args
    #inicialização de variáveis para representação gráfica
    if True:
        QP_gluc_max = []
        MIU_gluc_max = []
        Pout_gluc_max = []
        X_max = []
        c = 0
        x = []
        x_max = []
        Pout = []
        MIU = []
        QP = []
        X = []
    for P2 in P: #P2 varia na gama de valores definida
        for S2 in S: #S2 varia na gama de valores definida
                c += 1
                #cálculo do miu
                miu = mium*S2/(Ks+S2+(S2**2/Kis))*(1-(P2/Pm_sub)**b)
                #cálculo do caudal de saída de produto
                F = miu*V
                P_out = P2*F #caudal mássico de saída do produto
                #cálculo do qp
                qp = qpm*S2/(Kp+S2+(S2**2/Kip))*(1-(P2/Pm_prod)**g)
                #cálculo de X
                X2 = F*P2/(qp*V)
                
                if P_out > P_out_max: #quando a saída de produto é superior à máxima já encontrada
                    #atualização dos valores maximizantes
                    out_update = update_max_values(miu,MIU_max,qp,QP_max,F,P_out,Pout_max,S2,X2,X_max,P2)
                    (miu_max,MIU_max,F_max,P_out_max,Pout_max,qp_max,QP_max,X2_max,X_max,P2_max,S2_max) = out_update
                    #atualização de lista para grágicos
                    x_max.append(c)
                    
                if c%10 == 0: #atualização dos pontos para representação gráfica
                    x.append(c)
                    Pout.append(P_out)
                    QP.append(qp)
                    MIU.append(miu)
                    X.append(X2)
    out_update += (x,x_max,Pout,QP,MIU,X)
    return out_update

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
        V_gluc = 79307.74506 # definição do volume de acordo com a produtividade do quimiotato misto
        P_gluc = np.linspace(20,94,num=600) # a concentração de produto não pode passar os 95 g/L  
        S_gluc = np.linspace(12,60,num=500)
        #xilose
        V_xil = 20692.25494 # definição do volume de acordo com a produtividade do quimiotato misto
        P_xil = np.linspace(20,59,num=400) # O a concentração de produto não pode passar os 60 g/L  
        S_xil = np.linspace(7,10,num=100)
    #definição de parâmetros de entrada para calculo dos valores maximizantes
    args_gluc = (P_gluc,S_gluc,mium_gluc,Ks_gluc,Kis_gluc,Pm_sub_gluc,b_gluc,V_gluc,qpm_gluc,Kp_gluc,Kip_gluc,Pm_prod_gluc,g_gluc)
    args_xil = (P_xil,S_xil,mium_xil,Ks_xil,Kis_xil,Pm_sub_xil,b_xil,V_xil,qpm_xil,Kp_xil,Kip_xil,Pm_prod_xil,g_xil)
    #cálculo dos valores máximos
    out_gluc = calculate_max_values(args_gluc)
    out_xil = calculate_max_values(args_xil)
    #atualização de variáveis
    (miu_gluc_max,MIU_gluc_max,F_gluc_max,P_out_gluc_max,Pout_gluc_max,qp_gluc_max,QP_gluc_max,X2_gluc_max,X_gluc_max,P2_gluc_max,S2_gluc_max,x_gluc,x_gluc_max,Pout_gluc,QP_gluc,MIU_gluc,X_gluc) = out_gluc
    (miu_xil_max,MIU_xil_max,F_xil_max,P_out_xil_max,Pout_xil_max,qp_xil_max,QP_xil_max,X2_xil_max,X_xil_max,P2_xil_max,S2_xil_max,x_xil,x_xil_max,Pout_xil,QP_xil,MIU_xil,X_xil) = out_xil
    
    #cálculo dos qs
    qs_gluc_max = miu_gluc_max/Y_XS_gluc + ms_gluc
    qs_xil_max = miu_xil_max/Y_XS_xil + ms_xil
    #cálculo de [substrato] de entrada
    S1_gluc_max = S2_gluc_max + X2_gluc_max*qs_gluc_max*V_gluc/F_gluc_max
    S1_xil_max = S2_xil_max + X2_xil_max*qs_xil_max*V_xil/F_xil_max

    #atualização de tuplo para display de resultados
    out_gluc += (qs_gluc_max,S1_gluc_max,V_gluc)
    out_xil += (qs_xil_max,S1_xil_max,V_xil)

    #cálculo do caudal mássico de produto total
    P_out_total = P_out_gluc_max + P_out_xil_max
    #cálculo da produtividade
    prod = P_out_total/100000

    #DISPLAY DE RESULTADOS
    show_results(True, out_gluc, False)
    show_results(False, out_xil, False)

if __name__ == "__main__":    
    main()