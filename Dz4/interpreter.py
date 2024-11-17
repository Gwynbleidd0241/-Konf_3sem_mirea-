import struct
import yaml
import sys

COMMANDS = {
    15: 'LOAD_CONST',
    0: 'READ_MEM',
    12: 'WRITE_MEM',
    10: 'BINARY_LESS'
}

registers = [0] * 1024
memory = [0] * 1024

def load_const(binary_file):
    B, C = struct.unpack('<BB', binary_file.read(2))
    registers[C] = B

def read_mem(binary_file):
    B, C = struct.unpack('<BB', binary_file.read(2))
    registers[B] = memory[C]

def write_mem(binary_file):
    B, C = struct.unpack('<BB', binary_file.read(2))
    addr = registers[C]
    memory[addr] = registers[B]

def binary_less(binary_file):
    B, C = struct.unpack('<BB', binary_file.read(2))
    memory[B] = 1 if memory[B] < registers[C] else 0

def execute(binary_path, result_path, memory_range):
    with open(binary_path, 'rb') as binary_file:
        while True:
            opcode_byte = binary_file.read(1)
            if not opcode_byte:
                break

            opcode = opcode_byte[0]

            if opcode == 15:
                load_const(binary_file)
            elif opcode == 0:
                read_mem(binary_file)
            elif opcode == 12:
                write_mem(binary_file)
            elif opcode == 10:
                binary_less(binary_file)
            else:
                raise ValueError(f"Неизвестная команда с кодом: {opcode}")

    with open(result_path, 'w') as result_file:
        yaml.dump(memory[memory_range[0]:memory_range[1]], result_file)

if __name__ == "__main__":
    binary_path = sys.argv[1]
    result_path = sys.argv[2]
    memory_range = list(map(int, sys.argv[3].split(',')))
    execute(binary_path, result_path, memory_range)
