import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Global Skill Gap Intelligence System")

skills_input = st.text_input("Enter your skills (comma separated)")
country = st.text_input("Country")
career = st.text_input("Career Interest")

if st.button("Analyze"):

    demand = pd.read_csv("data/processed/skill_demand.csv")

    # Top skills in job market
    top_skills = demand.head(15)

    st.subheader("Top Global Skills")

    fig = px.bar(
        top_skills,
        x="skill",
        y="demand",
        title="Global Skill Demand"
    )

    st.plotly_chart(fig)

    # USER SKILLS
    user_skills = [s.strip().lower() for s in skills_input.split(",")]

    market_skills = demand["skill"].tolist()

    # SKILL GAP
    missing_skills = []

    for skill in market_skills[:20]:
        if skill not in user_skills:
            missing_skills.append(skill)

    st.subheader("Your Skills")

    st.write(user_skills)

    st.subheader("Recommended Skills to Learn")

    st.write(missing_skills[:5])

    # PIE CHART
    skill_data = {
        "Category": ["Your Skills", "Missing Skills"],
        "Count": [len(user_skills), len(missing_skills[:5])]
    }

    pie_df = pd.DataFrame(skill_data)

    pie_chart = px.pie(
        pie_df,
        names="Category",
        values="Count",
        title="Skill Gap Analysis"
    )

    st.plotly_chart(pie_chart)