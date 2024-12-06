import pandas as pd

path_to_input_file="input.csv"

df = pd.read_csv(path_to_input_file, sep=r"\s+", lineterminator='\r', header=None, names=["List1", "List2"])

df_sorted = df.sort_values(['List1', 'List2'])

list1 = sorted(df['List1'].values.tolist())
list2 = sorted(df['List2'].values.tolist())

answer1 = 0

for x, y in zip(list1, list2):
    answer1 = answer1 + abs(x - y)

print(answer1)

counter = 0

def counting(value, list):
    counter = 0
    for a in list:
        if a == value:
            counter = counter + 1
    return counter

def make_dict(list1, list2):
    result = {}
    for x in list1:
        result[x] = counting(x, list2)
    return  result

almost = make_dict(list1, list2)

answer2 = 0
for key, value in almost.items():
    answer2 = answer2 + (key * value)

print(answer2)
