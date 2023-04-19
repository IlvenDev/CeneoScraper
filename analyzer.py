import os
import pandas as pd
import matplotlib 

print(*[filename.split(".")[0] for filename in os.listdir("./opinions")], sep="\n")

product_code = input("Podaj kod produktu: ")

opinions = pd.read_json(f"./opinions/{product_code}.json")

opinions_count = len(opinions.index)
# pros_count = sum([False if len(p)== 0 else True for p in opinions.pros])
# cons_count = sum([False if len(c)== 0 else True for c in opinions.cons])
pros_count = opinions.pros.map(lambda p: False if len(p)== 0 else True for p in opinions.pros).sum()
cons_count = opinions.pros.map(lambda c: False if len(c)== 0 else True for c in opinions.pros).sum()
avg_score = 0

print(opinions.pros)