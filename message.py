
from dataclasses import dataclass

class CollectMessage():

    def __init__(self, message):

        self.message = message

        self.messages = []

    @dataclass
    class Message():

        message: str
    
    def collect_messages(self):

        message = self.Message(self.message)

        self.messages.append(message)

    def clear_messages(self):

        self.messages.clear()
    
    def return_message(self):

        return self.message