import pandas as pd

jobs = pd.read_csv("data/raw/linkedin_jobs/postings.csv")

skill_keywords = [
"python","machine learning","data science","ai",
"deep learning","cloud","aws","mlops",
"statistics","data analysis"
]

def extract_skills(text):

    text = str(text).lower()

    found = []

    for skill in skill_keywords:

        if skill in text:
            found.append(skill)

    return ",".join(found)

jobs["skills_found"] = jobs["description"].apply(extract_skills)

jobs.to_csv("data/processed/job_skills_extracted.csv", index=False)

print("job_skills_extracted.csv created")