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
def predict_career(user_skills, cgpa=None, year=None):
    user_vec = vectorizer.transform([user_skills])
    career = model.predict(user_vec)[0]

    # Adjust for CGPA
    if cgpa is not None:
        if cgpa < 7:
            career += " (Consider beginner-friendly internships)"
        elif cgpa >= 8:
            career += " (Aim for competitive internships)"
    
    return career
