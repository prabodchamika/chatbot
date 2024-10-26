import json
import random

# Load essay intents data
with open("data/essay_intents.json") as file:
    essay_intents = json.load(file)

# Function to match user input with essay intent patterns
def predict_essay_intent(user_input):
    for intent in essay_intents['intents']:
        for pattern in intent['patterns']:
            if pattern.lower() in user_input.lower():
                return intent
    return None

# Function to get a response for essay prompts
def essay_chatbot_response(user_input):
    # Predict the essay intent
    intent = predict_essay_intent(user_input)

    # Return a random response if a matching intent is found
    if intent:
        return random.choice(intent['responses'])
    else:
        return None  # Return None if no essay-related intent is found

# For testing the essay functionality interactively
if __name__ == "__main__":
    print("Essay Writer is running! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        response = essay_chatbot_response(user_input)
        print(f"Bot: {response}")
