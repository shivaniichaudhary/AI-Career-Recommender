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
def predict_career(user_skills):
    user_vec = vectorizer.transform([user_skills])
    return model.predict(user_vec)[0]
