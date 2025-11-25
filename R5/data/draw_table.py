
from experiment_data import dados_experimento_tabelas_1

chaves = list(dados_experimento_tabelas_1.keys())
    
for i in range(len(dados_experimento_tabelas_1[chaves[0]])):
    print(f'{dados_experimento_tabelas_1[chaves[0]][i]} & {dados_experimento_tabelas_1[chaves[1]][i]} & {dados_experimento_tabelas_1[chaves[2]][i]} \\\\')