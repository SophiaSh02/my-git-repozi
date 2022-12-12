# -*- coding: utf-8 -*-

# -- Sheet --

import pandas as pd

# ## Повторение анализа сводных таблиц
# 
# здесь повтрим $x^2=4$


df = pd.read_excel('RawData.xlsx', skiprows=2, usecols=[0,1,2,3])

df

df.shape

df.tail()

df.columns

df[df[df.columns[1]]== "Магазин 1"]

df.columns[1]

pd.pivot_table(df, values="Сумма", index = ['Статья расходов','Название магазина'])

pivoted_df = pd.pivot_table(df, values=["Сумма"], index = ["Название магазина"] , columns=['Статья расходов'])

pivoted_df

pivoted_df.columns = pivoted_df.columns.droplevel(level=0)

#python way
#pivoted_df.columns = list(zip(*pivoted_df.columns))[1]

#сделаем новую колонку с общем суммой
pivoted_df["Всего"] = pivoted_df.sum(axis=1)

pivoted_df

#вычисление процентного соотношения
pivoted_df[pivoted_df.columns].div(pivoted_df["Всего"], axis=0).mul(100).round(0)

pivoted_df.index

for colname in ["Аренда","Зарплата"]:
    pivoted_df[colname+"_Отличие"] = pivoted_df[colname] - pivoted_df.loc["Новый магазин", colname]
   

pivoted_df

#https://matplotlib.org/stable/tutorials/colors/colormaps.html
pivoted_df.style.background_gradient(cmap='Greens', subset=["Зарплата_Отличие", "Аренда_Отличие"])

df.groupby(["Статья расходов", 'Название магазина']).sum()

df.sort_values(["Статья расходов", 'Название магазина'], ascending=[False,True]).groupby("Статья расходов").head(3)

#вернем все обратно
pd.melt(pivoted_df.reset_index(), id_vars="Название магазина")

# ## Про супергероев
# 
# Проанализируйте самостоятельно данные про супергероев:
#  - Есть ли зависимость веса для мужчин и женщин супергероев?
#  - Есть ли зависимость веса от принадлежности к лагерю хороших или плохих?
#  - Представителей какой расы больше всего?
#  - Есть ли зависимость роста от принадлежности к лагерю хороших или плохих?
#  - Какая студия создала больше всего супергероев?


super_heroes = pd.read_csv("SuperHeroes.csv", sep=';')

super_heroes.shape

super_heroes.dropna().shape

super_heroes.dropna(axis=1, inplace = True)



