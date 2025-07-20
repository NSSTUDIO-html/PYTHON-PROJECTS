import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"what is your name?",
        ["My name is ChatBot.",]
    ],
    [
        r"how are you ?",
        ["I'm doing well!", "I'm fine, thank you.",]
    ],
    [
        r"(.*) (weather|temperature) (today|now)?",
        ["I'm sorry, I cannot provide real-time weather information.",]
    ],
    [
        r"bye|goodbye",
        ["Goodbye!", "Have a great day!"]
    ],
]

chatbot = Chat(pairs, reflections)

def nltk_chatbot():
    print("Hello! I'm a chatbot created with NLTK.")
    chatbot.converse()

if __name__ == "__main__":
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('wordnet')
    nltk_chatbot()
