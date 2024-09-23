import unittest
from io import StringIO
from unittest.mock import patch
from vfs import VirtualFileSystem
from commands import execute_command

class TestVirtualFileSystem(unittest.TestCase):
    def setUp(self):
        self.vfs = VirtualFileSystem('test_vfs.tar')

    @patch('sys.stdout', new_callable=StringIO)
    def test_ls(self, mock_stdout):
        self.vfs.change_directory('test_dir')
        execute_command(self.vfs, 'ls')
        output = mock_stdout.getvalue().strip()
        expected_output = "\n".join(['file2.txt', 'file3.txt', 'another_dir', 'file1.txt', 'empty_dir'])
        self.assertEqual(output, expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_tree(self, mock_stdout):
        execute_command(self.vfs, 'tree')
        output = mock_stdout.getvalue().strip()
        expected_output = (
            "vfs\n"
            "    |-- test_dir\n"
            "        |-- another_dir\n"
            "        |-- empty_dir\n"
            "        |-- file1.txt\n"
            "        |-- file2.txt\n"
            "        |-- file3.txt"
        )
        self.assertEqual(output, expected_output)

if __name__ == "__main__":
    unittest.main()
