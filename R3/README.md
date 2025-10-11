
## 📘 **`README.md`**

```markdown
# Hall Effect Analysis Toolkit ⚡

A clean, modular, and reproducible Python toolkit for analyzing **Hall effect experiments**.

This repository includes:
- Analysis of **Hall Voltage vs DC Current**
- Analysis of **Hall Voltage vs Magnetic Field**
- Automatic linear regression
- Estimation of the **Hall coefficient (R_H)** and **carrier concentration (n)**
- Publication-ready plots and results

---

## ⚙️ Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/yourusername/hall-effect-analysis.git
python -m venv .venv
source .venv/bin/activate
cd hall-effect-analysis
pip install -r requirements.txt
````

---

## 🧪 Usage

### 1️⃣ Analyze **Hall Voltage vs DC Current**

```bash
python hall_effect_analysis.py data/hall_data_current.csv --output results/
```

**Input CSV format:**

```csv
I_DC,V_saida_sem_offset,V
1.4,3.22,9.63
1.2,2.81,9.22
...
```

Generates:

* `results/hall_voltage_vs_current.png`
* Linear regression summary in terminal

---

### 2️⃣ Analyze **Hall Voltage vs Magnetic Field (B)**

```bash
python hall_effect_B_analysis.py data/hall_data_B.csv --current 0.01 --thickness 0.001 --output results/
```

**Input CSV format:**

```csv
B,V_H
-0.4,-0.0019
-0.3,-0.0014
...
```

Outputs:

* `results/hall_voltage_vs_B.png`
* Slope, intercept, Hall coefficient ( R_H ), and carrier concentration ( n )

---

## 📈 Example Output

* **Plot 1:** Hall Voltage vs DC Current
  Linear fit → ( V_H = m \cdot I_{DC} + b )

* **Plot 2:** Hall Voltage vs Magnetic Field
  Linear fit → ( V_H = m \cdot B + b )

---

## 📊 Physical Background

The Hall effect is a fundamental phenomenon where a voltage difference (Hall voltage) develops across a conductor carrying current in the presence of a magnetic field.

[
R_H = \frac{E_H}{J \cdot B} = \frac{V_H \cdot t}{I \cdot B}
]

where:

* ( R_H ): Hall coefficient ([m^3/C])
* ( t ): Sample thickness ([m])
* ( I ): Current through the sample ([A])
* ( V_H ): Hall voltage ([V])
* ( B ): Magnetic flux density ([T])

Carrier concentration:
[
n = \frac{1}{q R_H}
]
with ( q = 1.602 \times 10^{-19} , C ).

---

## 🧑‍💻 Author

**Thiago Ferreira**
Electrical Engineering Department – ENE, University of Brasília (UnB)

---

## 📜 License

This project is released under the **MIT License**.
Feel free to use, modify, and distribute with attribution.

```

