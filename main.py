from sys import path
from os.path import join
path.append(join(path[0], "SearchAPI"))
from SearchAPI.search import Search

search = Search()
print(search.query(input("Enter question:")), "\n\n", search.get_assisted_answers())
