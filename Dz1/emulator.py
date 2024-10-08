import argparse
import socket
from vfs import VirtualFileSystem
from commands import execute_command
import sys
from pathlib import Path
import tkinter as tk
from tkinter import scrolledtext
import os

def run_shell(vfs, start_script):
    if start_script:
        with open(start_script, 'r') as script:
            for line in script:
                execute_command(vfs, line.strip())

    while True:
        prompt = f"{socket.gethostname()}:{vfs.current_path}$ "
        try:
            command = input(prompt).strip()
            if command == "exit":
                break
            execute_command(vfs, command)
        except EOFError:
            break

def main():
    parser = argparse.ArgumentParser(description="Virtual File System Shell Emulator")
    parser.add_argument("hostname", help="Hostname for prompt", nargs='?', default='mycomputer')
    parser.add_argument("vfs_tar", help="Path to the VFS tar file", nargs='?', default='test_vfs.tar')
    parser.add_argument("start_script", help="Path to the startup script", nargs='?', default='start_script.txt')
    
    args = parser.parse_args()
    
    vfs = VirtualFileSystem(args.vfs_tar)
    run_shell(vfs, args.start_script)

if __name__ == "__main__":
    main()
