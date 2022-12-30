"""
This program was made in collaboration with: 
James Peter Bravo 
Josh Justin Mari Cemine
Myra Daitol 
Daenielle Rai Peladas
"""

from abc import ABC, abstractmethod

class Node(ABC):
    def __init__(self):
        pass

    def __repr__(self):
        pass

class File(Node):
    def __init__(self, name):
        self.name = name
        self.file_type = '.txt'
        self.children = None
        self.parent = None
    
    def __repr__(self):
        return f'/{self.name}{self.file_type}'

class Directory(Node):
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parent = None
    
    def __repr__(self):
        return f'/{self.name}'

class Tree: 
    def __init__(self, root):
        self.root = root
    
    def insert(self, data):
        data.parent = self
        self.root.children.append(data)

    def search(self, data):
        pass

    def delete(self, data):
        pass

    def print_tree(self):
        print(self.root)
        if self.root.children:
            for child in self.root.children:
                temp = Tree(child)
                temp.print_tree()
    
    # Temp only for testing, needs further modification to print all nodes in correct order 
    def __repr__(self):
        return f'{self.root}'


directory = Directory("foo")
file = File("bar")
tree = Tree(directory)
tree.insert(file)
print(file.parent)
print("")
tree.print_tree()

"""
Resources: 
File System Tree Implementation - Javascript/Tree Data Structure
    https://github.com/beforesemicolon/tutorials-files/blob/master/tree-file-system.js 
"""




