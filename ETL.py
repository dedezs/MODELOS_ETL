import pandas as pd
import openpyxl as opxl
from openpyxl import load_workbook
#https://paulovasconcellos.com.br/28-comandos-%C3%BAteis-de-pandas-que-talvez-voc%C3%AA-n%C3%A3o-conhe%C3%A7a-6ab64beefa93
#https://www.ti-enxame.com/pt/python/removendo-espaco-das-colunas-do-quadro-de-dados-em-pandas/828678710/

#base = pd.read_excel("C:/Users/felip/OneDrive/Área de Trabalho/JUPYTER/_ESTUDO/Emendas Apresentadas.xlsx")
base = pd.read_csv("BASE\BASE.csv")

#Metadados
base.groupby("Matéria Legislativa").sum()
base.head()
display(base)
base.isnull().sum()
base.count()
base.groupby('Partido').count()

#substituir valores da string
df = pd.DataFrame(base)
df['date'].replace('-', '/', regex=True, inplace=True)

#extrair informação pelo delimitador
df['date'].str.split(pat="/")
new = df["date"].str.split("/", n = 1, expand = True)
df["Mes_Temp"]= new[1]
#extrair informação pelo delimitador
df['Mes_Temp'].str.split(pat="/")
new = df["Mes_Temp"].str.split("/", n = 1, expand = True)
df["Mes"]= new[0]

#excluir coluna temporaria
df.drop(columns =["Mes_Temp"], inplace = True)

df.head()
df.info()
df.groupby('Mes').count()

#dividir coluna por numero de caracter
df['ano'] = df['date'].apply(lambda x: str(x)[:4])
df['mes'] = df['date'].apply(lambda x: str(x)[5:7])

df.head()

#remover espaços
df.columns = df.columns.str.strip()
#df.head()
df.shape
#filtrar linhas pelo índice
filtro = df[(df.index >= 0) & (df.index <= 10)]

#concatenar string com numero
#faturamento = 2
#lucro = 4
#print('O faturamento foi de: str(faturamento)') OU
#print('O faturamento foi de: {} e o lucro de: {}'.format(faturamento, lucro))

if lucro > faturamento:
    print(lucro)
else:
    print(faturamento)

if df['date'] == "2021/10/01":
    print(df)

lucro = 6
faturamento = 4
mensagem = 'String treino'

print(mensagem[:5])
print(mensagem[5:8])
print(mensagem[3])

if lucro > faturamento:
    print('O lucro {} foi maior que o faturamento {}'.format(lucro, faturamento))

elif lucro == lucro and faturamento == faturamento:
    print(lucro)

elif not 6 in lucro:
    print('AQUI')

elif lucro:
    print('Lucro não preenchido')

else:
    print('O faturamento {} foi maior que o lucro {}'.format(faturamento, lucro))

###################################

meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']

vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]
vendas_1sem.extend(vendas_2sem)

maior_valor = max(vendas_1sem)
menor_valor = min(vendas_1sem)

i_maior_valor = vendas_1sem.index(maior_valor)
i_menor_valor = vendas_1sem.index(menor_valor)

print('O melhor mês do ano foi {} com {} vendas'.format(meses[i_maior_valor], maior_valor))
print('O pior mês do ano foi {} com {} vendas'.format(meses[i_menor_valor], menor_valor))

fat_total = sum(vendas_1sem)
print('Faturamento Total: R${:,}'.format(fat_total))

percentual = maior_valor / fat_total
print('O melhor mês representou {:.1%} das vendas do ano todo'.format(percentual))

###################################
