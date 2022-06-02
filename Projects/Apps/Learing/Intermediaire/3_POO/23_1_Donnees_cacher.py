class Queue:
    def __init__(self, contenu):
        self._cacherlist = list(contenu)

    def push(self, valeur):
        self._cacherlist.insert(0, valeur)

    def pop(self):
        return self._cacherlist.pop(-1)

    def __repr__(self):
        return "Queue({})".format(self._cacherlist)

queue = Queue([1, 2, 3])
print(queue)
queue.push(0)
print(queue)
queue.pop()
print(queue)
print(queue._cacherlist)
print()

class pom:
    __oeuf = 7
    def print__oeuf(self):
        print(self.__oeuf)

s = pom()
s.print__oeuf()
print(s._pom__oeuf)
print(s.__oeuf)
print()