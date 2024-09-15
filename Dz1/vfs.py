import os
import tarfile
from pathlib import Path

class VirtualFileSystem:
    def __init__(self, tar_path):
        self.fs_path = '/tmp/vfs'
        self.extract_tar(tar_path)
        self.current_path = self.fs_path
    
    def extract_tar(self, tar_path):
        with tarfile.open(tar_path, 'r') as tar:
            tar.extractall(path=self.fs_path)
    
    def list_files(self):
        return os.listdir(self.current_path)
    
    def change_directory(self, path):
        if path == '/':
            self.current_path = self.fs_path
        else:
            new_path = os.path.normpath(os.path.join(self.current_path, path))
            if os.path.commonpath([self.fs_path, new_path]) == self.fs_path:
                if os.path.isdir(new_path):
                    self.current_path = new_path
                else:
                    print(f"cd: no such file or directory: {path}")
            else:
                print("cd: Access denied. You cannot leave the VFS.")
    
    def read_file(self, file_path):
        with open(file_path, 'r') as f:
            return f.read()
    
    def tree(self, path=None, level=0):
        path = path or self.current_path
        for root, dirs, files in os.walk(path):
            for name in dirs:
                print(' ' * level * 4 + '|-- ' + name)
                self.tree(Path(root) / name, level + 1)
            for name in files:
                print(' ' * level * 4 + '|-- ' + name)

#import os
#import tarfile
#from pathlib import Path
#
#class VirtualFileSystem:
#    def __init__(self, tar_path):
#        self.fs_path = '/tmp/vfs'
#        self.extract_tar(tar_path)
#        self.current_path = self.fs_path
#    
#    def extract_tar(self, tar_path):
#        with tarfile.open(tar_path, 'r') as tar:
#            tar.extractall(path=self.fs_path)
#    
#    def list_files(self):
#        return os.listdir(self.current_path)
#    
#    def change_directory(self, path):
#        new_path = Path(self.current_path) / path
#        if os.path.isdir(new_path):
#            self.current_path = str(new_path)
#        else:
#            print(f"cd: no such file or directory: {path}")
#    
#    def read_file(self, file_path):
#        with open(file_path, 'r') as f:
#            return f.read()
#    
#    def write_file(self, file_path, content):
#        with open(file_path, 'w') as f:
#            f.write(content)
#    
#    def tree(self, path=None, level=0):
#        path = path or self.current_path
#        for root, dirs, files in os.walk(path):
#            for name in dirs:
#                print(' ' * level * 4 + '|-- ' + name)
#                self.tree(Path(root) / name, level + 1)
#            for name in files:
#                print(' ' * level * 4 + '|-- ' + name)
#
