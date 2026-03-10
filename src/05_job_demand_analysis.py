import pandas as pd

jobs = pd.read_csv("data/processed/job_skills_extracted.csv")

skills_series = jobs["skills_found"].str.split(",")

skills_exploded = skills_series.explode()

demand = skills_exploded.value_counts()

demand_df = demand.reset_index()

demand_df.columns = ["skill","demand"]

demand_df = demand_df[demand_df["skill"] != ""]

demand_df.to_csv("data/processed/skill_demand.csv", index=False)

print("Skill demand analysis created")