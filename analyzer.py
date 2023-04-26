import os
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

print(*[filename.split(".")[0] for filename in os.listdir("./opinions")], sep="\n")

product_code = input("Podaj kod produktu: ")

opinions = pd.read_json(f"./opinions/{product_code}.json")
opinions.score = opinions.score.map(lambda x: float(x.split("/")[0].replace(",",".")))

opinions_count = len(opinions.index)
# opinions_count = opinions.shape[0]
# pros_count = sum([False if len(p)== 0 else True for p in opinions.pros])
# cons_count = sum([False if len(c)== 0 else True for c in opinions.cons])

# pros_count = opinions.pros.map(lambda p: False if len(p)==0 else True).sum()
# cons_count = opinions.cons.map(lambda c: False if len(c)==0 else True).sum()

pros_count = opinions.pros.map(bool).sum()
cons_count = opinions.cons.map(bool).sum()

avg_score = opinions.score.mean().round(1)

print(f'''\nDla produktu o kodzie {product_code} dostępnych jest {opinions_count} opinii. 
Dla {pros_count} opinii dostępna jest lista zalet, a dla {cons_count} opinni dostępna jest lista wad.
Średnia ocena produktu to {avg_score}.''')

# Histogram częstości występowania poszczególnych ocen

score = opinions.score.value_counts().reindex(list(np.arange(0,5.5,0.5)), fill_value = 0)

score.plot.bar(color = "hotpink")
plt.xticks(rotation = 0)
plt.title("Histogram ocen")
plt.xlabel("Liczba gwiazdek")

for index, value in enumerate(score):
    plt.text(index, value+0.5, str(value), ha="center")
 
try:    
    os.mkdir("./plots")
except FileExistsError:
    pass

plt.savefig(f"./plots/{product_code}_score.png")
plt.close()

# udział poszególnych rekomendacji w ogólnej liczbie opinii

recommendation = opinions.recommendation.value_counts(dropna = False).sort_index()
recommendation.plot.pie(label = "", 
                        autopct="%1.1f%%",
                        labels = ["Nie polecam" , "Polecam" , "Nie mam zdania"],
                        colors = ["crimson" , "forestgreen" , "gray"])

plt.legend(bbox_to_anchor = (1.5,0.5))
plt.savefig(f"./plots/{product_code}_recommendation.png")
plt.close()