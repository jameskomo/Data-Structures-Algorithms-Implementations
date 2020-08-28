graph={}
graph["You"]=["Alice", "Bob", "Claire"]
graph["Bob"]=["Anij", "Peggy"]
graph["Alice"]=["Peggy"]
graph["Claire"]=["Tom", "Jonny"]
graph["Anuj"]=[]
graph["Peggy"]=[]
graph["Tom"]=[]
graph["Jonny"]=[]

# print(graph["Alice"][0])

def person_is_seller(name):
  return name[-1]=="m"

from collections import deque #Double ended queue to allow add and remove from both ends

def search(name):
  search_queue=deque()
  search_queue+=graph[name]
  searched=[]
  while search_queue:
    person=search_queue.popleft()
    if not person in searched:
      if person_is_seller(person):
        print(person+"is a mango seller")
        return True
      else:
        search_queue+=graph[person]
        searched.append(person)
    return False
search("You")
