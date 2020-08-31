import pandas as pd

comp_list = list(set(df['‰ïĞ'].tolist()))

del_comp_list = ['032','037','132','176','230']

for code in del_comp_list:
    comp_list.remove(code)

display(len(comp_list), comp_list)