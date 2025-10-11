"""
Hall Effect Analysis
--------------------
This module provides tools to analyze Hall Effect measurements by:
1. Plotting Hall voltage (V_H) as a function of DC current (I_DC)
2. Plotting Hall voltage (V_H) as a function of magnetic field (B)
3. Performing linear regression to extract key parameters (e.g., Hall coefficient)

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
    Loads experimental data from a CSV file.
    The CSV must include the columns: 'I_DC', 'B', and 'V_H'.

    Parameters
    ----------
    file_path : str
        Path to the CSV file containing the data.

    Returns
    -------
    pd.DataFrame
        Cleaned data ready for analysis.
    """
    df = pd.read_csv(file_path)
    expected_cols = {'I_DC', 'B', 'V_H'}
    if not expected_cols.issubset(df.columns):
        raise ValueError(f"Missing required columns: {expected_cols - set(df.columns)}")
    return df.dropna().reset_index(drop=True)


def linear_fit(x: np.ndarray, y: np.ndarray) -> tuple[np.ndarray, float, float]:
    """
    Fits a linear model (y = m*x + b) using least squares.

    Parameters
    ----------
    x : np.ndarray
        Independent variable.
    y : np.ndarray
        Dependent variable.

    Returns
    -------
    tuple[np.ndarray, float, float]
        (predicted y values, slope m, intercept b)
    """
    model = LinearRegression()
    x = x.reshape(-1, 1)
    model.fit(x, y)
    y_pred = model.predict(x)
    return y_pred, model.coef_[0], model.intercept_


def plot_relationship(x, y, xlabel, ylabel, title, save_path=None):
    """
    Generates a clean scatter + regression plot.

    Parameters
    ----------
    x, y : array-like
        Data points to plot.
    xlabel, ylabel, title : str
        Plot labels.
    save_path : str or None
        Optional path to save the figure.
    """
    y_pred, m, b = linear_fit(np.array(x), np.array(y))

    plt.figure(figsize=(7, 5))
    plt.scatter(x, y, color='royalblue', alpha=0.8, label='Experimental data')
    plt.plot(x, y_pred, color='crimson', linewidth=2.2, label=f'Linear fit: y = {m:.3e}x + {b:.3e}')

    plt.title(title, fontsize=14, fontweight='bold')
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()
    plt.tight_layout()

    if save_path:
        Path(save_path).parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(save_path, dpi=300)
    plt.show()

def analyze_hall_data(data_file: str, output_dir: str = "results"):
    """
    Runs the full Hall Effect analysis workflow.

    Parameters
    ----------
    data_file : str
        CSV file path containing I_DC, B, and V_H columns.
    output_dir : str, optional
        Directory to save result plots (default: 'results').
    """
    df = load_data(data_file)

    plot_relationship(
        x=df["I_DC"].values,
        y=df["V_H"].values,
        xlabel="DC Current (A)",
        ylabel="Hall Voltage (V)",
        title="Hall Voltage vs DC Current",
        save_path=f"{output_dir}/hall_voltage_vs_current.png"
    )

    plot_relationship(
        x=df["B"].values,
        y=df["V_H"].values,
        xlabel="Magnetic Field (T)",
        ylabel="Hall Voltage (V)",
        title="Hall Voltage vs Magnetic Field",
        save_path=f"{output_dir}/hall_voltage_vs_B.png"
    )


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Analyze Hall Effect experimental data.")
    parser.add_argument("data_file", help="Path to CSV file with columns: I_DC, B, V_H")
    parser.add_argument("--output", default="results", help="Output directory for plots")

    args = parser.parse_args()
    analyze_hall_data(args.data_file, args.output)

