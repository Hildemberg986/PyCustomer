from functions.create import *
from functions.search import *
from functions.delete import *
from functions.clear import *
clear()
line = "\n"
add = create_user()
clear()
olhar = open("User.txt", "r")
print(olhar.readlines())