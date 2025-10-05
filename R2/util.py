import numpy as np

# Constantes
e = 1.602176634e-19   # C
c = 299792458.0       # m/s

def wavelength_from_diffraction(d_lines_per_mm, theta_deg, order=1):
    """
    Calcula lambda (m) = d * sin(theta) para rede de difração.
      - d_lines_per_mm: linhas por mm (ex.: 600)
      - theta_deg: ângulo em graus
      - order: ordem de difração (default 1)
    """
    d = 1.0 / (d_lines_per_mm * 1e3)  # distância entre linhas (m)
    theta = np.deg2rad(theta_deg)
    return order * d * np.sin(theta)

def freq_from_lambda(lambda_m):
    return c / lambda_m

def regression_h_w0(freq_Hz, V_volts):
    """
    Regressão linear V0 = (h/e)*f - w0/e
    Retorna dicionário com h_exp, w0_exp (J), w0_exp eV, f_cut (Hz),
    slope (h/e) e intercept (≈ -w0/e) e o model sklearn.
    """
    from sklearn.linear_model import LinearRegression
    X = np.array(freq_Hz).reshape(-1, 1)
    y = np.array(V_volts)
    model = LinearRegression().fit(X, y)
    slope = model.coef_[0]
    intercept = model.intercept_
    h_exp = slope * e
    w0_exp = -intercept * e
    f_cut = w0_exp / h_exp if h_exp != 0 else np.nan
    return {
        'h_exp': h_exp,
        'w0_exp_J': w0_exp,
        'w0_exp_eV': w0_exp / e,
        'f_cut_Hz': f_cut,
        'slope_h_over_e': slope,
        'intercept_minus_w0_over_e': intercept,
        'model': model
    }
