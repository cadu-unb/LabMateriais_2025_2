import numpy as np
import pandas as pd

# Measured data
I = np.array([1.4,1.2,1.0,0.8,0.6,0.4,0.2,0.0,-0.2,-0.4,-0.6,-0.8,-1.0,-1.2,-1.4])
V_saida_sem_offset = np.array([3.22,2.81,2.39,1.94,1.47,0.97,0.50,0.00,-0.49,-1.00,-1.46,-1.95,-2.41,-2.84,-3.27])
V = np.array([9.63,9.22,8.80,8.35,7.88,7.38,6.91,6.41,5.92,5.41,4.95,4.46,4.00,3.57,3.14])

# Magnetic circuit parameters
N = 50
R = 14705882.352941
A = 1e-4

# Calculate magnetic flux density B
B = (N * I) / (R * A)

# Create DataFrame with columns expected by your script
df = pd.DataFrame({
    "I_DC": I,
    "V_H": V_saida_sem_offset,  # rename for hall_effect_analysis.py
    "V": V,
    "B": B                      # rename for hall_effect_analysis.py
})

# Save to CSV
df.to_csv("hall_data_ready.csv", index=False, float_format="%.6f")
print("CSV saved as 'hall_data_ready.csv'")
