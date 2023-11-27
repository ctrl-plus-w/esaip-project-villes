import os

from src.classes.parser import Parser


data = Parser.retrieve_data("./src/assets/villes.txt")
parser = Parser(data)
print(parser.parse())
