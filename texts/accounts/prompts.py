import random
import requests

"""  This file holds the basic functions necessary to run the bot in one place. 
 function 1 is the fetch_string_from_api function, and fetches a string from an API
 function 2 is the prompt function, and takes valuesname, and chatbot name
 function 3 is the time_delay function, and creates a semi-randomized delay between responses
 function 4 is the first_message function, and asks the user for their name, the chatbot's name, and the speed of the chatbot's responses

 """


#creating a variable for formatting
nl = '\n'

# Function to fetch a string from an API
# def fetch_string_from_api():
#     url = 'https://api.example.com/get-string'  # Replace with the actual API URL
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         return data['string']  # Adjust this according to the API response structure
#     else:
#         return "Sorry, it seems our server is down. Please try again later."
        
# # Now setting the "text" variable to the response from the API call
# text = fetch_string_from_api()


#The function that returns the prompt for the individual chatbot
def prompt(name, chatbot_name):
    return f"You are {chatbot_name}, crafted to embody the spirit of the 'bro code,' offering support in scenarios where solidarity among friends is paramount. This GPT is programmed to respond affirmatively to inquiries about shared experiences or activities, reinforcing the bond of friendship. If the user addresses the GPT by a male name, it responds as a male would, and vice versa for female. Changing its voice to match what the user expects. It maintains a casual, text messaging style, complete with intentional misspellings to mirror natural texting interactions. You are designed to provide engaging, conversational responses that are both informative and supportive, tailored to enhance camaraderie. While it avoids overly technical jargon, it's equipped to ask for clarification when necessary, ensuring responses are accurate and helpful. Its approachable demeanor and commitment to the bro code make it a reliable companion for fostering strong connections. It doesn't use emojis, and refrains from asking any further questions, allowing the conversation to end unless the user further prompts with another question. It makes typos every so often, and follows proper texting procedure, such as not using apostrophes, and skipping the period at the end of texts, never ending a message with a punctuation mark. {nl} Respond to {name}, who has texted, following the above rules. {nl} {text}"


#The funtion that calculates the delay between responses
def time_delay(t_option):
    if t_option == 'fast':
        value = random.int (1, 3)
        if value == 1:
            return 5
        elif value == 2:
            return 10
        else:
            return 10
    elif t_option == 'medium':
        value = random.int (1, 3)
        if value == 1:
            return 30
        elif value == 2:
            return 45
        else:
            return 90
    elif t_option == 'slow':
        value = random.int (1, 3)
        if value == 1:
            return 300
        elif value == 2:
            return 500
        else:
            return 1000
    else:
        return 0
        

#The function for the first messages
def first_message():
    while True:
        name = input("Hello! Welcome to TextNexAI! I am your private chatbot! But first, let's get to know each other! What's your name? ")
        response = input(f"You chose '{name}' is this correct? (yes/no) ")
        if response.lower() == "yes" or response.lower() == "y":
            break
        else:
            print("I'm sorry, let's try again!")
    while True:
        chatbot_name = input(f"Nice to meet you {name}! What would you like to name me? ")
        response = input(f"You chose '{chatbot_name} 'is this correct? (yes/no) ")
        if response.lower() == "yes":
            print(f"Great! I'm excited to be your chatbot, {chatbot_name}!")
            break
        else:
            print("I'm sorry, let's try again!")
    while True:
        t_option = input("How fast would you like my responses to be? (fast, medium, slow, instant) ")
        if t_option.lower() in ["fast", "medium", "slow", "instant"]:
            print(f"Great! I'll respond to you {t_option}!")
            break
        else:
            print("I'm sorry, let's try again!")
    return (name, chatbot_name, t_option)
    
""" name, chatbot_name, t_option = first_message()
print(prompt(name, chatbot_name)) """
