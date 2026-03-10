import pandas as pd

tech = pd.read_csv("data/raw/onet/Technology Skills.txt", sep="\t")

tech_clean = tech[['Example']]

tech_clean.columns = ['technology']

tech_clean = tech_clean.drop_duplicates()

tech_clean.to_csv("data/processed/tech_skills.csv", index=False)

print("tech_skills.csv created")