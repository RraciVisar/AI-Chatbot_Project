import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import pickle

# Load the data from the CSV file
df = pd.read_csv('chatbot_data.csv')

# Handle missing values by dropping rows with any missing values
df.dropna(inplace=True)

# Define the pipeline
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', LogisticRegression())
])

# Train the model
pipeline.fit(df['User Input'], df['Response'])

# Save the trained model
with open('chatbot_model.pkl', 'wb') as file:
    pickle.dump(pipeline, file)

print("Model trained and saved successfully.")
