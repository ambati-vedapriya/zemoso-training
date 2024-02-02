from abc import ABC, abstractmethod


class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print("it is running")

com1=Laptop()
com1.process()