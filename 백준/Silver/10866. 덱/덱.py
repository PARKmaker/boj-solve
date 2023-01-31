import sys
si = sys.stdin.readline

class Deck:
  def __init__(self):
    self.arr = []

  def push_front(self, x):
    self.arr = [x] + self.arr

  def push_back(self, x):
    self.arr.append(x)

  def empty(self):
    if len(self.arr) == 0:
      return 1
    else:
      return 0

  def pop_front(self):
    if self.empty():
      return -1
    else:
      return self.arr.pop(0)

  def pop_back(self):
    if self.empty():
      return -1
    else:
      return self.arr.pop()

  def size(self):
    return len(self.arr)

  def front(self):
    if self.empty():
      return -1
    else:
      return self.arr[0]

  def back(self):
    if self.empty():
      return -1
    else:
      return self.arr[self.size()-1]

n = int(si())
deck = Deck()

for _ in range(n):
  command = si().strip().split()

  if command[0] == 'push_back':
        deck.push_back(int(command[1]))

  elif command[0] == 'push_front':
      deck.push_front(int(command[1]))
      
  elif command[0] == 'pop_front':
      print(deck.pop_front())

  elif command[0] == 'pop_back':
      print(deck.pop_back())

  elif command[0] == 'size':
      print(deck.size())

  elif command[0] == 'empty':
      print(deck.empty())

  elif command[0] == 'front':
      print(deck.front())

  elif command[0] == 'back':
      print(deck.back())