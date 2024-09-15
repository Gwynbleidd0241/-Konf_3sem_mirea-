import os
from pathlib import Path
from vfs import VirtualFileSystem

def execute_command(vfs, command):
    parts = command.split()
    cmd = parts[0]
    
    if cmd == "ls":
        print("\n".join(vfs.list_files()))
    elif cmd == "cd":
        if len(parts) > 1:
            vfs.change_directory(parts[1])
        else:
            print("cd: missing operand")
    elif cmd == "tree":
        vfs.tree()
    elif cmd == "tail":
        if len(parts) > 1:
            file_path = Path(vfs.current_path) / parts[1]
            content = vfs.read_file(file_path)
            print("\n".join(content.splitlines()[-10:]))
        else:
            print("tail: missing operand")
    elif cmd == "uniq":
        if len(parts) > 1:
            file_path = Path(vfs.current_path) / parts[1]
            content = vfs.read_file(file_path)
            unique_lines = set(content.splitlines())
            print("\n".join(unique_lines))
        else:
            print("uniq: missing operand")
    else:
        print(f"{cmd}: command not found")
