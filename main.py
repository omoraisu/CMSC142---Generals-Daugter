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
        self.file_type = '.txt' # Default file type, needs to be edited
        self.children = None
        self.parent = None
    
    def get_name(self):
        return self.name

    def __repr__(self):
        return f'/{self.name}'

class Directory(Node):
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parent = None
    
    def get_name(self):
        return self.name

    def __repr__(self):
        return f'{self.name}'

class Tree: 
    def __init__(self, root):
        self.root = root
    
    def insert(self, data):
        data.parent = self
        self.root.children.append(data)

    def search(self, data):
        if self.root.get_name() == data:
            return True
        elif self.root.children:
            for child in self.root.children:
                if child.get_name() == data:
                    return True
                else:
                    if Tree(child).search(data):
                        return True
        return False
    
    # Automatically deletes directory and files 
    # It was recommended that before deleting the directory, the files should be deleted first 
    # But it works, I guess? 
    def delete(self, data):
        if self.root.get_name() == data:
            self.root = None
            return True
        if self.root.children:
            for child in self.root.children:
                if child.get_name() == data:
                    self.root.children.remove(child)
                    return True
                else:
                    Tree(child).delete(data)

    def print_tree(self): 
        print(self.root)
        if self.root == None: 
            return
        elif self.root.children:
            for child in self.root.children:
                temp = Tree(child)
                temp.print_tree()
    
    # Temp only for testing, needs further modification to print all nodes in correct order 
    def __repr__(self):
        return f'{self.root}'

class FileSystem:
    def __init__(self, root: Tree):
        self.root = root
    
    def run(self):
        while True:
            command = input("Enter command > ")

            if command == "exit":
                break


### Testing ###

dir1 = Directory("Laptop")
t_dir1 = Tree(dir1)
t_dir1.insert(File("Mac"))
t_dir1.insert(File("Windows"))
t_dir1.insert(File("Linux"))

dir2 = Directory("Cellphone")
t_dir2 = Tree(dir2)
t_dir2.insert(File("Android"))
t_dir2.insert(File("iOS"))

dir3 = Directory("TV")
t_dir3 = Tree(dir3)
t_dir3.insert(File("Samsung"))
t_dir3.insert(File("LG"))
t_dir3.insert(File("Sony"))

root = Directory("Electronics")
t_root = Tree(root)
t_root.insert(t_dir3.root)
t_root.insert(t_dir2.root)
t_root.insert(t_dir1.root)
t_root.delete("LG")

#t_root.print_tree()

print(t_root.search(""))

"""
Resources: 
File System Tree Implementation - Javascript/Tree Data Structure
    https://github.com/beforesemicolon/tutorials-files/blob/master/tree-file-system.js 
"""
