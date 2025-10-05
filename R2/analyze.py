import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Constantes
e = 1.602e-19
h_ref = 6.62607015e-34

# Dados médios do relatório (substitua por leitura do CSV se quiser)
freq = np.array([8.218, 6.949, 6.735, 5.368, 5.125]) * 1e14   # Hz
V = np.array([1.64, 1.33, 1.28, 0.96, 0.91])              # Volts

# Regressão
X = freq.reshape(-1, 1)
y = V
reg = LinearRegression().fit(X, y)

slope = reg.coef_[0]
intercept = reg.intercept_

# Constantes experimentais
h_exp = slope * e
w0_exp = -intercept * e
f_cut = w0_exp / h_exp

def run_analysis(make_plot=True):
    """Executa análise e retorna dicionário com resultados principais"""
    results = {
        "freq": freq,
        "V": V,
        "h_exp": h_exp,
        "h_ref": h_ref,
        "w0_J": w0_exp,
        "w0_eV": w0_exp / e,
        "f_cut_Hz": f_cut,
        "slope": slope,
        "intercept": intercept,
        "reg": reg
    }

    if make_plot:
        plt.figure(figsize=(8,6))
        plt.scatter(freq*1e-14, V, color='blue', label='Dados experimentais')
        plt.plot(freq*1e-14, reg.predict(X), color='red', label='Ajuste linear')
        plt.xlabel('Frequência [1e14 Hz]')
        plt.ylabel('Tensão de Retardo V0 [V]')
        plt.title('Efeito Fotoelétrico - Regressão Linear')
        plt.legend()
        plt.grid(True)
        plt.savefig("V0_vs_f_regressao.png", dpi=300)
        plt.close()

    return results

if __name__ == "__main__":
    r = run_analysis(make_plot=True)
    print(r)
