# Global Skill Gap Intelligence System

AI-powered platform that analyzes global labor market data to identify **future skill demand and personal skill gaps** for students and professionals.

Instead of showing what jobs exist today, this system predicts **which skills will be valuable in the next 3–5 years** by analyzing real-world job postings and occupational skill databases.

The platform helps users answer a critical question:

> *Which skills should I learn today to remain competitive in the future job market?*

---

# Project Motivation

Many students choose degrees without understanding the **future demand for skills**.

Traditional career tools only show:

* current job listings
* existing career paths

They rarely analyze **emerging skills or declining competencies**.

This project builds a **data-driven intelligence system** that connects:

* occupational skill databases
* global job postings
* skill similarity models
* demand analysis

The result is a system that identifies:

* **emerging high-demand skills**
* **declining skill categories**
* **personal skill gaps**

---

# Key Features

### Skill Gap Detection

Compares user skills against global labor market demand.

### Emerging Skill Identification

Finds technologies and competencies gaining popularity.

### Declining Skill Detection

Detects skills losing relevance across industries.

### Global Skill Demand Analysis

Analyzes job posting data to determine skill trends.

### AI-based Skill Similarity

Uses vector embeddings to match related skills.

### Interactive Dashboard

Provides data visualizations and insights using Streamlit.

---

# Example Output

User Input

```
Degree: Computer Science
Skills: Python, Data Analysis
Country: Germany
Career Interest: AI
```

System Output

```
Top Global Skills
- Machine Learning
- MLOps
- Cloud Computing
- AI Ethics

Skill Gap Analysis
You should learn:
- Deep Learning
- Model Deployment
- Kubernetes
```

---

# System Architecture

The system consists of **five core modules**:

```
Raw Datasets
     ↓
Data Cleaning Pipeline
     ↓
Skill Extraction Engine
     ↓
Vector Similarity Model
     ↓
Demand Analysis Engine
     ↓
Interactive Dashboard
```

---

# Methodology

### 1 Data Collection

The system integrates multiple labor market datasets.

Main sources include:

O*NET Occupational Skill Database
[https://www.onetcenter.org/database.html](https://www.onetcenter.org/database.html)

LinkedIn Skill Dataset
[https://www.kaggle.com/datasets/arshkon/linkedin-job-postings](https://www.kaggle.com/datasets/arshkon/linkedin-job-postings)

These datasets provide:

* occupation skill requirements
* technology skills
* job market trends

---

### 2 Data Cleaning

Raw datasets contain:

* duplicates
* inconsistent naming
* missing values

Cleaning pipeline standardizes skill names and removes noise.

Scripts used:

```
src/01_clean_onet_data.py
src/02_clean_tech_skills.py
```

Output files:

```
skills_cleaned.csv
tech_skills.csv
```

---

### 3 Skill Extraction from Job Postings

Job descriptions are scanned to detect skills mentioned in job listings.

Processing includes:

* text normalization
* keyword matching
* skill frequency extraction

Script used:

```
src/03_extract_job_skills.py
```

Output:

```
job_skills_extracted.csv
```

---

### 4 Vector Embedding Model

Skills are converted into **numerical vectors** using machine learning.

This enables:

* similarity search
* skill clustering
* intelligent recommendations

Script:

```
src/04_build_skill_vectors.py
```

Vector models are **generated locally** and not stored in the repository due to size limitations.

---

### 5 Job Market Demand Analysis

The system aggregates skill frequencies across job postings to determine:

* high-demand skills
* declining skills
* emerging technologies

Script:

```
src/05_job_demand_analysis.py
```

Output:

```
skill_demand.csv
```

---

### 6 Interactive Dashboard

The final insights are visualized through a **Streamlit dashboard**.

Features include:

* skill demand bar charts
* skill distribution pie charts
* personalized recommendations

Run dashboard:

```
streamlit run dashboard/app.py
```

---

# Project Structure

```
skill-gap-intelligence-system
│
├── dashboard
│   └── app.py
│
├── data
│   ├── raw
│   │   ├── onet
│   │   │   ├── Skills.txt
│   │   │   ├── Occupation Data.txt
│   │   │   └── Technology Skills.txt
│   │   │
│   │   └── linkedin
│   │       └── linkedin_skills.csv
│   │
│   └── processed
│       ├── skills_cleaned.csv
│       ├── tech_skills.csv
│       ├── job_skills_extracted.csv
│       └── skill_demand.csv
│
├── src
│   ├── 01_clean_onet_data.py
│   ├── 02_clean_tech_skills.py
│   ├── 03_extract_job_skills.py
│   ├── 04_build_skill_vectors.py
│   └── 05_job_demand_analysis.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# Installation

Clone the repository

```
git clone https://github.com/USERNAME/skill-gap-intelligence-system.git
```

Navigate to the project

```
cd skill-gap-intelligence-system
```

Install dependencies

```
pip install -r requirements.txt
```

---

# Dataset Setup

Large datasets are **not included in the repository** due to GitHub file size limits.

Download datasets manually.

LinkedIn Job Postings Dataset

[https://www.kaggle.com/datasets/arshkon/linkedin-job-postings](https://www.kaggle.com/datasets/arshkon/linkedin-job-postings)

Place files here:

```
data/raw/linkedin_jobs/postings.csv
```

---

# Run Data Processing Pipeline

Execute scripts in order:

```
python src/01_clean_onet_data.py
python src/02_clean_tech_skills.py
python src/03_extract_job_skills.py
python src/04_build_skill_vectors.py
python src/05_job_demand_analysis.py
```

---

# Launch Dashboard

```
streamlit run dashboard/app.py
```

---

# Visualization Outputs

The dashboard generates visual analytics including:

Skill demand bar charts

Example:

```
Machine Learning  ███████████
Cloud Computing   █████████
AI Ethics         ███████
```

Skill distribution pie charts

```
AI Skills        35%
Cloud Skills     25%
Data Skills      20%
DevOps Skills    20%
```

---

# Research Contributions

This project demonstrates practical application of:

* labor market intelligence
* machine learning skill embeddings
* workforce analytics
* career recommendation systems

The approach can help:

* students plan learning paths
* universities design curriculum
* governments identify skill shortages
* companies forecast talent demand

---

# Future Improvements

Potential future upgrades:

Skill trend forecasting using time-series models

Integration with live job APIs

Deep learning NLP skill extraction

Country-specific skill demand analysis

Real-time career recommendation system

---

# Technologies Used

Python
Pandas
Scikit-learn
Streamlit
Plotly

---

# Author

Joseph D A costa

---

# License

This project is released under the MIT License.
