import pandas as pd

df = pd.read_csv("input.csv", sep=r"\s+", lineterminator='\r', header=None, names=["List1", "List2"])

df_sorted = df.sort_values(['List1', 'List2'])

list1 = sorted(df['List1'].values.tolist())
list2 = sorted(df['List2'].values.tolist())

sum = 0

for x, y in zip(list1, list2):
    sum = sum + abs(x - y)

print(sum)

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

answer = 0
for key, value in almost.items():
    answer = answer + (key * value)

print(answer)
