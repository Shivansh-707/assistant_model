import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib

# Sample dataset
data = {
    'text': [
        "what time is it", "tell me the time", "current time",
        "tell me a joke", "make me laugh", "say something funny",
        "who is albert einstein", "search wikipedia for python", "wikipedia artificial intelligence",
        "open youtube", "launch google", "go to facebook",
        "hello", "hi there", "hey",
        "bye", "quit", "exit"
    ],
    'intent': [
        "time", "time", "time",
        "joke", "joke", "joke",
        "wikipedia", "wikipedia", "wikipedia",
        "open_site", "open_site", "open_site",
        "greet", "greet", "greet",
        "exit", "exit", "exit"
    ]
}

df = pd.DataFrame(data)

# Create and train the model
model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(df['text'], df['intent'])

# Save the model
joblib.dump(model, "intent_model.pkl") #to save model
print("✅ Model trained and saved as intent_model.pkl")
