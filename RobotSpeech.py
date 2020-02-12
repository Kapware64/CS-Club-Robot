import random
import re

WORDS = ["MEANING", "OF", "LIFE"]

def handle(text, mic, profile):
    messages = ["It's 42.",
                "It's 42. How many times do I have to tell you?"]

    message = random.choice(messages)

    mic.say(message)

def isValid(text):
    return bool(re.search(r'\bmeaning of life\b', text, re.IGNORECASE))
