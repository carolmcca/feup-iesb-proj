import numpy as np

def update_max_values(args):
    (miu_gluc,miu_xil,miu_mist,F,P_out,qp_gluc,qp_xil,qp_mist,S1_gluc,S1_xil,Xm,Sm_gluc,Sm_xil,Pm,P2,S2_gluc,S2_xil,X2) = args

    #atualização dos valores de miu maximizantes
    miu_gluc_max = miu_gluc
    miu_xil_max = miu_xil
    miu_mist_max = miu_mist
    
    # atualização do caudal de saída de produto
    F_max = F
    P_out_max = P_out
    
    # atualização dos valores de qp maximizantes
    qp_gluc_max = qp_gluc
    qp_xil_max = qp_xil
    qp_mist_max = qp_mist

    # atualização das [] entrada maximizante
    S1_gluc_max = S1_gluc
    S1_xil_max = S1_xil

    # atualização das [] reator maximizante
    Xm_max = Xm
    Sm_gluc_max = Sm_gluc
    Sm_xil_max = Sm_xil
    Pm_max = Pm
    #atualização das [] saída maximizantes
    P2_max = P2
    S2_gluc_max = S2_gluc
    S2_xil_max = S2_xil
    X2_max = X2

    return (miu_gluc_max,miu_xil_max,miu_mist_max,F_max,P_out_max,qp_gluc_max,qp_xil_max,qp_mist_max,S1_gluc_max,S1_xil_max,Xm_max,Sm_gluc_max,Sm_xil_max,Pm_max,P2_max,S2_gluc_max,S2_xil_max,X2_max)
                
def results(V, args):
    (miu_gluc_max,miu_xil_max,miu_mist_max,F_max,P_out_max,qp_gluc_max,qp_xil_max,qp_mist_max,S1_gluc_max,S1_xil_max,Xm_max,Sm_gluc_max,Sm_xil_max,Pm_max,P2_max,S2_gluc_max,S2_xil_max,X2_max) = args

    print('\nPLUG FLOW MISTURA')
    print('Valores fixos:')
    print('V = ', V)
    print('Concentrações de entrada:')
    print('S1_gluc = ', S1_gluc_max)
    print('S1_xil  = ', S1_xil_max)
    print('Concentrações médias no reator:')
    print('Xm = ', Xm_max)
    print('Sm_gluc = ', Sm_gluc_max)
    print('Sm_xil  = ', Sm_xil_max)
    print('Pm = ', Pm_max)
    print('Concentrações de saída')
    print('X2 = ', X2_max)
    print('S2_gluc = ', S2_gluc_max)
    print('S2_xil  = ', S2_xil_max)
    print('P2 = ', P2_max)
    print('Parâmetros cinéticos:')
    print('miu_gluc = ', miu_gluc_max)
    print('miu_xil  = ', miu_xil_max)
    print('miu_mist = ', miu_mist_max)
    print('Fluxos:')
    print('F = ', F_max)
    print('Pout_max = ', P_out_max) 
    print('Produtividade = ', P_out_max/100000,'\n')               

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
        out_max = ()
        P_out_max = -1 
        c = 0
        V = 100000 # definição do volume
        P = np.linspace(40,59,num=100) # O produto não pode passar os 60
        S_gluc = np.linspace(50,90,num=80)
        S_xil = np.linspace(7,12,num=50)

    #CÁLCULO DE VALORES MÁXIMOS
    for Pm in P:
      for Sm_xil in S_xil:
        for Sm_gluc in S_gluc:
          # cálculo dos mius
          miu_gluc = mium_gluc*Sm_gluc/(Ks_gluc+Sm_gluc+(Sm_gluc**2/Kis_gluc))*(1-(Pm/Pm_sub_gluc)**b_gluc)
          miu_xil  = mium_xil *Sm_xil /(Ks_xil +Sm_xil +(Sm_xil**2 /Kis_xil ))*(1-(Pm/Pm_sub_xil )**b_xil )
          miu_mist = miu_gluc *Sm_gluc/(Sm_gluc+Sm_xil) + miu_xil*Sm_xil/(Sm_xil+Sm_gluc)
          
          # cálculo do caudal de saída de produto
          F = miu_mist*V/2
          P2 = Pm*2
          P_out = P2*F # caudal mássico de saída do produto
          c += 1
          
          # cálculo dos qps
          qp_gluc = qpm_gluc*Sm_gluc/(Kp_gluc+Sm_gluc+(Sm_gluc**2/Kip_gluc))*(1-(Pm/Pm_prod_gluc)**g_gluc)
          qp_xil  = qpm_xil *Sm_xil /(Kp_xil +Sm_xil +(Sm_xil**2 /Kip_xil ))*(1-(Pm/Pm_prod_xil )**g_xil )
          qp_mist = qp_xil + qp_gluc
          
          # cálculo de X
          Xm = F*P2/(qp_mist*V)
          
          # cálculo dos qs
          qs_gluc = miu_gluc/Y_XS_gluc + ms_gluc
          qs_xil  = miu_xil /Y_XS_xil  + ms_xil
          
          # cálculo de [substrato] de entrada
          S1_gluc = Sm_gluc + Xm*qs_gluc*V/(F*2)
          S1_xil  = Sm_xil  + Xm*qs_xil *V/(F*2)
          
          # cálculo [] de saída
          S2_gluc = 2*Sm_gluc - S1_gluc
          S2_xil  = 2*Sm_xil  - S1_xil
          X2 = Xm*2
          
          if P_out > P_out_max and S2_gluc>=0 and S2_xil>=0:
              args = (miu_gluc,miu_xil,miu_mist,F,P_out,qp_gluc,qp_xil,qp_mist,S1_gluc,S1_xil,Xm,Sm_gluc,Sm_xil,Pm,P2,S2_gluc,S2_xil,X2)
              
              # atualização dos valores maximizantes
              out_max = update_max_values(args)
              P_out_max = out_max[4]

    #DISPLAY DE RESULTADOS
    results(V, out_max)

if __name__ == "__main__":
    main()