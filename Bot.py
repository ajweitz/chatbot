from lib import Configurator
import psycopg2
import random

class Bot:
    DONT_UNDERSTAND = ["lol, not sure what you mean","wut","i don't understand"]
    DB_CONFIG = "database.ini"
    def __init__(self):
        self.dont_understand = self.DONT_UNDERSTAND
        self.config = Configurator.Configurator()
        self.dbConfig = self.config.dbConfig(self.DB_CONFIG)

        return

    def respond(self, str):
        answer = self.find_answer(str)
        if answer is None:
            return random.choice(self.dont_understand)
        return answer

    def greet(self):
        return "hi"

    def find_answer(self, str):
        return None