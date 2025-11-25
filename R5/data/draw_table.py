
from experiment_data import dados_experimento_tabelas_1, dados_experimento_tabelas_2, dados_experimento_tabelas_3

def table3_n(dict_entrada):
    chaves = list(dict_entrada.keys())
        
    for i in range(len(dict_entrada[chaves[0]])):
        print(f'{dict_entrada[chaves[0]][i]} & {dict_entrada[chaves[1]][i]} & {dict_entrada[chaves[2]][i]} \\\\')


def table5_n(dict_entrada):
    chaves = list(dict_entrada.keys())
        
    for i in range(len(dict_entrada[chaves[0]])):
        print(f'{dict_entrada[chaves[0]][i]} & {dict_entrada[chaves[1]][i]} & {dict_entrada[chaves[2]][i]} & {dict_entrada[chaves[3]][i]} & {dict_entrada[chaves[4]][i]} \\\\')

table5_n(dados_experimento_tabelas_2)