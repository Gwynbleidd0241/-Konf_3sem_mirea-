import struct
import yaml
import sys

COMMANDS = {
    'LOAD_CONSTANT': 15,
    'READ_MEMORY': 0,
    'WRITE_MEMORY': 12,
    'BINARY_LESS': 10
}

def parse_instruction(line):
    line = line.split('#', 1)[0].strip()
    if not line:
        return None, None

    parts = line.split()
    command = parts[0]
    args = [int(part) for part in parts[1:]]

    return command, args

def encode_instruction(command, args):
    opcode = COMMANDS.get(command)
    if opcode is None:
        raise ValueError(f"Неизвестная команда {command}")

    if command == 'LOAD_CONSTANT' and len(args) == 2:
        return struct.pack('<BBB', opcode, args[0], args[1])
    
    elif command == 'READ_MEMORY' and len(args) == 2:
        return struct.pack('<BBB', opcode, args[0], args[1])
    
    elif command == 'WRITE_MEMORY' and len(args) == 2:
        return struct.pack('<BBB', opcode, args[0], args[1])
    
    elif command == 'BINARY_LESS' and len(args) == 2:
        return struct.pack('<BBB', opcode, args[0], args[1])

    raise ValueError(f"Неверные аргументы для команды {command}: {args}")

def assemble(source_path, binary_path, log_path):
    """
    Считывает файл с исходным кодом, создает бинарный файл и лог с инструкциями в виде YAML.
    """
    log_data = []
    with open(source_path, 'r') as source_file, open(binary_path, 'wb') as binary_file:
        for line in source_file:
            command, args = parse_instruction(line)
            if command:
                try:
                    binary_instruction = encode_instruction(command, args)
                    binary_file.write(binary_instruction)
                    log_data.append({"command": command, "args": args, "binary": binary_instruction.hex()})
                except ValueError as e:
                    print(f"Ошибка в команде: {e}")

    with open(log_path, 'w') as log_file:
        yaml.dump(log_data, log_file, indent=4)

if __name__ == "__main__":
    source_path = sys.argv[1]
    binary_path = sys.argv[2]
    log_path = sys.argv[3]
    assemble(source_path, binary_path, log_path)