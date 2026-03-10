import pandas as pd

skills = pd.read_csv("data/raw/onet/Skills.txt", sep="\t")

skills_clean = skills[['Element Name']]

skills_clean.columns = ['skill']

skills_clean = skills_clean.drop_duplicates()

skills_clean.to_csv("data/processed/skills_cleaned.csv", index=False)

print("skills_cleaned.csv created")