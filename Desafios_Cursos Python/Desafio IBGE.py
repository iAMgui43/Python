# Importe a tabela dos 100 maiores municípios em relação ao PIB e responda as seguintes perguntas:
# • Quantos municípios estão no estado de São Paulo?
# • Qual a participação acumulada desses municípios?
# Dicas e informações:
# • Fonte dos dados: https://www.ibge.gov.br/estatisticas/downloads-estatisticas.html
# • Arquivo para importar: /IBGE-PIB_Municipios_2017/PIB_100_maiores_cidades_2017.txt
# • Para ler arquivos acesse o tópico 7.2 do link: https://docs.python.org/3/tutorial/inputoutput.html


# _________________________________________________________//____________________________________________________________

# RESOLUÇÃO 1


import pandas as pd
file_path = 'PIB_100_maiores_cidades_2017.csv'
with open(file_path) as f:
    f_data = f.readlines()
    f.closed

linhas = []
for i in range(len(f_data)):
    linhas.append(f_data[i].split(','))

colunas_dict = {}

for key in linhas[0]:
    colunas_dict[key] = []

    colunas_n = linhas[0].index(key)

    for i in range(1, len(linhas)):
        colunas_dict[key].append(linhas[i][colunas_n])

lista_de_estados = colunas_dict['Estado']
numeros_municipios_sp = lista_de_estados.count("SP")

print(numeros_municipios_sp)

PIB_acm_SP = 0
for i in range(len(colunas_dict['Estado'])):
    if colunas_dict['Estado'][i] == 'SP':
        PIB_acm_SP += float(colunas_dict['Participacao ()'][i])

print("{:.0f}".format(PIB_acm_SP))

# _____________________________________________________________//___________________________________________________
# RESOLUÇÃO 2 COM PANDAS

file_path = 'PIB_100_maiores_cidades_2017.csv'

df = pd.read_csv(file_path, encoding='latin-1')

sp = df['Estado'] == 'SP'
df_sp = df[sp]
print(df_sp.head())

pib_sp = df_sp['Participacao ()'].sum()

contador_estados = df['Estado'].value_counts()
print(contador_estados)
print("{:.0f}".format(pib_sp))
