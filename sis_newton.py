import numpy as np

    
def f1(miu, mium, S2, Ks, Kis, P2, Pm_sub, b):
    return miu-mium*S2/(Ks+S2+(S2**2/Kis))*(1-(P2/Pm_sub)**b)
def f2(qp, qm, S2, Kp, Kip, P2, Pm_prod, g):
    return qp-qm*S2/(Kp+S2+(S2**2/Kip))*(1-(P2/Pm_prod)**g)
def f3(F, S1, qs, X2, V, Fs, Fw, S2):
    return F*S1-qs*X2*V-Fs*S2-Fw*S2
def f4(qp, X2, V, Fw, P2, Fs):
    return qp*X2*V-Fw*P2-Fs*P2
def f5(F, Fr, X2, Fw, Xw):
    return (F+Fr)*X2-(Fw+Fr)*Xw



def df1dS2(P2,Pm_sub,b,S2,Kis,mium,Ks):
    return mium*Kis*((P2/Pm_sub)**b-1)*(Ks*Kis-S2**2)/(Ks*Kis+S2*(Kis+S2))**2
def df1dP2(P2,Pm_sub,b,S2,mium,Kis,Ks):
    # return ((P2/Pm_sub)**b*S2*b*mium)/(P2*(S2**2/Kis+S2+Ks))
    return b*mium*Kis*S2*(P2/Pm_sub)**b/(P2*(Ks*Kis+S2*(Kis+S2)))

def df2dS2(P2,Pm_prod,g,S2,Kp,Kip,qm,qp):
    # return ((1-(P2/Pm_prod)**g)*S2*((2*S2)/Kip+1)*qm)/(qp+S2**2/Kip+S2)**2-((1-(P2/Pm_prod)**g)*qm)/(qp+S2**2/Kip+S2)
    return Kip*qm*(Kip*Kp-S2**2)*((P2/Pm_prod)**g-1)/(Kip*(Kp+S2)+S2**2)**2
def df2dP2(P2,Pm_prod,g,S2,qm,qp,Kp,Kip):
    # return ((P2/Pm_prod)**g*S2*g*qm)/(P2*(qp+S2**2/Kip+S2))
    return Kip*g*qm*S2*(P2/Pm_prod)**g/(P2*(Kip*(Kp+S2)+S2**2))
def df2dqp():
    return 1

def df3dS2(Fw,Fs):
    return -Fw-Fs
def df3dX2(V,qs):
    return -V*qs

def df4dP2(Fw,Fs):
    return -Fw-Fs
def df4dqp(V,X2):
    return V*X2
def df4dX2(V,qp):
    return V*qp

def df5dX2(Fr,F):
    return Fr+F
def df5dXw(Fw,Fr):
    return -Fw-Fr


def mult(X,Y):
    result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]
    return result


def newton(S2_e,S1,P2_e,qp_e,X2_e,Xw_e,mium,Kis,Ks,b,g,Kp,Kip,Pm_sub,Pm_prod,qm,Fw,Fs,V,qs,Fr,F,miu,e1,e2,divergente):
    #definição do vetor solução com as estimativas iniciais
    X = np.array([[S2_e],[P2_e],[qp_e],[X2_e],[Xw_e]])
    S2, P2, qp, X2, Xw = S2_e, P2_e, qp_e, X2_e, Xw_e
    c = 0
    while (e1 > 40 or e2 > 40) and c<=500: #enquanto o erro não for aceitável
            c += 1
            print(c)
            #definição da matriz Jacobiana
            J = np.array([[df1dS2(P2,Pm_sub,b,S2,Kis,mium,Ks), df1dP2(P2,Pm_sub,b,S2,mium,Kis,Ks), 0, 0, 0],
                          [df2dS2(P2,Pm_prod,g,S2,Kp,Kip,qm,qp), df2dP2(P2,Pm_prod,g,S2,qm,qp,Kp,Kip), df2dqp(), 0, 0],
                          [df3dS2(Fw,Fs), 0, 0, df3dX2(V,qs), 0],
                          [0, df4dP2(Fw,Fs), df4dqp(V,X2), df4dX2(V,qp), 0],
                          [0, 0, 0, df5dX2(Fr,F), df5dXw(Fw,Fr)]])
            #cálculo do inverso da matriz Jacobiana
            J_inv = np.linalg.inv(J)
            #cálculo do sistema para os valores de X atuais
            FUN = np.array([[-f1(miu, mium, S2, Ks, Kis, P2, Pm_sub, b)],
                            [-f2(qp, qm, S2, Kp, Kip, P2, Pm_prod, g)],
                            [-f3(F, S1, qs, X2, V, Fs, Fw, S2)],
                            [-f4(qp, X2, V, Fw, P2, Fs)],
                            [-f5(F, Fr, X2, Fw, Xw)]])
            #cálculo do incremento
            H = mult(J_inv,FUN)
            #cálculo da nova estimativa de X
            Xn = X + H
            #atualização do cariáveis
            e1 = np.linalg.norm(FUN)
            e2 = np.linalg.norm(H)/np.linalg.norm(Xn)
            S2, P2, qp, X2, Xw = Xn[0][0], Xn[1][0], Xn[2][0], Xn[3][0], Xn[4][0]
            X = Xn        
    if  e1 > 40 or e2 > 40: #se o ciclo foi parado por limite de iterações
        Xn = np.array([[0],[0],[0],[0],[0]]) #as soluções são definidas como 0
        divergente += 1 # conta número de estimativas iniciais que não convergiram
        
    return Xn,divergente