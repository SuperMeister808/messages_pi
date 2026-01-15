
from dataclasses import dataclass
from typing import List

class CollectTitel():

    titels : List["CollectTitel.Titel"] = []
    
    def __init__(self, title):

        self.title = title

    @dataclass
    class Titel():

        title: str
        
    def collect_title(self):

        t = self.Titel(self.title)

        self.append_title(t)

    @classmethod
    def append_title(cls, title):

        cls.titels.append(title)

    @classmethod
    def clear_titles(cls):

        cls.titels.clear()
    
    @classmethod
    def return_titles(cls):

        return cls.titels

    