""" Normal inheritance hole amra by default eat and move method 2 ta peye jabo kintu jehetu abstraction use kortechi 
    tie derive class eo amader same method eat and move likhte hobe na likhle function ta kaj korbe na ....
    
    interview question -> abstract class vs interfaces    
"""

from abc import ABC, abstractmethod
#abc= abstract base class

class Amimal(ABC): # base class er moddhe ABC k inherit korlam
    @abstractmethod 
    # enforced all derived class to have a eat method
    # abstractmethod use korle derive class gulote eat and move method thaktei hobe eta amra enforced kortechi 
    # otherwise se ei class k inherit korleo se eta access pabe na 
    def eat(self):
        print('I need food')
        
    @abstractmethod
    def move(self):
        pass

class Monkey(Amimal):
    def __init__(self,name) -> None:
        self.category='Monkey'
        self.name=name
        super().__init__()

    def eat(self):
        print('he nanana , I am eating banana')

    def move(self):
        print('Hanging on the branches')

layka=Monkey('lucky')
layka.eat()


cnt = {}
i = 1
if i not in cnt:
    cnt[i] = 1
else:
    cnt[i] += 1

print(cnt)