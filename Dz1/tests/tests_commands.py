import unittest
from io import StringIO
from unittest.mock import patch
from vfs import VirtualFileSystem
from commands import execute_command

class TestCommands(unittest.TestCase):
    def setUp(self):
        self.vfs = VirtualFileSystem('test_vfs.tar')

    @patch('sys.stdout', new_callable=StringIO)
    def test_tail(self, mock_stdout):
        self.vfs.change_directory('test_dir')
        execute_command(self.vfs, 'tail file1.txt')
        output = mock_stdout.getvalue().strip()
        expected_output = "file1_content"
        self.assertEqual(output, expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_uniq(self, mock_stdout):
        self.vfs.change_directory('test_dir')
        with open('test_vfs/test_dir/file1.txt', 'a') as f:
            f.write("file1_content\nfile1_content")
        execute_command(self.vfs, 'uniq file1.txt')
        output = mock_stdout.getvalue().strip()
        expected_output = "file1_content"
        self.assertEqual(output, expected_output)

if __name__ == "__main__":
    unittest.main()
