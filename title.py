
from dataclasses import dataclass

class CollectTitel():

    def __init__(self, title):

        self.titles = []

        self.title = title

    @dataclass
    class Titel():

        title: str
        
    def collect_title(self):

        title = self.Titel(self.title)

        self.titles.append(title)

    def clear_titles(self):

        self.titles.clear()
    
    def return_titles(self):

        return self.titles

    