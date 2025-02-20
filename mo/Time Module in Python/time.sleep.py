import random
import re

class Elianna:
    ### Potential Responses
    negative_responses = ("no", "nope", "nah", "not a chance", "sorry")
    
    ### Exit Conversation Keyword
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")
    
    ### Random starter questions
    random_questions = (
        "Why are you here?",
        "Are there many humans like you?",
        "What do you consume for sustenance?",
        "Is there intelligent life on this planet?",
        "Does Earth have a leader?",
        "What planets have you visited?",
        "What technology do you have on this planet?"
    )

    def __init__(self):
        self.alienbabble = {
            "describe_planet_intent": r".*\s*your planet.*",
            "answer_why_intent": r"why\sare.*",
            "about_intellipat": r".*\s*intellipaat.*"
        }

    def greet(self):
        self.name = input("What is your name?\n")
        will_help = input(f"Hi {self.name}, I am Elianna. Will you help me learn about your planet?\n").lower()
        
        if will_help in self.negative_responses:
            print("Ok, have a nice Earth day!")
            return
        self.chat()

    def make_exit(self, reply):
        """Check if the user wants to exit."""
        if reply in self.exit_commands:
            print("Okay, have a nice Earth day!")
            return True
        return False

    def chat(self):
        """Main chat loop."""
        reply = input(random.choice(self.random_questions) + "\n").lower()
        
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply) + "\n").lower()

    def match_reply(self, reply):
        """Match user input to predefined responses."""
        for intent, regex_pattern in self.alienbabble.items():
            found_match = re.search(regex_pattern, reply)
            if found_match:
                if intent == "describe_planet_intent":
                    return self.describe_planet_intent()
                elif intent == "answer_why_intent":
                    return self.answer_why_intent()
                elif intent == "about_intellipat":
                    return self.about_intellipat()
        
        return self.no_match_intent()

    def describe_planet_intent(self):
        responses = (
            "My planet is a utopia of diverse organisms and species.",
            "I am from Opidipus, the capital of the Wayward Galaxies."
        )
        return random.choice(responses)

    def answer_why_intent(self):
        responses = (
            "I come in peace.",
            "I am here to collect data on your planet and its inhabitants.",
            "I heard the coffee is good."
        )
        return random.choice(responses)

    def about_intellipat(self):
        return "Elianna is a chatbot."

    def no_match_intent(self):
        responses = (
            "Please tell me more.",
            "Tell me more!",
            "Why do you say that?",
            "I see. Can you elaborate?",
            "Interesting. Can you tell me more?",
            "I see. What do you think?",
            "Why?",
            "How do you think I feel when you say that?"
        )
        return random.choice(responses)

# Run the chatbot
AlienBot = Elianna()
AlienBot.greet()
