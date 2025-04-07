import numpy as np

def fit_lin(x, y, w, display=True):
    '''
    Esegue un fit lineare sulle coppie di punti sperimentali x e y
    con pesi w e stampa a video i risultati se display=True (default).
    Restituisce i parametri A e B del fit con le loro deviazioni standard,
    la covarianza e il chi-quadro del fit.
    '''
    
    S0=np.sum(w)
    Sx=np.sum(w*x)
    Sy=np.sum(w*y)
    Sxx=np.sum(w*x*x)
    Sxy=np.sum(w*x*y)
    D=S0*Sxx-Sx**2
    A=(S0*Sxy-Sy*Sx)/D
    B=(Sxx*Sy-Sxy*Sx)/D
    std_A=np.sqrt(S0/D)
    std_B=np.sqrt(Sxx/D) 
    cov_AB=-Sx/D
    chi2=np.sum(w*(y-A*x-B)**2)
    
    if display:
        print('Parametri del fit:\n')
        print(f'A = {A} +/- {std_A}')
        print(f'B = {B} +/- {std_B}')
        print(f'Covarianza = {cov_AB}')
        print(f'Chi-quadro = {chi2}')

    return (A, B, std_A, std_B, cov_AB, chi2)

def fit_prop_dir(x, y, w, display=True):
    '''
    Esegue un fit con legge di proporzionalità diretta
    sulle coppie di punti sperimentali x e y con pesi w 
    e stampa a video i risultati se display=True (default).
    Restituisce il parametro A del fit, la deviazione standard e il chi-quadro del fit.
    '''
    
    Sxy=np.sum(w*x*y)
    Sxx=np.sum(w*x*x)
    A=Sxy/Sxx
    std_A=np.sqrt(1/Sxx)
    chi2=np.sum(w*(y-A*x)**2)
    
    if display:
        print('Parametri del fit:\n')
        print(f'A = {A} +/- {std_A}')
        print(f'Chi-quadro = {chi2}')

    return (A, std_A, chi2)
    
def fit_quad(x, y, w, display=True):
    '''
    Esegue un fit con una legge di tipo quadratica y=A*x^2+B*x+C
    sulle coppie di punti sperimentali x e y con pesi w 
    e stampa a video i risultati se display=True (default).
    Restituisce i parametri del fit e la matrice di covarianza.
    '''
    
    S0=np.sum(w)
    Sx=np.sum(w*x)
    Sx2=np.sum(w*(x**2))
    Sx3=np.sum(w*(x**3))
    Sx4=np.sum(w*(x**4))
    Sy=np.sum(w*y)
    Sxy=np.sum(w*x*y)
    Sx2y=np.sum(w*(x**2)*y)
    M=np.array([[Sx4, Sx3, Sx2],[Sx3, Sx2, Sx],[Sx2, Sx, S0]])
    V=np.array([Sx2y, Sxy, Sy])
    
    C=np.linalg.inv(M)
    G=np.linalg.solve(M,V)
    chi2=np.sum(w*(y-(A*x**2+B*X+C))**2)
    
    if display:
        print('Matrice di covarianza: \n')
        print(C)
        print('Parametri del fit: \n')
        print(f'A={G[0]}, B={G[1]}, C={G[2]}')
        print(f'Chi-quadro = {chi2}')   
    return (C, G, chi2)