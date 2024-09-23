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

        expected_output = "Разработать эмулятор для языка оболочки ОС. Необходимо сделать работу"
        self.assertIn(expected_output, output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_tail_single_line(self, mock_stdout):
        self.vfs.change_directory('test_dir')
        execute_command(self.vfs, 'tail single_line.txt')
        output = mock_stdout.getvalue().strip()

        expected_output = "Это единственная строка в файле."
        self.assertEqual(output, expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_tail_nonexistent_file(self, mock_stdout):
        self.vfs.change_directory('test_dir')
        execute_command(self.vfs, 'tail nonexistent.txt')
        output = mock_stdout.getvalue().strip()

        expected_output = "Ошибка: Файл не найден."
        self.assertEqual(output, expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_uniq(self, mock_stdout):
        self.vfs.change_directory('test_dir')
        execute_command(self.vfs, 'uniq file1.txt')
        output = mock_stdout.getvalue().strip()

        expected_output = "Разработать эмулятор для языка оболочки ОС."
        self.assertIn(expected_output, output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_uniq_no_duplicates(self, mock_stdout):
        self.vfs.change_directory('test_dir')
        execute_command(self.vfs, 'uniq unique_lines.txt')
        output = mock_stdout.getvalue().strip()

        expected_output = "Строка 1\nСтрока 2\nСтрока 3"
        self.assertEqual(output, expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_uniq_empty_file(self, mock_stdout):
        self.vfs.change_directory('test_dir')
        execute_command(self.vfs, 'uniq empty.txt')
        output = mock_stdout.getvalue().strip()

        expected_output = ""
        self.assertEqual(output, expected_output)

if __name__ == "__main__":
    unittest.main()
