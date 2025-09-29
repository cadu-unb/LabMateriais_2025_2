import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas as pd

# ------------------------------
# Formato sugerido para a planilha de dados brutos:
# data/medidas_raw.csv
# ------------------------------
# medida_id,cor,angulo_deg,voltage_V
# 1,azul,13,0.812
# 2,azul,15,0.663
# 3,azul,16,0.660
# 4,verde,20,0.398
# 5,laranja,21,0.333
# ...
# ------------------------------

# Exemplo: leitura do CSV
try:
    df = pd.read_csv("data/medidas_raw.csv")
    print("Dados carregados de data/medidas_raw.csv:")
    print(df.head())
except FileNotFoundError:
    print("Arquivo data/medidas_raw.csv não encontrado. Usando tabela média do relatório.")

    # Dados experimentais (Tabela Média)
    freq = np.array([8.214, 6.949, 6.525, 5.259, 5.019]) * 1e14   # Hz
    V = np.array([0.833, 0.670, 0.672, 0.404, 0.337])              # Volts

    df = pd.DataFrame({
        "freq_Hz": freq,
        "V": V
    })

# Constantes físicas
e = 1.602e-19   # C
h_ref = 6.626e-34  # J.s (valor esperado da constante de Planck)

# ------------------------------
# Regressão Linear: V0(f) = (h/e) * f - (w0/e)
# ------------------------------
X = df["freq_Hz"].values.reshape(-1, 1)
y = df["V"].values
reg = LinearRegression().fit(X, y)

slope = reg.coef_[0]   # h/e
intercept = reg.intercept_  # -w0/e

# Constante de Planck experimental
h_exp = slope * e
# Função trabalho experimental
w0_exp = -intercept * e
# Frequência de corte
f_cut = w0_exp / h_exp

# ------------------------------
# Resultados
# ------------------------------
print("--- Resultados Experimentais ---")
print(f"h experimental = {h_exp:.3e} J.s")
print(f"h esperado     = {h_ref:.3e} J.s")
print(f"Função trabalho (J) = {w0_exp:.3e} J")
print(f"Função trabalho (eV) = {w0_exp/e:.3f} eV")
print(f"Frequência de corte = {f_cut:.3e} Hz")

# ------------------------------
# Gráfico
# ------------------------------
plt.figure(figsize=(8,6))
plt.scatter(df["freq_Hz"]*1e-14, df["V"], color='blue', label='Dados experimentais')
plt.plot(df["freq_Hz"]*1e-14, reg.predict(X), color='red', label='Ajuste linear')

plt.xlabel('Frequência [1e14 Hz]')
plt.ylabel('Tensão de Retardo V0 [V]')
plt.title('Efeito Fotoelétrico - Regressão Linear')
plt.legend()
plt.grid(True)
plt.show()
