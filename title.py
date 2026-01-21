
from dataclasses import dataclass
from typing import List

class CollectTitle():

    titles : List["CollectTitle.Title"] = []
    
    def __init__(self, title):

        self.title = title

    @dataclass
    class Title():

        title: str
        
    def collect_title(self):

        t = self.Title(self.title)

        self.append_title(t)

    @classmethod
    def append_title(cls, title):

        cls.titles.append(title)

    @classmethod
    def clear_titles(cls):

        cls.titles.clear()
    
    @classmethod
    def return_titles(cls):

        return cls.titles

    