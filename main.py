"""
This program was made in collaboration with: 
James Peter Bravo 
Josh Justin Mari Cemine
Myra Daitol 
Daenielle Rai Peladas
"""

class File:
    def __init__(self, name, file_type, file_path):
        self.name = name
        self.file_type = file_type
        self.file_path = file_path

class Directory:
    def __init__(self, name, dir_path) -> None:
        self.name = name
        self.dir_path = dir_path

class Node: 
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree: 
    def __init__(self, root):
        self.root = root
    
    def insert(self, data):
        pass

    def search(self, data):
        pass

    def delete(self, data):
        pass

class Console:
    def __init__(self, tree: Tree):
        self.tree = tree

    def create_directory(self, dir: Directory):
        pass

    def delete_directory(self, dir: Directory):
        pass

    def change_directory(self, dir: Directory):
        pass
    
    def create_file(self, file: File):
        pass
    
    def delete_file(self, file: File):
        pass

    def edit_file(self, file: File):
        pass

    def rename_file(self, file: File):
        pass

    def move_file(self, file: File):
        pass

    def copy_file(self, file: File):
        pass

    def copy_directory(self, dir: Directory):
        pass

    




