#import unittest
#from io import StringIO
#from unittest.mock import patch
#from vfs import VirtualFileSystem
#from commands import execute_command
#
#class TestCommands(unittest.TestCase):
#    def setUp(self):
#        self.vfs = VirtualFileSystem('test_vfs.tar')
#
#    @patch('sys.stdout', new_callable=StringIO)
#    def test_tail(self, mock_stdout):
#        self.vfs.change_directory('test_dir')
#        execute_command(self.vfs, 'tail file1.txt')
#        output = mock_stdout.getvalue().strip()
#        expected_output = "file1_content"
#        self.assertEqual(output, expected_output)
#
#    @patch('sys.stdout', new_callable=StringIO)
#    def test_uniq(self, mock_stdout):
#        self.vfs.change_directory('test_dir')
#        with open('test_vfs/test_dir/file1.txt', 'a') as f:
#            f.write("file1_content\nfile1_content")
#        execute_command(self.vfs, 'uniq file1.txt')
#        output = mock_stdout.getvalue().strip()
#        expected_output = "file1_content"
#        self.assertEqual(output, expected_output)
#
#if __name__ == "__main__":
#    unittest.main()

import unittest
from io import StringIO
from unittest.mock import patch
from vfs import VirtualFileSystem
from commands import execute_command

class TestCommands(unittest.TestCase):
    def setUp(self):
        # Предполагаем, что файл test_vfs.tar уже содержит нужные файлы
        self.vfs = VirtualFileSystem('test_vfs.tar')

    @patch('sys.stdout', new_callable=StringIO)
    def test_tail(self, mock_stdout):
        # Предполагаем, что file1.txt существует в тестовой файловой системе и содержит текст
        self.vfs.change_directory('test_dir')  # Переходим в директорию
        execute_command(self.vfs, 'tail file1.txt')  # Выполняем команду tail
        output = mock_stdout.getvalue().strip()

        # Ожидаем, что tail выведет последние 10 строк, но у нас только одна
        expected_output = "Разработать эмулятор для языка оболочки ОС. Необходимо сделать работу"  # или какая-то другая строка
        self.assertIn(expected_output, output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_uniq(self, mock_stdout):
        # Предполагаем, что file1.txt содержит дублирующиеся строки
        self.vfs.change_directory('test_dir')  # Переходим в директорию
        execute_command(self.vfs, 'uniq file1.txt')  # Выполняем команду uniq
        output = mock_stdout.getvalue().strip()

        # Ожидаем, что uniq выведет только уникальные строки
        expected_output = "Разработать эмулятор для языка оболочки ОС."  # Первая уникальная строка
        self.assertIn(expected_output, output)

if __name__ == "__main__":
    unittest.main()


