# importing regex and random libraries
import re
import random


class AlienBot:
    # potential negative responses
    negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")
    # keywords for exiting the conversation
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")
    # random starter questions
    random_questions = (
        "Why are you here? ",
        "Are there many humans like you? ",
        "What do you consume for sustenance? ",
        "Is there intelligent life on this planet? ",
        "Does Earth have a leader? ",
        "What planets have you visited? ",
        "What technology do you have on this planet? "
    )
    goodbye = "Okay, have a nice Earth day!"

    def __init__(self):
        self.alienbabble = {'describe_planet_intent': r'(?i)(?:.*\b(?:your|the)\s+planet\b.*)',
                            'answer_why_intent': r'(?i)(why\s+are\s+you\s+here|what\s+brings\s+you\s+to\s+earth|why\b.*)',
                            'cubed_intent': r'(?i)(?:.*\bcube\b.*?(\d+))'
                            }

    # Define .greet() below:
    def greet(self):
        self.name = input("Hello there, what's your name? ")
        will_help = input(f"Hi {self.name}, I'm Etcetera. I\'m not from this planet. Will you help me learn about your planet? ")
        if will_help in self.negative_responses:
            print(self.goodbye)
            return
        self.chat()

    # Define .make_exit() here:
    def make_exit(self, reply):
        for word in self.exit_commands:
            if word in reply:
                print(self.goodbye)
                return True
        return False

    # Define .chat() next:
    def chat(self):
        reply = input(random.choice(self.random_questions)).lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply))

    # Define .match_reply() below:
    def match_reply(self, reply):
        for key, value in self.alienbabble.items():
            found_match = re.search(value, reply)
            if found_match:
                if key == "describe_planet_intent":
                    responses = (
                        "My planet is a utopia of diverse organisms and species. ",
                        "I am from Opidipus, the capital of the Wayward Galaxies. "
                    )
                    return random.choice(responses)
                
                elif key == "answer_why_intent":
                    responses = (
                        "I come in peace. ",
                        "I am here to collect data on your planet and its inhabitants. ",
                        "I heard the coffee is good. "
                    )
                    return random.choice(responses)
                
                elif key == "cubed_intent":
                    number = int(found_match.group(1))
                    cubed_number = number ** 3
                    return f"The cube of {number} is {cubed_number}. Isn't that cool? "
        

        responses = (
            "Please tell me more. ", "Tell me more! ",
            "Why do you say that? ",
            "I see. Can you elaborate? ",
            "Interesting. Can you tell me more? ",
            "I see. How do you think? ",
            "Why? ",
            "How do you think I feel when you say that? "
        )
        return random.choice(responses)
    
    # Define .describe_planet_intent():
    def describe_planet_intent(self):
        return "Inside .describe_planet_intent()"

    # Define .answer_why_intent():
    def answer_why_intent(self):
        return "Inside .answer_why_intent()"

    # Define .cubed_intent():
    def cubed_intent(self, number):
        return "Inside .cubed_intent()"

    # Define .no_match_intent():
    def no_match_intent(self):
        return "Inside .no_match_intent()"

# Create an instance of AlienBot below:
my_bot = AlienBot()
my_bot.greet()