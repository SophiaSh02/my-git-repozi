# -*- coding: utf-8 -*-

# -- Sheet --

import pandas as pd
import numpy as np
anime = pd.read_csv('anime.csv')
anime_modified = anime.set_index('name')
anime_modified


#первые 10 строк
anime.head(10)

#подсчёт количества типов аниме
anime.type.value_counts()

#конкатенация строк
df1 = anime[0:10]
df2 = anime[15:40]
pd.concat([df1, df2], ignore_index=True)

#поиск конкретных "тайтлов"
anime_modified.loc[['Fullmetal Alchemist','Gintama','Cowboy Bebop']]

#поиск всех OVA и полнометражных фильмов
anime[anime['type'].isin(['OVA', 'Movie'])]

#Поиск аниме с кол-вом эпизодов > 8
anime[anime['episodes'] > '8']

#Сортировка по имени сверху вниз
anime.sort_values('name', ascending=True)

