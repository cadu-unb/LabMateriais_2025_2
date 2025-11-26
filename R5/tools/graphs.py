import plotly.graph_objects as go

# Data transcribed from Table 1
# Vd = Voltage at the Diode [V]
# Id = Current (or proportional voltage) [V] as per the table

vd = [
    0.0, 0.12, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 
    1.6, 1.74, 1.82, 1.87, 1.91, 1.95, 1.98, 
    2.01, 2.04, 2.07, 2.09, 2.12, 2.15, 2.17, 
    2.2, 2.23, 2.25, 2.27
]

id_values = [
    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
    0.02, 0.54, 1.72, 3.14, 4.61, 6.19, 7.73, 
    9.29, 10.94, 12.55, 14.24, 15.86, 17.49, 
    19.11, 20.78, 22.52, 24.16, 25.82
]

# Creating the Figure
fig = go.Figure()

# Adding the trace (the line/points)
fig.add_trace(go.Scatter(
    x=vd, 
    y=id_values, 
    mode='lines+markers', # Shows both line and dots
    name='Experimental Data',
    marker=dict(size=8, color='blue'),
    line=dict(width=2, color='blue')
))

# Updating layout (Titles and Labels)
fig.update_layout(
    title='Table 1: Tensão e corrente do Fotodiodo',
    xaxis_title='V_D [V]',
    yaxis_title='I_D [V]',
    template='plotly_white', # A clean white background
    width=800, 
    height=600
)

# Show the interactive graph
fig.show()

# --- 1. Dados da Tabela 2 ---
v_fonte = np.array([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0])

# Corrente original em [A]
id_60v_a = np.array([0.0, 0.33, 0.52, 0.54, 1.18, 1.04, 1.24, 1.12, 1.18, 1.29, 1.25, 1.36, 1.27])
id_80v_a = np.array([0.0, 0.4, 0.89, 1.36, 1.86, 2.25, 2.52, 2.44, 2.69, 2.64, 2.56, 2.16, 2.58])

# Conversão para [mA] (x1000)
id_60v_ma = id_60v_a * 1000
id_80v_ma = id_80v_a * 1000

# --- 2. Cálculo da Regressão (Polinomial de 3º Grau) ---
# Cria um eixo X mais "fino" (com mais pontos) para que a linha da regressão fique suave
x_suave = np.linspace(v_fonte.min(), v_fonte.max(), 100)

# Regressão para 60V
coefs_60 = np.polyfit(v_fonte, id_60v_ma, 3) # O número 3 indica o grau do polinômio
poly_60 = np.poly1d(coefs_60)
y_regressao_60 = poly_60(x_suave)

# Regressão para 80V
coefs_80 = np.polyfit(v_fonte, id_80v_ma, 3)
poly_80 = np.poly1d(coefs_80)
y_regressao_80 = poly_80(x_suave)

# --- 3. Plotagem ---
fig = go.Figure()

# --- Caso 60V ---
# Pontos (Scatter)
fig.add_trace(go.Scatter(
    x=v_fonte, y=id_60v_ma,
    mode='markers',
    name='Dados 60V',
    marker=dict(symbol='square', color='black', size=8)
))
# Linha de Regressão
fig.add_trace(go.Scatter(
    x=x_suave, y=y_regressao_60,
    mode='lines',
    name='Regressão 60V',
    line=dict(color='gray', width=2, dash='dash') # Linha tracejada cinza
))

# --- Caso 80V ---
# Pontos (Scatter)
fig.add_trace(go.Scatter(
    x=v_fonte, y=id_80v_ma,
    mode='markers',
    name='Dados 80V',
    marker=dict(symbol='circle', color='red', size=8)
))
# Linha de Regressão
fig.add_trace(go.Scatter(
    x=x_suave, y=y_regressao_80,
    mode='lines',
    name='Regressão 80V',
    line=dict(color='blue', width=2, dash='dash') # Linha tracejada salmão
))

# --- 4. Layout ---
fig.update_layout(
    title={
        'text': 'Table 2: Tensão e corrente do Fototransistor',
        'y': 0.01, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'bottom'
    },
    xaxis_title='tensão [V]',
    yaxis_title='corrente [mA]',
    template='plotly_white',
    legend=dict(
        yanchor="top", y=0.99,
        xanchor="left", x=0.01, # Movi a legenda para a esquerda para não cobrir o gráfico
        bgcolor="rgba(255, 255, 255, 0.8)",
        bordercolor="Black", borderwidth=1
    ),
    margin=dict(b=80)
)

fig.update_xaxes(showline=True, linewidth=1, linecolor='black', mirror=True)
fig.update_yaxes(showline=True, linewidth=1, linecolor='black', mirror=True)

fig.show()

# --- 1. Dados transcritos da Tabela 3 (Apenas parte numérica) ---
# Entrada = Tensão CA (Vca) aplicada à lâmpada/fonte
v_entrada = np.array([60.0, 80.0, 100.0, 120.0, 140.0, 160.0, 180.0])

# I_out = Corrente de Saída (Icc) [A]
# Nota: Valores conforme imagem. Se forem microamperes na realidade, o formato do gráfico é o mesmo.
i_out = np.array([21.8, 46.7, 100.4, 163.0, 260, 350, 490])

# --- 2. Cálculo da Regressão (Polinomial de 2º Grau) ---
# Escolhi grau 2 pois a relação Luz x Tensão geralmente não é linear
x_suave = np.linspace(v_entrada.min(), v_entrada.max(), 100)

coefs = np.polyfit(v_entrada, i_out, 2) # Grau 2
poly_eq = np.poly1d(coefs)
y_regressao = poly_eq(x_suave)

# --- 3. Criação do Gráfico ---
fig = go.Figure()

# Pontos Experimentais
fig.add_trace(go.Scatter(
    x=v_entrada, 
    y=i_out,
    mode='markers',
    name='Dados Experimentais',
    marker=dict(size=10, color='darkblue', symbol='circle')
))

# Linha de Tendência (Regressão)
fig.add_trace(go.Scatter(
    x=x_suave, 
    y=y_regressao,
    mode='lines',
    name='Ajuste Polinomial',
    line=dict(color='red', width=2, dash='dash')
))

# --- 4. Configuração do Layout ---
fig.update_layout(
    title='Table 3: Tensão e corrente das Fotocélulas',
    xaxis_title='Tensão de Entrada (Vca) [V]',
    yaxis_title='Corrente de Saída (Icc) [A]',
    template='plotly_white',
    legend=dict(
        x=0.02, y=0.98,
        bgcolor='rgba(255,255,255,0.8)',
        bordercolor='black', borderwidth=1
    )
)

# Adicionar grades e bordas
fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray', showline=True, linewidth=1, linecolor='black', mirror=True)
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray', showline=True, linewidth=1, linecolor='black', mirror=True)

fig.show()
