
import random

class Bot:
    DONT_UNDERSTAND = ["lol, not sure what you mean","wut","i don't understand"]
    def __init__(self):
        self.dont_understand = self.DONT_UNDERSTAND
        return

    def talk(self, str):
        answer = self.find_answer(str)
        if answer is None:
            return random.choice(self.dont_understand)
        return answer

    def find_answer(self, str):
        return None