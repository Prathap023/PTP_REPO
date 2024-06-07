import spacy

# Load spaCy's English language model
nlp = spacy.load("en_core_web_sm")

# Sample responses for demonstration purposes
responses = {
    "greet": "Hello! How can I help you today?",
    "bye": "Goodbye! Have a great day!",
    "default": "I'm sorry, I don't understand that. Could you please rephrase?"
}

# Function to determine the user's intent
def get_intent(text):
    doc = nlp(text)
    for token in doc:
        if token.lemma_ in ["hi", "hello"]:
            return "greet"
        elif token.lemma_ in ["bye", "goodbye"]:
            return "bye"
    return "default"

# Main chatbot function
def chatbot_response(user_input):
    intent = get_intent(user_input)
    return responses.get(intent, responses["default"])

# Simulate a conversation
if __name__ == "__main__":
    print("Chatbot: Hi! I am a chatbot. Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")
