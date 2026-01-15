
from dataclasses import dataclass
from typing import List

class CollectMessage():

    messages : List["CollectMessage.Message"] = []
    
    def __init__(self, message):

        self.message = message

    @dataclass
    class Message():

        message: str
    
    def collect_messages(self):

        message = self.Message(self.message)

        self.append_message(message)

    @classmethod
    def append_message(cls, message):

        cls.messages.append(message)
    
    @classmethod
    def clear_messages(cls):

        cls.messages.clear()
    
    @classmethod
    def return_message(cls):

        return cls.messages