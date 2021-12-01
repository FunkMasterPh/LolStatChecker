from champ_class import Champ
from create_object import *
from read_data import *
from menu import *
choice = input("Enter name of your champion: ")
readData(choice)
champ1 = createObj(choice)
choice = input("Enter name of lane opponents champion: ")
readData(choice)
champ2 = createObj(choice)
printMenu(champ1, champ2)