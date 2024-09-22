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
            if os.path.isfile(file_path):
                content = vfs.read_file(file_path)
                print("\n".join(content.splitlines()[-10:]))
            else:
                print(f"tail: {parts[1]}: No such file")
        else:
            print("tail: missing operand")
    elif cmd == "uniq":
        if len(parts) > 1:
            file_path = Path(vfs.current_path) / parts[1]
            if os.path.isfile(file_path):
                content = vfs.read_file(file_path)
                unique_lines = set(content.splitlines())
                print("\n".join(unique_lines))
            else:
                print(f"uniq: {parts[1]}: No such file")
        else:
            print("uniq: missing operand")
    elif cmd == "pwd":
        print(vfs.current_path)
    else:
        print(f"{cmd}: command not found")

