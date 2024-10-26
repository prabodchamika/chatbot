import json
import random
import nltk
from nltk.stem import WordNetLemmatizer
import numpy as np
from essay_writer import essay_chatbot_response  


lemmatizer = WordNetLemmatizer()


with open("data/intents.json") as file:
    intents = json.load(file)



def preprocess(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words


def predict_intent(user_input):
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            if pattern.lower() in user_input.lower():
                return intent
    return None


def chatbot_response(user_input):
    
    essay_response = essay_chatbot_response(user_input)
    if essay_response:
        return essay_response  

    
    user_input = preprocess(user_input)

    
    intent = predict_intent(" ".join(user_input))

    
    if intent:
        return random.choice(intent['responses'])
    else:
        return "I didn't understand that. Could you please rephrase?"


if __name__ == "__main__":
    print("Chatbot is running! Type 'exit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = chatbot_response(user_input)
        print(f"Bot: {response}")