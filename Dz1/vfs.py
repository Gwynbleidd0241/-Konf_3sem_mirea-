import os
import tarfile
from pathlib import Path

class VirtualFileSystem:
    def __init__(self, tar_path):
        self.fs_path = 'vfs'
        self.extract_tar(tar_path)
        self.current_path = self.fs_path

    def extract_tar(self, tar_path):
        with tarfile.open(tar_path, 'r') as tar:
            tar.extractall(path=self.fs_path)

    def list_files(self):
        return [f for f in os.listdir(self.current_path) if f != '.DS_Store']

    def change_directory(self, path):
        if path == '/':
            self.current_path = self.fs_path
        else:
            new_path = os.path.normpath(os.path.join(self.current_path, path))
            if os.path.commonpath([os.path.abspath(self.fs_path), os.path.abspath(new_path)]) == os.path.abspath(self.fs_path):
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
        path = os.path.normpath(path)

        def print_tree(current_path, level):
            indent = ' ' * (level * 2)
            items = sorted(os.listdir(current_path))
            for item in items:
                if item == '.DS_Store':
                    continue
                item_path = os.path.join(current_path, item)
                if os.path.isdir(item_path):
                    print(f"{indent}|-- {item}")
                    print_tree(item_path, level + 1)
                else:
                    print(f"{indent}|-- {item}")

        if os.path.isdir(path):
            print(os.path.basename(path))
            print_tree(path, 1)
        else:
            print(f"tree: {path} is not a directory")

