import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

skills = pd.read_csv("data/processed/skills_cleaned.csv")

skill_list = skills["skill"].astype(str).tolist()

vectorizer = TfidfVectorizer()

skill_vectors = vectorizer.fit_transform(skill_list)

pickle.dump(vectorizer, open("vector_db/vectorizer.pkl", "wb"))

pickle.dump(skill_vectors, open("vector_db/skill_vectors.pkl", "wb"))

print("Skill vectors created successfully")