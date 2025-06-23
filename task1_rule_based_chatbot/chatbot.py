import re

def chatbot_response(user_input):
    user_input = user_input.lower()

    if re.search(r'\b(hi|hello|hey|good morning|good evening)\b', user_input):
        return "Hello! How can I assist you today?"
    elif re.search(r'\b(how are you|how’s it going)\b', user_input):
        return "I'm just a bot, but I'm functioning as expected!"
    elif re.search(r'\b(what is ai|define artificial intelligence)\b', user_input):
        return "AI is the simulation of human intelligence in machines that are programmed to think like humans."
    elif re.search(r'\b(bye|goodbye|see you)\b', user_input):
        return "Goodbye! Have a great day!"
    elif "thank you" in user_input or "thanks" in user_input:
        return "You're welcome! "
    else:
        return "I'm sorry, I don't understand that yet."

# Chat loop
while True:
    user = input("You: ")
    if user.lower() in ["bye", "exit", "quit"]:
        print("Bot: Goodbye!")
        break
    print("Bot:", chatbot_response(user))
