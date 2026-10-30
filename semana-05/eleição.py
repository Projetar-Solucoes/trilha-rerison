import pandas as pd

df = pd.read_csv("eleicao_ficticia.csv")

print(df.head())
print(df.shape)
print(df["bairro"].nunique())
print(df["bairro"].unique())

df['comparecimento'] = df['eleitores_aptos'] - df['abstencoes']
print(df[['secao', 'comparecimento']].head())

df['votos_validos'] = df['votos_ana'] + df['votos_bruno'] + df['votos_carla']
print(df[['secao', 'votos_validos']].head())


print(df[['secao', 'comparecimento', 'votos_validos', 'votos_brancos', 'votos_nulos'
]].head())
df['confere'] = df['comparecimento'] == df['votos_validos'] + df['votos_brancos'] + df['votos_nulos']
print(df['confere'].all())

print(df['eleitores_aptos'].sum())
print(df['abstencoes'].sum())
print(df['comparecimento'].sum())
print(df['votos_validos'].sum())

df['taxa_abstencao'] = 100 * df['abstencoes'] / df['eleitores_aptos']
df['taxa_comparecimento'] = 100 * df['comparecimento'] / df['eleitores_aptos']
df["taxa_brancos_nulos"] = 100 * (df["votos_brancos"] + df["votos_nulos"]) / df["comparecimento"]

print(df[["secao", "taxa_abstencao", "taxa_comparecimento", "taxa_brancos_nulos"]].head())
print(df["taxa_abstencao"].mean())
print(df["taxa_abstencao"].median())
print(df["taxa_abstencao"].min())
print(df["taxa_abstencao"].max())
print(df["taxa_abstencao"].max() - df["taxa_abstencao"].min())
print(df["taxa_abstencao"].quantile(0.25))
print(df["taxa_abstencao"].quantile(0.75))
print(df["taxa_abstencao"].quantile(0.75) - df["taxa_abstencao"].quantile(0.25))
print(df["taxa_abstencao"].std(ddof=0))

print(100 * df["abstencoes"].sum() / df["eleitores_aptos"].sum())
print(
    100 * df["abstencoes"].sum() / df["eleitores_aptos"].sum()
    - df["taxa_abstencao"].mean()
)
print(df.groupby("bairro")["eleitores_aptos"].sum())
print(df.groupby("bairro")["abstencoes"].sum())
por_bairro = df.groupby("bairro")[["eleitores_aptos", "abstencoes"]].sum()
por_bairro["taxa_abstencao"] = 100 * por_bairro["abstencoes"] / por_bairro["eleitores_aptos"]
print(por_bairro)

print(df["votos_ana"].sum())
print(df["votos_bruno"].sum())
print(df["votos_carla"].sum())

print(100 * df["votos_ana"].sum() / df["votos_validos"].sum())
print(100 * df["votos_bruno"].sum() / df["votos_validos"].sum())
print(100 * df["votos_carla"].sum() / df["votos_validos"].sum())

print(df["votos_ana"].sum() - df["votos_bruno"].sum())

print(
    100 * df["votos_ana"].sum() / df["votos_validos"].sum()
    - 100 * df["votos_bruno"].sum() / df["votos_validos"].sum()
)

print(df.groupby("bairro")[["votos_ana", "votos_bruno", "votos_carla"]].sum())

#Este projeto analisa dados fictícios de uma eleição usando Python (PANDAS).
#A tabela contém 24 seções eleitorais distribuídas por quatro bairros.
#No total, havia 10.695 eleitores aptos, e 1.988 se abstiveram.
#A taxa global de abstenção foi de aproximadamente 18,59%.
#Ana foi a candidatura mais votada, com 3.146 votos, ou cerca de 40,11% dos votos válidos.
#Ela foi a mais votada nos quatro bairros e superou Bruno por 444 votos.
#Lagoa teve a maior taxa de abstenção, enquanto Jardim teve a menor.

