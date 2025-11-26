import plotly.graph_objects as go
import numpy as np

# Configurações globais de estilo para facilitar alterações futuras
FONTE_GERAL = dict(size=18, family="Arial")  # Aumenta todo o texto
TAMANHO_MARKER = 14     # Aumenta os pontos
LARGURA_LINHA = 4       # Aumenta a espessura da linha

# ==========================================
# GRÁFICO 1: Tabela 1 (Fotodiodo)
# ==========================================

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

fig1 = go.Figure()

fig1.add_trace(go.Scatter(
    x=vd, 
    y=id_values, 
    mode='lines+markers',
    name='Experimental Data',
    marker=dict(size=TAMANHO_MARKER, color='blue'),
    line=dict(width=LARGURA_LINHA, color='blue')
))

fig1.update_layout(
    title='<b>Table 1: Tensão e corrente do Fotodiodo</b>', # Negrito
    xaxis_title='<b>V_D [V]</b>',
    yaxis_title='<b>I_D [V]</b>',
    template='plotly_white',
    width=900,  # Aumentei um pouco a largura
    height=700, # Aumentei um pouco a altura
    font=FONTE_GERAL # Aplica a fonte maior em tudo
)

# Bordas mais visíveis nos eixos
fig1.update_xaxes(showline=True, linewidth=2, linecolor='black', mirror=True)
fig1.update_yaxes(showline=True, linewidth=2, linecolor='black', mirror=True)

fig1.show()


# ==========================================
# GRÁFICO 2: Tabela 2 (Fototransistor)
# ==========================================

v_fonte = np.array([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0])

# Corrente original em [A]
id_60v_a = np.array([0.0, 0.33, 0.52, 0.54, 1.18, 1.04, 1.24, 1.12, 1.18, 1.29, 1.25, 1.36, 1.27])
id_80v_a = np.array([0.0, 0.4, 0.89, 1.36, 1.86, 2.25, 2.52, 2.44, 2.69, 2.64, 2.56, 2.16, 2.58])

# Conversão para [mA]
id_60v_ma = id_60v_a * 1000
id_80v_ma = id_80v_a * 1000

# Regressão
x_suave = np.linspace(v_fonte.min(), v_fonte.max(), 100)

coefs_60 = np.polyfit(v_fonte, id_60v_ma, 3)
poly_60 = np.poly1d(coefs_60)
y_regressao_60 = poly_60(x_suave)

coefs_80 = np.polyfit(v_fonte, id_80v_ma, 3)
poly_80 = np.poly1d(coefs_80)
y_regressao_80 = poly_80(x_suave)

fig2 = go.Figure()

# --- Caso 60V ---
fig2.add_trace(go.Scatter(
    x=v_fonte, y=id_60v_ma,
    mode='markers',
    name='Dados 60V',
    marker=dict(symbol='square', color='black', size=TAMANHO_MARKER)
))
fig2.add_trace(go.Scatter(
    x=x_suave, y=y_regressao_60,
    mode='lines',
    name='Regressão 60V',
    line=dict(color='gray', width=3, dash='dash') # Tracejada um pouco mais fina que a sólida
))

# --- Caso 80V ---
fig2.add_trace(go.Scatter(
    x=v_fonte, y=id_80v_ma,
    mode='markers',
    name='Dados 80V',
    marker=dict(symbol='circle', color='red', size=TAMANHO_MARKER)
))
fig2.add_trace(go.Scatter(
    x=x_suave, y=y_regressao_80,
    mode='lines',
    name='Regressão 80V',
    line=dict(color='blue', width=3, dash='dash')
))

fig2.update_layout(
    title={
        'text': '<b>Table 2: Tensão e corrente do Fototransistor</b>',
        'y': 0.05, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'bottom'
    },
    xaxis_title='<b>Tensão [V]</b>',
    yaxis_title='<b>Corrente [mA]</b>',
    template='plotly_white',
    font=FONTE_GERAL,
    legend=dict(
        yanchor="top", y=0.99,
        xanchor="left", x=0.01,
        bgcolor="rgba(255, 255, 255, 0.9)",
        bordercolor="Black", borderwidth=1,
        font=dict(size=16) # Legenda ligeiramente menor que o título, se desejar
    ),
    margin=dict(b=100) # Margem inferior maior por causa do título embaixo
)

fig2.update_xaxes(showline=True, linewidth=2, linecolor='black', mirror=True)
fig2.update_yaxes(showline=True, linewidth=2, linecolor='black', mirror=True)

fig2.show()


# ==========================================
# GRÁFICO 3: Tabela 3 (Fotocélulas)
# ==========================================

v_entrada = np.array([60.0, 80.0, 100.0, 120.0, 140.0, 160.0, 180.0])
i_out = np.array([21.8, 46.7, 100.4, 163.0, 260, 350, 490])

x_suave = np.linspace(v_entrada.min(), v_entrada.max(), 100)
coefs = np.polyfit(v_entrada, i_out, 2)
poly_eq = np.poly1d(coefs)
y_regressao = poly_eq(x_suave)

fig3 = go.Figure()

fig3.add_trace(go.Scatter(
    x=v_entrada, 
    y=i_out,
    mode='markers',
    name='Dados Experimentais',
    marker=dict(size=15, color='darkblue', symbol='circle') # Ainda maior
))

fig3.add_trace(go.Scatter(
    x=x_suave, 
    y=y_regressao,
    mode='lines',
    name='Ajuste Polinomial',
    line=dict(color='red', width=LARGURA_LINHA, dash='dash')
))

fig3.update_layout(
    title='<b>Table 3: Tensão e corrente das Fotocélulas</b>',
    xaxis_title='<b>Tensão de Entrada (Vca) [V]</b>',
    yaxis_title='<b>Corrente de Saída (Icc) [A]</b>',
    template='plotly_white',
    font=FONTE_GERAL,
    legend=dict(
        x=0.02, y=0.98,
        bgcolor='rgba(255,255,255,0.8)',
        bordercolor='black', borderwidth=1
    )
)

fig3.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray', showline=True, linewidth=2, linecolor='black', mirror=True)
fig3.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray', showline=True, linewidth=2, linecolor='black', mirror=True)

fig3.show()