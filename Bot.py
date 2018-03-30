from lib import Configurator
from lib import DbAccess
import random
import os

class Bot:

    HINT_GREET = os.path.join("lib","hints","greet.lsv")
    PRECISION = 100

    def __init__(self, precision = PRECISION):
        self.precision  = precision
        self.greeted = False
        self.db = DbAccess.DbAccess()
        return

    def respond(self, str):
        if(not self.greeted and self.isGreeting(str)):
            self.greeted = True
            return self.greet()
        answer = self.findAnswer(str)
        if answer is None:
            return random.choice(self.db.getUnknowns(self.precision))
        return answer

    def greet(self):
        precision = self.precision
        return random.choice(self.db.getGreetings(precision))

    # Gets words from hint file and db, and tries to see if the greeting
    def isGreeting(self, str):
        precision = self.precision
        with open(self.HINT_GREET) as f:
            greetHints = f.readlines()
        greetHints = [x.strip() for x in greetHints]
        greetHints = greetHints + self.db.getGreetings(precision)
        if matches(str.split(" "), greetHints):
            return True
        return False


    def findAnswer(self, str):
        return None


# Helper functions
def inArr(str,arr):
    for s in arr:
        if str.lower() == s.lower():
            return True
    return False
def matches(arr1,arr2):
    for s1 in arr1:
        for s2 in arr2:
            if s1.lower() == s2.lower():
                return True
    return False

