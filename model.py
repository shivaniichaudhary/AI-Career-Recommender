from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Training data (skills only for now)
skills = [
    "python ml",
    "java dsa",
    "html css js",
    "python sql"
]

careers = [
    "Machine Learning Engineer",
    "Software Developer",
    "Web Developer",
    "Data Analyst"
]

# Convert text to numbers
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(skills)

# Train model
model = MultinomialNB()
model.fit(X, careers)

# Prediction function
def predict_career(skills, cgpa=None, year=None):
    skills = skills.lower()

    if "ml" in skills or "machine learning" in skills or "ai" in skills:
        career = "Machine Learning Engineer"

    elif "html" in skills or "css" in skills or "javascript" in skills:
        career = "Web Developer"

    elif "java" in skills or "c++" in skills or "dsa" in skills:
        career = "Software Developer"

    elif "sql" in skills or "excel" in skills or "data" in skills:
        career = "Data Analyst"

    else:
        career = "Software Developer"

    # CGPA-based suggestion
    if cgpa is not None:
        if cgpa >= 8:
            career += " (Eligible for top internships)"
        elif cgpa < 7:
            career += " (Start with beginner internships)"

    return career

