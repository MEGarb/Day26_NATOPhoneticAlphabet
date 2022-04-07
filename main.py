import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")
data = {row.letter: row.code for (index, row) in df.iterrows()}

target = input("Please enter the would you would like to phonetically spell:  ").upper()

final = [data.get(char) for char in target]
print(final)










