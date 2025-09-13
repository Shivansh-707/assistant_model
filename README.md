# Voice Assistant with Intent Recognition

This project is a simple voice based assistant that understands spoken commands and performs tasks like telling the time opening a website fetching a Wikipedia summary or telling a joke The system combines natural language processing with speech recognition and text to speech  

The intent recognition model is built using Naive Bayes I first came across Naive Bayes in my 11th standard and ever since then I was hooked. I have always had a deep love for probability even as a kid I remember telling my orthodox and traditional parents that things are not luck papa and mummy , they are "probability". That mindset stuck with me and made Naive Bayes feel very natural and intuitive to me Naive Bayes is a probabilistic classifier that applies Bayes theorem with the assumption that words in a sentence are independent of each other Although this assumption is unrealistic in practice the model works very well for text classification problems like spam detection sentiment analysis and here intent recognition.

## Features

- Speech recognition using Google Speech API  
- Text to speech using pyttsx3  
- Tells current time  
- Fetches jokes using pyjokes  
- Summarizes Wikipedia articles  
- Opens common websites  
- Greeting and exit commands  

## How it works

1 Training  
   - A small dataset of example commands like "what time is it" or "tell me a joke" is vectorized using TF IDF  
   - The text is passed to a Multinomial Naive Bayes model which learns to classify each command into an intent such as time joke wikipedia open_site greet or exit  
   - The trained model is saved as intent_model.pkl  

2 Runtime  
   - The assistant listens to the user converts speech to text and predicts the intent using the trained model  
   - Based on the predicted intent it executes the appropriate action and responds with text to speech  

## System diagram
User Speech -> Speech Recognition ->Predicted Text -> Naive Bayes Classifier -> Predicted Intent -> Action Handler (time joke wiki open site exit) -> Response
