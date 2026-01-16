
from dataclasses import dataclass
from typing import List

class CollectTitel():

    titels : List["CollectTitel.Titel"] = []
    
    def __init__(self, titel):

        self.titel = titel

    @dataclass
    class Titel():

        titel: str
        
    def collect_title(self):

        t = self.Titel(self.titel)

        self.append_title(t)

    @classmethod
    def append_title(cls, titel):

        cls.titels.append(titel)

    @classmethod
    def clear_titles(cls):

        cls.titels.clear()
    
    @classmethod
    def return_titles(cls):

        return cls.titels

    