"""
Hall Effect Analysis - Magnetic Field Dependence
------------------------------------------------
This script analyzes the relationship between the Hall voltage (V_H)
and the applied magnetic field (B), for a fixed DC current (I_DC).

It performs:
1. Linear regression (V_H vs B)
2. Optional estimation of Hall coefficient (R_H) and carrier concentration (n)
3. Plot generation with publication-ready formatting

Author: Thiago Ferreira
Date: 2025-10-10
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.linear_model import LinearRegression


def load_data(file_path: str) -> pd.DataFrame:
    """
    Loads Hall effect measurement data from a CSV file.
    Required columns: 'B' and 'V_H'.

    Parameters
    ----------
    file_path : str
        Path to CSV file.

    Returns
    -------
    pd.DataFrame
        Cleaned dataframe.
    """
    df = pd.read_csv(file_path)
    expected_cols = {'B', 'V_H'}
    if not expected_cols.issubset(df.columns):
        raise ValueError(f"Missing required columns: {expected_cols - set(df.columns)}")
    return df.dropna().reset_index(drop=True)

def linear_fit(x: np.ndarray, y: np.ndarray) -> tuple[np.ndarray, float, float]:
    """
    Fits y = m*x + b using least squares.

    Returns
    -------
    (y_pred, slope, intercept)
    """
    model = LinearRegression()
    x = x.reshape(-1, 1)
    model.fit(x, y)
    y_pred = model.predict(x)
    return y_pred, model.coef_[0], model.intercept_


def estimate_hall_coefficient(slope: float, I: float, t: float) -> dict:
    """
    Estimates the Hall coefficient and carrier concentration.

    Formula:
        R_H = (slope * t) / I
        n = 1 / (q * R_H)

    Parameters
    ----------
    slope : float
        Slope from V_H vs B fit [V/T].
    I : float
        DC current [A].
    t : float
        Sample thickness [m].

    Returns
    -------
    dict
        Dictionary with R_H [m^3/C] and n [1/m^3].
    """
    q = 1.602e-19  #constant
    R_H = (slope * t) / I
    n = 1 / (q * R_H) if R_H != 0 else np.inf
    return {"R_H": R_H, "n": n}



def plot_hall_vs_B(x, y, slope, intercept, output_path=None):
    """
    Generates Hall voltage vs magnetic field plot.
    """
    plt.figure(figsize=(7, 5))
    plt.scatter(x, y, color='royalblue', label='Experimental data')
    plt.plot(x, slope * x + intercept, color='crimson', linewidth=2.2,
             label=f'Fit: V_H = {slope:.3e}·B + {intercept:.3e}')

    plt.title("Hall Voltage vs Magnetic Field", fontsize=14, fontweight='bold')
    plt.xlabel("Magnetic Field B [T]", fontsize=12)
    plt.ylabel("Hall Voltage V_H [V]", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()
    plt.tight_layout()

    if output_path:
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(output_path, dpi=300)
    plt.show()



def analyze_hall_vs_B(data_file: str, I: float, t: float, output_dir: str = "results"):
    """
    Main analysis function for Hall voltage vs magnetic field data.

    Parameters
    ----------
    data_file : str
        Path to CSV file with columns 'B' and 'V_H'.
    I : float
        DC current used during measurements [A].
    t : float
        Sample thickness [m].
    output_dir : str
        Folder to save plots.
    """
    df = load_data(data_file)

    y_pred, slope, intercept = linear_fit(df["B"].values, df["V_H"].values)
    coeffs = estimate_hall_coefficient(slope, I, t)

    print("\n=== Hall Effect Analysis ===")
    print(f"Slope (dV_H/dB): {slope:.3e} V/T")
    print(f"Intercept: {intercept:.3e} V")
    print(f"Hall Coefficient R_H: {coeffs['R_H']:.3e} m³/C")
    print(f"Carrier Concentration n: {coeffs['n']:.3e} 1/m³")

    plot_hall_vs_B(df["B"].values, df["V_H"].values, slope, intercept,
                   output_path=f"{output_dir}/hall_voltage_vs_B.png")



if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Analyze Hall voltage vs magnetic field data.")
    parser.add_argument("data_file", help="Path to CSV file with columns: B, V_H")
    parser.add_argument("--current", type=float, required=True, help="Applied DC current [A]")
    parser.add_argument("--thickness", type=float, required=True, help="Sample thickness [m]")
    parser.add_argument("--output", default="results", help="Output directory for plots")

    args = parser.parse_args()
    analyze_hall_vs_B(args.data_file, args.current, args.thickness, args.output)

