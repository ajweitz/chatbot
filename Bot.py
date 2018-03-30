from lib import Configurator
from lib import DbAccess
import random
import os

class Bot:

    DONT_UNDERSTAND = ["lol, not sure what you mean","wut","i don't understand"]
    HINT_GREET = os.path.join("lib","hints","greet.lsv")

    def __init__(self):
        self.dont_understand = self.DONT_UNDERSTAND
        self.greeted = False
        self.db = DbAccess.DbAccess()
        return

    def respond(self, str):
        if(not self.greeted and self.isGreeting(str)):
            self.greeted = True
            return self.greet()
        answer = self.find_answer(str)
        if answer is None:
            return random.choice(self.dont_understand)
        return answer

    def greet(self):
        return "hi"

    def isGreeting(self, str):
        with open(self.HINT_GREET) as f:
            greetHints = f.readlines()
        greetHints = [x.strip() for x in greetHints]
        return False


    def find_answer(self, str):
        return None

