This project is a simple yet powerful voice-activated AI assistant built using Python.
It listens to user commands through the microphone, interprets the intent using a trained Naive Bayes classifier, and performs actions accordingly. 
The assistant supports common tasks like 
telling the time, telling jokes, searching Wikipedia, opening websites, and greeting or exiting — all triggered by voice.

The intent detection is powered by a lightweight Natural Language Processing (NLP) model trained on example phrases using TfidfVectorizer and MultinomialNB.
The assistant uses speech_recognition for audio input, pyttsx3 for speaking responses, and joblib to save/load the intent model.
This setup makes the assistant fast, customizable, and fully offline (except for Wikipedia search and site launching).
It’s a great beginner-friendly example of combining voice interfaces with basic machine learning.
