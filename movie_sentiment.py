import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

data = pd.read_csv("reviews_dataset.csv")

X = data["review"]
y = data["sentiment"]

vectorizer = CountVectorizer()
X_vector = vectorizer.fit_transform(X)

model = MultinomialNB()
model.fit(X_vector, y)

review = input("Enter movie review: ")

review_vector = vectorizer.transform([review])
prediction = model.predict(review_vector)

print("Prediction:", prediction[0])
